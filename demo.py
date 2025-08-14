from src.fact_checker import fact_check_claim
from pathlib import Path

examples = Path(__file__).with_name("example_queries.txt").read_text(encoding="utf-8").splitlines()
for q in examples:
    if not q.strip():
        continue
    print("\n==============================")
    print("Claim:", q)
    res = fact_check_claim(q)
    print("Classification:", res["classification"])
    print("Report:\n", res["report"])
