const studenti = [
  { ime: "Marko", prezime: "Petrović", godina: 3, ocjene: [9, 8, 7, 10, 9] },
  { ime: "Ana", prezime: "Jovanović", godina: 1, ocjene: [7, 6, 8, 6, 7] },
  { ime: "Luka", prezime: "Simić", godina: 2, ocjene: [10, 9, 10, 8, 9] },
  { ime: "Maja", prezime: "Nikolić", godina: 4, ocjene: [6, 5, 7, 6, 6] },
  { ime: "Ivana", prezime: "Stanković", godina: 1, ocjene: [9, 10, 9, 8, 9] },
];

//a)  Napisati funkciju koja prolazi kroz niz i ispisuje studente koji imaju prosjek veći od 8.5.
//Ukoliko student ne zadovoljava kriterijum, ispiši samo njegovo ime.

function izracunajProsjek(ocjene) {
  let s = 0;
  for (let i = 0; i < ocjene.length; i++) {
    s += ocjene[i];
  }
  return s / ocjene.length;
}

function ispisiStudente(studenti) {
  for (let i = 0; i < studenti.length; i++) {
    let student = studenti[i];
    let prosjek = izracunajProsjek(student.ocjene);
    if (prosjek > 8.5) {
      console.log(student.ime + " " + student.prezime + " Prosjek: " + prosjek);
    } else {
      console.log(student.ime);
    }
  }
}

ispisiStudente(studenti);

//b)  Napisati funkciju koja pronalazi i ispisuje studenta sa najvišim prosjekom.
function najboljiStudent(studenti) {
  let best = "";
  let najboljiProsjek = 0;
  for (let i = 0; i < studenti.length; i++) {
    let student = studenti[i];
    let prosjek = izracunajProsjek(student.ocjene);
    if (prosjek > najboljiProsjek) {
      najboljiProsjek = prosjek;
      best = `${student.ime} ${student.prezime}`;
    }
  }
  console.log(`Najbolji student je ${best}.`);
}

najboljiStudent(studenti);

//c)  Napisati funkciju koja izračunava i ispisuje prosječan prosjek svih studenata u nizu.
function ispisiProsjeke(studenti) {
  let s = 0;
  for (let i = 0; i < studenti.length; i++) {
    let student = studenti[i];
    let prosjek = izracunajProsjek(student.ocjene);
    s += prosjek;
  }
  console.log(Math.round((s / studenti.length) * 100) / 100);
}

ispisiProsjeke(studenti);

//d)  Napisati funkciju koja sortira studente po prosjeku u opadajućem redosledu i ispisuje ih
function sortirajDesc(studenti) {
  studenti.sort(function (a, b) {
    let student1 = izracunajProsjek(a.ocjene);
    let student2 = izracunajProsjek(b.ocjene);

    return student2 - student1;
  });

  for (let i = 0; i < studenti.length; i++) {
    let prosjek = izracunajProsjek(studenti[i].ocjene);
    console.log(
      `${studenti[i].ime} ${studenti[i].prezime} ${
        Math.round(prosjek * 100) / 100
      }`
    );
  }
}
sortirajDesc(studenti);

//e)  Za svakog studenta u nizu, dodajte novi ključ prosjek sa odgovarajućom vrijednošću i
//ispišite novonastali niz studenata.
function dodajProsjek(studenti) {
  for (let i = 0; i < studenti.length; i++) {
    let student = studenti[i];
    let prosjek = izracunajProsjek(student.ocjene);
    student.prosjek = prosjek;
  }

  for (let i = 0; i < studenti.length; i++) {
    console.log(studenti[i]);
  }
}

dodajProsjek(studenti);
