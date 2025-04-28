"""Configs of the project."""

# %% IMPORTS

import os

# %% CONFIGS

PREFIX = "GENTWRITER"

LLM_MODEL = os.getenv(f"{PREFIX}_LLM_MODEL", "gemini-2.0-flash")

LOGGING_NAME = os.getenv(f"{PREFIX}_LOGGING_LEVEL", "INFO")
