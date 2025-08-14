from openai import OpenAI
from config.prompts import PROMPTS
from config.settings import OPENAI_API_KEY, OPENAI_MODEL, LLM_TEMPERATURE, MAX_TOKENS

client = OpenAI(api_key=OPENAI_API_KEY)

# ~4000 tokens ~ 12k-16k chars. Keep wide margin to avoid rate/TPM caps.
MAX_PROMPT_CHARS = 12000

def _truncate_text(text: str, max_chars: int = MAX_PROMPT_CHARS) -> str:
    if text is None:
        return ""
    if len(text) > max_chars:
        return text[:max_chars] + "\n\n[...Content Truncated Due to Token Limit...]"
    return text

def _ask(prompt: str) -> str:
    safe_prompt = _truncate_text(prompt)
    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are a precise, conservative fact-checking assistant."},
            {"role": "user", "content": safe_prompt},
        ],
        temperature=LLM_TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    return (resp.choices[0].message.content or "").strip()

def classify_claim(claim: str) -> str:
    return _ask(PROMPTS["classify_claim"].format(claim=_truncate_text(claim, 2000)))

def extract_assumptions(claim: str) -> str:
    return _ask(PROMPTS["extract_assumptions"].format(claim=_truncate_text(claim, 2000)))

def generate_report(claim: str, evidence: str) -> str:
    return _ask(PROMPTS["generate_report"].format(
        claim=_truncate_text(claim, 2000),
        evidence=_truncate_text(evidence, 9000),
    ))
