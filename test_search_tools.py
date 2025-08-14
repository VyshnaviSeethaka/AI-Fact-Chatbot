import src.search_tools as st

def test_empty_query_returns_no_results(monkeypatch):
    assert st.search_web("") == []

def test_fetch_page_handles_bad_url():
    assert st.fetch_page("http://invalid.localhost/___nope___") in ("", None)
