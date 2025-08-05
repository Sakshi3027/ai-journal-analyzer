import streamlit as st
from journal_analyzer import analyze_journal

st.set_page_config(page_title="AI Journal Analyzer", layout="centered")

st.title("AI Daily Journal Analyzer")
st.markdown("Analyze your journal entries for mood and themes using GPT-4o.")

# Text input
journal_entry = st.text_area("Write or paste your journal entry here:", height=250)

# Dropdown for analysis depth
depth = st.selectbox("Select analysis depth:", ["brief", "detailed"])

# Button to analyze
if st.button("Analyze Entry"):
    if not journal_entry.strip():
        st.warning("Please enter a journal entry.")
    else:
        with st.spinner("Analyzing..."):
            result = analyze_journal(journal_entry, depth)
            st.success("Analysis complete.")
            st.markdown("### Insights")
            st.markdown(result)