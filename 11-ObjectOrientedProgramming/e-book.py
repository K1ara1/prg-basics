class eBook():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current = 0
        self.is_open = False
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def change_page(self,page):
        if self.is_open:
            self.current = page
        else:
            print('Ebook is closed. Open ebook to change pages.')
    def status(self):
        if self.is_open:
            print(f"'{self.title}' by {self.author}.Page {self.current} of {self.pages}.")
        else:
            print(f"'{self.title}' by {self.author}.Ebook is closed.")
    
def main():
    my_e_book = eBook("The Great Gatsby","F.Scott Fitzgerald",180)
    my_e_book.status()
    my_e_book.open()
    my_e_book.status()
    my_e_book.change_page(20)
    my_e_book.status()
    my_e_book.close()
    my_e_book.change_page(10)
if __name__ =="__main__":
    main()
    
        

