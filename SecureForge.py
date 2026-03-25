import string
import random

def main():
    action = int(input("Generate a password(Press 1 and hit Enter) or Check a password? (Press 2 and hit Enter) "))

    if action == 1:
        while True:
            length = int(input("What will the length of the password? "))
            if length < 8:
                print("Length should at least be 8.")
            else:
                break

        while True:
            options = input("What character types do you want in your password?\n'u' for uppercase, 'l' for lowercase, 'd' for digits, 's' for symbols: ")
            if 'u' in options or 'l' in options or 'd' in options or 's' in options:
                break
            else:
                print("Enter at least 1 option.")

        pwd = generate(length, options)
        print(f"Generated Password: {pwd}")
        score, improvements = check(pwd)
        print(f"Score: {score}/8")
        if score <= 3:
            rating = "Weak 🔴"
        elif score <= 5:
            rating = "Moderate 🟡"
        elif score <= 7:
            rating = "Strong 🟢"
        else:
            rating = "Very Strong 💪"
        print(f"Your password is {rating}")
        for improvement in improvements:
            print(f"  - {improvement}")

    elif action == 2:
        while True:
            pwd = input("Enter the password: ")
            if pwd == "":
                print("Please enter a password.")
            else:
                break

        score, improvements = check(pwd)
        print(f"Score: {score}/8")
        if score <= 3:
            rating = "Weak 🔴"
        elif score <= 5:
            rating = "Moderate 🟡"
        elif score <= 7:
            rating = "Strong 🟢"
        else:
            rating = "Very Strong 💪"
        print(f"Your password is {rating}")
        for improvement in improvements:
            print(f"  - {improvement}")

    else:
        print("Invalid input")


def generate(length, options):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    draft = ""
    pool = ""

    if 'u' in options:
        draft += random.choice(uppercase)
        pool += uppercase
    if 'l' in options:
        draft += random.choice(lowercase)
        pool += lowercase
    if 'd' in options:
        draft += random.choice(digits)
        pool += digits
    if 's' in options:
        draft += random.choice(symbols)
        pool += symbols

    for _ in range(length - len(draft)):
        draft += random.choice(pool)

    password = "".join(random.sample(draft, len(draft)))
    return password


def check(pwd):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    common_patterns = [
        "1234", "12345", "123456", "1234567", "12345678",
        "0123", "9876", "987654",
        "0000", "1111", "2222", "3333", "aaaa", "bbbb",
        "aaa", "111", "000",
        "qwerty", "qwertyuiop", "asdf", "asdfgh", "zxcvbn",
        "qweasd", "qazwsx",
        "password", "pass", "passwd",
        "admin", "administrator",
        "login", "letmein", "welcome",
        "monkey", "dragon", "master",
        "hello", "shadow", "sunshine",
        "p@ssword", "p@ss", "passw0rd", "adm1n", "l0gin",
        "2024", "2025", "2026", "1990", "2000",
        "0101", "1201", "3112",
        "iloveyou", "abc123", "superman", "batman",
        "guest", "root", "test", "user"
    ]

    improvements = [
        "Use at least 12 characters for better security.",
        "Add uppercase letters.",
        "Add lowercase letters.",
        "Add digits.",
        "Add special characters (!@#$ etc).",
        "Avoid common patterns like '1234' or 'password'.",
    ]

    score = 0

    # Length checks
    if len(pwd) >= 8:
        score += 1
    if len(pwd) >= 12:
        score += 1
        improvements.remove("Use at least 12 characters for better security.")
    if len(pwd) >= 16:
        score += 1

    # Character type checks
    for char in pwd:
        if char in uppercase:
            score += 1
            uppercase = ""
            improvements.remove("Add uppercase letters.")
        elif char in lowercase:
            score += 1
            lowercase = ""
            improvements.remove("Add lowercase letters.")
        elif char in digits:
            score += 1
            digits = ""
            improvements.remove("Add digits.")
        elif char in symbols:
            score += 1
            symbols = ""
            improvements.remove("Add special characters (!@#$ etc).")

    # Common pattern check
    found_pattern = False
    for pattern in common_patterns:
        if pattern in pwd.lower():
            found_pattern = True
            break

    if not found_pattern:
        score += 1
        improvements.remove("Avoid common patterns like '1234' or 'password'.")

    score = min(score, 8)
    return (score, improvements)


if __name__ == "__main__":
    main()