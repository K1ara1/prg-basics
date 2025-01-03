class C:
    def __init__(self,name,surname,age,seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = str(seniority)
    def show(self):
        if self.age >= 18:
            print(self.surname.upper() + self.name[0].upper() + self.seniority)
        else:
            print(self.surname.lower() + self.name[0].lower() + self.seniority)

def main():
    employee_data1 = C("Anna","May",17,7)
    employee_data2 = C("George","Brown",21,4)
    employee_data1.show()
    employee_data2.show()

if __name__ =="__main__":
    main()

