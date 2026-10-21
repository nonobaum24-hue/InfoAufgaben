import random

EINSATZ = 2            # fester Einsatz pro Wurf
STARTGUTHABEN = 10     # Anzahl Münzen am Anfang
BODEN = "Z0"           # Kellerbodensymbol
MUENZE = "$"           # ein Symbol = 1 Münze


def guthaben(keller):
    return len(keller) - 1


def main():
    keller = [BODEN] + [MUENZE] * STARTGUTHABEN
    zustand = "BEREIT"

    print("=== Kellerautomat: Münzwurf ===")
    print(f"Fester Einsatz pro Wurf: {EINSATZ} | Startguthaben: {guthaben(keller)}")
    print("Du tippst auf Kopf oder Zahl. Richtig = Einsatz gewonnen, falsch = verloren.\n")

    while zustand != "ENDE":
        if zustand == "BEREIT":
            print(f"Keller: {''.join(keller)}  (Guthaben: {guthaben(keller)})")

            if guthaben(keller) < EINSATZ:
                print("Nicht genug Guthaben für einen weiteren Wurf.")
                zustand = "ENDE"
                continue

            eingabe = input("[k]opf, [z]ahl oder [q]uit: ").strip().lower()
            if eingabe == "q":
                zustand = "ENDE"
            elif eingabe in ("k", "z"):
                tipp = "Kopf" if eingabe == "k" else "Zahl"
                zustand = "WURF"
            else:
                print("Ungültige Eingabe.\n")

        elif zustand == "WURF":
            ergebnis = random.choice(["Kopf", "Zahl"])
            print(f"Münze zeigt: {ergebnis}")
            zustand = "GEWONNEN" if ergebnis == tipp else "VERLOREN"

        elif zustand == "GEWONNEN":
            for _ in range(EINSATZ):
                keller.append(MUENZE)        # push
            print(f"Gewonnen! +{EINSATZ}\n")
            zustand = "BEREIT"

        elif zustand == "VERLOREN":
            for _ in range(EINSATZ):
                keller.pop()                 # pop
            print(f"Verloren! -{EINSATZ}\n")
            zustand = "BEREIT"

    print(f"\nSpiel beendet. Endguthaben: {guthaben(keller)}")


if __name__ == "__main__":
    main()