import tkinter as tk
import random

amulets = 0
inventory = []
visited = set()
scene_index = 0

# Scenos su pasirinkimais ir rezultatais (20 scenų)
scenes = [
    {
        "title": "Miško pradžia",
        "text": "Stovi priešais paslaptingą mišką.",
        "choices": [
            ("Eiti į tankmę", "danger"),
            ("Apeiti per takelį", "find_amulet")
        ]
    },
    {
        "title": "Senas šulinys",
        "text": "Iš šulinio sklinda keisti garsai.",
        "choices": [
            ("Įmesti monetą", "find_item"),
            ("Ignoruoti ir eiti toliau", "next")
        ]
    },
    {
        "title": "Urvas",
        "text": "Tamsus urvas – viduje kažkas juda.",
        "choices": [
            ("Įeiti", "puzzle"),
            ("Pabėgti", "nothing")
        ]
    },
    {
        "title": "Tiltas per tarpeklį",
        "text": "Tilto lenta atrodo silpna.",
        "choices": [
            ("Pereiti tiltą", "danger"),
            ("Ieškoti kito kelio", "next")
        ]
    },
    {
        "title": "Švytinti pieva",
        "text": "Ant žolės spindi kažkas magiško.",
        "choices": [
            ("Paimti", "find_amulet"),
            ("Užkasti, kad niekas nerastų", "nothing")
        ]
    },
    {
        "title": "Apleista trobelė",
        "text": "Viduje guli senas dėklas.",
        "choices": [
            ("Atidaryti", "trap_or_reward"),
            ("Palikti", "next")
        ]
    },
    {
        "title": "Sargybinio skulptūra",
        "text": "Akis žiūri į tave. Gal tai mįslė?",
        "choices": [
            ("Pabandyti atspėti", "puzzle"),
            ("Pereiti tyliai", "danger")
        ]
    },
    {
        "title": "Kalno viršūnė",
        "text": "Vėjas stiprus, bet matai kažką žybsint.",
        "choices": [
            ("Patikrinti švytėjimą", "find_amulet"),
            ("Atsisėsti pailsėti", "nothing")
        ]
    },
    {
        "title": "Senovinė šventykla",
        "text": "Durys su simboliais.",
        "choices": [
            ("Bandyt atverti", "puzzle"),
            ("Išgraviruoti savo ženklą", "find_item")
        ]
    },
    {
        "title": "Paslaptinga ola",
        "text": "Užsikimšusi rieduliais.",
        "choices": [
            ("Prasiskverbti vidun", "danger"),
            ("Pažymėti žemėlapyje", "next")
        ]
    },
    {
        "title": "Dykuma",
        "text": "Karšta ir tolumoje matai objektą.",
        "choices": [
            ("Artėti prie objekto", "find_amulet"),
            ("Iškasti smėlį", "find_item")
        ]
    },
    {
        "title": "Kova su šešėliu",
        "text": "Tave užpuola šešėlinė figūra!",
        "choices": [
            ("Kovoti", "danger"),
            ("Pabėgti", "next")
        ]
    },
    {
        "title": "Akmenų labirintas",
        "text": "Reikia pasirinkti kryptį.",
        "choices": [
            ("Kairėn", "trap_or_reward"),
            ("Dešinėn", "find_amulet")
        ]
    },
    {
        "title": "Maginis medis",
        "text": "Medyje įstrigęs objektas.",
        "choices": [
            ("Lipti į medį", "find_item"),
            ("Palikti ramybėje", "nothing")
        ]
    },
    {
        "title": "Galutiniai vartai",
        "text": "Didžiuliai vartai laukia.",
        "choices": [
            ("Pabandyti atidaryti", "check_ending"),
            ("Dar ieškoti", "next")
        ]
    },
    {
        "title": "Užšalęs ežeras",
        "text": "Po ledu švyti kažkas paslaptingo.",
        "choices": [
            ("Bandyt pralaužti ledą", "trap_or_reward"),
            ("Eiti aplink", "next")
        ]
    },
    {
        "title": "Raganos trobelė",
        "text": "Ragana tau siūlo mainus: daiktą už amuletą.",
        "choices": [
            ("Mainyti daiktą", "trade"),
            ("Mandagiai atsisakyti", "nothing")
        ]
    },
    {
        "title": "Ugnies žiedas",
        "text": "Viduryje ugnies rato – amuletas.",
        "choices": [
            ("Šokti į ratą", "trap_or_reward"),
            ("Ieškoti būdo jį pasiekti", "next")
        ]
    },
    {
        "title": "Paslaptingas riteris",
        "text": "Riteris klausia mįslės, leisdamas laimėti amuletą.",
        "choices": [
            ("Atsakyti į mįslę", "puzzle"),
            ("Išvengti kontakto", "next")
        ]
    },
    {
        "title": "Pamirštas altorius",
        "text": "Ant altoriaus guli keistas simbolis.",
        "choices": [
            ("Paliesti simbolį", "find_item"),
            ("Atsitraukti tyliai", "nothing")
        ]
    }
]

