from model.contact import Contact
import re


def test_contact_information(app):
    test_data = Contact(first_name="John", last_name="Paparonchik", title="CEO", company="Purple Pants",
                        primary_address="1234 Somewhere Rd\nSan Matiago, CA 92109",
                        mobile_number="6192778990", email="paparonchik@pants.com", home_number="6190001122",
                        work_number="9189028877", email2="someone@gmail.com", email3="hey@yahoo.com")
    if app.contact_helper.get_count() == 0:
        app.contact_helper.create(test_data)
    hp_contact = app.contact_helper.get_contacts()[0]
    ep_contact = app.contact_helper.get_contact_from_edit_page(0)
    assert hp_contact.first_name == ep_contact.first_name
    assert hp_contact.last_name == ep_contact.last_name
    assert hp_contact.primary_address == ep_contact.primary_address
    assert hp_contact.all_phones == merge_data(
        [ep_contact.home_number, ep_contact.mobile_number, ep_contact.work_number])
    assert hp_contact.all_emails == merge_data(
        [ep_contact.email, ep_contact.email2, ep_contact.email3])


def merge_data(data):
    return "\n".join(filter(lambda each: each != "",
                            map(lambda each: clear(each),
                                filter(lambda each: each is not None,
                                       [each for each in data]))))


def clear(string):
    return re.sub("[() -]", "", string)
