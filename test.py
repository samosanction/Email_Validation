from Is_valid_function import is_valid

emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an Email",
    "invalid@Email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com"
]

for email in emails:
    if is_valid(email):
        print(email + " is valid")
    else:
        print(email + " is invalid")
