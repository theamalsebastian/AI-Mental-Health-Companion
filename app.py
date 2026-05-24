import streamlit as st
from textblob import TextBlob
import datetime

# ------------------- Utility Functions -------------------

def analyze_sentiment(user_text):
    """Analyze sentiment using TextBlob."""
    blob = TextBlob(user_text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        mood = "Positive 😊"
        suggestion = "Keep up the good vibes! Try journaling or sharing gratitude today."
    elif polarity < -0.2:
        mood = "Negative 😔"
        suggestion = "It seems you're feeling low. Consider a short walk, deep breathing, or talking to a friend."
    else:
        mood = "Neutral 😐"
        suggestion = "You're feeling balanced. Maybe try mindfulness meditation or a creative hobby."
    return mood, suggestion, polarity

def generate_report(user_text, mood, suggestion):
    """Generate a daily reflection report."""
    today = datetime.date.today().strftime("%B %d, %Y")
    report = f"""
    Daily Reflection Report - {today}

    Your Input:
    {user_text}

    Mood Analysis:
    {mood}

    Suggested Coping Strategy:
    {suggestion}
    """
    return report

# ------------------- Streamlit UI -------------------

st.set_page_config(page_title="AI Mental Health Companion", page_icon="💙", layout="wide")

st.markdown(
    """
    <style>
    .hero {
        text-align: center;
        padding: 25px;
        background-color: #3f72af;
        color: white;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    <div class="hero">
        <h1>💙 AI Mental Health Companion</h1>
        <p>Write how you feel and get supportive, non-diagnostic feedback with coping suggestions.</p>
    </div>
    """,
    unsafe_allow_html=True
)

user_text = st.text_area("📝 How are you feeling today?", height=150)

if user_text.strip() != "":
    with st.spinner("Analyzing your mood..."):
        mood, suggestion, polarity = analyze_sentiment(user_text)
        st.success("✅ Analysis Complete!")

        st.subheader("Results")
        st.write("**Mood Detected:**", mood)
        st.write("**Polarity Score:**", round(polarity, 2))
        st.write("**Suggested Coping Strategy:**", suggestion)

        # Download report
        report = generate_report(user_text, mood, suggestion)
        st.download_button("📥 Download Reflection Report", report, file_name="reflection_report.txt")
else:
    st.info("Please write a few sentences about how you feel.")
