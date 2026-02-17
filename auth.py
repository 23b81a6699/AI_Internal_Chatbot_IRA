import hashlib
from database import c, conn


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def signup(full_name: str, email: str, phone: str, password: str) -> tuple[bool, str]:
    email = email.strip().lower()
    try:
        c.execute(
            "INSERT INTO users(email, full_name, phone, password) VALUES (?, ?, ?, ?)",
            (email, full_name.strip(), phone.strip(), hash_password(password)),
        )
        conn.commit()
        return True, "Account created successfully. Please login."
    except Exception:
        return False, "Email is already registered. Please login."


def login(email: str, password: str):
    c.execute(
        "SELECT email, full_name, phone FROM users WHERE email=? AND password=?",
        (email.strip().lower(), hash_password(password)),
    )
    return c.fetchone()
