# top-n-hejterow-fb

Projekt dwuosobowy realizowany w semestrze 2021Z w ramach przedmiotu Wprowadzenie do aplikacji i rozwiązań opartych o Sztuczną Inteligencję i Microsoft Azure.

Celem projektu było stoworzenie prostego serwisu w chmurze Azure wyszukującego nieprzychylne komentarze na stronach marek bądź osób publicznych i grupowanie ich w celu ustalenia czy osoba publikująca je nie jest usilnym hejterem próbującym zniszczyć wizerunek marki poprzez częste komentowanie negatywnych informacji pod postami strony.

## Diagram rozwiązania
![Diagram](https://raw.githubusercontent.com/gubapatryk/top-n-hejterow-fb/main/diagram.png)

## Film z demo działania rozwiązania

[![Film](https://img.youtube.com/vi/nNFsQOQ9-wc/0.jpg)](https://www.youtube.com/watch?v=nNFsQOQ9-wc)

## Zespół
[Patryk Guba](https://github.com/gubapatryk)
[Maxymilian Kowalski](https://github.com/maxxx958)

## Opis funkcjonalności

Stworzone rozwiązanie pozwala na przeanalizowanie komentarzy w postach na stronie dla podanego id strony na Facebooku i zwrócenie listy osób piszących największą ilość "hejtujących" komentarzy.
Z rozwiązania korzystamy poprzez wysłanie zapytania HTTP GET do bezserwerowej funkcji z parametrem "name" reprezentującym id strony.
Jako odpowiedź na zapytanie zostaje zwrócony tekstowy raport zawierający sumę komentarzy dla poszczególnych użytkowników strony, ze szczególnym uwzględnieniem listy "hejterów", czyli osób, które pisały najwięcej komentarzy o negatywnym zabarwieniu emocjonalnym.

## Stos technologiczny

Cognitive services - Language sentiment detection  - wykrywanie sentymentu komentarzy
Function app - uruchomienie bezserwerowej funkcji w pythonie obsługującej zapytania HTTP


