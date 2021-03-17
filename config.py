import random
from string import ascii_lowercase, digits


def generate_username(count):
    final_info = ''.join(random.choices(
        ascii_lowercase + digits, k=count))
    return final_info


def generate_password(count):
    final_password = ''.join(random.choices(
        ascii_lowercase + digits, k=count))
    return final_password


def generate_first_last_name(count):
    final_name = ''.join(random.choices(
        ascii_lowercase, k=count))
    return final_name


def generate_email(count):
    final_email = ''.join(random.choices(
        ascii_lowercase + digits, k=count))
    return final_email + '@gmail.com'

