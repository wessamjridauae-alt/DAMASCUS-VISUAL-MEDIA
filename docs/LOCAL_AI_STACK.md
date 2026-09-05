# WESSAM LOCAL AI STACK

This stack is intentionally local-only. No paid model API, SaaS dependency, or cloud fallback is part of the supported examples.

## Components

### awesome-selfhosted/awesome-selfhosted
Role: catalog. It is not an application runtime. We use it to discover self-hosted software that can be installed on our own machine.

### ggml-org/llama.cpp
Role: local LLM runtime. llama.cpp runs GGUF language models on CPU and/or GPU and includes `llama-server`, an OpenAI-compatible local HTTP server.

### Significant-Gravitas/AutoGPT
Role: local agent/workflow layer. The current self-hosted AutoPilot path can use an OpenAI-compatible endpoint that you control. We point it at our own llama.cpp server instead of OpenAI/Anthropic/OpenRouter.

## Installation

Run:

```bash
bash scripts/install_local_ai_stack.sh
```

Default install root:

```text
~/wessam-local-stack/
  src/awesome-selfhosted/
  src/llama.cpp/
  src/AutoGPT/
  models/
  bin/
  local.env
```

The installer clones the three upstream projects and builds llama.cpp for CPU. Model weights are intentionally not bundled in this repository because GGUF files can be several GB. After a compatible GGUF model has been downloaded once and placed under `~/wessam-local-stack/models/`, inference can run offline.

## Start llama.cpp fully locally

Example with a small GGUF model already stored on disk:

```bash
~/wessam-local-stack/bin/llama-server \
  -m ~/wessam-local-stack/models/model.gguf \
  --host 127.0.0.1 \
  --port 8080 \
  -c 8192 \
  -ngl 0
```

No internet connection is needed after the model file and binaries are present.

## Local-only use cases

1. **Private document summarizer**
   Feed local `.txt` / extracted document text to `llama-cli` and ask for summaries, action items, or structured JSON. No document leaves the machine.

2. **Local Arabic writing assistant**
   Use a multilingual GGUF model to rewrite Arabic captions, emails, reports, property descriptions, or notes entirely offline.

3. **Local knowledge search**
   Index a folder locally with a lightweight script/database and send only retrieved local snippets to llama.cpp. This can become an offline Q&A system over your own files.

4. **Folder organizer agent**
   A local agent can inspect filenames and text metadata, propose categories, rename files, and move them between folders. All filesystem operations stay local.

5. **Local report generator**
   Read CSV/JSON/text data already on disk, calculate basic summaries with Python, then use llama.cpp to turn the results into a readable Arabic or English report.

6. **Offline coding/helper agent**
   Give AutoGPT access only to a sandbox project directory and the local llama.cpp endpoint. It can inspect files, draft code changes, write documentation, and run allowed local commands without using a cloud model.

7. **Self-hosted software scout**
   Search the local clone of `awesome-selfhosted` for categories such as CRM, finance, notes, monitoring, file transfer, document management, or automation. Shortlist projects without browsing the web.

8. **Local task decomposition**
   AutoGPT + llama.cpp can turn a goal into a sequence of local tasks, save the plan as files, inspect local project state, and iterate without an external model provider.

## Strict local-only rule

Supported examples must satisfy all of these:
- model inference happens on the user's own machine;
- data stays on the user's own machine;
- no OpenAI/Anthropic/OpenRouter/other paid LLM API;
- no SaaS dependency required to complete the task;
- internet may be used once to download source code/model files, but normal execution must work offline afterward.

## Current runtime note

The ChatGPT execution container used to prepare this repository currently has no terminal DNS/network access, so it cannot perform the three `git clone` operations inside this transient container. The installer and source locks are committed to the repository so the exact same setup can be executed on an internet-connected local machine. This limitation is recorded explicitly rather than pretending the source checkouts completed here.
