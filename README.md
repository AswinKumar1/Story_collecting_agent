# Story Collecting Agent

## Overview
**Story Collecting Agent** is an AI-powered tool built using **Model Context Protocol (MCP)** with **Claude Desktop** (via stdio and HTTP).  
It collects **data points related to user NLP queries**, integrates with **Google Search** to fetch relevant stories, and organizes them into a **classified Excel format** stored locally.  

This project demonstrates how MCP-based agents can be integrated with search engines and structured storage to build a knowledge pipeline.

---

## Features
- Collects and processes **user NLP queries**  
- Fetches relevant information from **Google Search**  
- Stores results in **classified Excel spreadsheets** for easy analysis  
- Built with **MCP** for seamless integration with **Claude Desktop**  
- Dependency management using **uv** (faster, modern alternative to pip/venv)

---

## Getting Started

### Prerequisites
- **Python 3.10+**  
- [uv](https://github.com/astral-sh/uv) installed (for dependency management)  
- Claude Desktop with MCP enabled  

### Installation
Clone the repository:
```bash
git clone https://github.com/AswinKumar1/Story_collecting_agent.git
cd Story_collecting_agent
````

Install dependencies using **uv**:

```bash
uv sync
```

### Running the Application

Run the main agent:

```bash
uv run python main.py
```

(Optional) Run debug/testing scripts:

```bash
uv run python debug.py
uv run python test.py
```

---

## Project Structure

| File/Folder                 | Description                                        |
| --------------------------- | -------------------------------------------------- |
| `main.py`                   | Entry point for running the Story Collecting Agent |
| `debug.py`                  | Debugging utilities                                |
| `test.py`                   | Test scripts for validation                        |
| `classifier_learning.db`    | Database storing classification logic/data         |
| `us_freedom_stories.xlsx`   | Example dataset of collected stories               |
| `*.xlsx` files              | Output files containing classified stories         |
| `pyproject.toml`, `uv.lock` | Project metadata and uv dependency lock file       |

---

## How It Works

1. User enters a **query** (NLP text input).
2. Agent connects via **Claude Desktop MCP (stdio + HTTP)**.
3. Query is enriched and sent to **Google Search**.
4. Relevant stories/data are retrieved and classified.
5. Results are saved into structured **Excel files** locally.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you’d like to add features, improve docs, or fix bugs.

---

## License

This project is licensed under the MIT License.




