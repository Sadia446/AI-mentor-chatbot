from itertools import zip_longest
import streamlit as st
from streamlit_chat import message
from langchain_openai import ChatOpenAI  # correct import
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# --- Load API key and base URL from Streamlit secrets ---
openai_api_key = st.secrets["OPENROUTER_API_KEY"]
openai_api_base = st.secrets.get("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")

# Set Streamlit page config
st.set_page_config(page_title="Cognitia")
st.title("Cognitia")

# Initialize session state
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "entered_prompt" not in st.session_state:
    st.session_state["entered_prompt"] = ""

# Debug check
# st.write("API key loaded?", bool(openai_api_key))
# st.write("Base URL:", openai_api_base)

# --- Initialize ChatOpenAI with OpenRouter ---
chat = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",  # you can change to any model supported by OpenRouter
    temperature=0.5,
    openai_api_key=openai_api_key,
    openai_api_base=openai_api_base
)

# --- Build message history ---
def build_message_list():
    zipped_messages = [
        SystemMessage(
            content="""You are an AI Mentor. Your task is to provide career guidance, suggest relevant courses, and offer resume-building advice. The advice should be professional, encouraging, and helpful.

1. Greet the user politely and ask how you can assist them.
2. Provide informative and relevant responses to questions.
3. You must avoid discussing sensitive, offensive, or harmful content. Refrain from engaging in any such topics.
4. If the user asks about a topic unrelated to AI, politely steer the conversation back to career guidance or AI information.
5. Be patient and considerate when responding to user queries, and provide clear explanations.
6. If the user expresses gratitude or indicates the end of the conversation, respond with a polite farewell.
7. Do not generate long paragraphs in response. Maximum words should be 100.

Remember, your primary goal is to assist and educate students in the field of Artificial Intelligence."""
        )
    ]

    for human_msg, ai_msg in zip_longest(st.session_state["past"], st.session_state["generated"]):
        if human_msg is not None:
            zipped_messages.append(HumanMessage(content=human_msg))
        if ai_msg is not None:
            zipped_messages.append(AIMessage(content=ai_msg))

    return zipped_messages

# --- Generate AI Response ---
def generate_response():
    zipped_messages = build_message_list()
    ai_response = chat(zipped_messages)
    return ai_response.content

# --- Handle input submission ---
def submit():
    st.session_state.entered_prompt = st.session_state.prompt_input
    st.session_state.prompt_input = ""

# --- Input field ---
st.text_input("YOU:", key="prompt_input", on_change=submit)

# --- Process input and get response ---
if st.session_state.entered_prompt != "":
    user_query = st.session_state.entered_prompt
    st.session_state.past.append(user_query)
    output = generate_response()
    st.session_state.generated.append(output)

# --- Display chat history ---
if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")