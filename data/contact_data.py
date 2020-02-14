from model.contact import Contact
import random
import string


def random_data(pre, limit):
    chars = string.ascii_letters + string.digits + " "
    body = "".join([random.choice(chars) for i in range(random.randrange(limit))])
    return f"{pre}{body}"


def random_number():
    nums = "".join([random.choice(string.digits) for i in range(10)])
    return f"{nums}"


def random_email(limit):
    name = "".join([random.choice(string.ascii_letters) for i in range(random.randrange(limit))])
    domain = random.choice(["gmail.com", "yahoo.com", "hotmail.com", "msn.com", "aol.com"])
    return f"{name}@{domain}"


data_provider = [
    Contact(first_name=random_data("f_n", 8), last_name=random_data("l_n", 8), title=random_data("t_", 5),
            company=random_data("c_", 6), primary_address=random_data("Address_", 30),
            mobile_number=random_number(), home_number=random_number(), work_number=random_number(),
            email=random_email(10), email2=random_email(10), email3=random_email(10))
]