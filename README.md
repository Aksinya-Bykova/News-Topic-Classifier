# News-Topic-Classifier

Put your title and description (optional). The service will show the most likely category: world, sport, business, scie/tech

## Service is available [here](https://immrass-news-classifier-ysda.hf.space/)

![sample](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/assets/Screenshot%20from%202026-04-09%2017-32-57.png)

| Category | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **World** | 0.92 | 0.88 | 0.90 | 497 |
| **Sports** | 0.94 | 0.99 | 0.97 | 483 |
| **Business** | 0.86 | 0.85 | 0.86 | 522 |
| **Sci/Tech** | 0.86 | 0.87 | 0.87 | 498 |
| | | | | |
| **Accuracy** | — | — | **0.90** | **2000** |
| **Macro avg** | 0.90 | 0.90 | 0.90 | 2000 |
| **Weighted avg** | 0.90 | 0.90 | 0.90 | 2000 |

## Data
Dataset: ag_news - texts with category ([why this? see EDA](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/EDA.ipynb))

Train subset: 10.000 samples

Test subset: 2000 samples

## Model
Model: **microsoft/deberta-v3-small** - tuned BERT is great in learning connection between context and word 

Made fine-tuning for news classification

## Experiments
*   **Number of Epochs:** 3 (times of learning all dataset)
*   **Learning Rate:** `2e-5` (a low value chosen to preserve the model's pre-trained knowledge and avoid breaking it)
*   **Batch Size:** 16 (the model processed the data in groups of 16 samples per iteration)
*   **Optimization:** `weight_decay=0.01` was used as a regularization technique to prevent overfitting
*   **Evaluation Strategy:** The model was evaluated on the test set at the end of every epoch (`eval_strategy="epoch"`)

## Results
*   Highest Accuracy: **Sports**, **F1-score of 0.97**, indicating very high precision and recall.
*   Classification Challenges: Performance slightly dips in the **Business** and **Sci/Tech** (**F1-score 0.86–0.87**). This marginal decrease is likely caused by lexical overlap, as both categories often share common terminology regarding finance, corporate entities, and technological innovation

# Optimization
![sample onnx](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/assets/Screenshot%20from%202026-04-09%2021-12-50.png)
