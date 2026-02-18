def load_css():
    return """
    <style>

    .block-container {
        padding-top: 2rem !important;
    }

    header {visibility: hidden;}

    /* Center container */
    .main-container {
        max-width: 500px;
        margin: auto;
        margin-top: 40px;
    }

    /* Title Box (UPDATED COLOR HERE) */
    .title-box {
        background: linear-gradient(135deg, #2d4b9b, #1e3573);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
        margin-bottom: 30px;
        color: white;
    }

    .title-box h1 {
        margin: 0;
        font-size: 32px;
        font-weight: 700;
        color: white;
    }

    .sub-title {
        font-size: 15px;
        margin-top: 5px;
        color: #e0e6ff;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        background-color: #2d4b9b;
        color: white;
        border-radius: 10px;
        height: 45px;
        font-size: 16px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1e3573;
    }

    /* Footer text */
    .bottom-text {
        text-align: center;
        margin-top: 15px;
        font-size: 14px;
    }

    </style>
    """
