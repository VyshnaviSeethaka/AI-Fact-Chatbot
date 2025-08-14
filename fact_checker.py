from typing import Dict, List
from .prompt_chains import classify_claim, extract_assumptions, generate_report
from .search_tools import search_and_fetch
from .utils import credibility_score

def _split_lines(text: str) -> List[str]:
    lines = [l.strip("- •\t ").strip() for l in (text or "").splitlines()]
    return [l for l in lines if l]

def fact_check_claim(claim: str) -> Dict:
    """
    Pipeline:
      1) classify
      2) extract short assumptions (fallback to claim)
      3) search web for each assumption
      4) generate final report
    """
    classification = (classify_claim(claim) or "").strip()

    assumptions_text = (extract_assumptions(claim) or "").strip()
    assumptions = _split_lines(assumptions_text) or [claim]

    evidence_chunks = []
    for a in assumptions:
        evidence = search_and_fetch(a)
        if evidence:
            evidence_chunks.append(evidence)

    combined = "\n\n".join(evidence_chunks)
    report = generate_report(claim, combined)

    return {
        "claim": claim,
        "classification": classification,
        "assumptions": assumptions,
        "evidence_excerpt": combined[:2500],
        "credibility": round(credibility_score(combined), 3),
        "report": report,
    }
