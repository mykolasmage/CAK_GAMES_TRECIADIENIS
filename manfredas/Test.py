import tkinter as tk
import pygame

istorija = {    
    "pradzia": {
        "tekstas": "tu atsiradai kvailiu name tu radai du koridorius vienas koridorius veda i miegamaji kitas i vonia", 
        "pasirinkimas": {
            "eiti i miegamaji": "miegamasis",
            "eiti i vonia": "vonia"
            

        }

    },
    "miegamasis": {
        "tekstas": "Miegamajame radai viena baisiausiu dalyku! Nepaklota kvailio lova! Ar eisi i miegamaji toliau?",
        "pasirinkimas": {
            "Iseiti is miegamojo": "vonia",
            "Eiti gilyn": "toliau"
        }

    },
    "vonia": {
        "tekstas" :  " Ieidami i vonios koridoriu  pamatete kvaili su kirviu ir kuo greiciau ibegote i vone o vonioje buvo raktas. O prie jo buvo skrynia atidariai ja ir radai rakta nuo isejimo bek prie isejimo greiciau! Bet is didelio streso pas jus atsirado noras kristi i depresija zinoma jus to nedarysite..Juk nedarysite to?",
        "pasirinkimas": {
            "begti prie isejimo": "isejimo",
            "Grizti atgal (kam?)": "pradzia",
            "Ikristi i depresija": "depresija"

        }
    
    },
     
    "toliau": {
        "tekstas" : "eidami gilyn jums pasislepes kvailys nukirto galva. Turite pradeti is naujo (Liudna muzika groja)",
        "pasirinkimas": {
             "pradeti isnaujo": "pradzia"
        }
        
        
    },
    "isejimo": {
        "tekstas": "Atbege prie isejimo pamatete, kad reikia 2 raktu o tu turi 1 pamatei iejima i virtuve o kitoje puseje i lauka",
        "pasirinkimas": {
             "virtuve": "virtuve",
             "lauka": "lauka"
        }
        

    },
    "virtuve": {
        "tekstas": "Radai su pelijusi maista, zmoniu kaulus, kaukoles ir kopecias ka jos cia daro imti jas ar geriau begti patirineti lauka?",
        "pasirinkimas": {
             "pasiimti kopecias": "kopecias",
             "lauka": "lauka"
        }
    },
    "kopecias": {
        "tekstas": "Su kopeciom pasiekiai dezute kuria suradai lauke  ir radai joje rakta! Bet jis nepanasus i isejimo gal jis ir nuo duru? Reikia pabandyti atidaryti duris.",
        "pasirinkimas": {
             "bandyti": "pabandyti"
             
        }
    },
    "pabandyti": {
        "tekstas": "Pabandiai ir..... Pavyko! Duris atsidare ir tu garso greiciu pabegai is ten bet duris palikai atdaras ir tave pamate kvailys...Begant tu pargriuvai kvailys tave sugavo ir nusitempe atgal iskur tu jau neiseisi, nes jis  nusitempes tave atgal paliko  is taves tik kaulus (Bad Ending reikejo neimti kopeciu bandyk dar karta ) ",
        "pasirinkimas": {
            "Bad Ending": "pradzia"
            
        }
    },
    "lauka":{
     "tekstas": "Lauke pamatei kad reikia kopeciu, kad nuimti sena dezute nuo sklepo stogo o tu ju neturi ar eisi atgal, kad jas pasiimti ar panaudosi kazka kita?",
      "pasirinkimas": {
             "eiti atgal": "eisi atgal",
             "ieskosi kazko kito lauke": "kazkas kita"
        }
     },
     "eisi atgal": {
         "tekstas": "Grizai atgal bet kopecios luzusios (Gal kvailiui nepatiko jos?) is kopeciu liko tik puse  kopeciu ar pasiimsi? Ar eisi i lauka ir vel ieskoti kazkokio daikto ",
          "pasirinkimas": {
             "pasiimti": "puse visu kopeciu",
             "eiti i lauka": "kazkas kita"
        }
     },
     "kazkas kita": {
         "tekstas": " Ieskodamas kazko radote skyle sklepe ilindai i ja ir patekai i sklepa kur radai sena surudijusi revolveri su 2 patronais ir rakta turbut nuo isejimo. Gal noretum isbandyti laime ir  pribaigti kvaili?",
         "pasirinkimas": {
             "Bandyti laime": "laime",
             "neimti ginklo ir grizti i virtuve ir pasiimti kopecias": "eisi atgal"
         }
             
             
     },
     "puse visu kopeciu": {
         "tekstas": "Pasiemes kopecias grizai prie dezutes ir pasokes pavyko paimti dezute, bet nusileisdamas kritai del ko kopecios luzo ir tu smarkiai susizalojai koja (dabar negali pabegti). O dezutei radai rakta!  Bet jis nepanasus i isejimo gal jis ir nuo duru reikia bandyti atidaryti duris?",
         "pasirinkimas": {
              "pabandyti": "bandyti"
         }
     },
     "bandyti": {
         "tekstas": "Pabandiai ir..... Pavyko! Duris atsidare ir tu kaip galejai begai is ten bet duris palikai atdaras ir tave pamate kvailys... Begant tu buvai sugautas kvailiu jis  tave  nusitempe atgal iskur tu jau neiseisi, nes jis nusitempes tave atgal paliko is taves tik kaulus (Bad Ending reikejo neimti  puses kopeciu bandyk dar karta )",
        "pasirinkimas": {
            "Bad Ending": "pradzia"
        }
     },
     "laime": {
         "tekstas": "Sklepe uzkrovei revolveri su jo 2 patronais ir ejai ieskoti to mulkio ir... Tu ji radai jis ziurejo per langa ir tu sovei jam i galva ir .... Jo galvoje atsirado skyle ir jis krito bet atbego kitas kvailys ir..",
         "pasirinkimas": {
             "begti": "kvailys",
             "pabandyti laime paskutini karta": "sovei"
         }
     },
     "kvailys": {
         "tekstas": "tave numete tavo revolveris krito ir ikrito i skyle tu bandydamas nustumti kvaili nuo saves radai kaskoki medzio gabala ir trenkei kvailiui per galva jis prarado samone, o tu begai prie duru atrakinai jas ir pabegai. Neutral Ending (Pabandyk sauti.Ir dar supranti kodel Neutral Ending nes tu palikai 2 kvaili gyva!) ",
         "pasirinkimas":{
             "pradeti is naujo": "pradzia"
         }
     },
     "sovei": {
         "tekstas": "tave numete tavo revolveris krito ir ikrito i skyle  tu bandydamas nustumti kvaili nuo saves radai kaskoki medzio gabala ir trenkei kvailiui per galva jis prarado samone, o tu isemei is skyles revolveri ir sovei ir tau pasiseke revolveris issove nors tu matei kaip pasisuko dalis su patronu. Prie kvailio pamatei skaicius 5632 gal jos reikia kaskur irasyti, bet buvo  ne iki tuo tu iskarto pabegai ir grizai namo. Good Ending(Hm.. New game plus Gal ten galima bus irasyti skaicius. Gal lauke atsirado liukas su kodine spyna kas zino.. kas zino..)",
         "pasirinkimas": {
             "New game plus": "new game"
         }
     },
     "new game": {
          "tekstas": "tu atsiradai kvailiu name tu radai du koridorius vienas koridorius veda i miegamaji kitas i vonia. Hm is kaskurtais jus prisimenate sia vieta ir pas jus atsirado noras patekti i lauka gal ten ir nueikite?", 
        "pasirinkimas": {
            "eiti i miegamaji": "miegamasis",
            "eiti i vonia": "vonia",
            "eiti i lauka": "Secret ending"



        }

     },
     "Secret ending": {
         "tekstas": "nubege i lauka radote liuka su kodinia spyna ir bandote suvesti koda kuri jus pusiau zinote bet kokie paskutiniai 2 skaiciai ne. Pabandykite prisiminti",
         "pasirinkimas": {
             "5632": "Secret ending 2",
             "5698": "mirtis",
             "5689": "mirtis2",
             "5678": "mirtis3"
         }
     },
     "mirtis": {
          "tekstas" : "suvede koda ant liuko sirena kurios net nepamatysi pradejo taip garsiai kaukti, kad atejo kvailys su kirviu ir  nukirto jums galva. Turite pradeti is naujo (Liudna muzika groja)",
        "pasirinkimas": {
             "pradeti isnaujo": "new game"
        }
     },
     "Secret ending 2": {
          "tekstas" : "Liukas atsidare! Jus i ji iejote ir viduje pamatete keista siena kurioje matesi kaskoks tai stulpas sviesos jus iejote i ji ir atsiradote kambaryje jus pamatete, kad kambaryje buvo didziulis ekranas ant kurio rode kvailiu nama? Ir buvo matomas ekrano kampe esantis uzrasas (Simuliacija 1). Jus supratote, kad jus istikro visa laika gyvenote simuliacijoje,nes netgi jusu namai matesi ekrane. Jus supratote, kad gyvenote netikrame pasaulyje visa gyvenima.Paliudeje jus pamatete duris su uzrasu (isejimas) iseisite? ",
          "pasirinkimas": {
              "iseiti": "tikrove"

          }
     },
     "tikrove": {
         "tekstas": "Iseje is kambario jus pamatete kaip atrodo sikart jau TIKRAS pasaulis ir supratote, kad nelaikas liudeti ir reikia gyventi toliau nors ir nezinomame pasaulyje. (Secret Ending . Netikras pasaulis, kaip jums turejo buti sunku... Sveikinu jus perejote zaidima ant pacio geriausio endingo! )",
         "pasirinkimas":{
             "Credits": "credits",
             "Hm?": "Hm"
             
             
         }
     },
     "credits":{
         "tekstas": "scenaristas: Manfredas, zaidimo kurejas Manfris, Endingose sakomu hintu sugalvotojas Manfreduska",
         "pasirinkimas":{
             "Pradeti isnaujo  (gal liko  neitirinetu endingu)": "pradzia"
         }
     },
    "mirtis2": {
          "tekstas" : "suvede koda jums su spastais nuo isilauziku nukirto  galva. Turite pradeti is naujo (Liudna muzika groja)",
        "pasirinkimas": {
             "pradeti isnaujo": "new game"
        }
    },
    "mirtis3": {
          "tekstas" : "suvede koda jums su  jums ant galvos nukrito sklepo stogo astrioji dalis ir ismigo jums i galva. Turite pradeti is naujo (Liudna muzika groja)",
        "pasirinkimas": {
             "pradeti isnaujo": "new game"
        }
    },
    "depresija": {
        "tekstas": "Jus ikritote i depresija ir isbuvote vonioje iki tol kol kvailys neislauze duris, bet pamates kas su jumis yra padave jums virve ir muila ir jus nusizudete(Badest Ending. Nu ir kam?! Jus taip nemegstat savo gyvenimo?! Pradekite isnaujo ..(keistas zmogus))",
        "pasirinkimas":{
            "Pradeti isnaujo": "pradzia"
        }
    },
    "Hm": {
        "tekstas" : "Kaskas cia netaip kodel kambarys is kurio isejote atrodo labai naujoviskai kol pasaulyje tik viduramžiai? Reikia patirineti teritorijas.",
        "pasirinkimas":{
            "Tirineti" : "Karas"
        }

    },
    "Karas": {
        "tekstas" : "Kai nuejote biski toliau nuo kambario su kameromis jis isnyko o jusu drabuziai pasikeite ir atrode kaip tikro viduramziu kario sarvai. Prie jusu pribego kaskoks karys ir padave jums kalavija ir nuvede jus iki kovos lauko. Kas vyksta? Gal begti ? Bet turbut reikia eiti i kovos lauka.",
        "pasirinkimas" :{
            "Begti": "mirtis 00",
            "Eiti": "klanai"

        }
    },
    "mirtis 00": {
            "tekstas" : "Jus begote ir parkritote jus sugavo karys ir nukirto jums galva, nes karys nebega nuo karo, o kovoja jame.",
            "pasirinkimas": {
                "Hm mirei ka padarysi": "Hm"
        }
    },
    "klanai":{
        "tekstas": "Kai atejote i karo lauka jums karys pasake, kad cia nauji kariai renkasi savo klana.Yra du klanai Bobu ir Grotu. Bobu klanas ypatingas savo papuliarumu tarp geriausiu kariu ir kovoja pries vergija. Grotu net neprijama naujoku tai apie ji informacijos nepasake karys nieko. O kam klause koki klana isiringti? Bet neuzmirskite kad jusu tikslas istrukti is cia, o ne tapti kariu.",
        "pasirinkimas":{
            "Bobu klanas": "bobu",
            "Nieko nesirinkti": "mirtis 01"
        }
        
    },
    "mirtis 01":{
        "tekstas": " Kai nesirinkote klano karys ismeige i jus kalavija ir pasake, kad pasirinkimas yra butinas  arba lauks mirtis.",
         "pasirinkimas": {
                "Hm mirei ka padarysi": "Hm"
         }

    },
    "bobu": {
        "tekstas": "isirinke bobu klana jus nuvede prie bobu klano kariu ir karys isejo jus pamatete, kad kitoje puseje irgi rinkosi kariai ir supratote, kad tai Grotu klano kariai ir , kad is sios vietos iseiti galesite kai nugalesite Grotu klana arba kai rasite kita iseiti.",
        "pasirinkimas": {
            "Karaujam!": "Pabaiga (sad)",
            "Kas ten?!": "Secret secret Ending"
        }
    },
    "Pabaiga (sad)":{
        "tekstas": "Prasidejo kova jus puikiai mokejote kautis su kalaviju( nes moketes kautis su ginklais kai nepatekote i kvailiu namus). Kare jus matete kaip mirsta klanu zmones... Jus kovetes gerai kol nesusidurete su  Grotu klano vadu jis iskarto jus nuzude su savo kalaviju.(Sad Ending gal galima buvo isgyventi jei rastumete kita iseiti?)",
        "pasirinkimas": {
            "Hm mirei ka padarysi": "Hm"
        }
    },
    "Secret secret Ending": {
        "tekstas": "Jus pamatete kas koki tai plysi dideliam akmenyje... Jus supratote, kad tai toks pat plysis, kaip ir kvailiu name! Jus iskarto begote prie akmens ir...",
        "pasirinkimas":{
            "Nu ir?!": "tikrove tikra"
        }
    },
    "tikrove tikra":{
        "tekstas": "Ilinde i plysi jus patekote i  kambari paemete kas koki tai bloknota ir... Iseje pamatete tikra pasuli! Jus supratote, kad tai tikras pasaulys kai paskaitete bloknota rasta kambaryje(Ultra Giga Super Mega Good Ending Sveikinu jus radote PATI GERIAUSIA ENDINGA!!!!)",
        "pasirinkimas": {
            "Credits": "credits",
            "Laiskas nuo autoriaus": "laiskas"
        }
    },
    "laiskas":{
        "tekstas": "Aciu labai, kad zaidete! Meldziuos jums patiko. Netgi idomu kiek laiko isleidote, kad atrakinti si endinga?O taip aciu, kad zaidete!!",
        "pasirinkimas":{
            "isnaujo": "pradzia"
        }
    }
        
    

     






}
dabartine_scena = "pradzia"
tekstas_p = None
mygtuku_remas = None

