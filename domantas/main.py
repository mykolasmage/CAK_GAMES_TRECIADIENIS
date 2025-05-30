import sys
import tkinter as tk

# https://www.celtx.com/a/ux/project?id=398d3689dca39a2536173e0be2939f6e29fb6a06#document=film-tv-script

# Exit function
def close_window():
    sys.exit()

# Story dictionary
# Number of scenes: 84
story = {
    "beginnings": {
        'text': 'PRO TIP: playing this game, I suggest you going into full screen mode. \nIn the midst of the wild and unknown world, you find yourself awake and fully self-conscious in a dark forest of Death. It is night time. You are desperate for food and water. Every breath drags your lungs down. You one and only choice. Go north and die.',
        'choices': {
            'Go north ': 'dead-house'
        }
    },
    "dead-house": {
        'text': 'You begin walking. Your whole body hurts. It is as you are going to be torn apart. After a while, you discover a dead house. It is dark. You do not see anyone. The house is covered in green moss that glows with weak light. Your heartbeat quickens, breath intensifies, and palms get sweaty. You can go in and risk everything, or you can move on and let your body degrade.',
        'choices': {
            'Go in': 'dead-house-2',
            'Go on': 'degrading'
        }
    },
    'dead-house-2': {
        'text': "You enter a ghost-quiet dark room. It smells rotten tomatoes. There are no windows. Your eyes adjust to the dark and you see everything is wood. The floor, the ceiling and the walls. In center a man sits on a chair. He turns his head. His mask is horrible. You can only perceive his dark pupils and a scar on a torn cheek. He stands up, having a bright knife in his arm. Fear grips your chest and lungs become heavier.'",
        'choices': {
            'Try to speak with the man': 'conversation-1',
            'Run away': 'run-away-forest'
        }
    },
    'conversation-1': {
        'text': "'Who... who are you?' You shouted. Your legs begin to tremble out of fear. 'Who are you?' you repeated. 'I owe you nothing. I don't have to answer. Leave if you care about your life.' The man responded in a deep and calm voice.",
        'choices': {
            'Stand your ground': 'conversation-2', 
            "Run away": "run-away-forest"
        }
    },
    'conversation-2': {
        'text': "'No. I won't leave,' you say. He chuckles, unleashing a dry and eerie sound, 'Then you are dead.'\nIn a second, he throws his knife at you--too fast for you to react. As you dodge it grazes through your forehead. Your head is burning. You grip on it, desperately trying to control the hot blood rushing through your fingers. You curl like a rock out of self defense. Your eyes get filled with blood. Your soul is planning to leave.\n\n'I'm sorry, darling,' the man mumbles as he walks towards you. 'Your fate was inevitable.' He sits down in front of you and tilts his head closely, examining your face. 'I’m Zephiel Korr.'",
        'choices': {
            'Give up': "hospital", 
            "Don't give up": 'fight scene'
        }
    },
    'fight scene': {
        'text': "You slowly raise your head. You try to get up, tripping and falling again and again on the way. Zephiel raises his eyebrows, 'Do you want to fight?' he asked and stabbed you in the chest. 'This is it,' you thought as you saw more blood rushing down your chest. 'Why did I choose not to give up?', you tripped and fell. 'This fight was not a fight; it was a child's play,' Zephiel said with a bit of disappointment in his tone, 'alas, one down.''", 
        'choices': {
            'Restart from before': "conversation-2",
            'Quit': "die"
        }
    },
    'hospital': {
        'text': "You slowly wake up and cover your eyes. You adjust to bright light and see a big and white, sterile room. Dozen of people are zooming around in green-yellow suits with a radiation symbol on them. You try to get up, but your head hits something. You lift your head and see glass. Then, you try to extend your arms, but they hit the same glass. You're in a cage. One of the people turns around, checking a gray tablet. When he looked at you his mouth dropped. Others turned around; their eyes widened as well.", 
        'choices': {
            'Break out of the cage': 'hospital cage-break', 
            'Watch what happens': 'doctor operation'
        }
    },
    'hospital cage-break': {
        'text': "You punched the cage you're in. Again. And again. Then give up after trying for so long, until the glass suddenly shattered into a million pieces. Glass bruised your arms and face. Scream errupts around you. Red lights turn on. The men in green-yellow suits rush through the door and less than few seconds everybody is gone. You are panting, adrenaline is rushing despite the million bruises on your body.", 
        'choices': {
            'Leave the hospital': 'NYC-streets', 
            'Have some business with the police': "police-hospital"
        }
    },
    'police-hospital': {
        'text': "The police came in, banging on the door. You see the S.W.A.T. emblem on their dark armor. You are smaller than them, but try to fight nevertheless. After few minutes of heated fighting they arest you. ",
        'choices': {
            'Break out': 'prison-break', 
            'Do nothing': 'imprisonment'
        }
    },
    'prison-break': {
        'text': 'As you enter the police station, you examine it. There are about 25 employees marching accross the ground floor. You see 4 escalators; every single time one opens, on average three people get out and in. Thus, there must be at least three people in each of the stories, and assuming they are all trained, there is no opportunity for you to break out loudly. \n S.W.A.T. takes you to the escalator. On it, you see about 16 buttons, each for every story. The escalator is about five feet wide and six feet long. The group leader presses the third button.', 
        'choices': {
            'Wait': 'prison-break-2'
        }
    },
    'prison-break-2': {
        'text': "As the escalator door opens, you immediately notice a few things. You enter what seems like an office with yellow walls and 30 people. The desks are put together in front of one another in two rows that each have 8 desks facing each other, 16 for one row. On the right side, there is a cell where you are being taken now; it is about five metres wide. As you walk, a man passes by, and you somehow mange to quickly snitch his ID card without anyone noticing. S.W.A.T. team member opens the cell door and lets you in.", 
        'choices': {
            'Breakout time!': 'prison-break-3'
        }
    },
    'prison-break-3': {
        'text': "You see a vent above three metres. You wait for the S.W.A.T. to leave. Because the wall is uneven, you manage to climb up and reach the vent as if it was made specifically for you. You hear a scream. You look down and see all 60 eyes looking at you. You realize you have to be quick with this one.", 
        'choices': {
            'Give up': 'imprisonment', 
            'Continue': 'prison-break-4'
        }
    },
    'prison-break-4': {
        'text': "Your palms get sweaty and you breath, heartbeat intensify. You you crawl as fast as possible through the vent to reach its end and then turn right. You see another vent below you, with another office room. Unlike with the previous one, this one is quiet and focused. You crawl forward until you reach another vent. This time it's an empty bathroom.. ", 
        'choices': {
            'Move on': 'prison-break-4.5', 
            'Jump in': 'prison-break-5'
        }
    },
    'prison-break-5': {
        'text': "You jump in and rush to the door, but… A woman enters in. 'Who the fuck are you?!' She screamed. 'Um, I'm sorry; must've, uh, read the sign wrong, miss…' With these words, you dashed through her and the door and run to the escalator. You finally can breathe freely again. You're free. You go to the first floor and out. ", 
        'choices': {
            'Move on': "NYC-streets"
        }
    },
    'NYC-streets': {
        'text': "You leave the building and enter sunny streets of New York. You look to the left, you look to the right, and a distinguished man in suit is driving a black limousine to you.", 
        'choices': {
            'Speak with the driver': "limousine-1", 
            'Run away': "run away-limousine"
        }
    },
    'limousine-1': {
        'text': "The limousine stopped besides you. Dark windows rolled, and you started into the soul of the driver. He stared at yours. Few minutes pass. The driver finally spoke: \n'Get into the limousine, sir. You've been invited to join the CIA conference today.'", 
        'choices': {
            'Get into the limosine': "limousine-2", 
            'Try to run away': "run away-limousine"
        }
    },
    "limousine-2": {
        'text': "You open the passenger limousine door. Oh, the luxury! Your eyes bursted. There's a leather couch opposite to you that can easily fit six people! There's a small bar next to the door, with two small seats made out of pure expensive leather. You look around, bursting with excitement. You want to try the bar, sleep on the couch, do anything and everything! You eagerly look at the driver. He's waiting for you.", 
        'choices': {
            'When will we reach the HQ?': "limousine-3"
        }
    },
    "limousine-3": {
        'text': "''When will we reach the headquarters?' you ask. The driver turns around and stares you in the eye with his handsome face. 'After eight hours. It should be six, but that route is more dangerous.' Your excitement disappears in an instant. 'Eight hours?? The conference is happening at midnight?!' the driver chuckles 'Yes.' With these words, he turns around, now facing the wheel. 'Are we ready?' You stare at his back with utter disgust. 'Is this why you brought a limo?' The driver doesn't reply. 'Well, thank you,' you grumble. 'So, are we ready?' the driver asked again politely.", 
        'choices': {
            'Yes, we are': "cia-headquarters-1", 
            "No, we're not": "not-ready-limo"
        }
    },
    'cia-headquarters-1' : {
        "text": "The limousine drives off. \n You arrived at the headquarters. It's nighttime. You see an entrance. If two tall men were stacked on top of another, that's how wide it would be. It's made out of dark opaque glass; nothing can be seen through. You and the driver get out of the limousine and march towards it. You feel like some pressure is put against your head, and your soul is starting to leave your body. At any moment you can pass out. The entrance door opens automatically and reveal a big, empty white foyer. It's wide; you can fit two trucks horizontally here. In the middle there is an emblem with an eagle on it and dark couches put around it. It smells plastic here. You see three pairs of pillars put symmetrically; on each there is an American flag. In the middle of them there is a receptionist behind a luxurious marble table. She raises her eyes up with a warm and welcoming smile.", 
        'choices': {
            "Speak with the secretary": "cia-headquarters-2"
        }
    },
    "cia-headquarters-2": {
        'text': "'Good evening, gentlemen.' The she spoke. 'Is he…' 'Yes, it's him; that's the man we're looking for.' The driver iterrupted. 'We're short of time, Miranda. Have to deliver him to the boss.' Miranda nodded. 'Go on.' The driver then grabbed your wrist with great strength. Are all limousine drivers this strong? He took you to the staircase on the right. They were made out of marble. You and the driver climbed about three floors and entered a seemingly dark hall. The empty meeting rooms are separated from it by crystal clear glasses. You quickly march on a dark carpet, but nothing can be heard. You hear crowd noise at the back. The driver took you to the end of the hall. Now you're facing a door. The driver knocks. ", 
        "choices": {
            "Walk in": "cia-headquarters-3", 
        }
    },
    'cia-headquarters-3': {
        'text': "You enter a large and bright room, with two dark leather armchairs and a couch placed symmetrically, with a brown rug underneath. To the left, there is a desk with a chair, a monitor, a keyboard, and an apple mouse. There is a good-looking man sitting there, dressed in a sharp black suit. As you walk in, he is already staring at the door. He faked a smile. 'Good evening, young lads.' He says and slowly his eyes at you, 'And you, welcome to the CIA; your first time being here, right?' He chuckles, unleashing a dry, eerie sound. 'Sit down, both of you.'",
        "choices": {
            'Interrogate': 'cia-headquarters-4', 
            'Be polite': "cia-headquarters-4"
        }
    },
    'cia-headquarters-4': {
        'text': "", 
        'choices': {}
    },
    "cia-headquarters-5": {
        'text': "", 
        'choices': {
            "Why am I here?": 'cia-headquarters-6'
        }
    },
    #Now this scene is going to be split up into a few sections for interactiveness
    'cia-headquarters-6': {
        'text': "", 
        'choices': {
            'What?..': 'cia-headquarters-6.1', 
        }
    },  
    "cia-headquarters-6.5": {
        'text': "", 
        "choices": {
            "Let him continue": "cia-headquarters-6.2", 
            "Leave, stay close minded": "cia-headquarters-6.1.5"
        }
    },
    "cia-headquarters-6.1": {
        'text': "", 
        "choices": {
            "Let him continue": "cia-headquarters-6.2", 
        }
    },
    "cia-headquarters-6.1.5": {
        'text': "", 
        'choices': ""
    },
    "cia-headquarters-6.2": {
        'text': "", 
        'choices': {
            "Agree": 'cia-headquarters-6.3', 
        }
    },
    'cia-headquarters-6.3': {
        'text': "", 
        'choices': {
            "What?..": "cia-headquarters-6.3.5", 
            "Let Zephiel do his thing": "cia-headquarters-7"
        }
    },
    "cia-headquarters-6.3.5": {
        'text': "", 
        'choices': {
            "Why am I special?": "why-am-i-special", 
            "Why was I at the hospital?": "why-was-i-at-the-hospital", 
            "Why did the police try to arrest me?": "why-did-the-police-try-to-arrest-me" ,
            "Continue": "cia-headquarter-leaving"
        }
    }, 
    'cia-headquarters-7': {
        'text': "Zephiel turns his head at you as if waiting for an answer. You stay silent. Zephiel picks a long teacher stick. And points to T. 'This constant represents time,' he says. He moves his stick. 'And 'I' represents the direction where time is going. Now, in an ideal world, constant I would be an increasing function, with equality on each side. This would mean that time is linear. The problem is that this constant is completely random. It cannot be predicted. Both sides are unequal. This causes time to fluctuate. Back and forth, you can appear in different timezones at any time. We don't know why that's happening. But I want you,' he fixes his eyes on your forehead, 'to find the answer to the 'Why?", 
        'choices': {
            "Why am I special?": "why-am-i-special", 
            "Why was I at the hospital?": "why-was-i-at-the-hospital", 
            "Why did the police try to arrest me?": "why-did-the-police-try-to-arrest-me" ,
            "Continue": "cia-headquarter-leaving"
        }
    },
    'cia-headquarters-8': {
        'text': "", 
        'choices': ""
    },
    "cia-headquarter-leaving": { 
        'text': "'It's time to go.' Zephiel says. He turns his head at the driver 'Adam, lead him to the foyer and book a fancy hotel.' The driver nods and gets, on the way gestures you to follow him. As you walk out of the room, everything blacks out.", 
        'choices': {
            "Quit": "", 
            "Continue": "forest-again-1"
        }
    },
    'forest-again-1': {
        'text': "You find yourself lying down. You open your eyes. Trees are rocking back and forth because of the wind. You are in a forest clearing. You get up and try to perceive your surroundings. It's daytime. It's dead silent. 'Wait...' you felt like someone gripped onto your heart. 'I recognize this place; I've been here be-' something jumps out of the bushes behind you. You turn around at a supersonic speed. The stalker has already gripped onto your legs and overturned you. You're on the ground. A man attacked you. He has a knife. You recognize Zephiel Korr. He victoriously raises his knife... You dodge, and he stabs grass. You quickly get up, kicked the knife and gripped onto his neck. You both roll on the grass. You together wrestle. You spot a big, sharp rock inches away. You grab it. You put it near his neck. He stops wrestling. You look at each other panting. 'Fuck. You won,' he finally said. ", 
        'choices': {
            'Kill Zephiel': "forest-again-bad-ending2", 
            'Talk to him': "forest-again-2"
        }
    },
    'forest-again-2': {
        'text': "'I will keep you alive if and only if you agree to talk to me,' you exclaimed. 'Sure, no problem. Just let go of me.' Zephiel squeezed out. It was hard for him to breathe. You let go, but you grip onto the rock stronger. You both stand up. He looks at you. 'What do you want?' he asked. You turn to him. 'Where's that house in green moss? Let's go there first.' He points panting to the west and leads the way. Good boy. He won't run. You have a weapon that could kill him.",
        'choices': {
            'Walk on': "forest-again-3", 
            "Murder him": "forest-again-bad-ending"
        }
    },
    # This is a very important dialogue. I want to keep the user engaged, therefore I am breaking it up into a few parts.
    "forest-again-3": {
        "text": "You enter a house covered in green moss. The hinges squeak loudly, it smells like rotten tomatoes in here. It's bright in here, there are two windows. Everything is made out of wood. There are two chairs in the middle of the house with no one on them. Zephiel turns around, fakes a smile 'Take a seat.' You two sit down on these hard chairs", 
        "choices": {
            'The heck?': "forest-again-3.1", 
            "Kill Korr": "forest-again-bad-ending2"
        }
    },
    "forest-again-3.1": {
        "text": "You sit down. You raise your eyes. 'Explain yourself.' you choked out. 'You are wondering why I wanted to kill you.' Zephiel finally started after a minute of silence. 'I keep this world clean. I make sure that nobody gets out of this forest. Do you know that time in our world is not linear?' Zephiel laughed 'And that shall be. One death after another in this forest and time never keeps a predictable trajectory. What if nobody dies here?' he awkwardly smiled 'If so... the world will die. Why? Because linear time leads to linear improvement. Improvement leads to more comfort. Comfort leads to desire of more comfort. Then we go too far. But it's too late! The world destroyed because of bad decisions for comfort. The universe set me to be a psycho. That's why I kill with a smile. If I don't, the human species are going kill one another. Better to have one dead than everybody deceased. I don't know how I know this. I just know. It's built into me.'", 
        "choices": {
            "Okay?.. What do I do?": "forest-again-4",
            "What proof do you have?": "forest-again-3.1.5"
        }
    },
    'forest-again-3.1.5': {
        "text": "You look at him sceptically. 'What proof do you have? Prove your words.' Zephiel leans back crossed his legs and looked behind you. 'There is no proof. ' he finally said 'It just is.'", 
        "choices": {
           "Okay?.. What do I do?": "forest-again-4", 
        }
    },
    "forest-again-4": {
        'text': "You stare at the wall. You feel empty. At this point you know you are already dead. Even if his words aren't true, he believes them. You sense the soft sunlight touch your skin like saying goodbye. You know you this fate fooled you. It's just a matter of time when Zephiel will kill you. Suddenly Zephiel leaned in front. 'I've killed a lot of people before.' He said 'I tried to kill you and failed. I don't trust myself anymore.' You looked at him. 'We could become amazing together.' He chuckles. 'I won't kill you. You would escape anyway. Life is a meaningless illusion. Agree and find meaning. Agree and run away from the lies they've sold you.'", 
        "choices": {
            "Agree": "forest-again-5", 
            "Kill Zephiel": "forest-again-bad-ending3"
        }
    },
    'forest-again-5': {
        'text': "You quickly nod. Your heart is racing. You've been granted the opportunity to escape fate. You don't care at this point if many will die. All that matters is that you stay alive. 'I agree,' you say. 'We can do this.' Zephiel stands up and puts his hand up in front. You stand up and shake his hand. \n Living with Zephiel you have became an immortal. It has been more than three million years. The world is going, the world is flourishing. And you both keep this forest clean.\n This is the end. This is it. I hope you had fun with my story -- Domantas. ", 
        'choices': {
            "QUIT": lambda: sys.exit()
        }
    },
    #Endings, additional scenes.

    # Zephiel answers player's main questions. 
    "why-am-i-special": {
        'text': "'Why am I so special?' You ask. Zephiel smiles. 'You can remember what happened in the previous timezones. I can't. No one can apart you. Past and future doesn't exist for the most. But it does for you.''", 
        'choices': {
            "Why was I at the hospital?": "why-was-i-at-the-hospital", 
            "Why did the police try to arrest me?": "why-did-the-police-try-to-arrest-me" ,
            "Continue": "cia-headquarter-leaving"
        }
    },
    'why-was-i-at-the-hospital': {
        'text': 'You look down cautiously. Zephiel reads your mind: "You were at the hospital, because neuroscientists were conducting a neuroscientific experiment on your brain." He says. ', 
        'choices': {
            "Why am I special?": "why-am-i-special",
            "Why did the police try to arrest me?": "why-did-the-police-try-to-arrest-me" ,
            "Continue": "cia-headquarter-leaving"
        }
    },
    "why-did-the-police-try-to-arrest-me": {
        'text': "'But... why did the police try to arrest me?' you enquire. Zephiel blinks three times. 'Such a stupid question. You broke ten thousand dollar worth hospital equipment. You had no allowance to do this. At that point you were at the hospital's ownership.'", 
        'choices': {
            "Why am I special?": "why-am-i-special", 
            "Why was I at the hospital?": "why-was-i-at-the-hospital", 
            "Continue": "cia-headquarter-leaving" 
        }
    },
    'imprisonment': {
        'text': 'You shoud not have chosen this option. You are now imprisoned for 25 years for the damage you have done.',
        'choices': {
            'Try again': 'police-hospital'
        }
    },
    'doctor operation': {
        'text': "The doctors gather around and stare excitedly like you're a zoo animal. Their lips are moving, but you can't hear anything. One of them nods, turns to the other and says something, and then turns around. After a few moments, everything blacks out. \n You died. It seems the doctors have decided to make you a mummy and exhibit in an archeological museum.", 
        'choices': {
            'Restart': "hospital", 
            'QUIT': lambda: sys.exit()
        }
    },
    "die": {
        'text': 'Dear player, I am afraid that your story is over.. Do you want to try again?',
        'choices': {
            'YES!': 'beginnings',
        }
    },
    'run away-limousine': {
        'text': "You try to run away from the limousine. You keep looking back, but never stop running. But the driver exits the car, pulls out the newest G-LOCK and shoots you right in the back. You fall down. Because of the adrenaline, you don't feel any pain, but it's starting to get quieter around you. You're losing too much blood. There is chaos all over your body and the streets; everyone is running and shouting. But perhaps now there is some peace, at last…", 
        'choices': {
            'Try again': 'NYC-streets'
        }
    },
    'forest-again-bad-ending': {
        'text': "You mercilessly cut through his neck. Blood, red as a Rosa flower, started flowing. Zephiel wanted to scream, but all he could do was wheeze. He looked you in the eye moments before his death. 'I'll get.. my..' he wheezed and died. His eyes were like metal balls. Empty. Made of plastic. \nYou wandered endlessly around the world. Never found an escape. Not a destiny, even. You're stuck. After thirty years you committed suicide.", 
        'choices': {
            'QUIT': lambda: sys.exit(), 
            "Restart": "beginnings"
        }
    },
    'forest-again-bad-ending2': {
        'text': "You jumped in front an mercilessly cut through his neck. Blood, red as a Rosa flower, started flowing. Zephiel wanted to scream, but all he could do was wheeze. He looked you in the eye moments before his death. 'I'll get.. my..' he wheezed out and died. His eyes were like metal balls. Empty. Made of plastic. \nYou wandered endlessly around the world. Never found an escape. Not a destiny, even. You're stuck. After thirty years you committed suicide. ",
        "choices": {
            'QUIT': lambda: sys.exit(), 
            "Restart": "beginnings"
        }
    },
    'forest-again-bad-ending3': {
        'text': "You got up. Zephiel got up, too. You put your hand in front. You look at him in the eye. 'I agree. Let's do this.' Zephiel shook your hand with great strength and looked at you with assurance. Then he twisted your hand. You screamed. He kicked you right in the balls, gripped onto hair and smacked your face against the wall so hard, that you saw stars. Your head is spinning. You stumble, but you get up. He kicked you in the balls again. Now you're completely prostrate. Zephiel snatches the rock and throws it at the back of your head. You saw stars. 'I read you.' Korr says. 'I knew you would try to murder me. It's unfortunate, we would have been such amazing killers together...' He picked up the rock and killed you. \n Dear player. I congradulate you on finishing my game. This is it. I hope you had your fun.", 
        'choices': {
            'QUIT': lambda: sys.exit()
        }
    },
    "not-ready-limo": {
        "text": "'It's okay, sir. Just tell me whenever we are.'", 
        'choices': {
            "We're ready": "cia-headquarters-1"
        }
    },
    "question-scene": {
        'text': "", 
        "choices": {}
    },
    'prison-break-4.5': {
        'text': "You crawl further, only to realize you've reached the end. You go back and jump through the vent to the bathrooms.", 
        'choices': {
            'Next': 'prison-break-5'
        }
    }, 
    'degrading': {
        'text': "You walk past the house. You walk for hours. But suddenly, you can't breathe. You started gasping for air, but couldn't get any. Evertyhing blacks. Alas, finally we have found some peace... ", 
        'choices': {
            'Restart': "beginnings", 
        }
    }, 
    "run-away-forest": {
        'text': "'No, no, no..' you start panicking 'this can't be true!' You turn around and rush to the door... except there is no door. 'Wait...' your heartbeat intesifies that you can't breathe anymore, your heart will jump out of your body. You turn around and see Zephiel standing and smiling making a grin face. 'So?.. No way out, huh?' he says 'I'm sorry to break it down to you, but you're dead.' with these words he threw his bloody knife at you. You try to fall down, but it grazes through your forehead and you feel heavy red liquid rushing through your head. ", 
        'choices': {
            "Give up": "hospital", 
            "Don't give up": "fight scene"
        }
    }
}


