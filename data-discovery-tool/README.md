
# Eco Data Mining - Data Discovery and Analysis Platform

## Project Overview

Eco Data Mining is an extensible and modular platform designed to automate the discovery, extraction, enrichment, and organization of ecological journal publications. Its primary aim is to bridge the gap between scientific literature and biological field stations by systematically mining research articles and linking them to verified field stations, research sites, and ecological observatories. The system supports both structured (relational) and semi-structured data processing workflows, making it suitable for ecological data scientists, researchers, and data engineers who require a scalable, research-grade solution.

---

## Objectives

- **Automate ingestion and processing** of ecological journal metadata.
- **Apply advanced NLP techniques** (NER, entity linking) to extract research locations and field station mentions from text.
- **Link extracted locations** to curated datasets such as OBFS and NEON field stations.
- **Build a hybrid relational database** integrating metadata, NLP-enriched content, and field station relationships.
- **Lay a foundation for advanced analysis** and visualization of ecological data.

---

## Project Architecture

```
(venv) PS C:\Users\VikRuhil\Desktop\MS DS\Capstone\Eco Data Mining\eco-data-mining\data-discovery-tool> py.exe .\extract_dir.py
data-discovery-tool/
├── README.md
├── __pycache__
├── api
│   ├── constellete
│   │   ├── fetch_sample.py
│   │   ├── fetch_stations.py
│   │   ├── login_test_constellete.py
│   │   └── venv
│   ├── jstor
│   └── utils
├── config.py
├── data
│   ├── eco.db
│   ├── images
│   │   ├── authers_per_publications.png
│   │   ├── keyphrase_cloud.png
│   │   ├── location word cloud.png
│   │   └── publication_over_time.png
│   ├── models
│   ├── processed
│   │   ├── ecology_dataset_50k.csv
│   │   ├── first_10_records.json
│   │   ├── first_record.json
│   │   └── splits
│   │       ├── ecology_dataset_chunk_1.csv
│   │       ├── ecology_dataset_chunk_10.csv
│   │       ├── ecology_dataset_chunk_11.csv
│   │       ├── ecology_dataset_chunk_12.csv
│   │       ├── ecology_dataset_chunk_13.csv
│   │       ├── ecology_dataset_chunk_14.csv
│   │       ├── ecology_dataset_chunk_15.csv
│   │       ├── ecology_dataset_chunk_16.csv
│   │       ├── ecology_dataset_chunk_17.csv
│   │       ├── ecology_dataset_chunk_18.csv
│   │       ├── ecology_dataset_chunk_19.csv
│   │       ├── ecology_dataset_chunk_2.csv
│   │       ├── ecology_dataset_chunk_20.csv
│   │       ├── ecology_dataset_chunk_21.csv
│   │       ├── ecology_dataset_chunk_22.csv
│   │       ├── ecology_dataset_chunk_23.csv
│   │       ├── ecology_dataset_chunk_24.csv
│   │       ├── ecology_dataset_chunk_25.csv
│   │       ├── ecology_dataset_chunk_26.csv
│   │       ├── ecology_dataset_chunk_27.csv
│   │       ├── ecology_dataset_chunk_28.csv
│   │       ├── ecology_dataset_chunk_29.csv
│   │       ├── ecology_dataset_chunk_3.csv
│   │       ├── ecology_dataset_chunk_30.csv
│   │       ├── ecology_dataset_chunk_31.csv
│   │       ├── ecology_dataset_chunk_32.csv
│   │       ├── ecology_dataset_chunk_33.csv
│   │       ├── ecology_dataset_chunk_34.csv
│   │       ├── ecology_dataset_chunk_35.csv
│   │       ├── ecology_dataset_chunk_36.csv
│   │       ├── ecology_dataset_chunk_37.csv
│   │       ├── ecology_dataset_chunk_38.csv
│   │       ├── ecology_dataset_chunk_39.csv
│   │       ├── ecology_dataset_chunk_4.csv
│   │       ├── ecology_dataset_chunk_40.csv
│   │       ├── ecology_dataset_chunk_41.csv
│   │       ├── ecology_dataset_chunk_42.csv
│   │       ├── ecology_dataset_chunk_43.csv
│   │       ├── ecology_dataset_chunk_44.csv
│   │       ├── ecology_dataset_chunk_45.csv
│   │       ├── ecology_dataset_chunk_46.csv
│   │       ├── ecology_dataset_chunk_47.csv
│   │       ├── ecology_dataset_chunk_48.csv
│   │       ├── ecology_dataset_chunk_49.csv
│   │       ├── ecology_dataset_chunk_5.csv
│   │       ├── ecology_dataset_chunk_50.csv
│   │       ├── ecology_dataset_chunk_6.csv
│   │       ├── ecology_dataset_chunk_7.csv
│   │       ├── ecology_dataset_chunk_8.csv
│   │       └── ecology_dataset_chunk_9.csv
│   └── raw
│       ├── 54d7df8f-d016-72c1-1841-ff05652a4c9f-jsonl.jsonl
│       ├── 944ad6df-e4b8-af27-d4f3-123f483acf35-jsonl.jsonl
│       ├── ecology_full_50k.jsonl
│       ├── ecology_full_50k.jsonl.gz
│       ├── ecology_sample_eeb16c.json
│       └── eeb16cb4-a04a-5e68-3f20-8d5e677fd5ac-jsonl.jsonl
├── db
│   ├── __pycache__
│   ├── engine.py
│   ├── migrations
│   └── models.py
├── debug_path_check.py
├── docker
├── docs
├── extract_dir.py
├── ml
│   ├── embeddings
│   ├── evaluation
│   ├── models
│   ├── preprocessing
│   │   ├── Counter.py
│   │   ├── extracting_fieldstationNLP.py
│   │   ├── field_search.py
│   │   ├── parse_jsonl_to_csv.py
│   │   ├── preview_split_chunks.py
│   │   ├── read_record_jsonl.py
│   │   ├── split_csv_into_chunks.py
│   │   └── testing_json.py
│   └── training
├── notebooks
│   └── Sample_read_jsonl.ipynb
├── requirements.txt
├── scripts
│   ├── __pycache__
│   ├── db_journalschema_py
│   ├── db_sanity_check.py
│   ├── db_verification.py
│   ├── ingest_journals.py
│   ├── setup_db.py
│   ├── update_journal_location.py
│   ├── verify_journals.py
│   ├── verify_keyphrases.py
│   └── visualization.py
├── services
│   ├── api
│   └── ui
│       └── static
├── tests
│   ├── api
│   ├── integration
│   └── ml
└── venv
```