def paleisti():
    global tekstas_p, mygtuku_remas

    window = tk.Tk()
    window.title("Kvailio namai")
    tekstas_p = tk.Label(window, wraplength=400)
    tekstas_p.pack(pady=20)
    mygtuku_remas = tk.Frame(window)
    mygtuku_remas.pack()
    rodyti_scena()
    pygame.mixer.init()
    window.mainloop()
   
def rodyti_scena():
    global dabartine_scena, mygtuku_remas, tekstas_p
    for widget in mygtuku_remas.winfo_children():
        widget.destroy()

    scena = istorija[dabartine_scena]
    tekstas_p.config(text=scena["tekstas"])
    
       
    karo_scenos = [
        "Hm", "Karas", "klanai", "bobu", "Pabaiga (sad)", "Secret secret Ending"
    ]
    if dabartine_scena in karo_scenos:
        groti_muzika("Midnight Trace - Jimena Contreras.mp3")
    elif dabartine_scena == "tikrove":
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        groti_muzika("Everyday - Jason Farnham.mp3")
    
    else:
        if pygame.mixer.get_init():
           pygame.mixer.music.fadeout(2000)
    
    

    for pasirinkimo_tekstas, kita_scena in scena["pasirinkimas"].items():
        mygtukas = tk.Button(mygtuku_remas, text=pasirinkimo_tekstas, width=30, command=lambda ns=kita_scena: keisti_scena(ns))
        mygtukas.pack(pady=5)
def groti_muzika(kelias):
    pygame.mixer.music.load(kelias)
    pygame.mixer.music.play(-1)


def keisti_scena(nauja_scena):
    global dabartine_scena
    dabartine_scena = nauja_scena
    rodyti_scena()
    
   
if __name__ == "__main__":
    paleisti()