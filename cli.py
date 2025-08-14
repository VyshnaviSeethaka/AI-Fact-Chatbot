import sys
from src.fact_checker import fact_check_claim

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.ui.cli '<claim>'")
        sys.exit(1)

    claim = sys.argv[1]
    result = fact_check_claim(claim)

    print("\n=== Fact-Check Result ===")
    print("Claim:", result["claim"])
    print("Classification:", result["classification"])
    print("Assumptions:", result["assumptions"])
    print("Credibility (0-1):", result["credibility"])
    print("\nReport:\n", result["report"])
    # If needed:
    # print("\nEvidence excerpt:\n", result["evidence_excerpt"])

if __name__ == "__main__":
    main()
