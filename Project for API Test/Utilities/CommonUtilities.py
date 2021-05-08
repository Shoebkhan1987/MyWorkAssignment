import random
import string

def generate_random_name_and_email():
    random_name_string = ''.join(random.choices(string.ascii_lowercase, k=5)) #+ ''.join(random.choices(string.ascii_lowercase, 4))
    name = random_name_string

    random_email_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    email = random_email_string + '@test.com'

    random_data = {'name': name, 'email': email}
    return random_data



