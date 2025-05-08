import tkinter as tk

# Žaidimo istorija
istorija = {
    "pradzia": {
        "tekstas": "Tu atsibundi Tamsos miško pakraštyje. Takeliai veda į šiaurę ir rytus.",
        "pasirinkimai": {
            "Eiti į šiaurę": "urvas",
            "Eiti į rytus": "upe",
            "Eiti į pietus": "dykuma"
        }
    },
    "urvas": {
        "tekstas": "Randi tamsų urvą. Iš vidaus girdisi urzgimas. Ar įeisi?",
        "pasirinkimai": {
            "Įeiti į urvą": "meska",
            "Grįžti atgal": "pradzia"
        }
    },
    "dykuma": {
        "tekstas": "Eidamas į pietus randi dykumą. Mėtosi krūmas ir kažkokia psichoaktyvi medžiaga ant smėlio.",
        "pasirinkimai": {
            "Pramegoti krūme": "atsikeli",
            "Pasiimti medžiagą": "paimta_medziaga",
            "Grįžti atgal": "pradzia"
        }
    },
    "paimta_medziaga": {
        "tekstas": "Pasiėmei psichoaktyvią medžiagą. Ji dabar tavo kuprinėje.",
        "pasirinkimai": {
            "Grįžti į dykumą": "dykuma_su_medziaga"
        }
    },
    "dykuma_su_medziaga": {
        "tekstas": "Stovi dykumoje. Tavo kuprinėje yra psichoaktyvi medžiaga. Ar ją išrūkysi?",
        "pasirinkimai": {
            "Išrūkyti medžiagą": "rukymas",
            "Pramegoti krūme": "atsikeli",
            "Grįžti atgal": "pradzia"
        }
    },
    "rukymas": {
        "tekstas": "Tu išrūkei psichoaktyvią medžiagą... Aplink pasaulis ima tirpti. Pamatęs viziją – seki šviesą ir atsiduri prie paslaptingos piramidės.",
        "pasirinkimai": {
            "Eiti prie piramidės": "piramide"
        }
    },
    "piramide": {
        "tekstas": "Piramidė atrodo sena ir apleista, bet įėjimas atviras. Viduje sklinda keistas kvapas.",
        "pasirinkimai": {
            "Įeiti į piramidę": "viduje_piramides",
            "Grįžti į dykumą": "dykuma_su_medziaga"
        }
    },
    "viduje_piramides": {
        "tekstas": "Įžengęs į piramidę, pasijunti apsvaigęs. Tave apsupa keisti žmonės su kaukėmis...",
        "pasirinkimai": {
            "Pasiduoti": "mumija",
            "Bėgti": "dykuma_su_medziaga"
        }
    },
    "mumija": {
        "tekstas": "Tave suriša, suvynioja į tvarsčius ir padeda į akmeninį sarkofagą. Tu tampi mumija. Žaidimo pabaiga.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "atsikeli": {
        "tekstas": "Kol miegojai, įkando erkė – tu užsikretei ir mirei po neilgo laiko tarpo.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        } 
    },
    "meska": {
        "tekstas": "Urve pamatai miegantį meškiną. Atsargiai praeini pro jį ir randi slaptą išėjimą į kalvos viršūnę.",
        "pasirinkimai": {
            "Išeiti pro išėjimą": "bokstas",
            "Grįžti atgal": "urvas"
        }
    },
    "upe": {
        "tekstas": "Prieini sraunią upę. Yra valtis be irklų ir tiltas toliau.",
        "pasirinkimai": {
            "Sėsti į valtį": "krioklys",
            "Eiti per tiltą": "pieva",
            "Grįžti atgal": "pradzia"
        }
    },
    "krioklys": {
        "tekstas": "Valtis nevaldomai plaukia... nukrenti nuo krioklio. Žaidimo pabaiga.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "pieva": {
        "tekstas": "Perėjęs tiltą patenki į ramią pievą. Yra senas bokštas ir namelis.",
        "pasirinkimai": {
            "Užlipti į bokštą": "bokstas",
            "Eiti į namelį miške": "namelis",
            "Grįžti prie upės": "upe"
        }
    },
    "namelis": {
        "tekstas": "Namelyje randi pirmosios pagalbos dėžutę. Viduje – pleistras.",
        "pasirinkimai": {
            "Paimti pleistrą": "paimtas_pleistras",
            "Grįžti į pievą": "pieva"
        }
    },
    "paimtas_pleistras": {
        "tekstas": "Tu paimi pleistrą ir įsidedi į kuprinę.",
        "pasirinkimai": {
            "Grįžti į pievą": "pieva"
        }
    },
    "bokstas": {
        "tekstas": "Nuo bokšto viršaus matai miestą vakaruose ir jūrą pietuose.",
        "pasirinkimai": {
            "Eiti link miesto": "miestas",
            "Eiti prie jūros": "jura",
            "Grįžti atgal": "pieva",
            "Eiti prie namo": "namas"
        }
    },
    "namas": {
        "tekstas": "Prieini apleistą namą. Benamis puola tave!",
        "pasirinkimai": {
            "Bandyt gintis": "puolimas"
        }
    },
    "puolimas": {
        "tekstas": "",
        "pasirinkimai": {}
    },
    "jura": {
        "tekstas": "Paplūdimyje stovi senas švyturys. Tolumoje matai laivą.",
        "pasirinkimai": {
            "Eiti į švyturį": "svyturys",
            "Signalizuoti laivui": "laivas",
            "Grįžti atgal": "bokstas"
        }
    },
    "svyturys": {
        "tekstas": "Randi veikiančią signalinę lempą.",
        "pasirinkimai": {
            "Signalizuoti lempa": "laivas",
            "Grįžti į paplūdimį": "jura"
        }
    },
    "laivas": {
        "tekstas": "Laivas pastebi tave ir išgelbėja! Tu pabėgai.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "miestas": {
        "tekstas": "Pasieki miestą. Sveikiname – pabėgai iš miško!",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    },
    "mirtis": {
        "tekstas": "Neturėjai pleistro. Sužeidimai per rimti. Žaidimo pabaiga.",
        "pasirinkimai": {
            "Pradėti iš naujo": "pradzia"
        }
    }
}

