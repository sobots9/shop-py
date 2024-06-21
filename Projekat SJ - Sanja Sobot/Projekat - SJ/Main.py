import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sobot99",
    database = "mydbsj"
)

cursor = mydb.cursor()

#FUNKCIJE ZA ADMINA
def izborAdmina(idAdmin) :
    if idAdmin == 1 :
        print("\n Izaberite opciju funkcije koju zelite da obavite: ")
        print("1. Dodajte sat")
        print("2. Prikaz stanja satova")
        print("3. Uklanjanaje sata")
        print("4. Izmena cene sata")
        print("5. Prikaz grafa")
        unosBr = int(input("Unesite broj: "))
        print("\n")

        if unosBr == 1 :
            print("Izabrali ste funkciju dodavanja sata")
            dodajSat(idAdmin)
        elif unosBr == 2 :
            print("Izabrali ste funkciju prikaz stanja satova")
            prikazSatova()
        elif unosBr == 3 :
            print("Izabrali ste funkciju uklanjanja sata")
            ukloniSat()
        elif unosBr == 4 :
            print("Izabrali ste funkciju izmena cene sata")
            izmenaCeneSata()
        elif unosBr == 5 :
            print("Izabrali ste funkciju prikaza grafa")
            prikazGraf1()
        else :
            print("Pogresan unos!")
            opetAdmin()
    else :
        print("\n Izaberite opciju funkcije koju zelite da obavite: ")
        print("1. Dodajte nakit")
        print("2. Prikaz stanja nakita")
        print("3. Uklanjanaje nakita")
        print("4. Izmena cene nakita")
        print("5. Prikaz grafa")
        unosBr = int(input("Unesite broj: "))
        print("\n")

        if unosBr == 1 :
            print("Izabrali ste funkciju dodavanja nakita")
            dodajNakit(idAdmin)
        elif unosBr == 2 :
            print("Izabrali ste funkciju prikaz stanja nakita")
            prikazNakita()
        elif unosBr == 3 :
            print("Izabrali ste funkciju uklanjanja nakita")
            ukloniNakit()
        elif unosBr == 4 :
            print("Izabrali ste funkciju izmene cene nakita")
            izmenaCeneNakita()
        elif unosBr == 5 :
            print("Izabrali ste funkciju prikaza grafa")
            prikazGraf2()
        else :
            print("Pogresan unos!")
            opetAdmin()


def opetAdmin() :
    br = int(input("Ukoliko zelite da odabrete jos neku funkciju unesite 1, a ukoliko ne zelite unesite 2: "))
    if br==1 :
        idAdmin = int(input("Radi potvrde identiteta ponovo unesite Vas ID: "))
        if idAdmin == 1 or idAdmin == 2 :
            izborAdmina(idAdmin)
        else :
            print("Niste potvrdili identitet!")
    elif br==2 :
        print("Ne zelite da nastavite. Dovidjenja!")
    else :
        print("Greska! Pogresan unos!")

#Funkcije za admina satova

def dodajSat(idAdmin) :
    prazanstr = ""
    print("Unesite podatke o satu kojeg unosite!")
    idSat = input("Unesite ID sata:" + "\n")
    naziv = input("Unesite naziv sata:" + "\n")
    cena = input("Unesite cenu sata:" + "\n")
    kolicina = input("Unesite kolicinu satova:" + "\n")
    if naziv != prazanstr and cena != prazanstr and kolicina != prazanstr :
        dodavanje1 = "INSERT INTO sat (idSat, nazivSata, Admin_idAdmin) VALUES (%s,%s,%s)"
        val1 = (idSat, naziv, idAdmin)
        cursor.execute(dodavanje1, val1)
        dodavanje2 = "INSERT INTO infosat (idInfoSat, cenaSat, kolicinaSat, Sat_idSat) VALUES (%s, %s, %s, %s)"
        val2 = (idSat, cena, kolicina, idSat)
        cursor.execute(dodavanje2, val2)
        dodavanjeUPrikaz1(idSat)
        mydb.commit()
        print("Uspesno ste dodali novi sat u bazu podataka!")
    else :
        print("Greska prilikom unosa podataka o satu!")
    opetAdmin()

