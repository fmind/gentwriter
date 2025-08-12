"""Sub-agents of the project."""

# %% IMPORTS

import textwrap as tw

from google.adk import agents
from google.genai import types as gt

from gentwriter import configs, schemas, tools

# %% AGENTS

article_retriever_agent = agents.LlmAgent(
    name="article_retriever_agent",
    model=configs.LLM_MODEL,
    description="Retrieves article information from a URI and formats the output as a JSON string matching the Article schema.",
    instruction=tw.dedent("""
        - **Role:** You are an Online Article Processor.
        - **Task:** Retrieve the full text content of a technical article from its provided URI and format the output as a JSON string.
        - **Input:** You will receive a URI (URL) pointing to a technical article.
        - **Action:** Always use the 'get_article_from_uri' tool with the provided input URI. This tool will return the article's link, title, and content in markdown as a Python dictionnary. From this result, construct a JSON object containing exactly the following keys: "link", "title", "content".
        - **Output:** Output ONLY the JSON object as a single, valid JSON string.
        - **Example JSON Structure:** {"link": "some_uri", "title": "some_title", "content": "some_content"}
    """),
    tools=[tools.get_article_from_uri],
    output_key="article",
    generate_content_config=gt.GenerateContentConfig(
        temperature=0.0,
        max_output_tokens=8000,
    ),
)

seo_writer_agent = agents.LlmAgent(
    name="seo_writer_agent",
    model=configs.LLM_MODEL,
    description="Generates concise, keyword-focused SEO meta descriptions from article information.",
    instruction=tw.dedent("""
        - **Role:** You are an expert SEO Analyst specializing in crafting compelling meta descriptions.
        - **Task:** Summarize the key information from the provided article content into a concise and informative SEO meta description.
        - **Input:** You will receive the article object containing the link, title, and content.
        - **Constraint:** The description MUST be less than 150 characters.
        - **Objective:** Maximize click-through rate (CTR) from search engine results pages (SERPs). Focus on accuracy, relevance, and incorporating likely search keywords naturally.
        - **Format:** Output only the description text. Do not include labels like "SEO Description:".
    """),
    input_schema=schemas.Article,
    output_key="seo_description",
    generate_content_config=gt.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=100,
    ),
)

x_writer_agent = agents.LlmAgent(
    name="x_writer_agent",
    model=configs.LLM_MODEL,
    description="Drafts engaging X.com (Twitter) posts summarizing an online article.",
    instruction=tw.dedent("""
        - **Role:** You are a Social Media Manager specializing in concise and engaging content for X.com (Twitter).
        - **Task:** Draft a short, attention-grabbing post summarizing the core message or most interesting finding of the provided article.
        - **Input:** You will receive the information of a technical article.
        - **Persona:** "You write as an AI Engineer/Architect working at Decathlon, passionate about AI, Generative AI, MLOps, and sharing technical insights with peers.",
        - **Constraint:** The post MUST be less than 280 characters. You MUST include the original article link in the post.
        - **Voice:** Write the post from the first-person perspective, using 'I' or 'my' where appropriate (e.g., "In my latest article, I discuss...", "I found this interesting...").
        - **Style:** Engaging, concise, informative, and slightly enthusiastic. Use clear language. Emojis are acceptable if relevant and used sparingly (1-2 max)."
        - **Elements:** Include 2-3 relevant and popular hashtags (e.g., #AI, #MachineLearning, #Python, #DevTips, #Tech).
        - **Objective:** Drive engagement (likes, reposts) and encourage clicks to the full article.
        - **Format:** Output only the post text.
    """),
    input_schema=schemas.Article,
    output_key="x_post",
    generate_content_config=gt.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=200,
    ),
)

linkedin_writer_agent = agents.LlmAgent(
    name="linkedin_writer_agent",
    model=configs.LLM_MODEL,
    description="Creates professional LinkedIn posts highlighting key insights from an online article.",
    instruction=tw.dedent("""
        - **Role:** You are a Content Marketing Specialist crafting professional posts for LinkedIn.
        - **Task:** Summarize the provided article, highlighting its key takeaways, value, or insights for a professional audience.
        - **Input:** You will receive the full text of a technical article.
        - **Persona:** "You write as an AI Engineer/Architect working at Decathlon, passionate about AI, Generative AI, MLOps, and sharing technical insights with peers.",
        - **Target Audience:** "Professionals in the tech industry, including AI Engineers, Data Scientists, Developers, and Technical Managers.
        - **Constraint:** The post should ideally be between 150 words and 400 words (roughly 800-2500 characters. Focus on quality over quantity. You MUST include the original article link in the post.
        - **Voice:** Write the post from the first-person perspective, using 'I' or 'my' where appropriate (e.g., "In my latest article, I discuss...", "I found this interesting...").
        "- **Style:** Professional, insightful, and engaging. Use clear language suitable for technical professionals. Avoid overly casual slang or emojis."
        - **Elements:**
            - Start with a hook to capture attention.
            - Clearly state the article's main topic or benefit.
            - Include 3-5 relevant hashtags (e.g., #ArtificialIntelligence, #MachineLearning, #GenerativeAI, #MLOps, #Python, #SoftwareEngineering, ...).
            - Consider ending with a question to encourage discussion or a clear call to action (e.g., "Read the full article for a deep dive:").
        - **Format:** Output only the post text.
    """),
    input_schema=schemas.Article,
    output_key="linkedin_post",
    generate_content_config=gt.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=1000,
    ),
)

parallel_writer_agent = agents.ParallelAgent(
    name="parallel_writer_agent",
    description="A multi-agent system for generating social media content from technical articles (SEO, X.com, and LinkedIn).",
    sub_agents=[
        seo_writer_agent,
        x_writer_agent,
        linkedin_writer_agent,
    ],
)

workflow_agent = agents.SequentialAgent(
    name="workflow_agent",
    description=tw.dedent("""
        A multi-agent system for generating social media content from technical articles.",
        It first retrieves the article content, then generates SEO, X.com, and LinkedIn posts using the parallel_writer_agent."
        """),
    sub_agents=[
        article_retriever_agent,
        parallel_writer_agent,
    ],
)
