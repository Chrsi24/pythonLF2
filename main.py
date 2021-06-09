def berechnungsTypFunktion():
    while True:
        try:
            berechnungsTyp = input("Möchtest du über Strecke(D) oder über Zeit(T) berechnen?\n")[0]
            if berechnungsTyp in "dD":
                print("Strecke ")
                return "d"
                break

            elif berechnungsTyp in "tT":
                print("Zeit ")
                return "t"
                break

        except:
            print("Bitte eien gültige eingabe...")


def streckenBerechnungsFunktion():
    while True:
        try:
            strecke = int(input("Wie weit möchtest du Fahren (in Km)? \n"))
            break
        except:
            print("Ungültige Eingabe!")
    preis = float(strecke) * 0.75
    return preis


def zeitBerechnungsFunktion():
    while True:
        try:
            zeit = int(input("Wie lange möchtest du Fahren (in Minuten)? \n"))
            break
        except:
            print("Ungültige Eingabe!")
    preis = float(zeit) * 0.25
    return preis


if __name__ == '__main__':
    berechnungsTyp = berechnungsTypFunktion()

    if berechnungsTyp == "d":
        preis = streckenBerechnungsFunktion()
    elif berechnungsTyp == "t":
        preis = zeitBerechnungsFunktion()

    print("Es wird " + str(preis) + "€ kosten.")
    input()
