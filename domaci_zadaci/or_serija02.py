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
        self._naslov = naslov
        self._autor = autor
        self._godina_izdanja = godina_izdanja
        self._br_kopija = br_kopija
    
    def get_naslov(self): return self._naslov
    def get_autor(self): return self._autor
    def get_godina_izdanja(self): return self._godina_izdanja
    def get_br_kopija(self): return self._br_kopija

    def set_naslov(self, naslov): self._naslov = naslov
    def set_autor(self, autor): self._autor = autor
    def set_godina_izdanja(self, godina): self._godina_izdanja = godina
    def set_br_kopija(self, br): self._br_kopija = br

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

        choice = input("Opcija: ")

        if choice == "1":
            naslov = input("Naslov: ")
            autor = input("Autor: ")
            godina = input("Godina izdanja: ")
            kopije = int(input("Broj kopija: "))
            biblioteka.dodaj_knjigu(Book(naslov, autor, godina, kopije))

        elif choice == "2":
            biblioteka.prikazi_knjige()

        elif choice == "3":
            naslov = input("Unesite naslov za pretragu: ")
            for k in biblioteka.pretraga_po_naslovu(naslov):
                print(f"{k.get_naslov()} | {k.get_autor()} | {k.get_godina_izdanja()}")

        elif choice == "4":
            autor = input("Unesite autora: ")
            for k in biblioteka.pretraga_po_autoru(autor):
                print(f"{k.get_naslov()} | {k.get_autor()} | {k.get_godina_izdanja()}")

        elif choice == "5":
            naslov = input("Unesite naslov knjige za brisanje: ")
            biblioteka.obrisi_knjigu(naslov)

        elif choice == "6":
            naslov = input("Naslov knjige za uredjivanje: ")
            rezultat = biblioteka.pretraga_po_naslovu(naslov)
            if rezultat:
                knjiga = rezultat[0]
                print("1. Naslov 2. Autor 3. Godina 4. Broj kopija")
                op = input("Opcija: ")
                if op == "1": knjiga.set_naslov(input("Novi naslov: "))
                elif op == "2": knjiga.set_autor(input("Novi autor: "))
                elif op == "3": knjiga.set_godina_izdanja(input("Nova godina: "))
                elif op == "4": knjiga.set_br_kopija(int(input("Novi broj kopija: ")))
                print("Knjiga azurirana!")

        elif choice == "0":
            break

        else:
            print("Nevazeca opcija!")

#12. 
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} | {self.position} | {self.salary}€"


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        self.employees = [e for e in self.employees if e.name != name]

    def search_employee(self, name):
        return [e for e in self.employees if name.lower() in e.name.lower()]

    def update_salary(self, name, new_salary):
        for e in self.employees:
            if e.name == name:
                e.salary = new_salary
                return True
        return False

    def print_all_employees(self):
        if not self.employees:
            print("Trenutno nema zaposlenih u kompaniji.")
        else:
            for e in self.employees:
                print(e)


if __name__ == "__main__":
    company = Company()

    while True:
        print("\n--- COMPANY ---")
        print("1. Dodaj zaposlenog")
        print("2. Prikazi sve zaposlene")
        print("3. Pretraga zaposlenog po imenu")
        print("4. Obrisi zaposlenog")
        print("5. Azuriraj platu zaposlenog")
        print("0. Izlaz")

        choice = input("Opcija: ")

        if choice == "1":
            name = input("Ime: ")
            position = input("Pozicija: ")
            salary = float(input("Plata (€): "))
            company.add_employee(Employee(name, position, salary))

        elif choice == "2":
            company.print_all_employees()

        elif choice == "3":
            name = input("Unesite ime za pretragu: ")
            results = company.search_employee(name)
            if results:
                for e in results:
                    print(e)
            else:
                print("Nema rezultata.")

        elif choice == "4":
            name = input("Unesite ime zaposlenog za brisanje: ")
            company.remove_employee(name)
            print("Zaposleni obrisan (ako je postojao).")

        elif choice == "5":
            name = input("Unesite ime zaposlenog: ")
            new_salary = float(input("Nova plata (€): "))
            if company.update_salary(name, new_salary):
                print("Plata azurirana.")
            else:
                print("Zaposleni nije pronadjen.")

        elif choice == "0":
            break

        else:
            print("Nevažeća opcija!")
