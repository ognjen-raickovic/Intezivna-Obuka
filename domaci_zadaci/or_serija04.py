import requests 
from bs4 import BeautifulSoup
import csv

fakulteti = ['fmefb', 'fkt', 'fist', 'politehnika', 'fpn', 'hs', 'fu', 'fptbhe', 'fsm', 'fdm', 'ff', 'fprn']
known_titles = ["Prof. dr", "Doc. dr", "Doc. mr", "mr", "dr"]
counts = {faks: {} for faks in fakulteti}
with open("professors.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Ime&Prezime", "Titula", "Fakultet"])

    for faks in fakulteti:
        base_url = f'https://{faks}.udg.edu.me/predavaci/'
        print(f'Scraping fakultet: {faks} → {base_url}')
        
        try:
            response = requests.get(base_url)
            if response.status_code != 200:
                print(f"Ne mogu pristupiti {base_url}, status: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            teachers_h6 = soup.select("h6")
            teachers_p = soup.select("h6 + p")
            
            if not teachers_h6:
                print(f"Nema predavača pronađenih na {base_url}")
                continue
            
            for h6, p in zip(teachers_h6, teachers_p):
                full_text = h6.get_text(strip=True)
                title_from_p = p.get_text(strip=True) if p else ""
                title = ""
                name = full_text
                for t in known_titles:
                    if full_text.startswith(t):
                        title = t
                        name = full_text[len(t):].strip()
                        break
                if not title:
                    for t in known_titles:
                        if title_from_p.startswith(t):
                            title = t
                            break
                if not title:
                    continue  

                writer.writerow([name, title, faks])

                counts[faks][title] = counts[faks].get(title, 0) + 1

                print(f"{name} - {title}")
        
        except Exception as e:
            print(f"Greška kod {faks}: {e}")

with open("counts.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Fakultet", "Titula", "Broj"])

    for faks, titule in counts.items():
        for title, broj in titule.items():
            writer.writerow([faks, title, broj])