def dodavanjeUPrikaz1(idSat) :
    upit1 = "SELECT idKorisnik FROM korisnik"
    cursor.execute(upit1)
    idKorisnika = cursor.fetchall()
    size1 = len(idKorisnika)

    upit2 = "SELECT idPrikazSat FROM prikazsat"
    cursor.execute(upit2)
    idPrikaz = cursor.fetchall()
    size = len(idPrikaz)

    for x in range(size1) :
        y = x + 1
        idP = size + y
        dodavanje = "INSERT INTO prikazsat (idPrikazSat, Korisnik_idKorisnik, Sat_idSat) VALUES (%s, %s, %s)"
        val = (idP, y, idSat)
        cursor.execute(dodavanje, val)
        mydb.commit()
    
def prikazSatova() :
    br = int(input("Unesite broj koliko satova zelite da prikazete:"))
    if br != 0 :
        for x in range(br):
            y = int(input("Unesite ID sata: " + "\n"))
            val=(y, )
            prikaz1 = "SELECT nazivSata FROM sat WHERE idSat = %s"
            cursor.execute(prikaz1, val)
            rez11 = cursor.fetchone()
            rez1 = rez11[-1]
            prikaz2= "SELECT cenaSat FROM infosat WHERE Sat_idSat = %s"
            cursor.execute(prikaz2, val)
            rez22 = cursor.fetchone()
            rez2 = rez22[-1]
            prikaz3 = "SELECT kolicinaSat FROM infosat WHERE Sat_idSat = %s"
            cursor.execute(prikaz3, val)
            rez33 = cursor.fetchone()
            rez3 = rez33[-1]
            print("Naziv sata: ", rez1)
            print("Cena sata: ", rez2)
            print("Kolicina satova na lageru: ", rez3)
    else :
        print("Greska! Niste popunili potrebna polja!") 
    opetAdmin()   

def ukloniSat() :
    idSat = int(input("Unesite ID sata kojeg zelite da obrisete: " + "\n"))
    if idSat != 0 :
        val1 = (idSat, )
        izbrisi2 = "DELETE FROM infosat WHERE Sat_idSat = %s"
        cursor.execute(izbrisi2, val1)
        izbrisi3 = "DELETE FROM prikazsat WHERE Sat_idSat = %s"
        cursor.execute(izbrisi3, val1)
        izbrisi1 = "DELETE FROM sat WHERE idSat = %s"
        cursor.execute(izbrisi1, val1)
        mydb.commit()
        #updatePrikazaSat()
        print("Uspesno ste obrisali sat iz baze podataka!" + "\n")
    else :
        print("Greska! Niste uneli odgovarajuci parametar!")
    opetAdmin()

#def updatePrikazaSat() :
#    izbrisi1 = ("DELETE FROM prikazSat")
#    cursor.execute(izbrisi1)   
#    mydb.commit()

#    upit1 = "SELECT idKorisnik FROM korisnik"
#    cursor.execute(upit1)
#    idKorisnika = cursor.fetchall()
#    size1 = len(idKorisnika)   

#    upit3 = "SELECT idSat FROM sat"
#    cursor.execute(upit3)
#    idSat = cursor.fetchall()
#    size2 = len(idSat)

#    for x in range(size2) :
#        for y in range(size1) :
#            upit2 = "SELECT idPrikazSat FROM prikazsat"
#            cursor.execute(upit2)
#            idPrikaz = cursor.fetchall()
#            br = 0
#            br1 = br + 1
#            dodavanje = "INSERT INTO prikazsat (idPrikazSat, Korisnik_idKorisnik, Sat_idSat) VALUES (%s, %s, %s)"
#            val = (br1, x, y)
#            cursor.execute(dodavanje, val)
#            mydb.commit()


def izmenaCeneSata() :
    prazan = ""
    print("Unesite podatke o satu koje zelite da izmenite")
    idSat = input("Unesite ID sata:" + "\n")
    novaCena = input("Unesite novu cenu sata" + "\n")
    if idSat != prazan or novaCena != prazan :
        upit = "UPDATE infosat SET cenaSat = %s WHERE Sat_idSat = %s "
        val = (novaCena, idSat)
        cursor.execute(upit, val)
        mydb.commit()
    print("Ispis novih podataka o satu:" + "\n")
    prikaz1 = "SELECT nazivSata FROM sat WHERE idSat = %s"
    val = (idSat, )
    cursor.execute(prikaz1, val)
    rez11 = cursor.fetchone()
    rez1 = rez11[-1]
    prikaz2= "SELECT cenaSat FROM infosat WHERE Sat_idSat = %s"
    val = (idSat, )
    cursor.execute(prikaz2, val)
    rez22 = cursor.fetchone()
    rez2 = rez22[-1]
    print("Naziv sata: ", rez1)
    print("Nova cena sata: ", rez2)
    opetAdmin()

