ekwipunek = {'miecz': 1, 'mikstura': 3, 'złoto': 15}

def pokaz():
    print(ekwipunek)

def dodaj():
    n = input("Podaj przedmiot\n")
    if sum(ekwipunek.values()) < 20:
        if n in ekwipunek:
            ekwipunek[n] += 1
        else:
            ekwipunek[n] = 1
    else:
        print("Limit 20 sztuk osiągnięty")

def uzyj():
    a = input("Podaj przedmiot\n")
    if a in ekwipunek:
        ekwipunek[a] -= 1
        if ekwipunek[a] <= 0:
            del ekwipunek[a]
    else:
        print("Nie ma tego przedmiotu w ekwipunku")

def sprawdz():
    c = input("Podaj przedmiot\n")
    if c in ekwipunek:
        print(c, "jest w ekwipunku")
    else:
        print("Nie ma tego przedmiotu w ekwipunku")


print("1. Pokaz przedmioty")
print("2. Dodaj przedmiot")
print("3. Uzyj przedmiotu")
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