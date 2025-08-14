import argparse
import sys
import subprocess

def main():
    parser = argparse.ArgumentParser(description="AI Fact Checker Bot Launcher")
    parser.add_argument(
        "--mode",
        type=str,
        default="cli",
        choices=["cli", "streamlit", "gradio"],
        help="Interface to run: cli | streamlit | gradio",
    )
    parser.add_argument(
        "claim",
        type=str,
        nargs="?",
        help="Claim to fact-check (required for CLI mode)",
    )
    args = parser.parse_args()

    if args.mode == "cli":
        if not args.claim:
            print("Usage: python main.py --mode cli '<claim>'")
            sys.exit(1)
        from src.ui.cli import main as cli_main
        # pass single positional claim to CLI module
        sys.argv = ["cli.py", args.claim]
        cli_main()

    elif args.mode == "streamlit":
        subprocess.run(["streamlit", "run", "src/ui/streamlit_app.py"])

    elif args.mode == "gradio":
        from src.ui.gradio_app import launch_app
        launch_app()

if __name__ == "__main__":
    main()