#Funkcije za admina nakita

def dodajNakit(idAdmin) :
    prazanstr = ""
    print("Unesite podatke o nakitu koje unosite!")
    idNakit = input("Unesite ID nakita:" + "\n")
    naziv = input("Unesite naziv nakita:" + "\n")
    cena = input("Unesite cenu nakita:" + "\n")
    kolicina = input("Unesite kolicinu nakita:" + "\n")
    if naziv != prazanstr and cena != prazanstr and kolicina != prazanstr :
        dodavanje1 = "INSERT INTO nakit (idNakit, nazivNakita, Admin_idAdmin) VALUES (%s,%s,%s)"
        val1 = (idNakit, naziv, idAdmin)
        cursor.execute(dodavanje1, val1)
        dodavanje2 = "INSERT INTO infonakit (idInfoNakit, cenaNakita, kolicinaNakita, Nakit_idNakit) VALUES (%s, %s, %s, %s)"
        val2 = (idNakit, cena, kolicina, idNakit)
        cursor.execute(dodavanje2, val2)
        dodavanjeUPrikaz2(idNakit)
        mydb.commit()
        print("Uspesno ste dodali novi nakit u bazu podataka!")
    else :
        print("Greska prilikom unosa podataka o nakitu!")
    opetAdmin()

def dodavanjeUPrikaz2(idNakit) :
    upit1 = "SELECT idKorisnik FROM korisnik"
    cursor.execute(upit1)
    idKorisnika = cursor.fetchall()
    size1 = len(idKorisnika)

    upit2 = "SELECT idPrikazNakit FROM prikaznakit"
    cursor.execute(upit2)
    idPrikaz = cursor.fetchall()
    size = len(idPrikaz)

    for x in range(size1) :
        y = x + 1
        idP = size + y
        dodavanje = "INSERT INTO prikaznakit (idPrikazNakit, Korisnik_idKorisnik, Nakit_idNakit) VALUES (%s, %s, %s)"
        val = (idP, y, idNakit)
        cursor.execute(dodavanje, val)
        mydb.commit()

def prikazNakita() :
    br = int(input("Unesite broj koliko nakita zelite da prikazete:"))
    if br != 0 :
        for x in range(br):
            y = int(input("Unesite ID nakita: " + "\n"))
            val=(y, )
            prikaz1 = "SELECT nazivNakita FROM nakit WHERE idNakit = %s"
            cursor.execute(prikaz1, val)
            rez11 = cursor.fetchone()
            rez1 = rez11[-1]
            prikaz2= "SELECT cenaNakita FROM infonakit WHERE Nakit_idNakit = %s"
            cursor.execute(prikaz2, val)
            rez22 = cursor.fetchone()
            rez2 = rez22[-1]
            prikaz3 = "SELECT kolicinaNakita FROM infonakit WHERE Nakit_idNakit = %s"
            cursor.execute(prikaz3, val)
            rez33 = cursor.fetchone()
            rez3 = rez33[-1]
            print("Naziv nakita: ", rez1)
            print("Cena nakita: ", rez2)
            print("Kolicina nakita na lageru: ", rez3)
    else :
        print("Greska! Niste popunili potrebna polja!") 
    opetAdmin()   

def ukloniNakit() :
    idSat = int(input("Unesite ID nakita kojeg zelite da obrisete: " + "\n"))
    if idSat != 0 :
        val1 = (idSat, )
        izbrisi2 = "DELETE FROM infonakit WHERE Nakit_idNakit = %s"
        cursor.execute(izbrisi2, val1)
        izbrisi3 = "DELETE FROM prikaznakit WHERE Nakit_idNakit = %s"
        cursor.execute(izbrisi3, val1)
        izbrisi1 = "DELETE FROM nakit WHERE idNakit = %s"
        cursor.execute(izbrisi1, val1)
        mydb.commit()
        print("Uspesno ste obrisali izabrani nakit iz baze podataka!" + "\n")
    else :
        print("Greska! Niste uneli odgovarajuci parametar!")
    opetAdmin()

