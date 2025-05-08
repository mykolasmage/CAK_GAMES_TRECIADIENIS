import tkinter as tk

#Zaidimo istorija
istorija = {
    "pradzia": {
        "tekstas": "Tu atsibundi Lemties miško pakraštyje. Takeliai veda į šiaurę ir rytus.",
        "pasirinkimai": {
            "Eiti į šiaurę": "urvas",
            "Eiti į rytus": "upe"
        }
    },
    "urvas": {
        "tekstas": "Randi tamsų urvą. Iš vidaus girdisi urzgimas. Ar įeisi?",
        "pasirinkimai": {
            "Įeiti į urvą": "meska",
            "Grįžti atgal": "pradzia"
        }
    },
    "meska": {
        "tekstas": "Pamatai mešką. Bet pamatai ir kitą takelį kuris veda gilyn į urvą.",
        "pasirinkimai": {
            "Grįžti atgal": "urvas",
            "Eiti prie meškos": "meska suvalgo", 
            "Eiti kitu takeliu": "gilyn i urva"
        }
    },
    "meska suvalgo": {
        "tekstas": "Meška tave suvalgė. Pralaimėjai.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "gilyn i urva": {
        "tekstas": "Nuėjai giliau į urvą ir pamatei išėjimą, bet jį saugo meška.",
        "pasirinkimai": {
            "Eiti prie meškos": "meska suvalgo",
            "Grįžti atgal": "meska"
        }
    }, 
    "upe": {
        "tekstas": "Prieni plačią ir sraunią upę. Yra valtis be irklų. Toliau stovi tiltas.",
        "pasirinkimai": {
            "Sėsti į valtį": "krioklys",
            "Eiti per tiltą": "miskas",
            "Grįžti atgal": "pradzia"
        }
    },
    "krioklys": {
        "tekstas": "Tu nukritai nuo krioklio ir mirei.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "miskas": {
        "tekstas": "Tu priėjai mišką. Kur eisi toliau?",
        "pasirinkimai": {
            "eiti į kairę": "misko kaire",
            "eiti tiesiai": "misko vidurys",
            "eiti į dešinę": "misko desine",
            "grįžti atgal": "upe"
        }
    },
    "misko kaire": {
        "tekstas": "Tu priėjai vilką ir jis tave suvalgė.",
        "pasirinkimai": {
            "pradėti iš naujo": "pradzia"
        }
    },
    "misko vidurys": {
        "tekstas": "Tu priėjai kryžkėlę kurioje parašyta, kad toliau yra tryjų raganų namai.",
        "pasirinkimai": {
            "eiti į mėlyną namą": "namas1", 
            "eiti į raudoną namą": "namas2", 
            "eiti į žalią namą": "namas3",
            "grįžti atgal": "miskas"
        }
    },
    "namas1": {
        "tekstas": "Name buvo mėlyna ragana. Ji davė tau melyną eleksyrą. Ar jį gersi?",
        "pasirinkimai": {
            "Taip": "kitas pasaulis",
            "Ne": "namas sugriuvo",
            "grįžti atgal": "misko vidurys"
        }
    },
    "namas sugriuvo": {
        "tekstas": "Ragana supyko, sugriovė namą ir tu mirei.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "kitas pasaulis": {
        "tekstas": "Tu užmigai ir atsiradai kitam pasaulyje.",
        "pasirinkimai": {
            "Eiti prie skraidančio žmogaus": "skraidantis zmogus",
            "Eiti prie jūros": "jura",
            "Eiti prie šuns": "suo",
            "Eiti prie baisaus namo": "baisus namas"
        }
    },
    "skraidantis zmogus": {
        "tekstas": "Skraidantis žmogus pasiūlė tau eiti į jo namus.",
        "pasirinkimai": {
            "Eiti": "skraidancio zmogaus namai",
            "Grįžti atgal": "kitas pasaulis"
        }
    },
    "skraidancio zmogaus namai": {
        "tekstas": "Namuose jis turėjo vilką kuris tave suvalgė.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "jura": {
        "tekstas": "Tu priėjai prie jūros ir ryklys tave suvalgė.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "baisus namas": {
        "tekstas": "Tu įėjai į namą ir sutikai vaiduoklį.",
        "pasirinkimai": {
            "Kalbėti su juo": "vaiduoklis",
            "grįžti atgal": "kitas pasaulis"
        }
    },
    "vaiduoklis": {
        "tekstas": "Vaiduoklis buvo draugiškas ir pasakė, kad šuo žino kaip tau grįžti namo",
        "pasirinkimai": {
            "grįžti atgal": "kitas pasaulis"
        }
    },
    "suo": {
        "tekstas": "Šuo pasakė, kad žino kaip tu gali grįžti namo",
        "pasirinkimai": {
            "Eiti su šunimi": "du keliai",
            "Grįžti atgal": "kitas pasaulis"
        }
    },
    "du keliai": {
        "tekstas": "Jūs priėjote du kelius, bet šuo pamiršo kuris teisingas.",
        "pasirinkimai": {
            "Eiti į kairę": "laimejimas",
            "Eiti į dešinę": "blogas kelias",
            "Grįžti atgal": "suo"
        }
    },
    "blogas kelias": {
        "tekstas": "Jūs nuėjote blogu keliu ir mirėte",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "laimejimas": {
        "tekstas": "Jūs priėjote portalą kuris sugrąžins tave namo",
        "pasirinkimai": {
            "Eiti į portalą": "namai",
            "Grįžti atgal": "du keliai"
        }
    },
    "namai": {
        "tekstas": "Jūs grįžote namo!",
        "pasirinkimai": {
            "Toliau": "zaidimo pabaiga"
        }
    },
    "zaidimo pabaiga": {
        "tekstas": "Ačiū, kad žaidei",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "namas2": {
        "tekstas": "Name buvo raudona ragana. Ji tau davė raudoną eleksyrą. Ar jį gersi?",
        "pasirinkimai": {
            "Taip": "raudonas eleksyras",
            "Ne": "sudegino nama",
            "grįžti atgal": "misko vidurys"
        }
    },
    "raudonas eleksyras": {
        "tekstas": "Tu išgėrei raudoną eleksyra ir mirei.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "sudegino nama": {
        "tekstas": "Ragana supyko ir sudegino namą.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "namas3": {
        "tekstas": "Name buvo žalia ragana. Ji tau davė žalią eleksyrą. Ar jį gersi?",
        "pasirinkimai": {
            "Taip": "zalias eleksyras",
            "Ne": "ragana iskepe",
            "grįžti atgal": "misko vidurys"
        }
    },
    "zalias eleksyras": {
        "tekstas": "išgerei eleksyrą ir sprogai",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "ragana iskepe": {
        "tekstas": "Ragana supyko ir tave iškepė",
        "pasirinkimai": {
           "Pradėti iš naujo": "pradzia"
        }
    },
    "misko desine": {
        "tekstas": "Tu priėjai kryžkėlę.",
        "pasirinkimai": {
            "eiti prie ežero": "ezeras",
            "eiti prie žmogaus": "zmogus",
            "grįžti atgal": "miskas"
        }
    },
    "ezeras": {
        "tekstas": "Tu radai ežerą, bet iššoko pabaisa ir tave suvalgė",
        "pasirinkimai": {
            "pradėti iš naujo": "pradzia",
        }
    },
    "zmogus": {
        "tekstas": "Tu sutikai žmogų, bet jis tave nužudė",
        "pasirinkimai": {
            "pradėti iš naujo": "pradzia"
        }
    },
}

#globalus kintamieji
dabartine_scena = "pradzia"
teksto_laukas = None
mygtuku_remas = None
inventorius = []

def rodyti_scena():
    global dabartine_scena, teksto_laukas, mygtuku_remas
    
    #isvalyti senus mygtukus
    for widget in mygtuku_remas.winfo_children():
        widget.destroy()

    scena = istorija[dabartine_scena]
    teksto_laukas.config(text=scena["tekstas"])

    #sukurti naujus pasirinkimo mygtukus
    for pasirinkimo_tekstas, kita_scena in scena["pasirinkimai"].items():
        mygtukas = tk.Button(mygtuku_remas, text=pasirinkimo_tekstas, width=30, command=lambda ns=kita_scena: keisti_scena(ns))
        mygtukas.pack(pady=5)

    #inventorius
    inventoriaus_tekstas = "Inventorius: " + (", ".join(inventorius) if inventorius else "Tuščias")
    inv_label = tk.Label(mygtuku_remas, text=inventoriaus_tekstas, fg="gray")
    inv_label.pack(pady=5)


#Funkcija scenai keisti
def keisti_scena(nauja_scena):
    global dabartine_scena
    dabartine_scena = nauja_scena
    rodyti_scena()


#Paleidimo funkcija
def paleisti():
    global teksto_laukas, mygtuku_remas

    langas = tk.Tk()
    langas.title("Lemties miškas")

    teksto_laukas = tk.Label(langas, wraplength=400, font=("Helvetica", 14))
    teksto_laukas.pack(pady=20)

    mygtuku_remas = tk.Frame(langas)
    mygtuku_remas.pack()

    #kvieciam funkcija
    rodyti_scena()

    langas.mainloop()

if __name__ == "__main__":
    paleisti()

