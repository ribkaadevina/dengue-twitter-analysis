\# Examining Dengue-Related Information Diffusion on Indonesian Twitter Through Sentiment-Based Network Analysis, Spatial Mapping, and Temporal Dynamics



This repository contains the full implementation code for the manuscript analyzing dengue-related discourse on Indonesian Twitter (X) using sentiment classification, network analysis, spatial mapping, and temporal dynamics.



\## Repository Structure

dengue-twitter-analysis/

├── data/

│   ├── daftar-nama-daerah.csv          # City/region geocoding reference list

│   └── tweet\_ids\_and\_labels.csv        # Tweet IDs + sentiment/community labels (no raw text)

├── notebooks/

│   ├── 01\_scraping/

│   │   ├── scrapekey1.py               # Keyword: "dbd"

│   │   ├── scrapekey2.py               # Keyword: "aedes aegypti"

│   │   └── scrapekey3.py               # Keyword: "demam berdarah dengue"

│   ├── 01\_preprocessing.ipynb

│   ├── 02\_preprocessing\_location.ipynb

│   ├── 03\_sentiment\_analysis.ipynb

│   ├── 04\_random\_sampling.ipynb

│   ├── 05\_network\_construction.ipynb

│   ├── 06\_sensitivity\_analysis.ipynb

│   ├── 07\_community\_detection.ipynb

│   ├── 08\_spatial\_analysis.ipynb

│   └── 09\_temporal\_time\_analysis.ipynb

├── outputs/                             # All generated result files (Excel)

├── requirements.txt

└── README.md



\## Setup Instructions



1\. \*\*Clone this repository\*\*

git clone <repository-url>

cd dengue-twitter-analysis



2\. \*\*Create and activate a virtual environment\*\*

python -m venv venv

venv\\Scripts\\activate        # Windows

source venv/bin/activate     # Mac/Linux



3\. \*\*Install dependencies\*\*

pip install -r requirements.txt



4\. \*\*Set up environment variables\*\* (for data collection scripts only)

&#x20;  Create a `.env` file in the repository root:

SCWEET\_AUTH\_TOKEN=your\_twitter\_x\_auth\_token



\## Data Collection



Tweets were collected using the `Scweet` library (browser-automation-based, not the official X/Twitter API) across three keywords: `dbd`, `aedes aegypti`, and `demam berdarah dengue`, covering January 2021 to December 2025. Collection was conducted as a series of discrete scraping sessions per keyword and sub-period; scripts in `notebooks/01\_scraping/` were re-run repeatedly with `SINCE\_DATE` and `UNTIL\_DATE` manually adjusted to cover the full study window.



\## Data Availability



Raw tweet text is \*\*not included\*\* in this repository, in accordance with X/Twitter's Terms of Service regarding redistribution of platform content. Instead, we provide:

\- `data/tweet\_ids\_and\_labels.csv`: tweet IDs paired with derived sentiment labels, community assignments, and city labels, allowing legal re-collection ("rehydration") of tweet content by researchers who agree to X's terms.

\- All aggregated/derived outputs used to generate the manuscript's tables and figures (see `outputs/`), which do not contain raw tweet text.



\## Reproducing Notebooks 05-09 Without Raw Tweet Access



Since raw tweet text cannot be redistributed, `data/tweet\_ids\_and\_labels.csv` is provided as a substitute input for notebooks 05 through 09 (network construction, sensitivity analysis, community detection, spatial analysis, temporal analysis), all of which rely only on derived fields (sentiment labels, mentions, city, timestamps) rather than raw tweet content.



To use it, convert it to the expected input format before running these notebooks:



```python

import pandas as pd



df = pd.read\_csv("data/tweet\_ids\_and\_labels.csv")

df.to\_excel("outputs/dataset\_with\_sentiment.xlsx", index=False)

```



Notebooks 01-03 (scraping, preprocessing, sentiment classification) require raw tweet text and cannot be run without independently re-collecting tweets via the provided `tweet\_id` values, in accordance with X/Twitter's data-sharing policies.



\## Sentiment Classification and Model Selection



Sentiment labels were assigned using \*\*IndoBERT\*\* (`taufiqdp/indonesian-sentiment`), selected via ground-truth validation rather than output distribution alone. This involved:



1\. Drawing a validation sample of 374 tweets from the full dataset (N = 5,715) using \*\*Slovin's formula\*\* (5% margin of error)

2\. Independent labelling by two annotators, blind to model predictions (`04\_random\_sampling.ipynb`)

3\. Inter-annotator agreement assessment via \*\*Cohen's Kappa\*\* (κ = 0.53, moderate agreement)

4\. Benchmarking six pretrained sentiment classifiers against this ground truth (`03\_sentiment\_analysis.ipynb`), selecting the model with the highest \*\*macro-F1\*\* score



| Model | HuggingFace Identifier | Macro-F1 |

|---|---|---|

| \*\*IndoBERT (selected)\*\* | `taufiqdp/indonesian-sentiment` | \*\*0.6014\*\* |

| RoBERTa | `w11wo/indonesian-roberta-base-sentiment-classifier` | 0.5705 |

| IndoRoBERTa-SmSA | `ayameRushia/roberta-base-indonesian-sentiment-analysis-smsa` | 0.5295 |

| IndoBertweet (2024) | `Aardiiiiy/indobertweet-base-Indonesian-sentiment-analysis` | 0.4881 |

| XLM-R | `cardiffnlp/twitter-xlm-roberta-base-sentiment` | 0.3801 |

| mBERT | `nlptown/bert-base-multilingual-uncased-sentiment` | 0.2162 |



\*\*Inference settings:\*\* zero-shot/pretrained (no fine-tuning); input truncated to 512 characters; default tokenizer per model; no custom inference threshold (default highest-probability label).



\*\*Environment:\*\* Python 3.11.0, transformers 5.6.0, torch 2.11.0 (CPU-only).



\## Network Construction and Community Detection



Sentiment-weighted interaction networks (complete, positive, neutral, negative) were constructed from mention/reply edges (`05\_network\_construction.ipynb`). Community detection used the \*\*Louvain algorithm\*\* with a fixed random seed (`random\_state=42`) for reproducibility (`07\_community\_detection.ipynb`). A sensitivity analysis testing robustness to self-loops and bot-like accounts is provided in `06\_sensitivity\_analysis.ipynb`.



\## Spatial and Temporal Analysis



City-level location was determined using tweet-level geotags where available, falling back to user profile location otherwise, matched against the geocoding reference list in `data/daftar-nama-daerah.csv` (`02\_preprocessing\_location.ipynb`, `08\_spatial\_analysis.ipynb`). Temporal trends and seasonality are analyzed in `09\_temporal\_time\_analysis.ipynb`.



\## Reproducing the Manuscript's Tables



Run notebooks in numerical order (01 through 09). Each notebook reads its inputs from `outputs/` (populated by earlier notebooks) and `data/` (static reference files), and writes its results back to `outputs/`. Note that the manual annotation step (Step 3 in `04\_random\_sampling.ipynb`) involves human judgment and cannot be regenerated by code; the completed annotation files are provided directly in `outputs/`.



\## Citation



If you use this code or dataset structure, please cite:

\[Citation details to be added upon publication]

