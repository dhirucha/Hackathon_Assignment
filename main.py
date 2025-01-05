
import json
import requests
import streamlit as st
from streamlit_chat import message as st_message 
import os
from dotenv import load_dotenv

load_dotenv()


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "711e5f10-89f4-45dc-b683-7861cc2ff0cc"
FLOW_ID = "7fc1aed6-b351-487c-913a-5562853e7de1"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "analysis-1" # You can set a specific endpoint name in the flow settings



def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Main function
def main():
    st.set_page_config(
        page_title="Social Media Performance Analysis",
        page_icon="📊",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    # Header section
    st.markdown(
        """
        <style>
        .title-style {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 20px;
        }
        .subtitle-style {
            text-align: center;
            font-size: 18px;
            color: #6c757d;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="title-style">📊 Social Media Performance Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-style">Get insights into your social media strategies!</div>', unsafe_allow_html=True)

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Input section
    st.markdown("---")
    st.markdown("### 💬 Enter a post type to get insights:")
    message = st.text_area("", placeholder="Post type (e.g. reels, carousel, static images)...", height=100)

    # Button to send the query
    if st.button("🔍 Get Insights"):
        if not message.strip():
            st.error("🚫 Please enter a message.")
        else:
            try:
                with st.spinner("⏳ Running analysis..."):
                    response = run_flow(message)  # Simulated function call
                    response_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]

                # Add new message at the top of the history
                st.session_state["messages"].insert(0, {"user": message, "bot": response_text})

            except Exception as e:
                st.error(f"⚠ An error occurred: {str(e)}")

    # Display chat messages, latest at the top
    st.markdown("---")
    for i, msg in enumerate(st.session_state["messages"]):
        st_message(msg["user"], is_user=True, key=f"user_{i}")
        st_message(msg["bot"], is_user=False, key=f"bot_{i}")

    # Footer section
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; font-size: 14px; color: #6c757d;">
        Made by TechTea Team
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()