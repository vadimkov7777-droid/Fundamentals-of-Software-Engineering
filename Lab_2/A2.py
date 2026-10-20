expressions = [
    "'123е'",
    "'91.4'",
    "524.345 ** 435345345311145345",
    "'7.1 + 4'",
    "'4' - 2",
    "'4 - 2'",
    "'42'",
    "-12.12"
]

for expression in expressions:
    try:
        result = eval(expression)
        print(expression, "->", int(result))
    except Exception as error:
        print(expression, "->", type(error).__name__)