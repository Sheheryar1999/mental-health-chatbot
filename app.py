import streamlit as st


# Must Use Model off of hugging face directly as I cant load into local

def get_bot_response(user_input):
    return "This is a placeholder response from the chatbot."

def main():
    st.title("Chatbot Tester")
    user_input = st.text_input("Enter your message here:")

    if st.button("Send"):
        bot_response = get_bot_response(user_input)
        st.text_area("Chatbot:", value=bot_response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()
