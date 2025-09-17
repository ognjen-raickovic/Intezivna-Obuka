# cetvrta grupa zadataka (Domaci zadatak 4.pdf)

#2. 
def studenti_iznad_85(imena, ocjene):
    return [(ime, ocjena) for ime, ocjena in zip(imena, ocjene) if ocjena > 8.5]

imena = ["Marko", "Ana", "Boris", "Mina"]
ocjene = [9.2, 7.8, 8.6, 8.4]
print(studenti_iznad_85(imena, ocjene))  

# 5.
from functools import reduce

def prosjek_po_predmetu(lista):
    predmeti = set(map(lambda x: x[2], lista))
    rezultat = {}

    for predmet in predmeti:
        ocjene = list(map(lambda x: x[1],
                          filter(lambda x: x[2] == predmet, lista)))
        suma = reduce(lambda a, b: a + b, ocjene)
        rezultat[predmet] = suma / len(ocjene)
    return rezultat

lista = [("Marko", 9, "Matematika"), ("Ana", 8, "Matematika"),
         ("Boris", 10, "Programiranje"), ("Mina", 9, "Programiranje")]
print(prosjek_po_predmetu(lista))

# 14.
def append_to_file(student_list, filename="students.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        for s in student_list:
            f.write(f"{s['ime']},{s['prezime']},{s['godina']},{s['prosjek']}\n")


def get_students_with_greater_grade(year, grade, filename="students.txt"):
    grade_ranges = {
        "A": (9.5, 10),
        "B": (8.5, 9.5),
        "C": (7.5, 8.5),
        "D": (6.5, 7.5),
        "E": (6.0, 6.5)
    }

    low, high = grade_ranges[grade]
    studenti = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            ime, prezime, godina, prosjek = line.strip().split(",")
            godina, prosjek = int(godina), float(prosjek)
            if godina == year and prosjek >= low:
                studenti.append({
                    "ime": ime, "prezime": prezime,
                    "godina": godina, "prosjek": prosjek
                })
    return studenti

student_list = [
    {"ime": "Marko", "prezime": "Markovic", "godina": 2, "prosjek": 8.6},
    {"ime": "Boris", "prezime": "Boricic", "godina": 3, "prosjek": 7.9},
    {"ime": "Novak", "prezime": "Novovic", "godina": 3, "prosjek": 6.9}
]
append_to_file(student_list)
print(get_students_with_greater_grade(3, "C"))

# 16.
import os
from datetime import datetime

VALID_GENRES = ["Action", "RPG", "Adventure", "Strategy", "Sports"]

def valid_game(game):
    naziv, ocjena, godina, izdavac, zanrovi = game
    if not (2 <= len(naziv) <= 50):
        return False
    try:
        ocjena = float(ocjena)
        if not (1 <= ocjena <= 10):
            return False
    except:
        return False
    if not (1950 < int(godina) < datetime.now().year):
        return False
    if izdavac and not (2 <= len(izdavac) <= 40):
        return False
    zanrovi_lista = zanrovi.split()
    if len(zanrovi_lista) > 3 or any(z not in VALID_GENRES for z in zanrovi_lista):
        return False
    return True

def load_games(filename="igrice.txt"):
    igre = []
    if not os.path.exists(filename):
        return igre
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == 5 and valid_game(parts):
                naziv, ocjena, godina, izdavac, zanrovi = parts
                igre.append({
                    "naziv": naziv,
                    "ocjena": float(ocjena),
                    "godina": int(godina),
                    "izdavac": izdavac,
                    "zanrovi": zanrovi.split()
                })
    return igre

def filter_games(igre, by, value):
    if by == "naziv":
        return [g for g in igre if g["naziv"].startswith(value)]
    elif by == "ocjena":
        return [g for g in igre if g["ocjena"] > float(value)]
    elif by == "godina_before":
        return [g for g in igre if g["godina"] < int(value)]
    elif by == "godina_after":
        return [g for g in igre if g["godina"] > int(value)]
    elif by == "izdavac":
        return [g for g in igre if g["izdavac"].startswith(value)]
    elif by == "zanr":
        return [g for g in igre if value in g["zanrovi"]]
    else:
        return []

# 17.
import time
from functools import wraps

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        rezultat = func(*args, **kwargs)
        end = time.time()
        print(f"Funkcija {func.__name__} trajala je {end - start:.4f} sekundi")
        return rezultat
    return wrapper

@timer_decorator
def suma_do_n(n):
    return sum(range(n))

@timer_decorator
def sporo_mnozenje(n):
    rez = 1
    for i in range(1, n):
        rez *= i
    return rez

print(suma_do_n(10**6))
print(sporo_mnozenje(10000))
