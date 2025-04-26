"""Tools of the project."""

# %% IMPORTS

from markitdown import MarkItDown

# %% TOOLS


async def get_article_from_uri(uri: str) -> dict:
    """Get information for an online article from its URI.

    Args:
        uri (str): The URI of the online article to retrieve.

    Returns:
        dict: link, title and content in markdown format of the article.
    """
    try:
        mitd = MarkItDown()
        result = mitd.convert_uri(uri=uri)
        return {"link": uri, "title": result.title, "content": result.markdown}
    except Exception as error:
        return {
            "status": "error",
            "error": f"An error occurred while retrieving the article from '{uri}': {error}",
        }
