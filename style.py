def load_css():
    return """
    <style>
    header[data-testid="stHeader"]{display:none;}
    .block-container{padding-top:0.8rem;padding-bottom:1rem;max-width:1300px;}

    .topbar{background:#242526;color:#fff;padding:12px 20px;border-radius:10px;font-weight:700;text-align:center;margin-bottom:18px;}
    .app-shell{background:#edf1f7;border-radius:24px;padding:22px;min-height:88vh;}

    .brand-row{display:flex;justify-content:space-between;align-items:center;padding:8px 4px 14px 4px;}
    .brand-title{font-size:40px;line-height:1.08;font-weight:800;color:#0f172a;margin:10px 0;}
    .blue{color:#0b4ab8;}
    .subtitle{font-size:18px;color:#5a6b86;margin-bottom:6px;}

    .card{background:#fff;border-radius:18px;padding:20px;box-shadow:0 10px 30px rgba(15,23,42,.08);}

    .right-image{border-radius:20px;overflow:hidden;border:8px solid #fff;box-shadow:0 20px 40px rgba(2,6,23,.2)}
    .hint{color:#7d8da9;font-size:14px;}

    div[data-testid="stTextInput"] input{border-radius:12px !important;height:44px !important;border:1px solid #d6deea !important;}
    .stButton>button{border-radius:12px !important;background:#0b4ab8 !important;color:#fff !important;font-weight:700 !important;border:none !important;height:46px !important;}

    .auth-box{background:#fff;border-radius:18px;padding:24px;box-shadow:0 10px 30px rgba(15,23,42,.08)}
    .auth-title{font-size:48px;font-weight:800;color:#0f172a;margin:0;}
    .auth-sub{font-size:17px;color:#687891;margin-bottom:12px;}

    .chat-wrapper{background:#f8fafd;border:1px solid #dbe4f1;border-radius:20px;height:70vh;display:flex;flex-direction:column;}
    .chat-header{padding:16px 20px;border-bottom:1px solid #e1e8f4;font-size:30px;font-weight:700;color:#0f172a;}
    .chat-scroll{padding:18px;overflow:auto;flex:1;}
    .bubble{padding:14px 16px;border-radius:14px;margin:8px 0;max-width:75%;font-size:20px;line-height:1.5;}
    .bot{background:#ffffff;border:1px solid #d8e1ef;}
    .user{background:#dbeafe;margin-left:auto;border:1px solid #bfdbfe;}
    .disclaimer{font-size:13px;color:#8ea0bd;text-align:center;margin-top:10px}
    </style>
    """
