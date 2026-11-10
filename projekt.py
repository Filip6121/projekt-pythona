ekwipunek = {"miecz": 1, "mikstura": 3, "zloto": 50}

def pokaz():
    print(ekwipunek)

def dodaj():
    nazwa = input("Podaj przedmiot\n")
    if nazwa == "zloto":
        print("Nie mozna dodać zlota")
        return
    ilosc = int(input("Podaj ilosc\n"))
    cena = int(input("Podaj cene za sztuke\n"))
    waga = int(input("Podaj wage za sztuke\n"))
    
    koszt = ilosc * cena
    dodana_waga = ilosc * waga
    
    aktualna_waga = 0
    for przed in ekwipunek:
        if przed != "zloto":
            aktualna_waga += ekwipunek[przed]
            
    if ekwipunek["zloto"] < koszt:
        print("Nie masz tyle złota!")
    elif aktualna_waga + dodana_waga > 20:
        print("Za ciężko! Przekroczono limit wagi 20.")
    else:
        ekwipunek["zloto"] -= koszt
        if nazwa in ekwipunek:
            ekwipunek[nazwa] += ilosc
        else:
            ekwipunek[nazwa] = ilosc
        print("Kupiono i dodano pomyślnie!")

def uzyj():
    nazwa = input("Podaj przedmiot\n")
    if nazwa in ekwipunek and nazwa != "zloto":
        wybor = input("Wpisz 'u' (użyj) lub 's' (sprzedaj)\n")
        if wybor == "u":
            ekwipunek[nazwa] -= 1
            print("Użyto przedmiotu.")
        elif wybor == "s":
            ekwipunek[nazwa] -= 1
            ekwipunek["zloto"] += 10
            print("Sprzedano przedmiot za 10 złota.")
            
        if ekwipunek[nazwa] <= 0:
            del ekwipunek[nazwa]
    else:
        print("Nie ma takiego przedmiotu w ekwipunku.")

def sprawdz():
    nazwa = input("Podaj przedmiot\n")
    if nazwa in ekwipunek:
        print(nazwa, "jest w ekwipunku, ilość:", ekwipunek[nazwa])
    else:
        print("Nie ma tego przedmiotu.")

print("1. Pokaz przedmioty")
print("2. Dodaj przedmiot")
print("3. Uzyj / Sprzedaj")
print("4. Sprawdz przedmiot")
print("5. Wyjdz")

while True:
    opcja = int(input("Wybierz opcje\n"))
    if opcja == 1:
        pokaz()
    elif opcja == 2:
        dodaj()
    elif opcja == 3:
        uzyj()
    elif opcja == 4:
        sprawdz()
    elif opcja == 5:
        print("Koncze dzialanie")
        break