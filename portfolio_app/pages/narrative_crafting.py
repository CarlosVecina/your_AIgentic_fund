from dystopic_investment_aigents.agents.base_agents.agent_base import (
    Mood,
    Percentage,
    Personality,
)
from dystopic_investment_aigents.agents.discussion import Discussion
from dystopic_investment_aigents.agents.impl_agents.future_envision import (
    FutureScenario,
    DEFAULT_INITIAL_SCENARIOS,
    FutureSocraticAgent,
)
import streamlit as st

from dystopic_investment_aigents.utils.model_client_utils import OpenAIClientTraceable

# Initialize session state for selected scenario if it doesn't exist
if "selected_scenario" not in st.session_state:
    st.session_state.selected_scenario = None

# Initialize session state for current page if it doesn't exist
if "current_page" not in st.session_state:
    st.session_state.current_page = "scenario_selection"

scenarios = [FutureScenario(**scenario) for scenario in DEFAULT_INITIAL_SCENARIOS]

# Custom CSS for the selected button
st.markdown(
    """
    <style>
    .selected-button {
        background-color: #28a745;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 0.25rem;
        border: none;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        margin: 5px 3px;
        cursor: default;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Create columns for each scenario
cols = st.columns(len(scenarios))

# Display each scenario in its own column
if st.session_state.current_page == "scenario_selection":
    for col, scenario in zip(cols, scenarios):
        with col:
            with st.container():
                st.markdown("---")  # Horizontal line for separation

                # Show either 'Select' button or 'Selected' status
                if st.session_state.selected_scenario == scenario:
                    st.markdown(
                        '<button class="selected-button">Selected</button>',
                        unsafe_allow_html=True,
                    )
                else:
                    if st.button("Select", key=f"select_{scenario.name}"):
                        st.session_state.selected_scenario = scenario
                        st.rerun()

                st.markdown(
                    f"<h4 style='font-size: 16px;'>{scenario.name}</h4>",
                    unsafe_allow_html=True,
                )
                preview = (
                    scenario.description[:100] + "..."
                    if len(scenario.description) > 100
                    else scenario.description
                )
                st.markdown(
                    f"<div style='font-size: 14px;'>{preview}</div>",
                    unsafe_allow_html=True,
                )

                with st.expander("Read more"):
                    st.markdown(
                        f"<div style='font-size: 12px;'>...{scenario.description[100:]}</div>",
                        unsafe_allow_html=True,
                    )

    # Add a container for the Next button
    if st.session_state.selected_scenario:
        st.markdown("<br>", unsafe_allow_html=True)  # Add some spacing
        col1, col2, col3 = st.columns([1, 1, 1])
        with col3:  # Place button in the right column
            if st.button("Next →"):
                # You can add a new session state variable to track the current page
                st.session_state.current_page = "scenario_details"
                st.rerun()
elif st.session_state.current_page == "scenario_details":
    import time

    time.sleep(1)
    st.write("Let's discuss a bit...")

    # Initialize chat history if it doesn't exist
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Custom CSS for chat avatars and names
    st.markdown(
        """
        <style>
        .agent1-avatar {
            background-color: #FF6B6B !important;
        }
        .agent2-avatar {
            background-color: #4ECDC4 !important;
        }
        .chat-name {
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    master1 = FutureSocraticAgent(
        personality=Personality(
            mood=Mood.DYSTOPIC,
            risk_tolerance=Percentage(0.5),
        ),
        seniority=OpenAIClientTraceable(),
        seniority_args={
            "model": "gpt-4o-mini",
            "temperature": 0.5,
        },
    )

    master2 = FutureSocraticAgent(
        personality=Personality(
            mood=Mood.DYSTOPIC,
            risk_tolerance=Percentage(0.5),
        ),
        seniority=OpenAIClientTraceable(),
        seniority_args={
            "model": "gpt-4o-mini",
            "temperature": 0.5,
        },
    )

    # Only generate discussion if chat history is empty
    if not st.session_state.chat_history:
        discussion = Discussion(
            topic="Future of the world",
            max_turns=2,
            participants=[
                (
                    master1,
                    "how you envision the future the different main industries in this scenario? Which can of companies in this sector could be a good investment?",
                ),
                (master2, "Avoid evident calls and go further in the thought process"),
            ],
        )()

        # Store discussion in chat history with avatar classes
        for turn, (participant, response) in enumerate(discussion):
            avatar_class = "agent1-avatar" if turn % 2 == 0 else "agent2-avatar"
            display_name = f"Agent {turn + 1}"
            st.session_state.chat_history.append(
                {
                    "role": str(participant),
                    "content": response,
                    "avatar_class": avatar_class,
                    "display_name": display_name,
                }
            )

    # Display chat messages
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(
                f"<div class='chat-name'>{message['display_name']}</div>",
                unsafe_allow_html=True,
            )
            st.write(message["content"])

    # Add a back button if needed
    if st.button("← Back"):
        st.session_state.current_page = "scenario_selection"
        st.session_state.chat_history = []  # Clear chat history when going back
        st.rerun()
