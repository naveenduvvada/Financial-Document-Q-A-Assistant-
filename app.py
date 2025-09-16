import streamlit as st
from extract import process_file
from qa import answer_question

st.set_page_config(page_title="Financial Q&A", layout="wide")
st.title("📊 Financial Document Q&A Assistant")

uploaded = st.file_uploader("Upload a PDF or Excel file", type=["pdf","xlsx","xls"]) 

if uploaded:
    with st.spinner("Processing document..."):
        summary = process_file(uploaded)
    st.success("✅ Document processed")
    st.subheader("Extracted summary (preview)")
    st.write(summary)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.text_input("Ask a question about this document:")
    if question:
        answer = answer_question(question, summary, st.session_state.chat_history)
        st.session_state.chat_history.append({"q": question, "a": answer})

    for item in st.session_state.chat_history[::-1]:
        st.markdown(f"**Q:** {item['q']}\n\n**A:** {item['a']}")
