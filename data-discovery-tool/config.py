# config.py

import sys
import os
from pathlib import Path
from dotenv import load_dotenv
sys.path.append(str(Path(__file__).resolve().parent.parent))
PROJECT_ROOT = Path(__file__).resolve().parent

# Ensure project root is in sys.path
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Load environment variables from .env file (if exists)
load_dotenv()

#  Project root
PROJECT_ROOT = Path(__file__).resolve().parent

#  Environment type (can be set via `.env`)
APP_ENV = os.getenv("APP_ENV", "development")

#  Core folders
GITHUB_DIR = PROJECT_ROOT / ".github"
API_DIR = PROJECT_ROOT / "api"
API_CONSTELLETE_DIR = API_DIR / "constellete"
API_JSTOR_DIR = API_DIR / "jstor"
API_UTILS_DIR = API_DIR / "utils"

DATA_DIR = PROJECT_ROOT / "data"
DATA_RAW_DIR = DATA_DIR / "raw"
DATA_PROCESSED_DIR = DATA_DIR / "processed"
DATA_MODELS_DIR = DATA_DIR / "models"

DB_DIR = PROJECT_ROOT / "db"
DB_MIGRATIONS_DIR = DB_DIR / "migrations"

DOCKER_DIR = PROJECT_ROOT / "docker"
DOCS_DIR = PROJECT_ROOT / "docs"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

SERVICES_DIR = PROJECT_ROOT / "services"
SERVICES_API_DIR = SERVICES_DIR / "api"
SERVICES_UI_DIR = SERVICES_DIR / "ui"
SERVICES_UI_STATIC_DIR = SERVICES_UI_DIR / "static"

ML_DIR = PROJECT_ROOT / "ml"
ML_EMBEDDINGS_DIR = ML_DIR / "embeddings"
ML_EVALUATION_DIR = ML_DIR / "evaluation"
ML_MODELS_DIR = ML_DIR / "models"
ML_PREPROCESSING_DIR = ML_DIR / "preprocessing"
ML_TRAINING_DIR = ML_DIR / "training"

TESTS_DIR = PROJECT_ROOT / "tests"
TESTS_API_DIR = TESTS_DIR / "api"
TESTS_INTEGRATION_DIR = TESTS_DIR / "integration"
TESTS_ML_DIR = TESTS_DIR / "ml"

#  Misc
VENV_DIR = PROJECT_ROOT / "venv"
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG" if APP_ENV == "development" else "INFO")

# Git branch info (auto-detection)
def get_git_branch():
    try:
        import subprocess
        result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception:
        return "unknown"

CURRENT_BRANCH = os.getenv("GIT_BRANCH", get_git_branch())



#  Feature flags
USE_CONSTELLATE_CLIENT = os.getenv("USE_CONSTELLATE_CLIENT", "true").lower() == "true"
