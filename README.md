# GentWriter 🖋️

[![Build Status](https://github.com/fmind/gentwriter/actions/workflows/check.yml/badge.svg)](https://github.com/fmind/gentwriter/actions/workflows/check.yml)
[![Publish Status](https://github.com/fmind/gentwriter/actions/workflows/publish.yml/badge.svg)](https://github.com/fmind/gentwriter/actions/workflows/publish.yml)
[![Documentation](https://img.shields.io/badge/documentation-available-brightgreen.svg)](https://fmind.github.io/gentwriter/)
[![License](https://img.shields.io/github/license/fmind/gentwriter)](https://github.com/fmind/gentwriter/blob/main/LICENSE.txt)
[![Release](https://img.shields.io/github/v/release/fmind/gentwriter)](https://github.com/fmind/gentwriter/releases)

**GentWriter** is an AI-powered agent designed to automatically generate various social media content based on an input article URL.

It leverages Large Language Models (LLMs) via the [Google AI SDK](https://google.github.io/adk-docs/) to create tailored posts for different platforms.

## ✨ Features

* **Article Fetching:** Retrieves the content and title of an article from a given URL.
* **SEO Meta Description Generation:** Creates concise, keyword-focused meta descriptions suitable for search engines.
* **X.com (Twitter) Post Generation:** Crafts short, engaging tweets summarizing the article, including relevant hashtags and the article link.
* **LinkedIn Post Generation:** Generates professional LinkedIn posts highlighting key insights from the article, tailored for a professional audience, and includes the article link.
* **Modular Agent Design:** Built using the `google-adk` framework, organizing different functionalities into distinct agents (retrieval, SEO, X, LinkedIn) managed by a sequential workflow.
* **Configurable:** Allows setting the underlying LLM model via environment variables.

## ⚙️ Setup & Installation

1.  **Clone the repository:**

```bash
git clone https://github.com/fmind/gentwriter
cd gentwriter
```

2.  **Install dependencies:**

```bash
uv sync
```

3.  **Authentication:**

This project uses Google Generative AI. Ensure you have authenticated your environment for Google Cloud access. This typically involves:
* Installing the Google Cloud CLI (`gcloud`).
* Running `gcloud auth application-default login`.
* Ensure the necessary APIs (like Vertex AI) are enabled in your Google Cloud project.

## 🔧 Configuration

The application uses environment variables for configuration:

- `GENTWRITER_LLM_MODEL`: Specifies the Google Generative AI model to use (defaults to `gemini-2.0-flash`).
- `GENTWRITER_LOGGING_LEVEL`: Sets the logging level (e.g., `INFO`, `DEBUG`).

## 🚀 Usage

- **`just agent-api`**: start an API server based on FastAPI.
- **`just agent-eval`**: evaluate the agent against an evaluation set.
- **`just agent-deploy`**: deploy the agent to Google Cloud Run.
- **`just agent-run`**: run the agent locally from the CLI.
- **`just agent-web`**: run the web UI locally.

## 🧪 Testing

The project includes unit tests. To run them:

1. Navigate to the project's root directory.
2. Install development dependencies
3. Run the following command:

```bash
just check
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE.txt file for details.
