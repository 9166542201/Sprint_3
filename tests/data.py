from secrets import token_hex

user_valid = "cvn1@mail.ru", "123123"
user_short_password = "cvn@mail.ru", "123"

user_generated = f"{token_hex(8)}@cvn.ru", "123123"