# GUI setup
# Window settings
window = tk.Tk()
window.config(bg='white')
window.title("????")

# Important settings that will be changed later in the game. 
current_scene = 'beginnings'
text = None
choice_buttons = None
name = ""

chr_interaction1 = {
    'sayings': {
        '1': "", 
        "2": "", 
        "3": "", 
        "4": "", 
        "5": "", 
        "6": "", 
        "7": ""
        }
    }


# We get name by applying this function. We set the name to be global (usable outside the function's scope), so we do the same for name_entry, because we want to access it from a different scope. 
def get_name():
    global name_entry, name
    name = name_entry.get()

    story['cia-headquarters-5']['text'] = f"You look at Zephiel with suspicion. 'I know this name... What's your last name?' The man leans on, looks at your shoes. 'It is Korr.' he replies. At that point it feel like your heart skipped a beat. Your hair stood up like you were touched by a taser. Nervously you swallowed your saliva and replied. 'Oh shit. My name is {name}'"

    change_scene('cia-headquarters-5')
    return name

# This is the funciton that will handle the button info. It does two things. First, whenever the user presses some 'choice' button it changes to the according scene. Next, because we allow the user (later in the story) to choose the main character's character, the dialogue, the manners changes.  If the user chose to be aggresive, then he will act agressive for the whole game. 
def handle_btn_info(ns, ct):
    global chr_interaction1, name


    if ct == 'Interrogate':
        # dialogues for interrogative behaviour
        chr_interaction1['sayings']["1"] = "Who the fuck are you, bitch? What do you want from me?'"
        chr_interaction1['sayings']["2"] = "'Now, you know my name, dude, so may I ask you why the heck am I here?'"
        chr_interaction1['sayings']["3"] = "What does that supposed to fucking mean?"
        chr_interaction1['sayings']["4"] = "You took me to headquarters only to hear some madman rambling?."
        chr_interaction1['sayings']["5"] = "Where are you going with this? I'd better get some sleep.", 
        chr_interaction1['sayings']["6"] = "'No, dear prime minister of Central Intelligence Agency, I have no idea what time is' you say sarcastically."
        chr_interaction1['sayings']["7"] = ""
    
        # dialogues for polte behaviour. 
    elif ct == 'Be polite':
        chr_interaction1['sayings']["1"] = "What is your name, sir, and why am I here?"
        chr_interaction1['sayings']["2"] = "May I ask you again, sir, why did I need to come to this place?"
        chr_interaction1['sayings']["3"] = "What do you mean, sir?"
        chr_interaction1['sayings']["4"] = "I'm sorry, but I'm I listening to some madman rambling?"
        chr_interaction1['sayings']["5"] = "Okay, I hear you. But where are you going?"
        chr_interaction1['sayings']["6"] = "'No, sir. I have no idea what time is.' you reply."
        chr_interaction1['sayings']["7"] = ""
    
    # In order for this to work, we only want to change how the character behaves, the scene remains static. Thus, we use f"" and later reference the interactions we want to use. This also works because chr_interaction1 is mutually exclusive, meaning only one character type can be chosen. 
    story['cia-headquarters-4']['text'] = f"Everybody sits. You and the driver—on the chairs, the boss—on the couch in front. {chr_interaction1['sayings']['1']} you ask. The driver, now sitting on an armchair next to you, looks at you like you're a complete idiot. The man in suit chuckles, staring you in the eye. 'Me? I'm Zephiel, the head of the CIA. You?' "

    story['cia-headquarters-6']['text'] = f"Seems familiar, doesn't it? I know why. Where have you been before? Did you have coffee in the '65s? Or was it 1000 BCE? We have never met before. But it seems we did. It is beyond what we can describe at present."
    #We after this scene have one choice: reply "what?.."
    #Reply yes 
    story['cia-headquarters-6.1']['text'] = f"You frown at him, '{chr_interaction1['sayings']['3']}' Oh, nothing. I don't remember. Nobody does. But you do. Every one of us jumps back and forth between the worlds, and yet we can't remember what happened... we have no sense of the past. It's only the present."
    # After this we have an option: we can let him continue. 
    story['cia-headquarters-6.2']['text'] = f"{chr_interaction1['sayings']['4']} Time is a madman. Not me. How can we predict it? We can't. Everyone lives in lies. They think time is linear, but in fact, it's not. It swings like a crazy dog's tail."

    story['cia-headquarters-6.3']['text'] = f"{chr_interaction1['sayings']['5']} Oh, I'm not going anywhere. I'm staying here only to disappear and meet with someone else. We can't move on; it's not possible. We'll go back. Why am I even telling you this? I will forget it anyway. But it is worthy of trying. Ever thought about why we jump back and forth between time zones? I don't know. But I think you can figure out the answer. Nobody can, except you."


    # Now we present the character with two choices. React or 'Let Zephiel do his thing'

    # Let Zephiel do his thing.

    story['cia-headquarters-6.3.5']['text'] = f"{chr_interaction1['sayings']['5']}. Zephiel picks a long teacher stick. And points to T. 'This constant represents time,' he says. He moves his stick. ''I' represents the direction of time. In an ideal world, constant I would be an increasing function, with equality on each side. This would mean that time is linear. But the constnat is completely random. It cannot be predicted. Both sides are unequal. This causes time to fluctuate. Back and forth, you can appear in different timezones. We don't know why that's happening. And I want you,' he fixes his eyes on your forehead, 'to find the answer to the question.'"

    change_scene(ns)


