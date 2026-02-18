import hashlib
from database import c, conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(full_name, email, phone, password):
    try:
        c.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?)",
            (email, full_name, phone, hash_password(password))
        )
        conn.commit()
        return True
    except:
        return False

def login(email, password):
    c.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, hash_password(password))
    )
    return c.fetchone()
