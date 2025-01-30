Car Selection Expert System
To prosty system ekspercki wspierający użytkowników w wyborze odpowiedniego samochodu na podstawie ich potrzeb, preferencji oraz budżetu. Program wykorzystuje zestaw reguł, aby rekomendować kategorie samochodów oraz konkretne modele.

  Funkcjonalności
Zbieranie informacji od użytkownika: System zadaje pytania dotyczące preferencji (np. rodzaj samochodu, budżet, potrzeby użytkowe).
Wnioskowanie na podstawie reguł: Reguły pozwalają dopasować rekomendacje do zebranych danych.
Lista modeli samochodów: Program podaje konkretne propozycje modeli odpowiadających wybranej kategorii.
Intuicyjny interfejs tekstowy: Użytkownik odpowiada na pytania w sposób prosty (np. „tak/nie” lub liczbowo).

   
 Logika programu
Zbieranie faktów:

Program zadaje pytania użytkownikowi, np.:
„Czy potrzebujesz samochodu rodzinnego?” (tak/nie)
„Jaki jest Twój budżet na samochód?” (kwota w PLN)
Odpowiedzi są zapisywane jako fakty w systemie.
Zasady (reguły):

Reguły opisują zależności między potrzebami użytkownika a rekomendowanymi kategoriami samochodów.
Przykład:
python
Kopiuj
(lambda f: f.get("family_car") and f.get("large_trunk"), "SUV lub kombi dla rodzin.")
Dopasowanie modeli:

Na podstawie zebranych rekomendacji program podaje konkretne modele samochodów z bazy.


 Struktura projektu
car_expert_system.py: Główny plik programu, zawiera implementację systemu eksperckiego.
README.md: Plik dokumentacji projektu.


   Przykładowe działanie
Pytania programu:

makefile
Kopiuj
Czy potrzebujesz samochodu rodzinnego? (tak/nie)
Odpowiedź: tak
Jaki jest Twój budżet na samochód? (podaj kwotę w PLN)
Odpowiedź: 50000
Czy jeździsz głównie po mieście? (tak/nie)
Odpowiedź: tak
...
Wynik:

markdown
Kopiuj
**Rekomendacje:**
- Hybrydy do miasta.
- Nowe modele z niższego segmentu.

**Proponowane modele samochodów:**
- Toyota Yaris
- Hyundai i20
- Skoda Fabia
- Toyota Prius
- Hyundai Ioniq Hybrid
- Honda Jazz Hybrid