def izmenaCeneNakita() :
    prazan = ""
    print("Unesite podatke o nakitu koje zelite da izmenite")
    idNakita= input("Unesite ID nakita:" + "\n")
    novaCena = input("Unesite novu cenu nakita" + "\n")
    if idNakita != prazan or novaCena != prazan :
        upit = "UPDATE infonakit SET cenaNakita = %s WHERE Nakit_idNakit = %s "
        val = (novaCena, idNakita)
        cursor.execute(upit, val)
        mydb.commit()
    print("Ispis novih podataka o satu:" + "\n")
    prikaz1 = "SELECT nazivNakita FROM nakit WHERE idNakit = %s"
    val = (idNakita, )
    cursor.execute(prikaz1, val)
    rez11 = cursor.fetchone()
    rez1 = rez11[-1]
    prikaz2= "SELECT cenaNakita FROM infonakit WHERE Nakit_idNakit = %s"
    val = (idNakita, )
    cursor.execute(prikaz2, val)
    rez22 = cursor.fetchone()
    rez2 = rez22[-1]
    print("Naziv nakita: ", rez1)
    print("Nova cena nakita: ", rez2)
    opetAdmin()

#Funkcija za graf

def prikazGraf1() :
    upit1 = "SELECT kolicinaSat FROM infosat ORDER BY kolicinaSat"
    cursor.execute(upit1)
    x = cursor.fetchall()
    upit2 = "SELECT nazivSata FROM sat"
    cursor.execute(upit2)
    y = cursor.fetchall()
    kolicina = []
    naziv = []
    for i in x :
        kolicina.append(int(i[0]))
    for z in y :
        naziv.append(z[0])
    print(kolicina)
    print(naziv)
    plt.bar(naziv, kolicina)
    plt.ylim(0,30)
    plt.xlabel('NAZIVI SATOVA')
    plt.xticks(rotation = 90)
    plt.ylabel('KOLICINA')
    plt.title('PRIKAZ KOLICINE SATOVA')
    plt.show()
    opetAdmin()

def prikazGraf2() :
    upit1 = "SELECT ukupnaCenaNakit FROM racunnakit"
    cursor.execute(upit1)
    x = cursor.fetchall()
    upit2 = "SELECT ukupnaCenaSat FROM racunsat"
    cursor.execute(upit2)
    y = cursor.fetchall()
    ukupnoNakit = []
    ukupnoSat = []
    for i in x :
        ukupnoNakit.append(int(i[0]))
    for z in y :
        ukupnoSat.append(int(z[0]))
    plt.plot(ukupnoNakit)
    plt.plot(ukupnoSat)
    plt.show()
    opetAdmin()

#FUNKCIJE ZA KORISNIKA

def izborKorisnika(idKupac) :
    print("\n Izaberite opciju funkcije koju zelite da obavite: ")
    print("1. Pogledajte informacije o satu")
    print("2. Uporedite cene satova")
    print("3. Kupovina sata")
    print("4. Pogledajte informacije o nakitu")
    print("5. Uporedite cene nakita")
    print("6. Kupovina nakita")
    
    unosBr = int(input("Unesite broj: "))
    print("\n")

    if unosBr == 1 :
        print("Izabrali ste funkciju informacije o satu")
        informacijeSat()
    elif unosBr == 2 :
        print("Izabrali ste funkciju poredjenja cena dva sata")
        uporediCenu()
    elif unosBr == 3 :
        print("Izabrali ste funkciju kupovina sata")
        kupiSat(idKupac)
    elif unosBr == 4 :
        print("Izabrali ste funkciju informacije o nakitu")
        informacijeNakit()
    elif unosBr == 5 :
        print("Izabrali ste funkciju poredjenja cena dva nakita")
        uporediCenuNakita()
    elif unosBr == 6 :
        print("Izabrali ste funkciju kupovina nakita")
        kupiNakit(idKupac)
    else :
        print("Pogresan unos!")
    opetKorisnik()

def opetKorisnik() :
    br = int(input("Ukoliko zelite da odabrete jos neku funkciju unesite 1, a ukoliko ne zelite unesite 2: "))
    if br==1 :
        idKupac = int(input("Da biste potvrdili identitet unesite Vas ID: "))
        izborKorisnika(idKupac)
    elif br==2 :
        print("Ne zelite da nastavite. Dovidjenja!")
    else :
        print("Greska! Pogresan unos!")

