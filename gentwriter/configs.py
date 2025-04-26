"""Configs of the project."""

# %% IMPORTS

import os

# %% CONFIGS

PREFIX = "GENTWRITER"

LLM_MODEL = os.getenv(f"{PREFIX}_LLM_MODEL", "gemini-2.0-flash")

LOGGING_NAME = os.getenv(f"{PREFIX}_LOGGING_LEVEL", "INFO")

TARGET_AUDIENCE = os.getenv(
    f"{PREFIX}_TARGET_AUDIENCE",
    "Professionals in the tech industry, including AI Engineers, Data Scientists, Developers, and Technical Managers.",
)

USER_PERSONA = os.getenv(
    f"{PREFIX}_USER_PERSONA",
    "You write as an AI Engineer/Architect working at Decathlon, passionate about AI, Generative AI, MLOps, and sharing technical insights with peers.",
)
