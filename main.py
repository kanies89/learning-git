# Zadanie 1
"""
Załóżmy, że mamy do zrobienia zakupy spożywcze, potrzebujemy pójść do piekarni, w której kupujemy chleb, bułki oraz pączka.
Poza tym po drodze wstąpimy też do warzywniaka, gdzie kupimy marchew, seler i rukolę.

W pliku, który właśnie utworzyliśmy:

zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: Idę do <sklep> i kupuję tam <rzeczy>.
Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były
wypisane wielką literą (sięgnij do oficjalnej dokumentacji, by odnaleźć taką funkcjonalność).
Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.. X to sumaryczna liczba towarów, które są na listach.
Twój program po uruchomieniu, powinien wyświetlić następujące informacje:

Lista zakupów
Idę do Piekarnia, kupuję tu następujące rzeczy: ['Chleb', 'Pączek', 'Bułki'].
Idę do Warzywniak, kupuję tu następujące rzeczy: ['Marchew', 'Seler', 'Rukola'].
W sumie kupuję 6 produktów.
"""

groceries = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

for n in groceries:
    x = []
    for m in groceries[n]:
        x.append(m.capitalize())
    print(f'Idę do {n.capitalize()}, kupuję tu następujące rzeczy: {x}')

# Zadanie 2

"""
apisz program, który:

Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
W następnym wierszu wyświetli te liczby podniesione do potęgi 3.
Przesyłanie zadań
Zrób zrzuty ekranu z uruchomienia Twoich programów przez VSCode wraz z ich kodem źródłowym i wyślij je swojemu Mentorowi.

Wskazówka: Staraj się trzymać porządek w strukturze projektu i plików. Dobrym pomysłem będzie utrzymywanie każdego zadania jako osobnego pliku.

Zestaw zrzutów ekranu przekaż Mentorowi w jeden z poniższych sposobów:

umieść je w nowym katalogu na swoim dysku sieciowym (np. Dropbox, Google Drive, etc.), wklej poniżej link do katalogu (uzyskany za pomocą guzika "Udostępnij"),
otwórz nowy dokument na Google Docs i przeciągnij do niego zrzuty ekranu, wklej poniżej link do tego dokumentu (uzyskany za pomocą guzika "Udostępnij"),
zrób zdjęcie ekranu aparatem typu Polaroid i wyślij je gołębiem pocztowym.
"""

x_5 = []
x_5_3 = []

for x in range(0,101):
    if x % 5 == 0:
        x_5.append(x)

for x in x_5:
    x_5_3.append(x**3)
print(x_5)
print(x_5_3)