def informacijeSat() :
    prazanstr = ""
    naziv = input("Unesite naziv sata za koji zelite da Vam se prikazu informacije:" + "\n")
    if naziv != prazanstr :
        upit1 = "SELECT idSat FROM sat WHERE nazivSata = %s"
        val = (naziv, )
        cursor.execute(upit1, val)
        id1 = cursor.fetchone()
        id = id1[-1]
        if id>0 :
            upit2 = "SELECT cenaSat FROM infosat WHERE Sat_idSat = %s"
            val1 = (id, )
            info1 = cursor.execute(upit2, val1)
            info = cursor.fetchone()
            infocena = info[-1]
            upit3 = "SELECT kolicinaSat FROM infosat WHERE Sat_idSat = %s"
            val2 = (id, )
            info2 = cursor.execute(upit3, val2)
            info2 = cursor.fetchone()
            infokolicina = info2[-1]
            print("Cena sata u dinarima je: ", infocena, "\n")
            print("Kolicina satova na lageru je: ", infokolicina, "\n")


def uporediCenu() :
    prazanstr = ""
    naziv1 = input("Unesite naziv prvog sata kojeg zelite da uporedite: " + "\n")
    naziv2 = input("Unesite naziv drugog sata kojeg zelite da uporedite: " + "\n")
    if naziv1 != prazanstr and naziv2 != prazanstr:
        val1 = (naziv1, )
        val2 = (naziv2, )
        idP = "SELECT idSat FROM sat WHERE nazivSata = %s"
        idrez1 = cursor.execute(idP, val1)
        rez1 = cursor.fetchone()
        id1 = rez1[-1]
        idD = "SELECT idSat FROM sat WHERE nazivSata = %s"
        idrez2 = cursor.execute(idD, val2)
        rez2 = cursor.fetchone()
        id2 = rez2[-1]
        if id1 > 0 and id2 > 0 :
            upitSat1  = "SELECT cenaSat FROM infosat WHERE Sat_idSat = %s"
            valS1 = (id1, )
            rezs11 = cursor.execute(upitSat1, valS1)
            rezsx1 = cursor.fetchone()
            rezs1 = int(rezsx1[-1])
            upitSat2  = "SELECT cenaSat FROM infosat WHERE Sat_idSat = %s"
            valS2 = (id2, )
            rezs22 = cursor.execute(upitSat2, valS2)
            rezsx2 = cursor.fetchone()
            rezs2 = int(rezsx2[-1])
            x = rezs1-rezs2
            if x > 0 :
                print("Prvi sat je skuplji za:", x, "\n")
            elif x < 0 :
                y = rezs2-rezs1
                print("Drugi sat je skuplji za: ", y, "\n")
            else :
                print("Cene satova su jednake")

def kupiSat(idKupac) :
    prazanstr=""
    nazivSata = input("Unesite naziv sata koji zelite da kupite: \n")
    if nazivSata != prazanstr :
        upitID = "SELECT idSat FROM sat WHERE nazivSata = %s"
        val = (nazivSata, )
        cursor.execute(upitID, val)
        rez = cursor.fetchone()
        idSata = rez[-1]
        upitKolicina = "SELECT kolicinaSat FROM infosat WHERE Sat_idSat = %s"
        val1 = (idSata, )
        cursor.execute(upitKolicina, val1)
        rez1 = cursor.fetchone()
        kolicina = int(rez1[-1])
        if kolicina > 0 :
            print("Izabrani sat imamo na lageru. Maksimalna kolicina sata pri kupovini je: ",  kolicina, "\n")
            brSatova = int(input("Unesite koliko satova zelite da kupite: \n"))
            x = kolicina - brSatova
            upitIzmena = "UPDATE infosat SET kolicinaSat = %s WHERE Sat_idSat = %s"
            val2 = (x, idSata)
            cursor.execute(upitIzmena, val2)
            cena = "SELECT cenaSat FROM infosat WHERE Sat_idSat = %s"
            val3 = (idSata, )
            cursor.execute(cena, val3)
            cena1 = cursor.fetchone()
            cenaKonacno = cena1[-1]
            ukupnaCena = brSatova * cenaKonacno
            mydb.commit()
            print("Uspesno ste kupili sat. Kolicina satova kojeg ste kupili je: ", brSatova, "\n")
            dodajNaRacunSat(ukupnaCena, nazivSata, idKupac, idSata)
        else :
            print("Zao nam je. Trenutno nemamo izabrani sat na lageru.")

