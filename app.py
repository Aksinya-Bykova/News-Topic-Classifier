import gradio as gr
import pandas as pd
import traceback
from config import AppConfig
from model_service import NewsClassifierService

try:
    config = AppConfig()
    service = NewsClassifierService(config)
except Exception as e:
    print(f"CRITICAL ERROR DURING INIT: {e}")


def classify_process(title: str, abstract: str):
    try:
        if not title.strip():
            return "Error: Title is required", {}, "Please enter a title."

        full_text = f"{title}. {abstract}" if abstract.strip() else title

        df, latency = service.predict(full_text)

        top_95_set = service.get_top_p_results(df)

        confidences = {res["label"]: float(res["score"]) for _, res in df.iterrows()}

        top_95_html = "### 🎯 Decision (Top-95% Set):  \n"
        for item in top_95_set:
            top_95_html += f"✅ **{item['label']}**: {item['score']:.2%}  \n"

        latency_info = f"⚡ Inference Latency: {latency:.2f} ms"

        return latency_info, confidences, top_95_html

    except Exception as e:
        error_msg = f"❌ Error: {str(e)}\n{traceback.format_exc()}"
        return "Error", {}, error_msg


with gr.Blocks(title=AppConfig.APP_TITLE) as demo:
    gr.Markdown(f"# 📰 {AppConfig.APP_TITLE}")
    gr.Markdown("Fine-tuned DeBERTa-v3 model | Status: PROD")

    with gr.Row():
        with gr.Column():
            title_input = gr.Textbox(label="Article Title", lines=1)
            abstract_input = gr.Textbox(label="Abstract (Optional)", lines=6)
            submit_btn = gr.Button("Classify Article", variant="primary")
            latency_output = gr.Markdown("⚡ Latency: -- ms")

        with gr.Column():
            label_output = gr.Label(label="Category Distribution")
            top95_output = gr.Markdown("Results will appear here...")

    submit_btn.click(
        fn=classify_process,
        inputs=[title_input, abstract_input],
        outputs=[latency_output, label_output, top95_output],
    )

demo.launch()
