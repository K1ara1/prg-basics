class Contacts_List():
    def __init__(self):
        self.contacts = []
    def add(self,new_contact):
        self.contacts.append(new_contact)
    def display(self):
        for new_contact in self.contacts:
            print(new_contact)