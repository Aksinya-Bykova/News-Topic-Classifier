import time
import pandas as pd
from transformers import pipeline
from config import AppConfig


class NewsClassifierService:
    def __init__(self, config: AppConfig):
        self.config = config
        self._pipeline = pipeline(
            "text-classification",
            model=config.MODEL_ID,
            top_k=None,
        )

    def predict(self, text: str):
        if not text.strip():
            return pd.DataFrame(), 0.0

        start_time = time.perf_counter()

        results = self._pipeline(text, truncation=True, max_length=128)[0]

        latency = (time.perf_counter() - start_time) * 1000

        df = pd.DataFrame(results).sort_values("score", ascending=False)
        return df, latency

    def get_top_p_results(self, df: pd.DataFrame):
        if df is None or df.empty:
            return []

        results = []
        cumulative_prob = 0.0

        for _, row in df.iterrows():
            score = float(row["score"])
            results.append({"label": row["label"], "score": score})
            cumulative_prob += score
            if cumulative_prob >= self.config.TOP_P_THRESHOLD:
                break
        return results