---

## Database Design (Hybrid 3-Tier Model)

| Tier    | Table           | Description                                                                 |
| ------- | -------------- | --------------------------------------------------------------------------- |
| Tier 1  | field_stations | Biological field station metadata (name, location, lat, lon, ecosystem)     |
| Tier 2  | journals       | Journal metadata (title, authors, publication date, keyphrases, full text)  |
| Tier 3  | journal_nlp    | NLP-enriched data: n-grams, entities, topics, embeddings (planned)          |

**Note:** The `journals` table includes a `meta_json` field for storing semi-structured data such as n-gram counts and extracted metadata.

---

## Technology Stack

- **Python 3.11+**
- **SQLite3** (via SQLAlchemy ORM)
- **spaCy 3.8+** (for NER and NLP pipelines)
- **pandas** (data handling and manipulation)
- **rapidfuzz** (fuzzy string matching)
- **Jupyter Notebooks** (exploratory data analysis)

---

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/INFO-698-InfoSci-Capstone/eco-data-mining.git
cd eco-data-mining
```

### 2. Setup Virtual Environment and Install Dependencies

```bash
python -m venv venv
# On Windows:
.
env\Scripts ctivate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## Workflow and Usage

**1. Ingest Journal Metadata**

```bash
python scripts/ingest_journals.py
```

**2. Extract Field Stations from Journal Full Text Using NLP**

```bash
python ml/preprocessing/extracting_fieldstationNLP.py
```

**3. Verify Data Completeness and Sanity**

```bash
python scripts/db_sanity_check.py
```

**4. Explore Data Using Jupyter Notebooks**

