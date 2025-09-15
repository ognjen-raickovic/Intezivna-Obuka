#5
class Podcast():
    def __init__(self, naziv, br_pozitivni, br_negativni):
        self.naziv = naziv
        self.br_pozitivni = br_pozitivni
        self.br_negativni = br_negativni
    def odnos(self):
        return self.br_pozitivni/self.br_negativni


podcasti = [
    Podcast("Español para principiantes", 1000, 10),
    Podcast("Philophize This!", 500, 30),
    Podcast("Science VS.", 600, 45)
]

najgori = min(podcasti, key=lambda p: p.odnos())
print(najgori.naziv)

#7
class Book():
    def __init__(self, naslov, autor, godina_izdanja, br_kopija):
        self.naslov = naslov
        self.godina_izdanja = godina_izdanja
        self.br_kopija = br_kopija
    def get_naslov(self):
        return self.naslov
    
    def get_autor(self):
        return self._autor

    def get_godina_izdanja(self):
        return self._godina_izdanja

    def get_br_kopija(self):
        return self._br_kopija

    def set_naslov(self, naslov):
        self._naslov = naslov

    def set_autor(self, autor):
        self._autor = autor

    def set_godina_izdanja(self, godina_izdanja):
        self._godina_izdanja = godina_izdanja

    def set_br_kopija(self, br_kopija):
        self._br_kopija = br_kopija

class Library():
    def __init__(self):
        self.knjige = []

    def dodaj_knjige(self, knjiga):
        self.knjige.append(knjiga)

    def obrisi_knjigu(self, naslov):
        self.knjige = [knjiga for knjiga in self.knjige if knjiga.get_naslov() != naslov]

    def pretraga_po_naslovu(self, naslov):
        self.knjige = [knjiga for knjiga in self.knjige if naslov.lower() in knjiga.get_naslov().lower()]
    
    def pretraga_po_autoru(self, autor):
        self.knjige = [knjiga for knjiga in self.knjige if autor.lower() in knjiga.get_autor.lower()]
    
    def prikazi_knjige(self):
        if not self.knjige:
            print("Nema trenutno knjiga u biblioteci.")
        for knjiga in self.knjige:
            print(f"{knjiga.get_naslov()} | {knjiga.get_autor()} | {knjiga.get_godina_izdanja()}")

if __name__ == "__main__":
    biblioteka = Library()

    while True:
        print("\n--- BIBLIOTEKA ---")
        print("1. Dodaj knjigu")
        print("2. Prikazi sve knjige")
        print("3. Pretrazi po naslovu")
        print("4. Pretrazi po autoru")
        print("5. Obrisi knjigu")
        print("6. Uredi knjigu")
        print("0. Izlaz")

        choice1 = input("Unesite jednu od sljedecih opcija: ")
        
        if choice1 == "1":
            input('Unesite knjigu: ')
        elif choice1 == "2":
            biblioteka.prikazi_knjige()
        elif choice1 == "3":
            naslov = input("Unesite naslov za pretragu: ")
            rezultat = biblioteka.pretraga_po_naslovu(naslov)
            for knjiga in rezultat:
                print(f"{knjiga.get_naslov()} | {knjiga.get_autor()} | {knjiga.get_godina_izdanja()}")
        elif choice1 == "4":
            autor = input("Unesite autora za pretragu: ")
            rezultat = biblioteka.pretraga_po_autoru(autor)
            for knjiga in rezultat:
                print(f"{knjiga.get_naslov()} | {knjiga.get_autor()} | {knjiga.get_godina_izdanja()}")
        elif choice1 == "5":
            naslov = input("Unesite naslov knjige za brisanje: ")
            biblioteka.obrisi_knjigu(naslov)
            print("Knjiga obrisana (ako je postojala).")

        elif choice1 == "6":
            naslov = input("Unesite naslov knjige koju zelite da izmijenite: ")
            rezultat = biblioteka.pretraga_po_naslovu(naslov)
            if rezultat:
                knjiga = rezultat[0]
                print("Izaberite sta mijenjate: 1. Naslov 2. Autor 3. Godina 4. Broj kopija")
                choice2 = input("Opcija: ")
                if choice2 == "1":
                    knjiga.set_naslov(input("Novi naslov: "))
                elif choice2 == "2":
                    knjiga.set_autor(input("Novi autor: "))
                elif choice2 == "3":
                    knjiga.set_godina_izdanja(input("Nova godina izdanja: "))
                elif choice2 == "4":
                    knjiga.set_br_kopija(int(input("Novi broj kopija: ")))
                print("Knjiga azurirana!")
            else:
                print("Knjiga nije pronadjena.")

        if choice1 == '0':
            print("Izlaz iz programa...")
            break
        else:
            print("Netacan unos.")

#12
