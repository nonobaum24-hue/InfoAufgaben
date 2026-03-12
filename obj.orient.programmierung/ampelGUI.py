#------------------------------------------------------------------------------
# Datenmodell
#------------------------------------------------------------------------------

from ampel import *
ampel = Ampel('rot')
ampel2 = Ampel('gruen')

#------------------------------------------------------------------------------
# GUI
#------------------------------------------------------------------------------

def anzeigeAktualisieren(lampeRot, lampeGelb, lampeGruen):
    if lampeRot:
        labelRot.config(background='red')
    else:
        labelRot.config(background='gray')
    if lampeGelb:
        labelGelb.config(background='yellow')
    else:
        labelGelb.config(background='gray')
    if lampeGruen:
        labelGruen.config(background='green')
    else:
        labelGruen.config(background='gray')

def anzeigeAktualisieren2(lampeRot, lampeGelb, lampeGruen):
    if lampeRot:
        labelRot2.config(background='red')
    else:
        labelRot2.config(background='gray')
    if lampeGelb:
        labelGelb2.config(background='yellow')
    else:
        labelGelb2.config(background='gray')
    if lampeGruen:
        labelGruen2.config(background='green')
    else:
        labelGruen2.config(background='gray')

def buttonWeiterClick():
    ampel.schalten()
    (lampeRot, lampeGelb, lampeGruen) = ampel.getLampen()
    anzeigeAktualisieren(lampeRot, lampeGelb, lampeGruen)

    ampel2.schalten()
    (lampeRot, lampeGelb, lampeGruen) = ampel2.getLampen()
    anzeigeAktualisieren2(lampeRot, lampeGelb, lampeGruen)


from tkinter import *
# Erzeugung des Fensters
fenster = Tk()
fenster.title("Ampel")
fenster.geometry("400x200")
# Rahmen
frameAmpel = Frame(master=fenster, background='darkgray')
frameAmpel.place(x=80, y=20, width=40, height=100)
# Label Rot-Licht
labelRot = Label(master=frameAmpel, background='gray')
labelRot.place(x=10, y=10, width=20, height=20)
# Gelb-Licht
labelGelb = Label(master=frameAmpel, background='gray')
labelGelb.place(x=10, y=40, width=20, height=20)
# Grün-Licht
labelGruen = Label(master=frameAmpel, background='gray')
labelGruen.place(x=10, y=70, width=20, height=20)

# Rahmen
frameAmpel2 = Frame(master=fenster, background='darkgray')
frameAmpel2.place(x=180, y=20, width=40, height=100)
# Label Rot-Licht
labelRot2 = Label(master=frameAmpel2, background='gray')
labelRot2.place(x=10, y=10, width=20, height=20)
# Gelb-Licht
labelGelb2 = Label(master=frameAmpel2, background='gray')
labelGelb2.place(x=10, y=40, width=20, height=20)
# Grün-Licht
labelGruen2 = Label(master=frameAmpel2, background='gray')
labelGruen2.place(x=10, y=70, width=20, height=20)

# Aktualisierung der Anzeige
(lampeRot, lampeGelb, lampeGruen) = ampel.getLampen()
anzeigeAktualisieren(lampeRot, lampeGelb, lampeGruen)

(lampeRot, lampeGelb, lampeGruen) = ampel2.getLampen()
anzeigeAktualisieren2(lampeRot, lampeGelb, lampeGruen)

# Button zum Auswerten
buttonWeiter = Button(master=fenster,
                      text="weiter",
                      command=buttonWeiterClick)
buttonWeiter.place(x=50, y=150, width=100, height=20)
# Start der Ereignisschleife
fenster.mainloop()
