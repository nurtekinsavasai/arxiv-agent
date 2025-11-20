# Arxiv.org Agent

An LLM powered research assistant that finds, ranks, and explains recent AI papers on arxiv.org.

It fetches recent `cs.AI` and `cs.LG` papers, selects candidates with embeddings, classifies relevance with an LLM, predicts 1 year citation counts, and gives you a ranked, annotated digest with plain English summaries.

---

## Features

- 🔍 **Natural language research brief**  
  Describe what you are looking for and optionally what you are not interested in.  
  If you leave both fields empty the agent switches to a global mode and looks for the most impactful recent `cs.AI` and `cs.LG` papers overall.

- 📡 **Automatic arXiv fetching**  
  Fetches up to about 5000 papers in a date window from the `cs.AI` and `cs.LG` categories on arxiv.org.

- 🧭 **Embedding based candidate selection**  
  In targeted mode it uses OpenAI embeddings (`text-embedding-3-large`) to find the papers that are closest in meaning to your brief and keeps the top 150 candidates.  
  In global mode it simply takes the most recent 150 papers.

- 🧮 **LLM relevance classification**  
  In targeted mode an LLM reads each candidate and labels it as:
  - `primary`  main contribution directly matches your brief  
  - `secondary` your topic is only a minor part or example  
  - `off topic` not really about your brief  

- 🎯 **Prediction set construction**  
  The agent builds a prediction set for citation estimation:
  - Keeps all `primary` papers  
  - If there are fewer than about 20, it tops up with the strongest `secondary` papers  
  - In global mode all candidates are used  

- 📈 **1 year citation predictions**  
  For each paper in the prediction set an LLM estimates how many citations it might receive one year after publication, based on topic trendiness, novelty, depth, and breadth of audience.

- 🧾 **Plain English summaries**  
  For the top N ranked papers the agent generates a non technical summary so a smart reader without ML background can follow.

- 💾 **Full artifact export**  
  All intermediate artifacts and a markdown report are saved under  
  `~/arxiv_ai_digest_projects/project_<timestamp>/` and can be downloaded as a ZIP.

---

## Installation

You can install the package directly from the public GitHub repo:

```bash
pip install "git+https://github.com/YOUR_USER/arxiv-agent.git"
```

### Development install (recommended if you plan to modify the code)

```bash
git clone https://github.com/YOUR_USER/arxiv-agent.git
cd arxiv-agent

python3 -m venv .venv
source .venv/bin/activate

pip install -e .
```

## Running the App

Start the UI using the packaged command:

```bash
arxiv-agent
```

This launches the Streamlit UI in your browser.

Or run it explicitly with Streamlit:

```bash
streamlit run arxiv_agent/app.py
```

## OpenAI API Key

The app uses the OpenAI API for:

- Chat models for relevance classification
- Chat models for 1-year citation prediction
- Chat models for plain English summaries
- `text-embedding-3-large` for semantic similarity

You provide your API key in the sidebar.

**Important notes about the key:**

- It is used only in memory for the active session
- It is never written to disk
- It is never logged or exported in any artifact
- You are billed directly by OpenAI under your own account

## Current Limitations & Ethical Notes

- Citation predictions are heuristics, not ground-truth forecasts
- Predictions may reflect existing academic biases
  (Large labs, English-language venues, trendy areas, etc.)
- The tool is meant for exploration and inspiration, not evaluating people or institutions
- Always verify results by reading the actual papers
