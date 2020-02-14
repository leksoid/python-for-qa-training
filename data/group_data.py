import random
import string
from model.group import Group


def random_data(pre, limit):
    chars = string.ascii_letters + string.digits + " "
    body = "".join([random.choice(chars) for i in range(random.randrange(limit))])
    return f"{pre}{body}"


data_provider = [
    Group(name=random_data("name", 10), header=random_data("header", 20), footer=random_data("footer", 20)),
    Group(name="", header="", footer="")
]