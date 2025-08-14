import src.fact_checker as fc

def test_fact_checker_pipeline_monkeypatched(monkeypatch):
    # Stub out network/LLM for fast offline test
    monkeypatch.setattr(fc, "classify_claim", lambda c: "FACTUAL")
    monkeypatch.setattr(fc, "extract_assumptions", lambda c: "check capital of France")
    monkeypatch.setattr(fc, "search_and_fetch", lambda q: "Paris is the capital of France.")
    monkeypatch.setattr(fc, "generate_report", lambda c, e: "Verdict: TRUE\n- Multiple sources confirm Paris is capital.")

    result = fc.fact_check_claim("The capital of France is Paris.")
    assert result["classification"] == "FACTUAL"
    assert "TRUE" in result["report"]
