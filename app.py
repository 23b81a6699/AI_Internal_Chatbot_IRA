import streamlit as st
from style import load_css   # 👈 importing CSS
from datetime import datetime, date
from chatbot import chatbot_response

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="IRA Academic Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD CSS ----------------
st.markdown(load_css(), unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "login"

# ==================================================
# ================= LOGIN PAGE =====================
# ==================================================
if st.session_state.page == "login":

    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # ---------- TITLE BOX ----------
    st.markdown("""
    <div class="title-box">
        <h1>Login</h1>
        <div class="sub-title">Welcome back to IRA</div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- INPUT FIELDS ----------
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # ---------- LOGIN BUTTON ----------
    if st.button("Login"):
        st.session_state.page = "home"
        st.rerun()

    # ---------- SIGNUP INLINE ROW ----------
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
                st.session_state.page = "signup"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# ==================================================
# ================= SIGNUP PAGE ====================
# ==================================================
elif st.session_state.page == "signup":

    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # ---------- TITLE BOX ----------
    st.markdown("""
    <div class="title-box">
        <h1>Create an Account</h1>
        <div class="sub-title">Join the IRA academic platform</div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- INPUT FIELDS ----------
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    terms = st.checkbox("Accept Terms and Conditions")

    # ---------- SIGN UP BUTTON ----------
    if st.button("Sign Up"):
        if not full_name or not email or not phone or not password or not confirm_password:
            st.error("Please fill all fields.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        elif not terms:
            st.error("You must accept Terms and Conditions.")
        else:
            st.success("Account created successfully!")
            st.session_state.page = "login"
            st.rerun()

    # ---------- CENTERED LOGIN ROW ----------
    st.markdown("<br>", unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([2,3,2])

    with col_center:
        c1, c2 = st.columns([3,1])

        with c1:
            st.markdown(
                "<div style='text-align:right; padding-top:8px;'>Already have an account?</div>",
                unsafe_allow_html=True
            )

        with c2:
            if st.button("Login"):
                st.session_state.page = "login"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# ==================================================
# ================= HOME PAGE ======================
# ==================================================
elif st.session_state.page == "home":

    # Remove extra spacing
    st.markdown("""
        <style>
        .block-container {padding-top: 1rem !important;}

        .badge {
            display:inline-block;
            background:#e6f0ff;
            color:#1e4ed8;
            padding:6px 16px;
            border-radius:20px;
            font-size:13px;
        }

        .home-image img {
            border-radius:20px;
            box-shadow: 0px 15px 35px rgba(0,0,0,0.15);
        }

        .card-box {
            background:white;
            padding:25px;
            border-radius:15px;
            box-shadow:0px 8px 25px rgba(0,0,0,0.08);
        }
        /* HEADER SECTION */
        .ira-header {
            background-color: #1e4ed8;
            padding: 20px 40px;
            border-radius: 0px 0px 20px 20px;
            color: white;
            font-size: 26px;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    # ---------- NAVBAR ----------
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

    # ---------- HERO SECTION ----------
    col1, col2 = st.columns([1.1, 1])

    with col1:
        st.markdown("<div class='badge'>✨ AI Powered Assistant</div>", unsafe_allow_html=True)

        st.write("")

        st.markdown(
            "<span style='font-size:48px; font-weight:700;'>Instant Academic</span>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<span style='font-size:48px; font-weight:700;'>&</span>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<span style='font-size:48px; font-weight:700; color:#1e4ed8;'>Administrative Help</span>",
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            "IRA (Intelligent Response Assistant) analyzes the college portal "
            "to provide instant answers to your queries."
        )

        st.write("")
        st.write("")

        # Knowledge Base Card
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("#### Connect Knowledge Base")
        st.caption("Enter the college website URL to begin training the model.")

        website = st.text_input(
            "College Website URL",
            placeholder="https://yourcollege.edu"
        )

        if st.button("Process Website"):
            st.success("Website processing started...")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------- RIGHT IMAGE ----------
    with col2:
        st.markdown('<div class="home-image">', unsafe_allow_html=True)
        st.image("homepage.jpg", use_container_width=True)  # <-- your image file name
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ---------- Navigation ----------
    colA, colB = st.columns(2)

    with colA:
        if st.button("Open Chatbot"):
            st.session_state.page = "chatbot"
            st.rerun()

    with colB:
        if st.button("Logout"):
            st.session_state.page = "login"
            st.rerun()


# ==================================================
# ================= CHATBOT PAGE ===================
# ==================================================
elif st.session_state.page == "chatbot":

    # initialize chat message history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    def add_message(sender, text):
        st.session_state.messages.append({
            "sender": sender,
            "text": text,
            "time": datetime.now().strftime("%H:%M")
        })

    # Add initial greeting once
    if not st.session_state.messages:
        greeting = (
            "Hello! I am IRA, your Intelligent Response Assistant. "
            "I can help you with academic schedules, exam queries, attendance policies, and placement details. How can I assist you today?"
        )
        add_message("bot", greeting)

    # Layout: sidebar + chat area
    col_sidebar, col_main = st.columns([1, 3])

    # Sidebar
    with col_sidebar:
        st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
        st.markdown(
            """
            <div class='brand'><div class='logo'>IRA</div>
            <div><div style='font-weight:700'>IRA</div><div style='color:#64748b'>Intelligent Response Assistant</div></div></div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div class='nav-item selected'>Ask IRA</div>", unsafe_allow_html=True)
        st.markdown("<div class='nav-item'>Academic Queries</div>", unsafe_allow_html=True)
        st.markdown("<div class='nav-item'>Administrative Queries</div>", unsafe_allow_html=True)
        st.markdown("<div class='nav-item'>Help & Support</div>", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<div style='font-weight:700'>Student Login</div>", unsafe_allow_html=True)
        st.markdown("<div style='color:#64748b'>View Profile</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Main chat area
    with col_main:
        # header with online indicator
        st.markdown(
            "<div class='chat-header'><div class='chat-title'>IRA | Intelligent Response Assistant</div>"
            "<div class='online-badge'>Online</div></div>",
            unsafe_allow_html=True,
        )

        st.markdown("<div class='chat-window'>", unsafe_allow_html=True)

        # date pill
        today_label = date.today().strftime("%B %d, %Y")
        st.markdown(f"<div class='date-pill'>Today, {today_label}</div>", unsafe_allow_html=True)

        # messages
        for msg in st.session_state.messages:
            if msg["sender"] == "bot":
                st.markdown(f"<div class='message bot'>{msg['text']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='message user'>{msg['text']}</div>", unsafe_allow_html=True)

        # quick suggestion chips
        chips = [
            "What is the attendance policy?",
            "Show me the exam timetable",
            "Placement details for CSE",
            "Library opening hours",
        ]

        st.markdown('<div class="quick-chips">', unsafe_allow_html=True)
        chips_cols = st.columns(len(chips))
        for i, chip in enumerate(chips):
            with chips_cols[i]:
                if st.button(chip):
                    # process chip as query
                    add_message("user", chip)
                    with st.spinner("IRA is typing..."):
                        answer = chatbot_response(chip)
                    add_message("bot", answer)
                    st.experimental_rerun()

        st.markdown('</div>', unsafe_allow_html=True)

        # input form with attachment
        with st.form(key='chat_form', clear_on_submit=False):
            cols = st.columns([0.05, 0.85, 0.1])
            with cols[0]:
                file = st.file_uploader("", type=["pdf", "png", "jpg", "docx"], label_visibility='collapsed')
            with cols[1]:
                user_input = st.text_input("", key='chat_input', placeholder='Type your question here...')
            with cols[2]:
                submitted = st.form_submit_button("Send")

            if submitted and (user_input or file):
                # show user message
                if file and not user_input:
                    user_text = f"[Uploaded file] {file.name}"
                else:
                    user_text = user_input

                add_message("user", user_text)

                # get bot response
                with st.spinner("IRA is thinking..."):
                    answer = chatbot_response(user_text)

                add_message("bot", answer)
                # clear input box
                st.session_state.chat_input = ""
                st.experimental_rerun()

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div class='disclaimer'>Information is retrieved from the official college website. IRA can make mistakes, please verify important details.</div>", unsafe_allow_html=True)

        if st.button("Back to Home"):
            st.session_state.page = "home"
            st.rerun()
