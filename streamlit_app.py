
import streamlit as st

# Define the pipeline tasks and AI involvement
tasks = [
    {
        "name": "Checkout repo at PR branch",
        "ai_vibe": "✅ AI-Approved",
        "description": "Automatable with scripts; AI can assist with smart branching strategies."
    },
    {
        "name": "Collect updates, changed files, commit messages",
        "ai_vibe": "✅ AI-Approved",
        "description": "AI can summarize diffs, extract intent from commit messages, and flag anomalies."
    },
    {
        "name": "Install dependencies, build artefacts",
        "ai_vibe": "⚠️ AI-Assisted",
        "description": "AI can optimize builds or detect dependency issues, but actual install/build is better left to deterministic tools."
    },
    {
        "name": "Run unit and integration tests",
        "ai_vibe": "✅ AI-Approved",
        "description": "AI can prioritize tests, detect flaky ones, and analyze test coverage."
    },
    {
        "name": "Draft Push summary: scope, risky areas, files touched",
        "ai_vibe": "✅ AI-Approved",
        "description": "AI excels at summarizing changes and highlighting potential risks."
    },
    {
        "name": "Human reviewer approval of the push",
        "ai_vibe": "❌ Human-Only",
        "description": "Code review needs human judgment, ethics, and domain expertise. AI can assist, but not replace."
    },
    {
        "name": "Merge and deploy to production",
        "ai_vibe": "⚠️ AI-Assisted",
        "description": "AI can suggest optimal timing or detect merge conflicts, but final deploy should be controlled."
    },
    {
        "name": "Monitoring behavior and issues in production",
        "ai_vibe": "✅ AI-Approved",
        "description": "AI is great at anomaly detection, log analysis, and predictive alerts."
    }
]

# Streamlit app layout
st.set_page_config(page_title="DevOps AI Vibe Check", layout="centered")
st.title("🚀 DevOps Pipeline – AI Vibe Check")

for task in tasks:
    with st.expander(f"{task['name']} ({task['ai_vibe']})"):
        st.write(task['description'])

st.markdown("---")
st.caption("Click on each task to view how AI fits into the pipeline.")
