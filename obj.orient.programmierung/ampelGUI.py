#------------------------------------------------------------------------------
# Datenmodell
#------------------------------------------------------------------------------

from ampel import *
ampel = Ampel('rot')
ampel2 = Ampel('gruen')

#------------------------------------------------------------------------------
# GUI
#------------------------------------------------------------------------------

def anzeigeAktualisiereng(ampelnummer, lampeRot, lampeGelb, lampeGruen):
    if ampelnummer == 1:
        rot = labelRot
        gelb = labelGelb
        gruen = labelGruen
    elif ampelnummer == 2:
        rot = labelRot2
        gelb = labelGelb2
        gruen = labelGruen2
    elif ampelnummer == 3:
        rot = labelRot3
        gelb = labelGelb3
        gruen = labelGruen3

    if lampeRot:
        rot.config(background='red')
    else:
        rot.config(background='gray')

    if lampeGelb:
        gelb.config(background='yellow')
    else:
        gelb.config(background='gray')

    if lampeGruen:
        gruen.config(background='green')
    else:
        gruen.config(background='gray')
    

def buttonWeiterClick():
    ampel.schalten()
    (lampeRot, lampeGelb, lampeGruen) = ampel.getLampen()
    anzeigeAktualisiereng(1, lampeRot, lampeGelb, lampeGruen)

    ampel2.schalten()
    (lampeRot, lampeGelb, lampeGruen) = ampel2.getLampen()
    anzeigeAktualisiereng(2, lampeRot, lampeGelb, lampeGruen)


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
frameAmpel2.place(x=180, y=20, width=100, height=40)
# Label Rot-Licht
labelRot2 = Label(master=frameAmpel2, background='gray')
labelRot2.place(x=10, y=10, width=20, height=20)
# Gelb-Licht
labelGelb2 = Label(master=frameAmpel2, background='gray')
labelGelb2.place(x=40, y=10, width=20, height=20)
# Grün-Licht
labelGruen2 = Label(master=frameAmpel2, background='gray')
labelGruen2.place(x=70, y=10, width=20, height=20)

# Aktualisierung der Anzeige
(lampeRot, lampeGelb, lampeGruen) = ampel.getLampen()
anzeigeAktualisiereng(1, lampeRot, lampeGelb, lampeGruen)

(lampeRot, lampeGelb, lampeGruen) = ampel2.getLampen()
anzeigeAktualisiereng(2, lampeRot, lampeGelb, lampeGruen)

# Button zum Auswerten
buttonWeiter = Button(master=fenster,
                      text="weiter",
                      command=buttonWeiterClick)
buttonWeiter.place(x=50, y=150, width=100, height=20)
# Start der Ereignisschleife
fenster.mainloop()
