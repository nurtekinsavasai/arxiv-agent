# Arxiv.org Agent

An LLM powered research assistant that finds, ranks, and explains recent AI papers on arxiv.org.

Describe what you want
You write a short research brief in natural language about the kind of work you care about, and optionally what you are not interested in. If you leave both fields empty, the agent switches to a global mode and just looks for the most impactful recent cs.AI + cs.LG papers overall.

The agent fetches recent arXiv papers
It fetches up to about 5000 papers from arxiv.org in the Artificial Intelligence and Machine Learning categories (cs.AI and cs.LG) for the date range you choose.

The agent picks candidate papers
In targeted mode, the agent uses OpenAI embeddings (text-embedding-3-large) to measure how close each paper's title and abstract are to your brief in meaning and keeps the top 150 as candidates.
In global mode, it simply takes the most recent 150 cs.AI + cs.LG papers as candidates.
The agent judges how relevant each paper is
In targeted mode an LLM reads each candidate and labels it as:

primary: the main contribution directly matches your brief
secondary: your topic is only a minor part or example
off topic: not really about your brief
In global mode all candidates are treated as primary and this step is skipped.

The agent builds a prediction set
The agent builds a set of papers to send to the citation-prediction step:

It keeps all primary papers.
If there are fewer than about 20, it tops up with the strongest secondary papers until it reaches roughly 20, when possible.
In global mode, all candidates are used.
The agent predicts 1-year citation counts
For each paper in the prediction set, an LLM estimates how many citations it might receive one year after publication, based on factors like topic trendiness, novelty, depth, and potential audience size. These predictions are heuristic impact signals and are best used for ranking within this batch, not as ground truth.

The agent ranks, summarizes, and saves results
The agent ranks papers by predicted citation count, always showing primary papers first, then secondary ones. For the top N that you choose, it shows a plain English summary, relevance explanation, and links to arXiv and the PDF. All intermediate artifacts and a markdown report are saved in a project folder under ~/arxiv_ai_digest_projects/project_<timestamp>, and you can download everything as a ZIP.

## Local usage

```bash
pip install arxiv-agent
pip3 install arxiv-agent
arxiv-agent

