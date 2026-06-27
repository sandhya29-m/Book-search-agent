import streamlit as st
from main import agent_loop

st.set_page_config(
    page_title="Book Search Agent",
    page_icon="📚"
)

st.title("Book Search Agent")

st.write("Ask me about any book!")

query = st.text_input("Enter your question")

if st.button("Search"):

    if query.strip():

        with st.spinner("Searching..."):

            answer = agent_loop(query)

        st.success("Done!")

        st.write(answer)

    else:
        st.warning("Please enter a question.")