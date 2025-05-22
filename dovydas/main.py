import tkinter as tk

istorija = {
    "pradzia": {
        "tekstas": "Atsikeli magiškame miške. Takeliai veda kairėn, dešinėn ir tiesiai. Girdi keistus garsus.",
        "pasirinkimai": {
            "Eiti kairėn": "sviesus_upelis",
            "Eiti dešinėn": "kalbantis_medis",
            "Eiti tiesiai": "akmenu_apskritimas",
            "Apsižvalgyti": "vijokliu_urvas"
        }
    },
    "sviesus_upelis": {
        "tekstas": "Prieini švytintį upelį. Yra tiltelis ir valtelė.",
        "pasirinkimai": {
            "Pereiti tilteliu": "pelėda_mįslė",
            "Sėsti į valtį": "krioklio_pabaiga"
        }
    },
    "kalbantis_medis": {
        "tekstas": "Milžiniškas medis šneka: 'Atsakyk į mįslę ir praeisi.'",
        "pasirinkimai": {
            "Klausyti mįslės": "medzio_misle"
        }
    },
    "medzio_misle": {
        "tekstas": "'Be burnos kalbu, be ausų girdžiu. Neturiu kūno, bet gyvenu tarp uolų ir medžių. Kas aš?'",
        "pasirinkimai": {
            "Pasakyti: Aidas": "slaptas_takas",
            "Pasakyti: Vėjas": "neteisinga"
        }
    },
    "slaptas_takas": {
        "tekstas": "Medis prasiskleidžia ir parodo slaptą švytintį taką.",
        "pasirinkimai": {
            "Eiti taku": "laisvė"
        }
    },
    "neteisinga": {
        "tekstas": "Medis sušnabžda: 'Klaida.' Kelias užsidaro. Turi grįžti.",
        "pasirinkimai": {
            "Grįžti": "pradzia"
        }
    },
    "akmenu_apskritimas": {
        "tekstas": "Apeini ratą iš senovinių akmenų. Yra trys kryptys: kalva, ola arba grįžti.",
        "pasirinkimai": {
            "Lipti į kalvą": "bokštas",
            "Įeiti į olą": "samanota_ola",
            "Grįžti": "pradzia"
        }
    },
    "vijokliu_urvas": {
        "tekstas": "Tarp vijoklių randi angą. Viduje tamsu, bet sklinda švytėjimas.",
        "pasirinkimai": {
            "Įeiti į urvą": "samanota_ola",
            "Grįžti": "pradzia"
        }
    },
    "samanota_ola": {
        "tekstas": "Oloje šviečia samanos. Priešais siauras tunelis.",
        "pasirinkimai": {
            "Ropoti tuneliu": "lobio_kambarys",
            "Išeiti atgal": "akmenu_apskritimas"
        }
    },
    "lobio_kambarys": {
        "tekstas": "Randi kambaryje raktą ir žemėlapį. Gali padėti pabėgti.",
        "pasirinkimai": {
            "Pasiimti raktą ir žemėlapį": "akmenu_apskritimas",
            "Palikti viską": "pradzia"
        }
    },
    "bokštas": {
        "tekstas": "Kalvos viršuje stovi sargas prie bokšto. Durys užrakintos, bet turi raktą.",
        "pasirinkimai": {
            "Naudoti raktą": "laisvė",
            "Lįsti pro langą": "kritimo_pabaiga"
        }
    },
    "pelėda_mįslė": {
        "tekstas": "Pelėda sako: 'Kas prasideda aušroje, baigiasi prieblandoje ir matoma danguje?'",
        "pasirinkimai": {
            "Pasakyti: Raidė D": "lobio_kambarys",
            "Pasakyti: Saulė": "neteisinga"
        }
    },
    "krioklio_pabaiga": {
        "tekstas": "Valtelė nuplaukia prie krioklio... tu krenti. Žaidimo pabaiga.",
        "pasirinkimai": {}
    },
    "kritimo_pabaiga": {
        "tekstas": "Bandydamas įlipti pro langą nukrenti. Sąmonė pranyksta. Žaidimo pabaiga.",
        "pasirinkimai": {}
    },
    "laisvė": {
        "tekstas": "Išeini iš miško į šviesą. Pabėgai iš magiško miško! Sveikiname!",
        "pasirinkimai": {}
    },
    "gyvūnu_takelis": {
        "tekstas": "Pastebi gyvūnų takelį į krūmus. Takas susilieja su gėlėmis.",
        "pasirinkimai": {
            "Sekti takelį": "snaudziančio_zvėries_urvas",
            "Grįžti": "pradzia"
        }
    },
    "snaudziančio_zvėries_urvas": {
        "tekstas": "Randi urvą. Viduje miega kažkas didelis. Ar pažadinsi?",
        "pasirinkimai": {
            "Pažadinti": "zveris_supyksta",
            "Tyliai pasitraukti": "akmenu_apskritimas"
        }
    },
    "zveris_supyksta": {
        "tekstas": "Žvėris pabunda ir supyksta... Turi bėgti!",
        "pasirinkimai": {
            "Bėgti": "netikras_takas"
        }
    },
    "netikras_takas": {
        "tekstas": "Takelis veda į pelkę. Klampoji ir galiausiai įstringi. Žaidimo pabaiga.",
        "pasirinkimai": {}
    },
    "skaidrus_ezeras": {
        "tekstas": "Prieini skaidrų ežerą. Vidury stovi sala su bokštu.",
        "pasirinkimai": {
            "Plaukti į salą": "sala_mįslė",
            "Apeiti ežerą": "laukiniai_krumai"
        }
    },
    "sala_mįslė": {
        "tekstas": "Ant salos randi raides ant akmens: 'Aš gyvenu šviesoje, bet mano širdis tamsi.'",
        "pasirinkimai": {
            "Pasakyti: Urvas": "slaptas_tunelis",
            "Pasakyti: Akmuo": "neteisinga"
        }
    },
    "slaptas_tunelis": {
        "tekstas": "Po akmeniu atsiveria tunelis. Veda į išėjimą.",
        "pasirinkimai": {
            "Eiti tuneliu": "laisvė"
        }
    },
    "laukiniai_krumai": {
        "tekstas": "Krumuose kažkas juda. Ar nori patikrinti?",
        "pasirinkimai": {
            "Taip": "keistas_padaras",
            "Ne": "gyvūnu_takelis"
        }
    },
    "keistas_padaras": {
        "tekstas": "Iš krūmų išlenda keistas padaras ir tau duoda gėrimą. Ar gersi?",
        "pasirinkimai": {
            "Išgerti": "migla",
            "Atsisakyti": "gyvūnu_takelis"
        }
    },
    "migla": {
        "tekstas": "Išgėręs matai miglą ir viskas susilieja. Pabundi kitur... tai pradžia?",
        "pasirinkimai": {
            "Žiūrėti aplink": "pradzia"
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
