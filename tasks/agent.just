# run agent tasks
[group('agent')]
agent: agent-run

# run the agent API
[group('agent')]
agent-api:
    uv run adk api_server

# eval the agent
[group('agent')]
agent-eval:
    uv run adk eval {{SOURCES}} {{EVALS}}/*

# deploy the agent
[group('agent')]
agent-deploy: package-requirements
    cp requirements.txt {{SOURCES}} # required
    adk deploy cloud_run \
        --project={{env('GOOGLE_CLOUD_PROJECT')}} \
        --region={{env('GOOGLE_CLOUD_LOCATION')}} \
        --service_name={{SOURCES}} \
        --with_ui {{SOURCES}}

# run the agent
[group('agent')]
agent-run:
    uv run adk run {{SOURCES}}

# run the agent web UI
[group('agent')]
agent-web:
    uv run adk web --reload --reload_agents
