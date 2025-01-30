**System Ekspertowy** 

To prosty system ekspercki wspierający użytkowników w wyborze odpowiedniego samochodu na podstawie ich potrzeb, preferencji oraz budżetu. Program wykorzystuje zestaw reguł, aby rekomendować kategorie samochodów oraz konkretne modele.

-----
**Funkcjonalności**

- **Zbieranie informacji od użytkownika**: System zadaje pytania dotyczące preferencji (np. rodzaj samochodu, budżet, potrzeby użytkowe).
- **Wnioskowanie na podstawie reguł**: Reguły pozwalają dopasować rekomendacje do zebranych danych.
- **Lista modeli samochodów**: Program podaje konkretne propozycje modeli odpowiadających wybranej kategorii.
- **Intuicyjny interfejs tekstowy**: Użytkownik odpowiada na pytania w sposób prosty (np. „tak/nie” lub liczbowo).
-----
` `**Logika programu**

1. **Zbieranie faktów**:
   1. Program zadaje pytania użytkownikowi, np.:
      1. „Czy potrzebujesz samochodu rodzinnego?” (tak/nie)
      1. „Jaki jest Twój budżet na samochód?” (kwota w PLN)
   1. Odpowiedzi są zapisywane jako fakty w systemie.
1. **Zasady (reguły)**:
   1. Reguły opisują zależności między potrzebami użytkownika a rekomendowanymi kategoriami samochodów.
   1. Przykład:
(lambda f: f.get("family\_car") and f.get("large\_trunk"), "SUV lub kombi dla rodzin.")


1. **Dopasowanie modeli**:
   1. Na podstawie zebranych rekomendacji program podaje konkretne modele samochodów z bazy.
-----
` `**Struktura projektu**

- car\_expert\_system.py: Główny plik programu.
- README.md: Plik dokumentacji projektu
-----


