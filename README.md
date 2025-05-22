---
title: OSINT_Investigator
app_file: app.py
sdk: gradio
sdk_version: 5.30.0
---
# OSINT_Investigator

**OSINT_Investigator** is an Open Source Intelligence (OSINT) application designed to help identify potential money laundering red flags associated with individuals and businesses. It leverages the CrewAI framework for multi-agent collaboration, Serper API for web searches, and modern LLMs for analysis and reporting. The user interface is powered by Gradio, making it easy to deploy and use on platforms like Hugging Face Spaces.

## Features

- **Multi-Agent AI System:** Built with CrewAI, enabling Research, Analysis, and Reporting agents to collaborate on investigations.
- **Automated Web Intelligence Gathering:** Integrates Serper web search for comprehensive data collection.
- **LLM-Powered Analysis:** Uses large language models to analyze collected information and generate structured reports.
- **User-Friendly Gradio Interface:** Easily input target names and affiliations, and receive clear, actionable risk assessments.
- **Ready for Hugging Face Spaces:** Out-of-the-box compatibility for online deployment and sharing.

## Demo

Try the live app on [Hugging Face Spaces](https://huggingface.co/spaces/raznis/OSINT_Investigator) (if available).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/raznis/OSINT_Investigator.git
   cd OSINT_Investigator
   ```

2. **Install dependencies:**
   ```bash
   pip install uv
   uv pip install -r requirements.txt
   ```

3. **Set up API keys:**
   - Create a `.env` file and add your required API keys (e.g., `OPENAI_API_KEY`).

4. **Run locally:**
   ```bash
   uv run app.py
   ```
   This launches the Gradio interface in your browser.

## Usage

1. Enter the target's name and known affiliations.
2. Click **Investigate**.
3. Review the generated risk assessment and supporting research.

## Configuration

- **Agents and Tasks:** Customize `src/investigators/config/agents.yaml` and `tasks.yaml` to define different agent roles and task flows.
- **Logic and Tools:** Extend or modify the agent logic in `src/investigators/crew.py`.
- **Frontend:** The Gradio interface is defined in `app.py`.

## Project Structure

```
app.py                   # Main Gradio app and entry point
requirements.txt         # Python dependencies
investigators/           # CrewAI agent logic, configs, and documentation
  └─ src/investigators/
      ├─ crew.py         # Main CrewAI logic
      ├─ config/         # YAML config files for agents and tasks
      └─ ...             # Additional supporting code and docs
README.md                # This file
```

## Requirements

- Python >=3.10, <3.13
- CrewAI, Gradio, OpenAI, and related dependencies (see `requirements.txt`)
- API access for LLMs and Serper

## Acknowledgements

- [CrewAI](https://crewai.com)
- [Gradio](https://gradio.app)
- [OpenAI](https://openai.com)

## License

MIT License

---
