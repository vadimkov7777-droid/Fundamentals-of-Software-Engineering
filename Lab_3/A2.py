import string

password = input()

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
special_chars = '*-#'
errors = []

if len(password) != 8:
    errors.append("Длина пароля не равна 8")
if not any(c in string.ascii_uppercase for c in password):
    errors.append("В пароле отсутствуют заглавные буквы")
if not any(c in string.ascii_lowercase for c in password):
    errors.append("В пароле отсутствуют строчные буквы")
if not any(c in string.digits for c in password):
    errors.append("В пароле отсутствуют цифры")
if not any(c in special_chars for c in password):
    errors.append("В пароле отсутствуют специальные символы")
if not all(c in allowed for c in password):
    errors.append("В пароле используются непредусмотренные символы")

if errors:
    for error in errors:
        print(error)
else:
    print("Надежный пароль")