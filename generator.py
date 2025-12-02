import random
import string

def generate_email():

    random_digits = random.randint(100, 999)
    return f"vitaliy_gulevaty_35_{random_digits}@yandex.ru"

def generate_password(length=8):

    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


