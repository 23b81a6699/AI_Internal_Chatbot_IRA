def load_css():
    return """
    <style>

    .block-container {
        padding-top: 2rem !important;
    }

    header {visibility: hidden;}

    /* Title Box (original blue palette) */
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

    /* Layout */
    .sidebar-box {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(16,24,40,0.06);
        height: 100%;
    }

    .brand {
        display:flex; gap:12px; align-items:center; margin-bottom:18px;
    }

    .brand .logo {
        width:44px; height:44px; border-radius:8px; background:#2d4b9b; color:white; display:flex; align-items:center; justify-content:center; font-weight:700;
    }

    .nav-item {padding:10px 6px; color:#334155; font-weight:600;}
    .nav-item.selected {background:#eef2ff; border-radius:10px; color:#1e3573}

    /* Chat area */
    .chat-header {display:flex; justify-content:space-between; align-items:center; padding:14px 8px;}
    .chat-title {font-size:22px; font-weight:700; color:#0f172a}

    .online-badge {background:#e6f0ff; color:#1e4ed8; padding:6px 12px; border-radius:999px; font-weight:600}

    .chat-window {background:#f8fafc; padding:28px; border-radius:12px; min-height:420px;}

    .date-pill {text-align:center; color:#64748b; font-size:13px; margin-bottom:12px}

    .message {max-width:70%; padding:14px 18px; border-radius:14px; margin-bottom:12px; box-shadow:0 6px 18px rgba(2,6,23,0.06);}
    .message.bot {background:white; color:#0f172a; border-radius:16px 16px 16px 4px}
    .message.user {background:#cfe8ff; color:#08306b; margin-left:auto; border-radius:16px 16px 4px 16px}

    .quick-chips {display:flex; gap:10px; flex-wrap:wrap; margin-top:12px}
    .chip {background:#e6f0ff; color:#1e4ed8; padding:8px 14px; border-radius:20px; font-weight:600; cursor:pointer}

    .input-row {display:flex; gap:10px; align-items:center; margin-top:16px}
    .input-text {flex:1}
    .send-button {background:#2d4b9b; color:white; width:44px; height:44px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700}

    .attachment {color:#475569; margin-right:8px}

    .disclaimer {text-align:center; color:#94a3b8; font-size:13px; margin-top:10px}

    </style>
    """
