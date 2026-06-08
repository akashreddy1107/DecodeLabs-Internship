import secrets
import string

length = int(input("Enter password length: "))

if length < 4:
    print("Password length must be at least 4")
else:
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    password = ''.join(password)

    print("Generated Password:")
    print(password)