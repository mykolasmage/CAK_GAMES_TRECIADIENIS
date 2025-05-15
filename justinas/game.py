import tkinter as tk



istorija = {
    "pradzia": {
        "tekstas": "Tu atsibundi Salos pakrastyje. Takeliai veda i siaure ir rytus.",
        "pasirinkimai": {
            "Eiti i siaurę": "duobe",
            "Eiti i rytus": "ezeras"
        }
    },
    "duobe": {
        "tekstas": "Randi tamse duobe. Is vidaus girdisi urzgimas. Ar ieisi?",
        "pasirinkimai": {
            "ieiti i duobe": "gyvaciu lyzdas",
            "Grizti atgal": "pradzia"
        }
    },
    "ezeras": {
        "tekstas": "Prieni prie ezero. Yra valtis. Toliau stovi tiltas.",
        "pasirinkimai" : {
            "Sesti i valti": "krokodilas",
            "Eiti per tilta": "senas namas",
            "Grizti atgal": "pradzia"
        }
    },
    "senas namas": {
        "tekstas": "Randi sena apleista nama.",
        "pasirinkimai": {
            "ieiti": "namas",
            "Grizti atgal": "pradzia"
        }

    },

    "namas": {
        "tekstas": "prasideda naktis. ar tu nakvosi namie ar liksi lauke?",
        "pasirinkimai": {
            "nakvoti": "rytas",
            "lykti lauke": "vabzdziai"
        }
    },

    "rytas": {
        "tekstas": "tu atsibundi. ar busi namuke ar  eisi tuoliau?",
        "pasirinkimai": {
            "eiti tuoliau": "pieva",
            "lykti": "Objektas"
        }
    },

    "Objektas": {
        "tekstas": "Tu nusprendei lykti namuke ir tu randi auksine dezute",
        "pasirinkimai": {
            "atidaryti": "prakeiksmas",
            "neatidaryti": "rytas"

        }
    },

    "namas2": {
        "tekstas": "tu nusprendiai lykti namuke. ar tu tikrai isitikines?",
        "pasirinkimai": {
            "lykti": "vaiduoklis",
            "iseiti": "pieva"
        }
    },
    "pieva": {
        "tekstas": "Tu atsiduriai pievoje. Tu randi viena arkli. Ka darysi?",
        "pasirinkimai" : {
            "pabandyti sesti ant jo": "jis tave pervercia",
            "nuzudyti ji": "Jis nubego",
            "ignoruoti": "pieva2"
        }
    },

    "pieva2": {
        "tekstas": "tu eini po pieva ir randi grybu. ka darysi?",
        "pasirinkimai": {
            "suvalgyti juos": "jie buvo nuodingi",
            "ignoruoti juos": "pieva3"
        }
    },
    "pieva3": {
        "tekstas": "Eini per pieva ir randi deze",
        "pasirinkimai": {
            "Atidaryti": "Ten buvo gyvates",
            "Ignoruoti": "Papludimys"
        }
    },
    "Papludimys": {
        "tekstas": "Tu randi papludimi",
        "pasirinkimai": {
            "grizti i pradzia": "pradzia",
            "likti": "pabaiga"

        }
    },
    "pabaiga": {
        "tekstas": "Tave isgelbejo!",
        "pasirinkimai": {
            "zaisti is naujo": "pradzia",
            
        }

    }


}


dabartine_scena = "pradzia"
teksto_laukas = None
mygtuku_remas = None

def rodyti_scena():
    global dabartine_scena, teksto_laukas, mygtuku_remas

    
    for widget in mygtuku_remas.winfo_children():
        widget.destroy()

    scena = istorija[dabartine_scena]
    teksto_laukas.config(text=scena["tekstas"])

    
    for pasirinkimo_tekstas, kita_scena in scena["pasirinkimai"].items():
        mygtukas = tk.Button(mygtuku_remas, text=pasirinkimo_tekstas, bg="#88c411", foreground="white", width=30, command=lambda ns=kita_scena: keisti_scena(ns))
        mygtukas.pack(pady=5) 




def keisti_scena(nauja_scena):
    global dabartine_scena
    dabartine_scena = nauja_scena
    rodyti_scena()







def paleisti():
    global teksto_laukas, mygtuku_remas

    langas = tk.Tk()
    langas.title("Sala")
    langas.config(bg="#88c411")


    teksto_laukas = tk.Label(langas, wraplength=400, font=("Arial", 14), bg="#88c411", foreground="white")
    teksto_laukas.pack(pady=20)

    mygtuku_remas = tk.Frame(langas, bg="#88c411")
    mygtuku_remas.pack()

    
    rodyti_scena()

    langas.mainloop()








if __name__ == "__main__":
    paleisti()
