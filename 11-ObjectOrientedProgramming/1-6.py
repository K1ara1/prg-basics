class Phone():
    def __init__(self,battery):
        self.muted = False
        self.charging = True
        self.calling = False
        self.battery = battery

    def is_calling(self):
        self.calling = True

    def is_muted(self):
        self.muted = False
    
    def is_charging(self):
        self.charging = False

    def display_info(self):
        print(f'My battery is {self.battery}')
        if self.calling:
            print('My phone is calling.')
        else:
            print('My phone is not calling.')
        if self.muted:
            print('My phone is muted')
        else:
            print('My phone is not muted')
        if self.charging:
            print('My phone is charging')
        else:
            print('My phone is not charging')

def main():
    my_phone = Phone(100)
    my_phone.is_calling()
    my_phone.is_muted()
    my_phone.is_charging()
    my_phone.display_info()
    

if __name__ =="__main__":
    main()

        