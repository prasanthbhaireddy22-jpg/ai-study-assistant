import streamlit as st
import google.generativeai as genai
import PyPDF2
import os

# -------------------------
# Configure Gemini API
# -------------------------

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------
# App Title
# -------------------------

st.title("📚 Advanced Smart AI Study Assistant")

st.write(
    "Ask questions, summarize notes, generate quizzes, flashcards, and study plans using AI."
)

# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("📖 Study Assistant")

st.sidebar.info(
"""
AI-powered study tools:

💬 AI Chat  
📄 Notes Summary  
📝 Quiz Generator  
🧠 Flashcards  
📅 Study Planner
"""
)

# -------------------------
# Tabs
# -------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💬 AI Chat",
    "📄 Summarize Notes",
    "📝 Generate Quiz",
    "🧠 Flashcards",
    "📅 Study Plan"
])

# -------------------------
# TAB 1 — AI CHAT
# -------------------------

with tab1:

    st.subheader("Ask AI anything about your studies")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if st.button("Clear Chat"):
        st.session_state.messages = []

    user_prompt = st.chat_input("Ask a study question...")

    if user_prompt:

        st.session_state.messages.append({
            "role": "user",
            "content": user_prompt
        })

        prompt = f"""
        You are a helpful study assistant.
        Explain clearly and simply for students.

        Question:
        {user_prompt}
        """

        response = model.generate_content(prompt)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response.text
        })

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])


# -------------------------
# TAB 2 — SUMMARIZE NOTES
# -------------------------

with tab2:

    st.subheader("Summarize Study Notes")

    notes = st.text_area("Paste your notes here")

    uploaded_file = st.file_uploader("Or upload a PDF", type="pdf")

    text = ""

    if uploaded_file:

        reader = PyPDF2.PdfReader(uploaded_file)

        for page in reader.pages:
            text += page.extract_text()

        st.success("PDF uploaded successfully")

    if st.button("Summarize Notes"):

        content = notes if notes else text

        if content == "":
            st.warning("Please enter notes or upload a PDF")

        else:

            prompt = f"""
            Summarize the following study material into simple bullet points:

            {content}
            """

            response = model.generate_content(prompt)

            st.success("Summary")

            st.write(response.text)


# -------------------------
# TAB 3 — QUIZ GENERATOR
# -------------------------

with tab3:

    st.subheader("Generate Study Quiz")

    topic = st.text_input("Enter topic")

    if st.button("Generate Quiz"):

        if topic == "":
            st.warning("Please enter a topic")

        else:

            prompt = f"""
            Create a 5 question quiz with answers about {topic}.
            """

            response = model.generate_content(prompt)

            st.success("Quiz")

            st.write(response.text)


# -------------------------
# TAB 4 — FLASHCARDS
# -------------------------

with tab4:

    st.subheader("Flashcard Generator")

    topic = st.text_input("Flashcard topic")

    if st.button("Generate Flashcards"):

        if topic == "":
            st.warning("Please enter a topic")

        else:

            prompt = f"""
            Create 5 study flashcards for {topic}.

            Format:
            Question:
            Answer:
            """

            response = model.generate_content(prompt)

            st.success("Flashcards")

            st.write(response.text)


# -------------------------
# TAB 5 — STUDY PLAN
# -------------------------

with tab5:

    st.subheader("AI Study Plan Generator")

    subject = st.text_input("Subject")

    days = st.number_input(
        "Days to prepare",
        min_value=1,
        max_value=30,
        value=7
    )

    if st.button("Create Study Plan"):

        if subject == "":
            st.warning("Please enter a subject")

        else:

            prompt = f"""
            Create a {days}-day study plan for learning {subject}.
            Break it into daily tasks.
            """

            response = model.generate_content(prompt)

            st.success("Your Study Plan")

            st.write(response.text)


# -------------------------
# Footer
# -------------------------

st.markdown("---")
st.caption("Built with Streamlit + Gemini AI")