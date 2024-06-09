# Precision RAG: Automatic Prompt Engineering for Enterprise LLMs

This repository contains the development of a system for Automatic Prompt Engineering (APE), designed to optimize the use of large language models (LLMs) in various business applications.

## Overview

The goal of this project is to create an APE system that can:

- Automatically generate effective prompts for LLMs, tailored to specific tasks and objectives.
- Evaluate the quality of prompts through rigorous testing and ranking mechanisms.
- Provide a user-friendly interface for interacting with the system, enabling users to easily input objectives, receive generated prompts, and view evaluation results.

## Key Features

- **Retrieval-Augmented Generation (RAG) focus:** Leverages RAG techniques to enhance prompt effectiveness and relevance for enterprise LLMs.
- **Customizable prompt generation:** Generates multiple prompt options based on user input and desired outcomes.
- **Automatic test case generation:** Creates diverse test cases to evaluate prompts in various scenarios.
- **Comprehensive prompt testing and ranking:** Employs Monte Carlo matchmaking and ELO rating systems (or alternative methods) for robust evaluation.
- **User-friendly interface:** Facilitates easy data input, prompt output, and result visualization.
- **Integration with LLMs:** Seamlessly integrates with LLMs like GPT-4 and GPT-3.5-Turbo for prompt testing and application.

## Technical Requirements

- **Programming languages:** Python, Streeamlite (for UI)
- **Libraries and frameworks:** Langchain
- **LLM access:** Requires access to LLM APIs (e.g., GPT-4, GPT-3.5-Turbo) for prompt testing and application.


## Getting Started

1. Clone this repository:

```sh
git clone https://github.com/Wandera-Martin/RAG-Systems
cd RAG-Systems
```

2. Setup environment variables on `.env`:

(create .env file in the [Title](Makefile)root directory)

```bash
#################
# Development env
#################

OPENAI_API_KEY=""
VECTORDB_MODEL="gpt-3.5-turbo"
```


# Installation

**Run**

```bash
# create virtual environment
python3 -m venv venv

# activate
source venv/bin/activate

# install requirements
pip install -r requirements.txt

```

## Contribution Guidelines
We welcome contributions from the community. Feel free to open issues, submit pull requests, and collaborate with us to improve the toolkit.

## License
This project is licensed under the [MIT License](LICENSE.md).

Let's optimize language models together! 🚀