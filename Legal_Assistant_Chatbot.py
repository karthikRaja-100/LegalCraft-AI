import streamlit as st
import pandas as pd


csv_file_path = "CHATBOT_Q&A.csv"
df = pd.read_csv(csv_file_path)


question_to_answer = {row['Question']: row['Answer'] for _, row in df.iterrows()}


questions = df['Question'].tolist()


def chatbot_response(input_text):
    if input_text in question_to_answer:
        response = question_to_answer[input_text]
    else:
        response = "Sorry, I don't know the answer to that question."
    return response 


def main():
    st.set_page_config(page_title="Legal Assistant Chatbot",page_icon="🤖")
    st.header("LegalCraft-Legal Assistant Chatbot")

    user_question = st.text_input("Ask a Question from your legal friend")

    if user_question:
        output=chatbot_response(user_question)
    
   
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            st.write(output)
            st.success("Done")



if __name__ == "__main__":
    main()