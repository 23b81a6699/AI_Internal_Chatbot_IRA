import streamlit as st
import base64
from scraper import scrape_website
from chatbot import chatbot_response
from auth import signup_user, login_user

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="IRA Academic Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "front"

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- NAVIGATION ----------------
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
        if st.button("⬅ Back"):
            go_back()

# ---------------- IMAGE FUNCTION ----------------
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

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
            background: rgba(0, 0, 0, 0.6);
            padding: 80px 40px;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin-top: 150px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }}

        .ira-title {{
            font-size: 64px;
            font-weight: 800;
        }}

        .ira-sub {{
            font-size: 24px;
            margin-top: 15px;
            color: #e0e0e0;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="front-overlay">
        <div class="ira-title">IRA</div>
        <div class="ira-sub">Intelligent Responsive Agent</div>
        <p style="margin-top:20px;">
        AI-powered academic assistant that analyzes institutional portals 
        and provides instant academic & administrative support.
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
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(email, password):
            st.success("Login successful!")
            navigate("home")
        else:
            st.error("Invalid email or password")

    if st.button("Go to Sign Up"):
        navigate("signup")

# ==================================================
# ================= SIGNUP PAGE ====================
# ==================================================
elif st.session_state.page == "signup":

    back_button()
    st.title("Create Account")

    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if signup_user(full_name, email, phone, password):
            st.success("Account created successfully!")
            navigate("login")
        else:
            st.error("User already exists!")

# ==================================================
# ================= HOME PAGE ======================
# ==================================================
elif st.session_state.page == "home":

    back_button()
    st.title("IRA - Home")

    website = st.text_input("Enter College Website URL")

    if st.button("Process Website"):
        if website:
            with st.spinner("Processing website..."):
                try:
                    result = scrape_website(website)

                    if len(result.strip()) > 50:
                        st.success("Website processed successfully!")
                    else:
                        st.warning("Website content too small.")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a valid URL")

    if st.button("Open Chatbot"):
        navigate("chatbot")

    if st.button("Logout"):
        navigate("login")

# ==================================================
# ================= CHATBOT PAGE ===================
# ==================================================
elif st.session_state.page == "chatbot":

    back_button()
    st.title("🤖 Ask IRA")

    query = st.text_input("Type your question here...")

    if st.button("Ask"):
        if query:
            with st.spinner("Generating answer..."):
                response = chatbot_response(query)
                st.success("Answer:")
                st.write(response)
        else:
            st.warning("Please enter a question.")