# globalūs kintamieji
dabartine_scena = "pradzia"
teksto_laukas = None
mygtuku_remas = None
inventoriaus_laukas = None
inventorius = []

def rodyti_scena():
    global dabartine_scena

    scena = istorija[dabartine_scena]

    # Logika dėl puolimo
    if dabartine_scena == "puolimas":
        if "pleistras" in inventorius:
            dabartine_scena = "miestas"
        else:
            dabartine_scena = "mirtis"
        rodyti_scena()
        return

    # Įsidėjimas į inventorių
    if dabartine_scena == "paimtas_pleistras" and "pleistras" not in inventorius:
        inventorius.append("pleistras")
    if dabartine_scena == "paimta_medziaga" and "psichoaktyvi medžiaga" not in inventorius:
        inventorius.append("psichoaktyvi medžiaga")

    # Atnaujinti tekstą
    teksto_laukas.config(text=scena["tekstas"])

    # Išvalyti mygtukus
    for widget in mygtuku_remas.winfo_children():
        widget.destroy()

    # Kurti mygtukus
    for pasirinkimo_tekstas, kita_scena in scena["pasirinkimai"].items():
        mygtukas = tk.Button(
            mygtuku_remas,
            text=pasirinkimo_tekstas,
            font=("Cinzel", 11, "bold"),
            width=35,
            bg="#2E5939",
            fg="white",
            activebackground="#3B7250",
            activeforeground="white",
            relief="flat",
            command=lambda ns=kita_scena: keisti_scena(ns)
        )
        mygtukas.pack(pady=4)

    # Atnaujinti inventorių
    inventoriaus_laukas.config(text="Inventorius: " + ", ".join(inventorius) if inventorius else "Inventorius: tuščias")

def keisti_scena(nauja):
    global dabartine_scena
    dabartine_scena = nauja
    rodyti_scena()

def paleisti():
    global teksto_laukas, mygtuku_remas, inventoriaus_laukas

    langas = tk.Tk()
    langas.title("🌲 Tamsos Miškas 🌲")
    langas.configure(bg="#1B2A20")

    teksto_laukas = tk.Label(
        langas,
        wraplength=520,
        font=("Georgia", 14),
        justify="left",
        bg="#1B2A20",
        fg="#DDE6D5",
        padx=20,
        pady=20
    )
    teksto_laukas.pack(pady=15)

    mygtuku_remas = tk.Frame(langas, bg="#1B2A20")
    mygtuku_remas.pack()

    inventoriaus_laukas = tk.Label(
        langas,
        text="Inventorius: tuščias",
        font=("Courier New", 10, "italic"),
        bg="#1B2A20",
        fg="#A5C9A3"
    )
    inventoriaus_laukas.pack(pady=10)

    rodyti_scena()
    langas.mainloop()

if __name__ == "__main__":
    paleisti()
