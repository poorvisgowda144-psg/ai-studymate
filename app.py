import streamlit as st
import re
from collections import Counter

st.set_page_config(page_title="AI StudyMate", page_icon="📚")

st.title("📚 AI StudyMate")
st.write("Your personal study assistant")
st.write("Understand notes, revise faster, and test your knowledge.")

notes = st.text_area(
    "Paste your study notes here",
    height=220,
    placeholder="Paste your class notes or textbook content..."
)

def summarize(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s for s in sentences if s]
    if len(sentences) <= 3:
        return text

    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    common = Counter(words)
    scored = []

    for i, sentence in enumerate(sentences):
        sentence_words = re.findall(
            r'\b[a-zA-Z]{4,}\b', sentence.lower()
        )
        score = sum(common[w] for w in sentence_words)
        scored.append((score, i, sentence))

    selected = sorted(
        sorted(scored, reverse=True)[:3],
        key=lambda item: item[1]
    )
    return " ".join(item[2] for item in selected)

if st.button("✨ Summarize Notes"):
    if notes.strip():
        st.subheader("Summary")
        st.write(summarize(notes))
    else:
        st.warning("Please enter your study notes first.")

if st.button("📝 Generate Practice Questions"):
    if notes.strip():
        sentences = [
            s for s in re.split(r'(?<=[.!?])\s+', notes.strip())
            if len(s.split()) >= 5
        ]

        if sentences:
            st.subheader("Practice Questions")
            for i, sentence in enumerate(sentences[:5], 1):
                st.write(f"{i}. Explain this statement in your own words:")
                st.info(sentence)
        else:
            st.warning("Please enter longer notes.")
    else:
        st.warning("Please enter your study notes first.")

st.divider()
st.caption("AI StudyMate | A student learning project")
