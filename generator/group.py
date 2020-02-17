import random
import string
import os
import jsonpickle
from model.group import Group
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_data(pre, limit):
    chars = string.ascii_letters + string.digits + " "
    body = "".join([random.choice(chars) for i in range(random.randrange(limit))])
    return f"{pre}{body}"


data_provider = [Group(name="", header="", footer="")] + [
    Group(name=random_data("name", 10), header=random_data("header", 20), footer=random_data("footer", 20))
    for _ in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(data_provider))
