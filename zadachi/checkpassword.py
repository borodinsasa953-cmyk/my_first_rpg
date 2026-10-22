
def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False
def has_upper(password):
    for char in password:
        if char.isupper():
            return True
        return False
def check_password(password):
    if len(password) < 8:
        return 'Меньше восьми символов'
    if not has_digit(password):
        return 'Нет цифр'
    if not has_upper(password):
        return 'Нет заглавной буквы'
    return 'Пароль верный'
password = input('Введите пароль: ')
print(check_password(password))