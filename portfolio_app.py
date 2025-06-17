# portfolio_app.py
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# --- Page Configuration ---
st.set_page_config(page_title="Sultan Ahmed | Portfolio", layout="wide")

# --- Load Lottie Animation from URL ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


coding_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")


# --- Light/Dark Theme Toggle ---
theme = st.sidebar.radio("🌗 Theme", ["Light", "Dark"])

if theme == "Light":
    bg_color = "#f5f7fa"
    text_color = "#333"
    box_color = "white"
else:
    bg_color = "#1e1e1e"
    text_color = "#f5f5f5"
    box_color = "#2c2c2c"

# --- Custom CSS ---
st.markdown(f"""
    <style>
    html, body, [class*="css"] {{
        background-color: {bg_color};
        color: {text_color};
        font-family: 'Poppins', sans-serif;
    }}
    .main {{
        padding: 2rem;
        background-color: {box_color};
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    h1, h2, h3 {{
        color: {text_color};
    }}
    .stButton>button {{
        border-radius: 8px;
        background: #4a90e2;
        color: white;
        font-weight: bold;
        border: none;
    }}
    .stButton>button:hover {{
        background-color: #1c6dd0;
    }}
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://via.placeholder.com/150", width=150)  # Replace with your own
    st.title("Sultan Ahmed")
    st.caption("Web Developer | Python Enthusiast")
    st.markdown("[🌐 GitHub](https://github.com/sultanmedico)")
    st.markdown("[💼 LinkedIn](https://linkedin.com)")
    st.markdown("[✉️ Email](mailto:sultan@example.com)")

# --- Main Content ---
st.title("Sultan IT Web")

st.title("✨ Welcome to My Portfolio")

with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        st.header("👋 About Me")
        st.write("""
            I’m a passionate web developer who loves building elegant interfaces and learning emerging technologies.
            I work with Python, JavaScript, and design tools to deliver exceptional user experiences.
        """)
    with col2:
        st_lottie(coding_animation, height=300, key="coding")

st.markdown("---")

with st.container():
    st.header("🛠️ My Skills")
    st.markdown("""
    - 💻 HTML / CSS / JavaScript  
    - 🎨 TailwindCSS / Bootstrap  
    - 🐍 Python (Flask, Streamlit)  
    - 📁 Git & GitHub  
    - 🎯 UI/UX Design  
    """)

st.markdown("---")

# --- Contact Form ---
st.header("📬 Contact Me")
with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Send Message")

    if submit:
        st.success("✅ Message sent! I’ll reply soon. Thank you.")