def dodajNaRacunSat(ukupnaCena, nazivSata, idKupac, idSata) :
    upit = "SELECT idRacunSat FROM racunsat"
    cursor.execute(upit)
    idRacun = cursor.fetchall()
    size = len(upit)
    size1 = size - 28

    idA = 1
    date = datetime.now()
    datum = date.strftime('%Y-%m-%d %H:%M:%S')

    idR = size1 + 1
    dodaj = "INSERT INTO racunsat(idRacunSat, ukupnaCenaSat, porudzbinaSat, Korisnik_idKorisnik, Sat_idSat, Admin_idAdmin, datumPorudzbineSat) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (idR, ukupnaCena, nazivSata, idKupac, idSata, idA, datum)
    cursor.execute(dodaj, val)
    mydb.commit()
    print("Iznos Vaseg racuna je: ", ukupnaCena)

#Funkcije korisniku za nakit

def informacijeNakit() :
    prazanstr = ""
    naziv = input("Unesite naziv nakita za koji zelite da Vam se prikazu informacije:" + "\n")
    if naziv != prazanstr :
        upit1 = "SELECT idNakit FROM nakit WHERE nazivNakita = %s"
        val = (naziv, )
        cursor.execute(upit1, val)
        id1 = cursor.fetchone()
        id = id1[-1]
        if id>0 :
            upit2 = "SELECT cenaNakita FROM infonakit WHERE Nakit_idNakit = %s"
            val1 = (id, )
            info1 = cursor.execute(upit2, val1)
            info = cursor.fetchone()
            infocena = info[-1]
            upit3 = "SELECT kolicinaNakita FROM infonakit WHERE Nakit_idNakit = %s"
            val2 = (id, )
            info2 = cursor.execute(upit3, val2)
            info2 = cursor.fetchone()
            infokolicina = info2[-1]
            print("Cena nakita u dinarima je: ", infocena, "\n")
            print("Kolicina nakita na lageru je: ", infokolicina, "\n")


def uporediCenuNakita() :
    prazanstr = ""
    naziv1 = input("Unesite naziv prvog nakita kojeg zelite da uporedite: " + "\n")
    naziv2 = input("Unesite naziv drugog drugog kojeg zelite da uporedite: " + "\n")
    if naziv1 != prazanstr and naziv2 != prazanstr:
        val1 = (naziv1, )
        val2 = (naziv2, )
        idP = "SELECT idNakit FROM nakit WHERE nazivNakita = %s"
        idrez1 = cursor.execute(idP, val1)
        rez1 = cursor.fetchone()
        id1 = rez1[-1]
        idD = "SELECT idNakit FROM nakit WHERE nazivNakita = %s"
        idrez2 = cursor.execute(idD, val2)
        rez2 = cursor.fetchone()
        id2 = rez2[-1]
        if id1 > 0 and id2 > 0 :
            upitNakit1  = "SELECT cenaNakita FROM infonakit WHERE Nakit_idNakit = %s"
            valN1 = (id1, )
            rezs11 = cursor.execute(upitNakit1, valN1)
            rezsx1 = cursor.fetchone()
            rezs1 = int(rezsx1[-1])
            upitNakit2  = "SELECT cenaNakita FROM infonakit WHERE Nakit_idNakit = %s"
            valN2 = (id2, )
            rezs22 = cursor.execute(upitNakit2, valN2)
            rezsx2 = cursor.fetchone()
            rezs2 = int(rezsx2[-1])
            x = rezs1-rezs2
            if x > 0 :
                print("Prvi nakit je skuplji za:", x, "\n")
            elif x < 0 :
                y = rezs2-rezs1
                print("Drugi nakit je skuplji za: ", y, "\n")
            else :
                print("Cene nakita su jednake")

