from datetime import date

import streamlit as st

from auth import login, signup
from chatbot import chatbot_response
from scraper import scrape_website
from style import load_css

st.set_page_config(page_title="IRA Academic Platform", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

for key, default in {
    "page": "landing",
    "website_url": "",
    "website_text": "",
    "messages": [],
    "current_user": None,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


def nav_to(page_name: str):
    st.session_state.page = page_name
    st.rerun()


st.markdown("<div class='topbar'>AI Chatbot Web UI Design</div>", unsafe_allow_html=True)
st.markdown("<div class='app-shell'>", unsafe_allow_html=True)

if st.session_state.page == "landing":
    st.markdown(
        """
        <div class='brand-row'>
            <div><h2 style='margin:0;color:#0b4ab8'>IRA</h2><div class='subtitle'>Intelligent Response Assistant</div></div>
            <div style='font-weight:700;color:#7c8da8'>Internal Systems v2.0</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.05, 1], gap="large")
    with left:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='hint'>✨ AI Powered Assistant</div>", unsafe_allow_html=True)
        st.markdown("<h1 class='brand-title'>Instant Academic &<br><span class='blue'>Administrative Help</span></h1>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>IRA analyzes the college portal and answers student queries from indexed pages.</div>", unsafe_allow_html=True)
        url = st.text_input("College Website URL", placeholder="https://cvr.ac.in", value=st.session_state.website_url)

        if st.button("Process Website", use_container_width=True):
            if not url.strip():
                st.error("Please enter a college website URL first.")
            else:
                with st.spinner("Scraping and indexing website pages..."):
                    text, pages = scrape_website(url)
                if not text.strip():
                    st.error("Unable to extract website content. Try another URL.")
                else:
                    st.session_state.website_url = url.strip()
                    st.session_state.website_text = text
                    st.success(f"IRA is ready. Indexed {len(pages)} pages.")
                    nav_to("login")

        st.markdown("<div class='hint'>Powered by NLP & AI | IRA System</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='right-image'>", unsafe_allow_html=True)
        st.image("homepage.jpg", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "login":
    c1, c2 = st.columns([1, 1.08], gap="large")
    with c1:
        st.markdown("<div class='auth-box'>", unsafe_allow_html=True)
        st.markdown("<h2 style='margin-bottom:4px'>Welcome Back</h2><div class='subtitle'>Login to access your IRA dashboard</div>", unsafe_allow_html=True)
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Sign In", use_container_width=True):
            user = login(email, password)
            if user:
                st.session_state.current_user = dict(user)
                st.session_state.messages = []
                nav_to("home")
            else:
                st.error("Invalid credentials")

        st.caption("Don't have an account?")
        if st.button("Sign Up", use_container_width=True):
            nav_to("signup")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='right-image'>", unsafe_allow_html=True)
        st.image("homepage.jpg", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "signup":
    c1, c2 = st.columns([1, 1.08], gap="large")
    with c1:
        st.markdown("<div class='auth-box'>", unsafe_allow_html=True)
        st.markdown("<h2 style='margin-bottom:4px'>Create an Account</h2><div class='subtitle'>Join the IRA academic platform</div>", unsafe_allow_html=True)
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        terms = st.checkbox("Accept Terms & Conditions")

        if st.button("Sign Up", use_container_width=True):
            if not full_name or not email or not password or not confirm_password:
                st.error("Please fill all required fields.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif not terms:
                st.error("Please accept terms and conditions.")
            else:
                ok, msg = signup(full_name, email, phone, password)
                if ok:
                    st.success(msg)
                    nav_to("login")
                else:
                    st.error(msg)

        if st.button("Back to Login", use_container_width=True):
            nav_to("login")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='right-image'>", unsafe_allow_html=True)
        st.image("homepage.jpg", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "home":
    user_name = (st.session_state.current_user or {}).get("full_name", "Student")
    st.markdown(f"<div class='chat-header'>IRA | Intelligent Response Assistant <span style='float:right;font-size:16px;background:#dcfce7;color:#15803d;padding:6px 12px;border-radius:999px'>● Online</span></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle'>Welcome, {user_name}. Ask questions retrieved from: <b>{st.session_state.website_url}</b></div>", unsafe_allow_html=True)

    if not st.session_state.messages:
        greeting = (
            "Hello! I am IRA. I can answer academic and administrative queries using your college website data."
        )
        st.session_state.messages.append({"sender": "bot", "text": greeting})

    st.markdown("<div class='chat-wrapper'><div class='chat-scroll'>", unsafe_allow_html=True)
    st.markdown(f"<div class='hint' style='text-align:center'>Today, {date.today().strftime('%d/%m/%Y')}</div>", unsafe_allow_html=True)

    for msg in st.session_state.messages:
        cls = "user" if msg["sender"] == "user" else "bot"
        st.markdown(f"<div class='bubble {cls}'>{msg['text']}</div>", unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    with st.form("ask_form", clear_on_submit=True):
        question = st.text_input("", placeholder="Type your question here...")
        submitted = st.form_submit_button("Send", use_container_width=True)

    if submitted and question.strip():
        st.session_state.messages.append({"sender": "user", "text": question.strip()})
        answer = chatbot_response(question.strip(), st.session_state.website_text)
        st.session_state.messages.append({"sender": "bot", "text": answer})
        st.rerun()

    st.markdown("<div class='disclaimer'>Information is retrieved from the indexed college website. Please verify critical details.</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Logout", use_container_width=True):
            st.session_state.current_user = None
            nav_to("login")
    with c2:
        if st.button("Re-process Website", use_container_width=True):
            nav_to("landing")

st.markdown("</div>", unsafe_allow_html=True)
