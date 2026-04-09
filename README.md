# News-Topic-Classifier

Put your title and description (optional). The service will show the most likely category: world, sport, business, scie/tech

## Train code in PDF is available [here](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/train_baseline.pdf)

## Service is available [here](https://immrass-news-classifier-ysda.hf.space/)

## (here is baseline slow version)

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
*   **Dataset:** `ag_news` - benchmark dataset for short text classification
*   **Why this choice?** Great balance across 4 distinct categories. Clean data, this dataset is popular (don't need to do dirty work, I'm too busy)
*   **Subset sizes:** 10,000 samples for training and 2,000 samples for testing
*   See [EDA Notebook](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/EDA.ipynb)

## Model
`microsoft/deberta-v3-small`

DeBERTa-v3 represents content and relative position separately. This architecture is more effective for short, structured texts like news headlines compared to traditional BERT. Small - just for fast inference on CPU (metrics are fine so why not)

## Experiments
*   **Number of Epochs:** 3 
*   **Learning Rate:** `2e-5`
*   **Batch Size:** 16
*   **Optimization:** `weight_decay=0.01`
*   **Evaluation Strategy:** `eval_strategy="epoch"`

## Results
*   Highest Accuracy: **Sports**, **F1-score of 0.97**, indicating very high precision and recall.
*   Classification Challenges: Performance slightly dips in the **Business** and **Sci/Tech** (**F1-score 0.86–0.87**). This marginal decrease is likely caused by lexical overlap, as both categories often share common terminology regarding finance, corporate entities, and technological innovation

# Optimization
## [Optimization Code PDF](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/onnx/train_onnx.pdf)

This version is deployed on HF

# from 751 to 12 ms!!! (see previous picture)

![sample onnx](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/assets/Screenshot%20from%202026-04-09%2021-22-55.png)

# Trumped (why not?)

![sample onnx](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/assets/Screenshot%20from%202026-04-09%2021-12-50.png)

# Add description (also fast)


![sample onnx](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/assets/Screenshot%20from%202026-04-09%2021-36-18.png)


-----
Там, если что, помимо тестов со скринов есть тесты прямо внутри ноутбука, нормально всё работает, вполне правдоподобно

Я сделала весь этот проект только ради того, чтобы поиграться с оптимизацией. Узнала, что такое onnx - такая библиотека на C++ для ускорения выполнения операций из торча. Напоминает -O3 компиляцию в C++, когда компилятор подбирает, как на низком уровне выполнится программа. Тут есть свой аналог дизассемблера:

![](https://github.com/Aksinya-Bykova/News-Topic-Classifier/blob/main/assets/Screenshot%20from%202026-04-09%2022-15-17.png)


Обычно я занимаюсь ресерчем, где я ускоряю код для обучения, а это библиотека для инференса преимущественно. Впрочем, дорогой электронный друг говорит, что для обучения иногда надо: в гигантских LLM,  edge learning (это когда файнтюнинг происходит на смартфоне юзера, например) или когда пишешь код не под NVIDIA. Видимо, палочка-выручалочка, когда нет времени или средств написать свою красоту на C++

Люблю оптимизацию и всё, что с этим связано, ставьте звёзды, подписывайтесь на канал. У меня крутой проект есть https://github.com/Aksinya-Bykova/mclsr-abstract
