# %% IMPORTS

from gentwriter import schemas

# %% SCHEMAS


def test_article_schema():
    # given
    title = "Title"
    link = "http://blog.com/article"
    content = "# My Article"
    # when
    article = schemas.Article(title=title, link=link, content=content)
    # then
    assert article.title == title
    assert article.link == link
    assert article.content == content