def show_scene():
    global text, choice_buttons, current_scene, window, name_entry

    # Every time we enter a new scene, we destroy the prior scene elements. WE don't need to destroy the label per se, because it's dynamic, meaning it changes from time to time. 

    for widget in choice_buttons.winfo_children():
        widget.destroy()


    # label changes
    scene = story[current_scene]
    text.config(text=scene['text'])

    # We create a Quit button
    exit_btn = tk.Button(choice_buttons, text='No thank you (quit)', command=close_window)
    # these following elements are necessary to get the name. Entry lets one enter it, the button allows us to do something with it 
    name_entry = tk.Entry(choice_buttons, width=30, bg='white', font=('Garamond', 25, 'normal'), fg='black')
    continue_name_btn = tk.Button(choice_buttons, text='continue', command=get_name, font=('Garamond', 25), bg='white', fg='black')


    # We want the name to be asked only at a specific scene (cia-headquarters-4), so we will append the items only there. If the scene isn't cia-headquarters-4, we destroy 'name' elements

    if scene == story['cia-headquarters-4']:
        name_entry.pack(pady=10)
        continue_name_btn.pack(pady=10)
    else:
        name_entry.pack_forget()
        continue_name_btn.pack_forget()

    # same goes for the quit button - we want it to appear only when the character dies. 
    if scene == story['die']: 
        exit_btn.pack()

    # As each scene changes, so does the location. The title represents it, therefore we shall change it.]
    if scene == story['hospital']:
        window.title('Mount Sinal hospital, New York')
    elif scene == story['police-hospital']:
        window.title("One Police Plaza")
    elif scene == story['cia-headquarters-1']:
        window.title("CIA headquarters")

    # Every single time a code runs through the scenes of the story[] dict, it appends the buttons (choices) that belongs to each. Later, it takes us to the scene relative to the button that user has chosen. 
    for choice_text, next_scene in scene['choices'].items():
        button = tk.Button(choice_buttons, text=choice_text, width=25, command=lambda ns=next_scene, ct=choice_text: handle_btn_info(ns, ct), font=('Open Sans', 20))
        button.pack(pady=5)

# We change the scene. 
def change_scene(new_scene):
    global current_scene
    current_scene = new_scene
    show_scene()

# This is the start of our program
def start():
    global text, choice_buttons
    # This is the label that will contain the story's text,
    text = tk.Label(window, wraplength=1000, font=('Garamond', 25), bg='white', fg='black')
    text.pack(pady=20, padx=100, anchor='center', expand=True)
    # And the buttons
    choice_buttons = tk.Frame(window, bg='white')
    choice_buttons.pack(anchor='center', side='bottom')
    # We run the program, show the scene. 
    show_scene()
    window.mainloop()
# I don't know what this does. 
if __name__ == '__main__':
    start()

# There are a few things that are concerning at the moment. First, we don't get to use the name variable. Second, we can't use the character's unique interactions. 
