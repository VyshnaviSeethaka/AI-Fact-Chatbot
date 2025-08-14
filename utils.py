def credibility_score(evidence: str) -> float:
    """
    Simple placeholder credibility heuristic:
    - longer aggregated evidence => slightly higher confidence.
    Returns float in [0, 1].
    """
    length = len(evidence or "")
    if length <= 0:
        return 0.0
    return min(length / 4000.0, 1.0)
