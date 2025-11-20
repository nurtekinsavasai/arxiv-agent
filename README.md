# Arxiv.org Agent

An LLM powered research assistant that finds, ranks, and explains recent AI papers on arxiv.org.

▶️ **Watch a demo**: https://youtu.be/PqJiYTvOP1M

## 🚀 Try it Online (no installation needed)

You can use the hosted Streamlit version here:

👉 **https://arxiv-agent-atclu7bhsjhbqjk8lndeus.streamlit.app/**

You'll provide your own OpenAI API key in the sidebar.  
Your key is used only in memory for the session and never saved or logged.

---

## 📦 Install Locally (via PyPI)

```bash
pip install arxiv-ai-agent
```

Then launch the app:

```bash
arxiv-ai-agent
```

This will start the Streamlit interface and open it in your browser (or show you a Local URL if the browser does not auto-launch).

## 💻 Install from GitHub (development mode)

```bash
git clone https://github.com/nurtekinsavasai/arxiv-agent.git
cd arxiv-agent

python3 -m venv .venv
source .venv/bin/activate

pip install -e .
```

Then run:

```bash
arxiv-ai-agent
```

## 🔑 OpenAI API Key

The app uses the OpenAI API for:

- Relevance classification
- Citation prediction
- Plain-English paper summaries
- Embeddings (`text-embedding-3-large`)

Your key is:

- Provided manually in the sidebar
- Used only for the active session
- Never saved
- Never exported
- Never written to disk

You are billed directly under your own OpenAI account.

## 📚 What the Agent Does

**You provide:**

- A short research brief in natural language
- Optional exclusions (things you don't want)
- A date range (3 days, 7 days, or 30 days)

**The agent:**

- Fetches recent `cs.AI` + `cs.LG` papers from arXiv
- Uses embeddings to rank semantic similarity
- Uses an LLM to classify papers as primary, secondary, or off-topic
- Selects ~20 promising papers
- Predicts 1-year citation impact using an LLM
- Ranks papers by predicted influence

**Provides:**

- Paper metadata
- Abstract
- PDF link
- Plain-English summary
- Explanation of the citation prediction
- Lets you download all artifacts as a ZIP

## ⚠️ Limitations & Ethical Notes

- Citation predictions are heuristic and approximate.
- They may reflect academic biases, trends, and popularity.
- This tool is for exploration and inspiration — not formal evaluation of researchers, institutions, or grant proposals.
- Always read the actual papers before relying on any automated ranking.

## 🧭 Future Work

- Expand beyond `cs.AI` + `cs.LG`
- Support more LLM providers and models
- Add multi-step agentic reasoning
- Add full background workflows for autonomous research assistants
- Enhance citation prediction framework
