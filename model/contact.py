from sys import maxsize


class Contact:

    def __init__(self, first_name=None, last_name=None, title=None, company=None, primary_address=None,
                 mobile_number=None, email=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.company = company
        self.primary_address = primary_address
        self.mobile_number = mobile_number
        self.email = email
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.last_name}:{self.first_name}"

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id)
                and self.first_name == other.first_name
                and self.last_name == other.last_name)

    def by_id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
