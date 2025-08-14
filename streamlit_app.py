# src/ui/streamlit_app.py

import sys
import os
import streamlit as st

# Ensure src is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.fact_checker import fact_check_claim

st.set_page_config(page_title="AI Fact-Checker Bot", page_icon="🕵️‍♂️", layout="wide")

st.title("🕵️ AI Fact-Checker Bot")
st.write("Enter a claim below, and I'll fact-check it using AI, web search, and credibility scoring.")

claim = st.text_area("✍️ Claim to check", height=100)

if st.button("Check Fact"):
    if not claim.strip():
        st.warning("⚠️ Please enter a claim before checking.")
    else:
        with st.spinner("🔍 Fact-checking... please wait"):
            try:
                result = fact_check_claim(claim)

                # Extract fields from result
                claim_text = result.get("claim", "N/A")
                classification = result.get("classification", "N/A")
                assumptions = result.get("assumptions", [])
                evidence_excerpt = result.get("evidence_excerpt", "No evidence found.")

                # ✅ Nicely formatted output
                st.markdown(f"### 📝 Claim:\n> {claim_text}")
                
                if classification.upper() == "FACTUAL":
                    st.markdown(f"### 📊 Classification: <span style='color:black;'>{classification}</span>", unsafe_allow_html=True)
                elif classification.upper() == "FALSE":
                    st.markdown(f"### 📊 Classification: <span style='color:green;'>{classification}</span>", unsafe_allow_html=True)
                else:
                    st.markdown(f"### 📊 Classification: <span style='color:orange;'>{classification}</span>", unsafe_allow_html=True)

                st.markdown("### 🔍 Assumptions:")
                for i, assumption in enumerate(assumptions, start=1):
                    st.write(f"{i}. {assumption}")

                st.markdown("### 📚 Evidence:")
                st.write(evidence_excerpt)

            except Exception as e:
                st.error(f"❌ Error: {e}")

st.caption("Powered by LLM + Web Search + Credibility Scoring")
