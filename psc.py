import re
import hashlib  

def check_strength(password):
    reasons = []

    if len(password) < 8:
        reasons.append("Password is too short (min 8 characters).")

    if not re.search(r"[A-Z]", password):
        reasons.append("Add at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        reasons.append("Add at least one lowercase letter.")

    if not re.search(r"[0-9]", password):
        reasons.append("Add at least one number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        reasons.append("Add at least one special character.")

    if reasons:
        return "Weak Password ❌", reasons
    else:
        return "Strong Password ✅", []


# ───── MAIN UI ─────

password = input("Enter a password: ")

result, feedback = check_strength(password)

print("\nResult:", result)
for reason in feedback:
    print("-", reason)

# ───── HASHING─────

def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

hashed_pw = hash_password(password)

print("\nHashed Password (You’re using):")
print(hashed_pw)
