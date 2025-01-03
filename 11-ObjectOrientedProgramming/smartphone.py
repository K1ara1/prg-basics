from contact import Contact
from contact_list import Contacts_List

def main():
    contact_list = Contacts_List()
    contact_list.add(Contact("John Brown", "brown@onet.pl", "555234000"))
    contact_list.add(Contact("Anna May", "am@o2.pl", "232000199"))
    contact_list.add(Contact("George Small", "smallg@google.pl", "222999100"))
    contact_list.add(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    contact_list.display()

if __name__ == "__main__":
    main()