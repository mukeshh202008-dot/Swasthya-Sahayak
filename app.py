import html

import streamlit as st
from agent import ask_agent

st.set_page_config(
    page_title="Swasthya Sahayak",
    page_icon="🩺",
    layout="wide"
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, .stApp {
    font-family: 'Inter', sans-serif;
            background:
                radial-gradient(circle at 10% 10%, rgba(52, 211, 153, 0.22), transparent 20%),
                radial-gradient(circle at 90% 0%, rgba(96, 165, 250, 0.20), transparent 22%),
                linear-gradient(135deg, #f4fff7 0%, #eef7ff 30%, #f8f5ff 100%);
            color: #0f172a;
        }

        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: 0.4rem 0 1.2rem 0;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 1.1rem;
            font-weight: 800;
            color: #0f172a;
        }

        .brand-badge {
            width: 42px;
            height: 42px;
            border-radius: 14px;
            display: grid;
            place-items: center;
            background: linear-gradient(135deg, #10b981, #3b82f6);
            box-shadow: 0 10px 20px rgba(59, 130, 246, 0.25);
            font-size: 1.35rem;
        }

        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.52rem 0.8rem;
            border-radius: 999px;
            background: rgba(16, 185, 129, 0.12);
            border: 1px solid rgba(16, 185, 129, 0.2);
            color: #047857;
            font-weight: 700;
            font-size: 0.78rem;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }

        .status-pill::before {
            content: "";
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #22c55e;
            box-shadow: 0 0 0 5px rgba(34, 197, 94, 0.12);
        }

        .hero {
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, rgba(16,185,129,0.18), rgba(59,130,246,0.12), rgba(168,85,247,0.10));
            border: 1px solid rgba(15, 23, 42, 0.08);
            border-radius: 30px;
            padding: 2.5rem 2.2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 22px 60px rgba(15, 23, 42, 0.12);
        }

        .hero::before {
            content: "";
            position: absolute;
            inset: auto -55px -60px auto;
            width: 220px;
            height: 220px;
            background: rgba(255,255,255,0.18);
            border-radius: 50%;
            filter: blur(16px);
        }

        .hero::after {
            content: "";
            position: absolute;
            left: 8%;
            top: 12%;
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 1px solid rgba(15, 23, 42, 0.05);
            background: rgba(255,255,255,0.10);
        }

        .badge {
            display: inline-block;
            padding: 0.52rem 0.9rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.55);
            border: 1px solid rgba(5, 150, 105, 0.25);
            color: #047857;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.85rem;
            backdrop-filter: blur(8px);
        }

        .hero h1 {
            position: relative;
            z-index: 1;
            margin: 0;
            font-size: clamp(2.3rem, 4vw, 3.8rem);
            line-height: 1.05;
            font-weight: 900;
            color: #0f172a;
        }

        .hero p {
            position: relative;
            z-index: 1;
            margin-top: 0.9rem;
            font-size: 1.12rem;
            color: #334155;
            max-width: 860px;
            line-height: 1.7;
        }

        .mini-row {
            position: relative;
            z-index: 1;
            display: flex;
            flex-wrap: wrap;
            gap: 0.7rem;
            margin-top: 1rem;
        }

        .mini-pill {
            padding: 0.45rem 0.8rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.45);
            border: 1px solid rgba(15,23,42,0.06);
            color: #0f172a;
            font-weight: 700;
            font-size: 0.8rem;
        }

        .feature-grid {
            margin-top: 0.6rem;
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.76);
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 22px;
            padding: 1.25rem 1.1rem;
            box-shadow: 0 16px 32px rgba(15, 23, 42, 0.08);
            height: 100%;
            backdrop-filter: blur(6px);
            transition: transform 0.22s ease, box-shadow 0.22s ease;
        }

        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 38px rgba(15, 23, 42, 0.10);
        }

        .glass-card .icon {
            font-size: 1.5rem;
            margin-bottom: 0.55rem;
            display: inline-block;
        }

        .glass-card h3 {
            margin-top: 0;
            margin-bottom: 0.4rem;
            font-size: 1.08rem;
            color: #0f172a;
            font-weight: 800;
        }

        .glass-card p {
            margin: 0;
            color: #475569;
            line-height: 1.7;
        }

        .warning-note {
            margin-top: 1.5rem;
            background: rgba(254, 243, 199, 0.84);
            border: 1px solid rgba(251, 191, 36, 0.45);
            border-radius: 16px;
            padding: 0.95rem 1rem;
            color: #78350f;
            font-weight: 600;
            box-shadow: 0 10px 24px rgba(251, 191, 36, 0.12);
        }

        .question-panel {
            background: rgba(255, 255, 255, 0.8);
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 28px;
            padding: 1.6rem;
            box-shadow: 0 20px 48px rgba(15, 23, 42, 0.08);
            margin-top: 1.5rem;
        }

        .stTextArea textarea {
            border-radius: 18px !important;
            border: 1px solid #cbd5e1 !important;
            background: linear-gradient(180deg, #ffffff, #f8fafc) !important;
            min-height: 150px !important;
            font-size: 1rem !important;
            padding: 0.95rem 1rem !important;
            box-shadow: inset 0 2px 6px rgba(148, 163, 184, 0.08);
        }

        .stTextArea textarea:focus {
            border-color: #3b82f6 !important;
            box-shadow: 0 0 0 3px rgba(59,130,246,0.15) !important;
        }

        .stButton > button {
            background: linear-gradient(135deg, #10b981, #3b82f6, #8b5cf6);
            color: white;
            border: none;
            border-radius: 14px;
            padding: 0.82rem 1.75rem;
            font-weight: 800;
            font-size: 1rem;
            letter-spacing: 0.02em;
            box-shadow: 0 16px 28px rgba(59,130,246,0.25);
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 18px 32px rgba(59,130,246,0.30);
            background: linear-gradient(135deg, #059669, #2563eb, #7c3aed);
            color: white;
        }

        .question-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 0.65rem;
            margin: 0 0 1rem 0;
        }

        .chip {
            display: inline-block;
            padding: 0.5rem 0.8rem;
            border-radius: 999px;
            background: #eff6ff;
            border: 1px solid rgba(59,130,246,0.12);
            color: #1d4ed8;
            font-weight: 700;
            font-size: 0.8rem;
            cursor: pointer;
        }

        .response-box {
            background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(240,249,255,0.82));
            border-left: 6px solid #14b8a6;
            border-radius: 20px;
            padding: 1.25rem 1.35rem;
            box-shadow: 0 18px 36px rgba(15, 23, 42, 0.08);
            margin-top: 1.25rem;
        }

        .response-box h3 {
            margin-top: 0;
            margin-bottom: 0.75rem;
            color: #0f172a;
        }

        .response-box p, .response-box li {
            color: #1f2937;
            line-height: 1.8;
            font-size: 1rem;
        }

        .stAlert {
            border-radius: 14px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="topbar">
        <div class="brand">
            <div class="brand-badge">🩺</div>
            Swasthya Sahayak
        </div>
        <div class="status-pill">AI Health Guide</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <div class="badge">Health Companion</div>
        <h1>Care for your health with confidence.</h1>
        <p>Get simple, practical health awareness guidance, reliable wellness tips, and clear safety reminders whenever you need them.</p>
        <div class="mini-row">
            <span class="mini-pill">✔ Everyday wellness</span>
            <span class="mini-pill">✔ Symptom awareness</span>
            <span class="mini-pill">✔ Safety-first advice</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """
        <div class="glass-card">
            <div class="icon">💡</div>
            <h3>Clear guidance</h3>
            <p>Learn about common symptoms and healthy habits in simple, easy-to-understand language.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="glass-card">
            <div class="icon">🧠</div>
            <h3>Smart support</h3>
            <p>Get basic awareness support for everyday questions about wellness, prevention, and care.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div class="glass-card">
            <div class="icon">🚨</div>
            <h3>Safe decisions</h3>
            <p>Know when to seek urgent medical help and when general lifestyle guidance is appropriate.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="warning-note">
        This AI provides general health awareness information and is not a substitute for professional medical advice.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="question-panel">', unsafe_allow_html=True)

suggested_questions = [
    "What are the signs of dehydration?",
    "How can I improve my sleep quality?",
    "What foods help boost immunity?",
    "When should I worry about a headache?",
    "How can I manage a fever at home?",
    "What should I do for body pain or muscle soreness?",
]

if "question_text" not in st.session_state:
    st.session_state.question_text = ""

st.caption("Suggested questions")
button_cols = st.columns(3)
for index, question_text in enumerate(suggested_questions):
    with button_cols[index % 3]:
        if st.button(question_text, key=f"suggestion_{index}", use_container_width=True):
            st.session_state.question_text = question_text

question = st.text_area(
    "Ask your health-related question",
    value=st.session_state.question_text,
    placeholder="Example: What are the signs of dehydration or how can I improve my sleep routine?",
    height=140,
)
st.session_state.question_text = question

if st.button("Get Guidance", use_container_width=True):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = ask_agent(question)

        safe_answer = html.escape(answer).replace("\n", "<br>")
        st.markdown("### 🤖 Agent Response")
        st.markdown(f"<div class='response-box'><p>{safe_answer}</p></div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a question before continuing.")

st.markdown('</div>', unsafe_allow_html=True)