def kupiNakit(idKupac) :
    prazanstr=""
    nazivNakita = input("Unesite naziv nakita koji zelite da kupite: \n")
    if nazivNakita != prazanstr :
        upitID = "SELECT idNakit FROM nakit WHERE nazivNakita = %s"
        val = (nazivNakita, )
        cursor.execute(upitID, val)
        rez = cursor.fetchone()
        idNakita = rez[-1]
        upitKolicina = "SELECT kolicinaNakita FROM infonakit WHERE Nakit_idNakit = %s"
        val1 = (idNakita, )
        cursor.execute(upitKolicina, val1)
        rez1 = cursor.fetchone()
        kolicina = int(rez1[-1])
        if kolicina > 0 :
            print("Izabrani nakit imamo na lageru. Maksimalna kolicina nakita pri kupovini je: ",  kolicina, "\n")
            brNakita = int(input("Unesite koliko nakita zelite da kupite: \n"))
            x = kolicina - brNakita
            upitIzmena = "UPDATE infonakit SET kolicinaNakita = %s WHERE Nakit_idNakit = %s"
            val2 = (x, idNakita)
            cursor.execute(upitIzmena, val2)
            cena = "SELECT cenaNakita FROM infonakit WHERE Nakit_idNakit = %s"
            val3 = (idNakita, )
            cursor.execute(cena, val3)
            cena1 = cursor.fetchone()
            cenaKonacno = cena1[-1]
            ukupnaCena = brNakita * cenaKonacno
            mydb.commit()
            print("Uspesno ste kupili nakit. Kolicina nakita kojeg ste kupili je: ", brNakita, "\n")
            dodajNaRacunNakit(ukupnaCena, nazivNakita, idKupac, idNakita)
        else :
            print("Zao nam je. Trenutno nemamo izabrani sat na lageru.")

def dodajNaRacunNakit(ukupnaCena, nazivNakita, idKupac, idNakita) :
    upit = "SELECT idRacunNakit FROM racunnakit"
    cursor.execute(upit)
    idRN = cursor.fetchall()
    size = len(upit)
    size1 = size - 32

    idA = 2
    date = datetime.now()
    datum = date.strftime('%Y-%m-%d %H:%M:%S')

    idN = size + 1
    dodaj = "INSERT INTO racunnakit(idRacunNakit, ukupnaCenaNakit, porudzbinaNakit, Korisnik_idKorisnik, Nakit_idNakit, Admin_idAdmin, datumPorudzbineNakit) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (idN, ukupnaCena, nazivNakita, idKupac, idNakita, idA, datum)
    cursor.execute(dodaj, val)
    mydb.commit()
    print("Iznos Vaseg racuna je: ", ukupnaCena)

#LOGIN

def logInAdmin():
    prazan=""
    korisnickoImeAdmin = input("Unesite korisnicko ime:" + "\n")
    lozAdmin = input("Unesite lozinku: " + "\n")
    print("\n")
    if korisnickoImeAdmin != prazan and lozAdmin != prazan:
        adminID = "SELECT idAdmin FROM admin WHERE korisnickoImeAdmin = %s AND lozinkaAdmin = %s"
        values = (korisnickoImeAdmin, lozAdmin)
        cursor.execute(adminID, values)
        idA = cursor.fetchone()
        idAdmin = idA[-1]
        print("Uspesno ste se prijavili, Vas ID je: ", idAdmin, "\n")
        izborAdmina(idAdmin)
    else :
        print("Greska! Niste popunili sva polja!")

def logInKorisnik() :
    prazan = ""
    korisnickoIme = input ("Unesite korisnicko ime: ")
    lozinkaKorisnik = input ("Unesite lozinku: ")
    if korisnickoIme != prazan and lozinkaKorisnik != prazan :
        idK = "SELECT idKorisnik FROM korisnik WHERE korisnickoImeKorisnika = %s AND lozinkaKorisnika = %s"
        values = (korisnickoIme, lozinkaKorisnik)
        cursor.execute(idK, values)
        idK1 = cursor.fetchone()
        idKupac = idK1[-1]
        print("Uspesno ste se prijavili, Vas ID je: ", idK, "\n")
        izborKorisnika(idKupac)
    else :
        print("Greska! Niste popunili sva potrebna polja!")

#MAIN

print("Da biste se prijavili potrebno je da unesete broj.")
print("Unesite 1 ako se prijavljujete kao admin")
print("Unesite 2 ako se prijavljujete kao korisnik")

unos = int(input("Unesite broj: "))
print("\n")

if unos == 1 :
    print("Prijavljujete se kao admin")
    logInAdmin()
elif unos == 2 :
    print("Prijavljujete se kao korisnik")
    logInKorisnik()
else :
    print("Pogresan unos!")