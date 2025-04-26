"""Schemas of the project."""

# %% IMPORTS

import pydantic as pdt

# %% SCHEMAS


class Article(pdt.BaseModel):
    """Schema of an online article."""

    link: str = pdt.Field(description="The link of the article.")
    title: str = pdt.Field(description="The title of the article.")
    content: str = pdt.Field(description="The content of the article in markdown.")