```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

---

## Visualization and Exploratory Analysis

The project includes built-in visualizations to support analysis of publication metadata, NLP enrichment, and author collaboration patterns. These visualizations are generated using `matplotlib`, `seaborn`, and `wordcloud` and stored in `data/images/`.

### 1. Author Contribution Distribution

Displays a histogram of the number of authors per publication.

![Author Contribution Distribution](data/images/authers_per_publications.png)

---

### 2. Keyphrase Word Cloud

Shows frequently used keyphrases across the journal dataset.

![Keyphrase Word Cloud](data/images/keyphrase_cloud.png)

---

### 3. Publication Over Time

Plots number of publications by year.

![Publication Over Time](data/images/publication_over_time.png)

---

### To Run Visualizations

```bash
python scripts/visualize_journals.py
```

---

## Contact

For questions or collaborations, contact the maintainers or open an issue.

---

## Data Handling and Best Practices

- The primary database (`eco.db`) is excluded from the repository (see `.gitignore`) to avoid versioning large binary files and comply with GitHub’s storage policies.
- Curated field station lists (`obfs_fieldstations.csv`, `neon_fieldstations.csv`) must be placed in the `data/` directory for proper journal-to-station matching.
- Large datasets and output files (e.g., raw text, embeddings, JSONL exports) should be stored externally using repositories such as Zenodo, Figshare, Amazon S3, or institutional storage platforms.

**Limitations due to JSTOR/Constellate API deprecation**:
- As of late 2024, JSTOR’s Constellate platform discontinued open access to bulk metadata and full-text download for many datasets, limiting the automated ingestion of fresh ecological literature.
- The current dataset (50,000 journal records) reflects a snapshot from when access was granted. However, real-time updates, broader historical coverage, and additional metadata are now restricted unless explicitly licensed.

> Resolution in progress: We plan to formally reach out to the Organization of Biological Field Stations (OBFS) and JSTOR/Constellate to:
> - Request direct access to field station-tagged research publications.
> - Propose a collaborative research partnership to support transparent field station mapping from historical literature.
> - Ensure responsible use of copyrighted data under fair academic use or with negotiated access terms.

---

## Future Work and Enhancements

The current implementation provides the foundational infrastructure for ecological research metadata discovery. Planned upgrades include:

- Domain-specific NLP modeling: Train custom spaCy or transformer-based NER models to improve field station recognition beyond general-purpose models.
- Topic modeling and embeddings: Incorporate LDA, BERTopic, or SBERT for semantic clustering and search.
- REST API development: Build an API layer to expose journal metadata, NLP-derived tags, and location mappings for external apps or researchers.
- Streamlit or Dash dashboards: Create real-time dashboards for search, filtering, and spatial visualization of ecological literature by field station, year, or topic.
- Field station name normalization: Add fuzzy matching pipelines to handle aliasing and local name inconsistencies.
- External dataset integration: Enrich journal records with biodiversity, climate, or ecological observational data tied to locations or publication topics.

Current Gaps:
- Incomplete matching of field stations due to missing or implicit references in journal texts.
- Limited historical depth in OBFS and NEON field station data.
- Field station metadata lacks unique identifiers or consistent regional context in many entries.

---

## Contributing

We welcome contributions from the ecological informatics, NLP, and data science communities. To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/my-enhancement
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add new visualization module"
   ```
4. Push to your fork and open a pull request with a description of the improvement.

Please ensure your PR includes tests if applicable and aligns with the project’s modular architecture.

---

## License

This project is licensed under MIT License.  
All journal metadata is used under educational and research fair-use principles unless otherwise noted. Field station datasets are derived from publicly accessible sources or academic partner collaborations.

---

## Acknowledgments

- JSTOR/Constellate for historical access to ecological journal metadata.
- Organization of Biological Field Stations (OBFS) and NEON for field station directories.
- Open-source communities of spaCy, SQLAlchemy, pandas, and Matplotlib for tooling and libraries.
- This project was developed as part of the INFO 698 Capstone at the University of Arizona, with the support of the Data Science faculty and peers.

---

## Contact

For collaborations, support, or academic inquiries:

- GitHub Issues: https://github.com/INFO-698-InfoSci-Capstone/eco-data-mining/issues
- Maintainers: Vik Ruhil, vikruhil@arizona.edu 
           Saksham Gupta sakshamgupta@arizona.edu
- Institution: University of Arizona – School of Information (MSDS Capstone, Spring 2025)