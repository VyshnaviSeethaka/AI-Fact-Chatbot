import gradio as gr
from src.fact_checker import fact_check_claim

def run(claim: str):
    if not claim.strip():
        return "Please enter a claim.", "", "", ""
    res = fact_check_claim(claim)
    return (res["report"], res["classification"], "\n".join(res["assumptions"]), res["evidence_excerpt"])

def launch_app():
    iface = gr.Interface(
        fn=run,
        inputs=[gr.Textbox(label="Claim", lines=3)],
        outputs=[
            gr.Textbox(label="Report"),
            gr.Textbox(label="Classification"),
            gr.Textbox(label="Assumptions"),
            gr.Textbox(label="Evidence Excerpt"),
        ],
        title="AI Fact-Checker Bot",
        description="Fact-checks a claim using OpenAI + web search."
    )
    iface.launch()

if __name__ == "__main__":
    launch_app()