def show_scene(index=None):
    global scene_index
    scene_index = index if index is not None else random.randint(0, len(scenes)-1)
    scene = scenes[scene_index]

    text_box.config(text=f"{scene['title']}\n\n{scene['text']}")
    for widget in button_frame.winfo_children():
        widget.destroy()

    for label, result in scene["choices"]:
        tk.Button(button_frame, text=label, command=lambda r=result: handle_choice(r)).pack(fill="x")

def handle_choice(result):
    global amulets

    for widget in button_frame.winfo_children():
        widget.destroy()

    if result == "find_amulet":
        amulets += 1
        show_message(f"Radai amuletą! ({amulets}/15)", next_scene)
    elif result == "find_item":
        item = random.choice(["raktas", "žemėlapis", "akmuo"])
        if item not in inventory:
            inventory.append(item)
            show_message(f"Radai daiktą: {item}", next_scene)
        else:
            show_message("Čia jau nieko nėra.", next_scene)
    elif result == "danger":
        if random.random() < 0.5:
            show_message("Patekai į spąstus ir praradai galimybę. Žaidimas baigtas.", end_game)
        else:
            show_message("Išsisukai laiku!", next_scene)
    elif result == "puzzle":
        create_puzzle()
    elif result == "trap_or_reward":
        if random.random() < 0.5:
            amulets += 1
            show_message(f"Laimė! Radai amuletą! ({amulets}/15)", next_scene)
        else:
            show_message("Spąstai! Praradai šansą.", next_scene)
    elif result == "check_ending":
        if amulets >= 15:
            show_message("Tu surinkai 15 amuletų! Vartai atsiveria. Tu laimėjai!", end_game)
        else:
            show_message(f"Turi tik {amulets}/15 amuletų. Dar ieškok.", next_scene)
    elif result == "trade":
        if inventory:
            amulets += 1
            lost_item = inventory.pop()
            show_message(f"Mainai pavyko! Atidavei '{lost_item}' ir gavai amuletą! ({amulets}/15)", next_scene)
        else:
            show_message("Neturi daiktų mainams.", next_scene)
    elif result == "nothing":
        show_message("Nieko neįvyko.", next_scene)
    elif result == "next":
        next_scene()

def next_scene():
    next_index = random.randint(0, len(scenes)-1)
    show_scene(next_index)

def create_puzzle():
    a, b = random.randint(2, 6), random.randint(2, 6)
    answer = a * b

    def check():
        try:
            if int(entry.get()) == answer:
                show_message("Teisingai! Gavai amuletą!", lambda: handle_choice("find_amulet"))
            else:
                show_message("Klaida! Praradai galimybę.", next_scene)
        except:
            show_message("Blogas įvestas skaičius.", next_scene)

    text_box.config(text=f"Galvosūkis: kiek bus {a} × {b}?")
    for widget in button_frame.winfo_children():
        widget.destroy()

    entry = tk.Entry(button_frame)
    entry.pack()
    tk.Button(button_frame, text="Pateikti", command=check).pack()

def show_message(message, action):
    text_box.config(text=message)
    for widget in button_frame.winfo_children():
        widget.destroy()
    tk.Button(button_frame, text="Tęsti", command=action).pack()

def end_game():
    for widget in button_frame.winfo_children():
        widget.destroy()
    tk.Button(button_frame, text="Uždaryti", command=root.destroy).pack()


root = tk.Tk()
root.title("Gyvybingas Amuletų Nuotykis")
text_box = tk.Label(root, text="", wraplength=500, font=("Arial", 12), pady=20, justify="left")
text_box.pack()
button_frame = tk.Frame(root)
button_frame.pack()
show_scene(0)
root.mainloop()
root = tk.Tk()
root.title("Gyvybingas Amuletų Nuotykis")
text_box = tk.Label(root, text="", wraplength=500, font=("Arial", 12), pady=20, justify="left")
text_box.pack()
button_frame = tk.Frame(root)
button_frame.pack()
show_scene(0)
root.mainloop()
