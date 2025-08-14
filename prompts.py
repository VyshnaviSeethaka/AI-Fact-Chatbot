import os
import yaml

_PROMPTS_PATH = os.path.join(os.path.dirname(__file__), "prompts.yaml")

with open(_PROMPTS_PATH, "r", encoding="utf-8") as f:
    PROMPTS = yaml.safe_load(f)
