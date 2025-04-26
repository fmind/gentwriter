"""Scripts of the project."""

# %% IMPORTS

import logging

from gentwriter import configs

# %% CONFIGS

# APP_NAME = "weather_tutorial_app"
# USER_ID = "user_1"
# SESSION_ID = "session_001"
# DEFAULT_MESSAGE = "Hello, how can you help me?"


# %% LOGGING

LOGGING_LEVEL = logging.getLevelNamesMapping()[configs.LOGGING_NAME]

logging.basicConfig(
    level=LOGGING_LEVEL,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
)

# %% FUNCTIONS


def main() -> int:
    """Run the main script function."""
    # # state
    # state = {"user_preference_temperature_unit": "Celsius"}
    # # session
    # session_service = sessions.InMemorySessionService()
    # session = session_service.create_session(
    #     app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID, state=state
    # )
    # print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")
    # # runner
    # runner = runners.Runner(
    #     agent=agent.root_agent, app_name=APP_NAME, session_service=session_service
    # )
    # print(f"Runner created for agent '{runner.agent.name}'.")
    # # query
    # query = " ".join(sys.argv[1:]) if sys.argv and len(sys.argv) > 1 else DEFAULT_MESSAGE
    # print(sys.argv, query)
    # content = gt.Content(role="user", parts=[gt.Part(text=query)])
    # print(f"\n>>> User Query: {query}")
    # # events
    # for event in runner.run(user_id=USER_ID, session_id=session.id, new_message=content):
    #     if event.is_final_response():
    #         if event.content and event.content.parts:
    #             print(f"<<< Agent Response: {event.content.parts[0].text}")
    #         break
    return 0
