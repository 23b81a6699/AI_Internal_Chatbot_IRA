import streamlit as st
import base64
from style import load_css   # 👈 importing CSS
# from scrapper import scrape_website  
# from chatbot import chatbot_response  
# from auth import signup_user , login_user  

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="IRA Academic Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD CSS ----------------
st.markdown(load_css(), unsafe_allow_html=True)

# ---------------- FUNCTION TO LOAD IMAGE ----------------
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "front"

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- NAVIGATION FUNCTIONS ----------------
def navigate(page_name):
    st.session_state.history.append(st.session_state.page)
    st.session_state.page = page_name
    st.rerun()

def go_back():
    if st.session_state.history:
        st.session_state.page = st.session_state.history.pop()
        st.rerun()

def back_button():
    if st.session_state.page != "front":
        col1, col2 = st.columns([1, 20])
        with col1:
            if st.button("⬅"):
                go_back()


# ==================================================
# ================= FRONT PAGE =====================
# ==================================================
if st.session_state.page == "front":

    img_base64 = get_base64_image("Front_page.png")

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .front-overlay {{
            background: rgba(0, 0, 0, 0.65);
            padding: 80px 40px;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin-top: 120px;
            box-shadow: 0px 15px 40px rgba(0,0,0,0.5);
            transition: 0.4s ease-in-out;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }}

        .front-overlay:hover {{
            box-shadow: 0px 25px 60px rgba(0,0,0,0.8);
            transform: scale(1.02);
        }}

        .ira-title {{
            font-size: 56px;
            font-weight: 800;
        }}

        .ira-sub {{
            font-size: 22px;
            margin-top: 10px;
            color: #e0e0e0;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="front-overlay">
            <div class="ira-title">IRA</div>
            <div class="ira-sub">Intelligent Responsive Agent</div>

            <p style="font-size:18px; margin-top:25px; line-height:1.6;">
                IRA is an AI-powered academic assistant designed to provide 
                instant academic and administrative support. It intelligently 
                scrapes, analyzes, and responds to queries from institutional 
                portals using Natural Language Processing and Machine Learning.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Login"):
            navigate("login")

    with col2:
        if st.button("Sign Up"):
            navigate("signup")

    with col3:
        if st.button("Home"):
            navigate("home")


# ==================================================
# ================= LOGIN PAGE =====================
# ==================================================
elif st.session_state.page == "login":

    back_button()

    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.markdown("""
    <div class="title-box">
        <h1>Login</h1>
        <div class="sub-title">Welcome back to IRA</div>
    </div>
    """, unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        navigate("home")

    st.markdown("<br>", unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([2,3,2])

    with col_center:
        c1, c2 = st.columns([3,1])

        with c1:
            st.markdown(
                "<div style='text-align:right; padding-top:8px;'>Don't have an account?</div>",
                unsafe_allow_html=True
            )

        with c2:
            if st.button("Sign Up"):
                navigate("signup")

    st.markdown('</div>', unsafe_allow_html=True)


# ==================================================
# ================= SIGNUP PAGE ====================
# ==================================================
elif st.session_state.page == "signup":

    back_button()

    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.markdown("""
    <div class="title-box">
        <h1>Create an Account</h1>
        <div class="sub-title">Join the IRA academic platform</div>
    </div>
    """, unsafe_allow_html=True)

    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    terms = st.checkbox("Accept Terms and Conditions")

    if st.button("Sign Up"):
        st.success("Account created successfully!")
        navigate("login")

    st.markdown('</div>', unsafe_allow_html=True)


# ==================================================
# ================= HOME PAGE ======================
# ==================================================
elif st.session_state.page == "home":

    back_button()

    st.markdown("""
        <style>
        .block-container {padding-top: 1rem !important;}
        </style>
    """, unsafe_allow_html=True)

    col_nav1, col_nav2 = st.columns([4, 1])

    with col_nav1:
        st.markdown(
            "<div class='ira-header'>IRA (Intelligent Responsive Agent)</div>",
            unsafe_allow_html=True
        )

    with col_nav2:
        st.markdown(
            "<div style='text-align:right; padding-top:8px;'>Internal Systems v2.0</div>",
            unsafe_allow_html=True
        )

    st.divider()

    col1, col2 = st.columns([1.1, 1])

    with col1:
        st.markdown("<div class='badge'>✨ AI Powered Assistant</div>", unsafe_allow_html=True)
        st.markdown("<span style='font-size:48px; font-weight:700;'>Instant Academic</span>", unsafe_allow_html=True)
        st.markdown("<span style='font-size:48px; font-weight:700;'>&</span>", unsafe_allow_html=True)
        st.markdown("<span style='font-size:48px; font-weight:700; color:#1e4ed8;'>Administrative Help</span>", unsafe_allow_html=True)

        st.markdown(
            "IRA (Intelligent Response Assistant) analyzes the college portal "
            "to provide instant answers to your queries."
        )

        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("#### Connect Knowledge Base")
        st.caption("Enter the college website URL to begin training the model.")

        website = st.text_input("College Website URL", placeholder="https://yourcollege.edu")

        if st.button("Process Website"):
            st.success("Website processing started...")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="home-image">', unsafe_allow_html=True)
        st.image("homepage.jpeg", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    colA, colB = st.columns(2)

    with colA:
        if st.button("Open Chatbot"):
            navigate("chatbot")

    with colB:
        if st.button("Logout"):
            navigate("login")


# ==================================================
# ================= CHATBOT PAGE ===================
# ==================================================
elif st.session_state.page == "chatbot":

    back_button()

    st.title("🤖 Ask IRA")

    query = st.text_input("Type your question here...")

    if query:
        st.write("You asked:", query)
        st.write("Response will appear here.")
