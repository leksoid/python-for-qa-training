from sys import maxsize


class Contact:

    def __init__(self, first_name=None, last_name=None, title=None, company=None, primary_address=None,
                 mobile_number=None, home_number=None, work_number=None, all_phones=None, email=None, email2=None,
                 email3=None, id=None, all_emails=None):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.company = company
        self.primary_address = primary_address
        self.mobile_number = mobile_number
        self.email = email
        self.id = id
        self.all_phones = all_phones
        self.home_number = home_number
        self.work_number = work_number
        self.email2 = email2
        self.email3 = email3
        self.all_emails = all_emails

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
