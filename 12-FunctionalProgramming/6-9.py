temperaures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
positive = list(filter(lambda city: temperaures[city] > 0,temperaures))
print('Cities with positive temperatures:', ' '.join(positive))