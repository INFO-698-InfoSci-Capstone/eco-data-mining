# Data Discovery Tool: Intelligent Metadata Extraction from Ecological Archives

> A full-stack AI pipeline to locate, extract, and classify metadata from field station records and scientific journals using NER, classification, and GPT-based summarization.

---

## Abstract

This project introduces a unified data discovery framework designed to uncover ecological "dark data" embedded in historical scientific literature and field station archives. By integrating deep learning models for Named Entity Recognition (NER), document classification, and transformer-based summarization, the system enables automated extraction and enrichment of station and journal metadata.

The pipeline leverages APIs from JSTOR and Constellate, processes the data through advanced NLP pipelines, and stores structured outputs in a PostgreSQL database with pgvector for embedding-based search. A lightweight UI allows researchers to interactively explore, verify, and refine metadata, supporting both exploratory research and ecological informatics.

---

## Key Features

- **API Ingestion Modules** for JSTOR and Constellate archives  
- **NER & Classification Models** trained on SciBERT/BioBERT for metadata tagging  
- **GPT-based Summarization & Q&A** for full-text understanding  
- **PostgreSQL + pgvector** for semantic vector search  
- **Streamlit/React UI** for interactive exploration  
- **Model Evaluation & Visualization** via interactive notebooks  
- **Dockerized Full Stack** with Docker Compose  

---

## Project Structure

```
/data-discovery-tool
├── api/           # Data ingestion (JSTOR, Constellate)
├── data/          # Raw and cleaned data, saved models
├── db/            # DB schema, migrations, config
├── ml/            # NLP models, training, embeddings
├── notebooks/     # Interactive exploration notebooks
├── scripts/       # Pipeline execution scripts
├── services/      # Backend API and UI logic
├── tests/         # Unit and integration tests
├── docker/        # Docker and Compose files
├── docs/          # Project documentation
```

---

## Setup Guide

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/data-discovery-tool.git
cd data-discovery-tool
```

2. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**

```bash
cp .env.example .env
# Add your API keys, DB credentials, etc.
```

5. **Run Locally (Dev Mode)**

```bash
# Start API
cd services/api
uvicorn api_main:app --reload

# Launch UI
cd ../ui
streamlit run ui_main.py
```

6. **Run with Docker (Recommended for Production)**

```bash
docker-compose up --build
```

---

## Machine Learning Components

| Component              | Description                                 |
|------------------------|---------------------------------------------|
| `ner_model_best.pt`    | NER model for station/journal metadata      |
| `classification_model.pt` | Relevance classifier for extracted entries |
| `gpt_pipeline.py`      | GPT-based text summarization and QA         |
| `embedding_generator.py` | Converts text into semantic vectors       |

---

## Testing

Run all unit and integration tests:

```bash
pytest tests/
```

---

## Sample Data

| File Name             | Description                         |
|-----------------------|-------------------------------------|
| `stations_raw.json`   | Raw metadata from field stations    |
| `journals_cleaned.csv`| Processed journal entries           |
| `ner_model_best.pt`   | Saved NER model weights             |

---

## Evaluation Metrics

- **Named Entity Recognition**: Precision, Recall, F1-score  
- **Classification**: Accuracy, Confusion Matrix  
- **GPT Outputs**: BLEU, ROUGE, manual review  
- **Embedding Quality**: Cosine similarity search performance  

---

## Tech Stack

- **Languages**: Python 3.10  
- **Libraries**: PyTorch, HuggingFace Transformers, scikit-learn, OpenAI  
- **Frameworks**: FastAPI, Streamlit, React (optional)  
- **Database**: PostgreSQL + pgvector  
- **DevOps**: Docker, Docker Compose, Git  
- **Testing**: Pytest  

---

## Roadmap

- Add new source integrations (e.g., Springer, Elsevier)  
- Improve GPT prompt templates and output control  
- UI enhancements with tagging and filtering  
- Add Doccano/Prodigy integration for annotation  


## License

This project is licensed under the MIT License. See `LICENSE` for full terms.

---

## Acknowledgments

- JSTOR and Constellate for data access  
- HuggingFace for pretrained models  
- pgvector for vector storage in PostgreSQL  

---

## Citation

If you use this tool in your research or academic work, please cite:

```bibtex
@misc{data-discovery-tool,
  author = {Your Name},
  title = {Data Discovery Tool: Intelligent Metadata Extraction from Ecological Archives},
  year = {2025},
  howpublished = {\url{https://github.com/yourusername/data-discovery-tool}},
  note = {Version 1.0}
}
```
