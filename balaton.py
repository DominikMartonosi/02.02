class Balaton:
    def __init__(self, települes, fekves, lakossag):
        self.települes = települes
        self.fekves = fekves
        self.lakossag= lakossag
    def fekv(self):
        if self.fekves =='é':
            return 'északi parti'
        elif self.fekves =='d':
            return 'déli parti' 
    def lakos(self):
        if self.lakossag >= 10000:
            return 'város'
        elif self.lakossag >= 5000:
            return 'nagyközség'
        else:
            return 'falu'
        
lista=[]
for _ in range(2):
    telepnév=input('Add meg egy település nevét! ')
    hely=input('Add meg a fekvése (északi vagy déli(é/d))! ')
    szám=int(input('Add meg a lakosság számát! '))
    lista2 = Balaton(telepnév,hely,szám)
    lista.append(lista2)
for listak in lista:
    print(listak.települes,'egy',listak.fekv(),listak.lakos(),',', szám,'fővel.')