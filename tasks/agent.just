# run agent tasks
[group('agent')]
agent: agent-run

# debug the agent
[group('agent')]
agent-debug:
    uv run adk web

# run the agent
[group('agent')]
agent-run:
    uv run adk run {{SOURCES}}

# serve the agent
[group('agent')]
agent-serve:
    uv run adk api_server
