import os
from dotenv import load_dotenv

load_dotenv()

# --- API / LLM ---
OPENAI_API_KEY = (os.getenv("OPENAI_API_KEY") or "").strip()
OPENAI_MODEL = (os.getenv("OPENAI_MODEL") or "gpt-4o-mini").strip()
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.2))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 800))

# --- Search / Fetch ---
SEARCH_MAX_RESULTS = int(os.getenv("SEARCH_MAX_RESULTS", 5))
FETCH_TIMEOUT = int(os.getenv("FETCH_TIMEOUT", 10))

APP_TITLE = "AI Fact-Checker Bot"
APP_DESCRIPTION = "Fact-checks claims using OpenAI + web search."

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in .env")
