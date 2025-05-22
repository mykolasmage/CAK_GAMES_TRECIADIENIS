import tkinter as tk

istorija = {
    "pradzia": {
        "tekstas": "Atsikeli namuose. Gali eiti i mokykylal, eiti su draugais ir nesimokiti ",
        "pasirinkimai": {
            "Eiti i mokykla" "eiti_i_klase",
            "Eiti su draugais ir nesimokiti": "vartok_narkotikus",
            "pagalvoti": "eiti i pamoka"
        }
    },
    "eiti_i_klase": {
        "tekstas": "Prieini klase. Yra mikta mokitoja ir gali eiti pas draugelius.",
        "pasirinkimai": {
            "mokitis matematikos": "padeti draugui",
            
        }
    },
    "kalbanti_lenta": {
        "tekstas": "lenta kalba: 'ispresk veiksma ir galesi eti i kita klase.'",
        "pasirinkimai": {
            "ispresti veiksma":
        }
    },
    "veiksmas": {
        "tekstas": "'49*52?'",
        "pasirinkimai": {
            "2548": "3569",
            "5215": "1635"
        }
    },
    "2548": {
        "tekstas": "lenta sako teisinga"
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

    if not scena["pasirinkimai"]:
        pabaiga = tk.Label(mygtuku_remas, text="Žaidimas baigtas. Uždaryk langą.", fg="red")
        pabaiga.pack(pady=10)
        return

    for pasirinkimo_tekstas, kita_scena in scena["pasirinkimai"].items():
        mygtukas = tk.Button(mygtuku_remas, text=pasirinkimo_tekstas, width=40, command=lambda ns=kita_scena: keisti_scena(ns))
        mygtukas.pack(pady=5)

def keisti_scena(nauja_scena):
    global dabartine_scena
    dabartine_scena = nauja_scena
    rodyti_scena()

def paleisti():
    global teksto_laukas, mygtuku_remas

    langas = tk.Tk()
    langas.title("Pabėgimas iš Magiško Miško")

    teksto_laukas = tk.Label(langas, wraplength=500, font=("Helvetica", 14), justify="left")
    teksto_laukas.pack(pady=20)

    mygtuku_remas = tk.Frame(langas)
    mygtuku_remas.pack()

    rodyti_scena()
    langas.mainloop()

if __name__ == "__main__":
    paleisti()
