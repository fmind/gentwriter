# %% IMPORTS

from gentwriter import tools

# %% TOOLS


async def test_get_article_from_uri():
    # given
    uri = "https://fmind.dev"
    # when
    result = await tools.get_article_from_uri(uri=uri)
    # then
    assert result.keys() == {"link", "title", "content"}
    assert result["link"] == uri


async def test_get_article_from_uri__error():
    # given
    uri = "fmind.dev"
    # when
    result = await tools.get_article_from_uri(uri=uri)
    # then
    assert result.keys() == {"status", "error"}
    assert result["status"] == "error"
    assert result["error"].startswith(
        "An error occurred while retrieving the article from 'fmind.dev': Unsupported URI scheme"
    )
