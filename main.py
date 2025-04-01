# import os
# from dotenv import load_dotenv

# from groq import Groq
# load_dotenv()

# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )
# prompt = input("Enter your que.")
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )



import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Set up Streamlit page config
st.set_page_config(page_title="Groq Chat Interface", page_icon="💬")
st.title("Chat with Groq LLM")

# Create a text input for user messages
user_input = st.text_input("Enter your message:", key="user_input")

# Create a button to send the message
if st.button("Send"):
    if user_input:
        with st.spinner("Generating response..."):
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            # Display the response
            st.write("Response:", chat_completion.choices[0].message.content)
    else:
        st.warning("Please enter a message!")