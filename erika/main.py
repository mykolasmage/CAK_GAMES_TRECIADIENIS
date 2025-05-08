import tkinter as tk

istorija = {
    "Pradzia": {
        "tekstas": "You wake up at the edge of the Forest of Fate.\n There are two paths leading away from it.\n A path to the north and a path to the east. Witch one will you take?", 
        "pasirinkimai": {
            "Go to the north": "urvas", 
            "Go to the east": "Caltia1"
        }, 
    }, 

    "urvas": {
        "tekstas": "You see a cave entrance.\n You hear faint growling inside. Will you take your chances in going inside?", 
        "pasirinkimai": { 
            "Go inside": "meska",
            "Go back to the forest": "Pradzia"
        }, 
    }, 

    "meska":{
        "tekstas":"You walk in to the cave.\n The truther you go the growly gets louder.\n Little did you know a bear was waiting at the end\n Who could have guessed?\n But the bear doesn't look like a normal bear\n It's pitch black and has very long fangs.\nIt's eyes are black like charcoal, and there is a black mist radiating from it's back\n",
        "pasirinkimai": {
            "RUN AWAY": "Pradzia"
        },
    },

    "upe": {
        "tekstas": "You come across a wide river. You can hear a waterfall further away.\n There is a small boat close by, but it has no paddles.\n You can see a bridge a bit truther.\n The stream of the river is quite strong. What do you do?", 
        "pasirinkimai": {
            "Get in the boat": "krioklys", 
            "Walk to the bridge": "kita puse", 
            "Go back to the forest": "Pradzia"
        },
    },

    "krioklys": {
        "tekstas": "You get on the boat and start swimming along the stream.\n You get faster, and faster. You see the waterfall that you heard earlier.\n You probably realised by now that this wasn't a great idea, was it?\n You fall down the waterfall and land on a sharp rock.\n What did you expect???\n\nYOU DIED", 
        "pasirinkimai": {
            "RESTART": "Pradzia"
        }, 

    }, 

    "kita puse": {
        "tekstas": "You walk up to the bridge. It doesin't seem too sturdy...\n Are you sure you want to go on it? It doesin't seem too safe.", 
        "pasirinkimai": {
            "Yes": "pieva", 
            "No, I want to go back to the river": "upe"
        }, 
    }, 

    "pieva": {
        "tekstas": "You approach the bridge and start walking on it.\n You manage to get to the other side, but the bridge breaks down after.\n You cant go back now...\n I warned you that its not safe...\n Anyway on other side of the river\n there is a meadow with green grass, butterflies and flowers.", 
        "pasirinkimai": {
            "Walk around and see what you can find": "skardis", 
            "Try to find some food": "miskelis", 
            "Accept your fate that you will die here": "accepted fate"
        }, 
    }, 

    "miskelis":{   
        "tekstas": "You walk around and see a forest *is it the same Forest of Fate* You wonder.\n But it.. feels different. You feel your stomach growl with hunger.\n You decide to look for food. You walk around for a little.\n you see some red berries hanging on a bush.\n There are some green mushrooms growing next to the bush.\n There's also a tree with weird, blue fruits.\n Will you eat any of them?", 
        "pasirinkimai": {
            "Eat one of them": "Food", 
            "No, I'm not risking it": "Hunger", 
            "Go back to the meadow": "pieva2"
        },
    }, 

    "Hunger": {
        "tekstas": "You decide to not eat anything. Your stomach keeps growling.\n Your body starts feeling weak.\n Your legs give up on you and you fall to the ground.\n You slowly suffer for the next few days,\nThe pain getting stronger and stronger until you inevitably die.\n\nYOU DIED",
        "pasirinkimai": {
            "RESTART": "Pradzia"
        },
    },

    "miskelis2": {
        "tekstas": "You go back to the forest, you still have the unsettling feeling about it.\n Do you want to get back where the food was?",
        "pasirinkimai": {
            "Yea": "miskelis",
            "No, go back to the meadow": "pieva2"
        },
    },

    "Food":{
        "tekstas": "which one will you eat?",
        "pasirinkimai": {
            "Red berries": "Poisoning", 
            "Green mushrooms": "Deadly poison", 
            "Blue fruits": "Safe food",
            "I changed my mind...": "miskelis"
        },
    }, 

    "Poisoning": {
        "tekstas": "You eat some of the red berries.\n Your stomach starts hurting.\n Later you go behind a tree and have explosive diarrhoea...\n gross\n But you're still hungry, will you eat something else?",
        "pasirinkimai": {
            "Yes": "Food", 
            "No": "miskelis2" 
        },
    },

    "Deadly poison": {
        "tekstas": "Yea the mushrooms weren't a great idea.\nYou feel fine for the first few minutes, before the poison kicks in\n You start feeling dizzy.\n You fall to the ground as the world starts spinning around you.\n You start foaming at the mouth and blood starts oozing out of your eyes.\n You can't bear the pain so you pass out.\n\nDidin't your parents teach you to not eat wild mushrooms?\n\nYOU DIED",
        "pasirinkimai": {
            "RESTART": "Pradzia"
        },
    },

    "Safe food": {
        "tekstas": "You eat one blue fruit. They taste great! And you weren't poisoned!\nLucky you!\nYou take some of them for the road\nWill you eat something else or keep going?",
        "pasirinkimai": { 
            "Keep going": "puddle", 
            "Go back to the forest": "miskelis2"
        },
    },

    "puddle":{
        "tekstas": "You keep walking\nYou see a small puddle. The water is still.\n You look at it and see your reflection.\n *Who am I?*, *What's my name?*,\n *What am I even doing here?*, *Where is here anyway???*\n these are the questions running trough your head.",
        "pasirinkimai": {
            "Keep walking": "dagger", 
            "Stay here questiong life": "puddle2", 
            "Go back to the forest": "miskelis2"
        },
    },

    "dagger":{
        "tekstas": "You keep walking away from the puddle.\n You spot a dagger laying on the grass.\nTake it?",
        "pasirinkimai": {
            "Take it": "slimes", 
            "Leave it": "slimesD", 
            "Go back": "puddle"
        },
    },

    "slimes": {
        "tekstas": "You take the dagger and keep walking.\n You hear a faint rustling in the bushes when a... slime jumps out?\nIs it one of those slimes from video games?\nIt's kinda cute\n, buuut it starts attacking you and it hurts, A LOT more than you expected.\nTurns out in this forest slimes arent for beginners.\n They're membrane is coated with an acid like substance.\nDo you want to fight it?",
        "pasirinkimai": {
            "Fight": "SlimesF", 
            "Flee": "Flee"
        },

    },

    "Flee":{
	    "tekstas": "You try to flee  from the slimes,\n but they're faster that they look. You get pushed in to a corner.\nWhat do you do?",
        "pasirinkimai": {
            "Fight": "SlimesF"
        },
    },

    "SlimesF":{
        "tekstas": "You pull out your dagger and try stabbing the slime.\nThe slime dies after a few more tries.\nYour dagger sustained a considerable amount of damage from the acid\n, but you survived.\nIt leaves a puddle of acid in it's place, in it there's a small dim-green stone.\nTake it?", 
        "pasirinkimai": {
            "Take it": "2slimes",  
        },
    },

    "2slimes":{
        "tekstas":"You take the small stone that the slime dropped.\n it's no larger than your finger nail, and has a faint green colour.\n You keep walking until you spot a few slimes eating something. You quickly hide in a bush.\n they don't seem to have spotted you.\nWhat do you do now?",
        "pasirinkimai": {
            "Keep hiding": "Wait", 
            "Try attacing them": "2slime2", 
            "Try going back": "2SlimeDie"
        },
    },

    "Wait":{
        "tekstas":"You keep hiding but when the finish eating they start heading towards you.\nTurns out since they have bad vision they sensed you...\n(that's kinda op tbh -_-)\nThey start charging at you.\n You tried to pull out your dagger but it was too late\nOne of them jumped on your head and the other on your arm.\n Congrats you were slowly devoured by slimes...\n\nYOU DIED",
        "pasirinkimai": {
            "RESTART": "Pradzia"
        },
    },

    "2slime2":{
        "tekstas":"You mindlessly charge in.\n You try using your dagger again but it's too damaged to do anything.\n The slimes turn around and look at you.\nYou try to get out of there, but tough luck.\nThey soon catch up,\nyou pick up a stick that's close to you.\nYou hit the slime but the acid slowly melted the wood.\nYou were panicking,\nyou knew you were next\nin the heat of the moment you remember the think they were eating before\n'What was that?', you look past them\nIt looks like a human figure, they seem to have a sword with them.\nYou make a run for it.\nYou get to the lifeless body, its leg is missing already but it seems fresh\nYou quickly grab the sword.\nBut right after that you remember you don't know how to use a sword...\nWell its worth a shot",
        "pasirinkimai": {
            "Use the sword": "2slime2F", 
        },
    },

    "2slime2F":{
        "tekstas":"You pick up the sword and stand up.\nYou look at the slimes.\nYou get that deja-vu feeling that you've done this before.\nYou get in to a fighting stance and slash them with the sword.\nYou seem to have more skill with a sword than a dagger.\nalthough your memories are lost you, its mussle-memory that takes over.\nIt feells like you've been doing this for years.\nYou skillfully flash your sword and take down one of the slimes\nThe sword broke into small pieces\n but you still manage to win.\nThe slimes didint seem to drop anything this time,\n and the last slime seemed way harder to take down",
        "pasirinkimai": {
            "Check out the body": "Body", 
        },
    },

    "slimesD": {
        "tekstas": "You leave the dagger and keep walking.\n You hear a faint rustling in the bushes when a... slime jumps out?\nIs it one of those slimes from video games?\nIt's kinda cute, buuut it starts attacking you and it hurts\n, A LOT more than you expected.\nTurns out in this forest slimes arent for beginners.\n They'r membrane is coated with an acid like substance.\nWill you run?",
        "pasirinkimai": {
            "Give up": "SlimeDie", 
            "Run": "SlimeRun"
        },
    },

    "SlimeDie": {
        "tekstas": "You decide to give up.\n You stand in one place\n until the slime jumps on your head submerging you in it-self.\nYou can't breathe and the pain of your skin being devoured is unbearable.\n You slowly die by a slime.\n\nYOU DIED",
        "pasirinkimai": {
            "RESTART": "Pradzia"
        },
    },

    "SlimeRun": {
        "tekstas": "You start running for your life\n, knowing that you are no match for the slimes.\n but they're faster than they look.\n They eventually catch up to you. If only you had some kind of weapon.\nThe slime jumps on your head submerging you in it-self.\nYou can't breathe and the pain of your skin being devoured is unbearable.\n You slowly die by a slime.\n\nYOU DIED",
        "pasirinkimai": {
            "RESTART": "Pradzia"
        },
    },

    "2SlimeDie":{
        "tekstas":"You slowly start walking away, trying to not make any noise\n, but when the finish eating they start heading towards you.\nTurns out since they have bad vision they sensed you...\n(that's kinda op tbh -_-)\nThey start charging at you.\n You tried to pull out your dagger but it was too late\nOne of them jumped on your head and the other on your arm.\n Congrats you were slowly devoured by slimes...\n\nYOU DIED",
        "pasirinkimai": {
            "REASTART": "Pradzia"
        },
    },

    "puddle2":{
        "tekstas": "You stand next to the puddle thinking about... uhhh... stuff\nDo you want to go back?", 
        "pasirinkimai": {
            "Stay here for a bit longer": "puddle3",
            "Go back": "puddle4"
        },
    },

    "puddle3":{
        "tekstas":"You keep standing until you run out of things to think about.\nYou get bored and don't care about anything anymore.",
        "pasirinkimai": {
            "Go back": "puddle4"
        },
    },

    "puddle4":{
        "tekstas":"You come back to the small puddle.\nNothing else happened to it.",
        "pasirinkimai": {
            "Keep walking": "dagger", 
            "Go back to the forest": "miskelis2"
        },
    },

    "accepted fate": {
        "tekstas": "You arent even trying at this point, are you...\nI know you can do better that this...\nplease don't make the same mistake again.\n\nYOU DIED", 
        "pasirinkimai": {
            "RESTART": "Pradzia"
        }, 
    }, 

    "pieva2": {
        "tekstas": "You go back to the meadow. It still looks as nice as before.", 
        "pasirinkimai": {
            "Walk around and see what you can find": "skardis", 
            "Try to find some food": "miskelis"
        }, 
    }, 

    "skardis": {
        "tekstas": "You walk around for a little. You see a cliff. You walk up to it.\n The fall would be very painful.\n What can you even do with a cliff? Jump off??", 
        "pasirinkimai": {
            "Jump off": "Pasigailejimas", 
            "Keep walking" : "miskelis", 
            "Go back" : "pieva2"
        }, 
    },

    "Pasigailejimas": {
        "tekstas": "Well you jumped off...\n Didn't think you would actually do it...\n WHY DID YOU THINK THIS WAS A GOOD IDEA???\nIt's obvious that you will die\nI even told you it would be a painful fall!\n\n YOU DIED", 
        "pasirinkimai": {
            "RESTART": "Pradzia"
        }, 
    }, 

    "Body":{
        "tekstas":"You approach the body\nIt was a gruesome sight to see.\n You didint notice it while fighting but half of its head is missing\nYou cant even identify the gender, race or... anything at this point\nThey had a small bag with them.\nYou look inside, there is:\n    • a bag with coins that look like money\n   • a book with the title '⏚⏃⌇⟟☊⌇ ⍜⎎ ⋔⏃☌⟟☊'(I wonder what that means :3)\n   • a card\n  •some potions with small labels:\n         '⍙⟒⏃☍ ⊑⟒⏃⌰⟟⋏☌', '⌇⏁⏃⋔⟟⋏⏃ ⍀⟒☌⟒⋏' and '⋔⏃⋏⏃ ⟟⋏☊⍀⟒⏃⌇⟒ ⏁⟒⋏ ⋔⟟⋏'",
        "pasirinkimai": {
            "check out the coin bag": "CoinBag", 
            "check out the book": "book", 
            "check out the card": "card",
            "check out the potions": "potions",
            "take them and keep walking": "night1"
        },
    },

    "CoinBag":{
        "tekstas":"You check inside the coin bag.\n It seems to have 10 copper, 5 silver and 2 gold coins. 'Is this currency?'\nYou close the bag and check out the other stuff",
        "pasirinkimai": {
            "check out the book": "book",
            "check out the card": "card",
            "check out the potions": "potions", 
            "Keep walking": "Guard"
        },
    },

    "book":{
        "tekstas":"The book seems to be written in a different language.\n The title on the cover says '⏚⏃⌇⟟☊⌇ ⍜⎎ ⋔⏃☌⟟☊'.\nYou open the book and on the first page is writen:\n\n\n'⏚⏃⌇⟟☊⌇ ⍜⎎ ⋔⏃☌⟟☊\n\n ⏚⊬ ⋔⊬⟟⟒⊬ ⏁⊑⟒ ☌⍀⟒⏃⏁\n\n ⍙⊑⏃⏁⟟⌇ ⏃ ⌇⌿⟒⌰⌰?\n⏃ ⌇⌿⟒⌰⌰ ⟟⌇ ⏃ ⎅⟟⌇☊⍀⟒⏁⟒ ⋔⏃☌⟟☊⏃⌰ ⟒⎎⎎⟒☊⏁, ⎅⟒⎎⟟⋏⟒⎅ ⟟⋏ ⌇⌿⟒☊⟟⎎⟟☊ ⌰⏃⋏☌⎍⏃☌⟒.\n ⏃ ⌇⌿⟒⌰⌰ ⊑⏃⌇ ⌇⌿⟒☊⟟⎎⟟☊ ⏁⊑⟟⋏☌⌇ ⌰⟟☍⟒ ⏃ ⋏⏃⋔⟒, ⏃ ⎅⟒⎎⟟⋏⟒⎅ ⍀⏃⋏☌⟒,\n ⏃⋏⎅ ⍀⟒⍾⎍⟟⍀⟒⎅ ☊⍜⋔⌿⍜⋏⟒⋏⏁⌇⌇⌿⟒⌰⌰⌇ ☊⏃⋏\n ⏚⟒ ⎐⟒⍀⌇⏃⏁⟟⌰⟒ ⏁⍜⍜⌰⌇, ⍙⟒⏃⌿⍜⋏⌇, ⍜⍀ ⌿⍀⍜⏁⟒☊⏁⟟⎐⟒ ⍙⏃⍀⎅⌇.\n ⏁⊑⟒⊬ ☊⏃⋏ ⎅⟒⏃⌰ ⎅⏃⋔⏃☌⟒ ⍜⍀ ⎍⋏⎅⍜ ⟟⏁, ⟟⋔⌿⍜⌇⟒ ⍜⍀ ⍀⟒⋔⍜⎐⟒ ☊⍜⋏⎅⟟⏁⟟⍜⋏⌇,\n ⎅⍀⏃⟟⋏ ⌰⟟⎎⟒ ⟒⋏⟒⍀☌⊬ ⏃⍙⏃⊬, ⏃⋏⎅ ⍀⟒⌇⏁⍜⍀⟒ ⌰⟟⎎⟒ ⏁⍜ ⏁⊑⟒ ⎅⟒⏃⎅.\n\n⏁⊑⍜⎍⌇⏃⋏⎅⌇ ⍜⎎ ⌇⌿⟒⌰⌰⌇ ⊑⏃⎐⟒ ⏚⟒⟒⋏ ☊⍀⟒⏃⏁⟒⎅,\n ⎅⟟⌇☊⍜⎐⟒⍀⟒⎅, ⌰⍜⌇⏁, ⏃⋏⎅ ⍀⟒-⎅⟟⌇☊⍜⎐⟒⍀⟒⎅\n ⏁⊑⍀⍜⎍☌⊑⍜⎍⏁ ⏁⊑⟒ ⊑⟟⌇⏁⍜⍀⊬ ⍜⎎ ⏁⊑⟒ ⋔⎍⌰⏁⟟⎐⟒⍀⌇⟒.\n⊬⍜⎍ ⋔⟟☌⊑⏁ ⍀⟒⌰⊬ ⍜⋏ ⍙⟒⌰⌰-☍⋏⍜⍙⋏\n ⌇⌿⟒⌰⌰⌇, ⏁⊑⟒⊬ ⋔⟟☌⊑⏁ ⎅⟟⌇☊⍜⎐⟒⍀ ⌰⍜⋏☌-⎎⍜⍀☌⍜⏁⏁⟒⋏\n ⌇⌿⟒⌰⌰⌇ ⟟⋏ ⌇⍜⋔⟒ ⏃⋏☊⟟⟒⋏⏁ ⏁⍜⋔⟒, ⍜⍀ ⏁⊑⟒⊬ ⋔⟟☌⊑⏁ ⟒⎐⟒⋏ ☊⍀⟒⏃⏁⟒ ⏁⊑⟒⟟⍀ ⍜⍙⋏ ⌇⌿⟒⌰⌰,\n ⎎⍜⍀⟒⎐⟒⍀ ⌰⟒⏃⎐⟟⋏☌ ⏁⊑⟒⟟⍀ ⋔⏃⍀☍ ⍜⋏ ⏁⊑⟒ ⋔⎍⌰⏁⟟⎐⟒⍀⌇⟒.'\n\nCheck out something else?",
        "pasirinkimai": {
            "check out the coin bag": "CoinBag",
            "check out the card": "card",
            "check out the potions": "potions", 
            "Keep walking": "night1"
        },
    },

    "card":{
        "tekstas":"You check out the card. it kinda looks like an ID card, but not really.\n It doesn't have a picture or anything for that matter only writing.\nIt looks sturdy though\n The writing on it says:\n\n⏚⟟⌰⌰\n ⍀⟒☌⟟⌇⏁⟒⍀⟒⎅ ⏃⌇ ⏃⋏ ⏃⎅⎐⟒⋏⏁⎍⍀⟒⍀ ⟟⋏ ⏁⊑⟒ ⏃⎅⎐⟒⋏⏁⎍⍀⟒⍀'⌇ ☌⎍⟟⌰⎅\n ☊ ⍀⏃⋏☍ ⏃⎅⎐⟒⋏⏁⎍⍀⟒⍀\n ⊑⍜⋔⟒ ☊⟟⏁⊬ - ☊⏃⌰⏁⟟⏃",
        "pasirinkimai": {
            "check out the coin bag": "CoinBag",
            "check out the book": "book",
            "check out the potions": "potions", 
            "Keep walking": "night1"
        },
    },

    "potions":{
        "tekstas":"there are 3 differnt potions.\n the labels on them say:\n\n\n'⍙⟒⏃☍ ⊑⟒⏃⌰⟟⋏☌', '⌇⏁⏃⋔⟟⋏⏃ ⍀⟒☌⟒⋏' and '⋔⏃⋏⏃ ⟟⋏☊⍀⟒⏃⌇⟒ ⏁⟒⋏ ⋔⟟⋏'\n\nThe first potion with the label '⍙⟒⏃☍ ⊑⟒⏃⌰⟟⋏☌' is red with a purpleish tint,\n\nthe second one with the label '⌇⏁⏃⋔⟟⋏⏃ ⍀⟒☌⟒⋏' is green\n\nThe last one with the label '⋔⏃⋏⏃ ⟟⋏☊⍀⟒⏃⌇⟒ ⏁⟒⋏ ⋔⟟⋏'\n looks more expensive than the others and has a brilliant purple color",
        "pasirinkimai": {
            "check out the coin bag": "CoinBag",
            "check out the book": "book",
            "check out the card": "card",
            "Keep walking": "night1"
        },
    },

    "night1":{
        "tekstas":"You check out the items you found\n and decide to keep walking in hopes of finding something useful.\nIt's starting to get dark and it looks like it will rain tonight.\nYou spot a cave in the distance\n 'could I take shelter there for the night?'\nYou walk up to the cave do you want to go in?",
        "pasirinkimai": {
            "Go in": "Cave", 
            "Go back to the body": "Body"
        },
    },

    "Cave":{
        "tekstas":"You go inside the cave.\n It's not that big and it doesn't seem like anything's living in it.\nSeems safe to stay the night there\nBut there's one problem.\nYou don't have any pillows, blankets or anything like that.\nYou try to lay down on the cold, stone ground\nYou barely fall asleep. You wake up in the middle of the night.\nWhat do you do now?",
        "pasirinkimai": {
            "Try to fall back asleep": "Tired", 
            "Take a stroll through the forest": "Stroll", 
            "Sit there": "Sitting"
        },
    },

    "Tired":{
        "tekstas":"You try to go back to sleep.\n You lay down and close your eyes. It's way colder than before.\nYou cant seem to fall asleep.\nAfter a while, comes thich fog that you can barely see though.\nGo investigate? ",
        "pasirinkimai": {
            "Go check it out": "FogT", 
            "Keep sitting there": "SitT"
        },
    },

    "Stroll":{
        "tekstas":"You can't seem to fall asleep again.\nYou decide to take quick stroll though the forest.\nYou walk around for a moment or two when you find a path.\nYou don't know where it leads to.\nYou still start following it\nA thick fog starts appearing out of no where.\nYou keep following the path.\nAfter five minutes... or was it hours? You finally reach the end.\nThere's a small chest at the end.\nOpen it?",
        "pasirinkimai": {
            "Yup!": "WakeUp",
            "OFC!!": "WakeUp" 
        },
    },

    "Sitting":{
        "tekstas":"You just sit in silence.\nYou get bored fast.\nYou start daydreaming.\nYour daydream turns in to questions.\n*What am I doing here?*, *Why am I here?*, *Where am I from?, Earth I think...*, *How am I here?*\nBut they didn't help you fall asleep, did they?\nWell what do you do now?",
        "pasirinkimai": {
            "Take a stroll": "Stroll", 
            "Try to fall back asleep": "Tired"
        },
    },

    "FogT":{
        "tekstas":"You walk out of the cave.\nThe fog is making it hard to see but you spot a path in the distance\nYou start following it.\nAfter a few minutes.. or was it hours? You finally reach the end.\nThere's a small chest.\nOpen it?",
        "pasirinkimai": {
            "Sure!": "WakeUp", 
            "Will do!": "WakeUp", 
            "Kay!": "WakeUp"
        },
    },

    "SitT":{
        "tekstas":"You keep sitting on the cold, stone floor.\nThe fog get thicker and thicker.\nYou sure you're not interested?",
        "pasirinkimai": {
            "Fine, I'll check it out": "FogT", 
            "Nah, I'll pass": "..."
        },
    },

    "WakeUp":{
        "tekstas":"You try opening the chest.\nYou open it and a bright light flashes.\nYou seem to wake up.\nYou're back at the cave *Was it a dream?*\nYou run outside to see if the path is still there.\nIt's there...\nYou don't remember it being there before you fell asleep.\nYou follow it.\nThere's no fog this time and you don't feel dizzy anymore.\nThe sky is bright blue with only a few clouds.\nBirds are chirping in the trees.\nIts a nice day but you still feel uncomfortable remembering the dream\nbut the thing you're most exited to see is if the chest is still there.\nYou come to the end of the path again.\nIt's there!\nTry opening it?",
        "pasirinkimai": {
            "Okk": "Chest", 
            "Go back to the cave": "cave"
        },
    },

    "...":{
        "tekstas":"Oh come on... you know what you need to do...\nFine just sit here until you check it out",
        "pasirinkimai": {
            "Fine, check it out": "Path", 
            "Ig I'll just sit here then": "."
        },
    },

    "cave2":{
        "tekstas":"You go back to the cave following the path you came from.\nYour back at the cave now.\nWhat will you do now?",
        "pasirinkimai": {
            "Go back to the path": "Path"
        },
    },

    "Chest":{
        "tekstas":"You examine, the chest before trying to open it.\nIt's a small red box with weird clouds and fog drawings all over it.\nThere's a small drawing of a sheep carved on the back.\nYou try opening.\nIt seems to be locked. And after all that trouble my friend had to go through.\nFine I'll tell you the code, but remember it 'cause I wont tell you again.\nCode: 536470",
        "pasirinkimai": {
            "Use the code": "ChestCodeU"
        },
    },

    "Path":{
        "tekstas":"You follow the path. There's no fog\n, unlike in the dream. The path isn't as long as you remember.\nWhen you reach the end the chest is there!\nTry opening it?",
        "pasirinkimai": {
            "Sure!": "Chest", 
            "Nahh, I'm going back": "cave2"
        },
    },

    ".":{
        "tekstas":"You just sit there",
        "pasirinkimai": {
            "Fine, I'll check it out": "Path", 
            "I'll keep sitting here >:(": "."
        },
    },

    "ChestCodeU":{
        "tekstas":"Use the code",
        "pasirinkimai": {
            "Try again": "ChestCodeU"
        },
    },

    "ChestOpen":{
        "tekstas":"You open the chest. There are some earrings inside.\nThere're small, white and shaped like little clouds",
        "pasirinkimai": { 
            "Walk around and see what you can find": "Walk", 
            "Go back to the cave": "cave3"
        },
    },

    "Walk":{
        "tekstas":"You take a walk aroun the forest behind the cave. \nThe forest still seems the same as it did before.\n You feel hungry and eat the rest of the fruits you took.\nAfter a while of walking you spot a cliff in the distance.\nYou walk up to it and look around. The sun started setting already.\nYou see a beautiful dunset above the clouds.\nYou decide to look around, you spot a small village in the distance.\nYou get exited by your new find.\n You start walking in the direction of the village.\nBut then you remember that its a cliff...\nWhat do you do now?",
        "pasirinkimai": {
            "Jump off": "Jumping_off2", 
            "levitate to the bottom": "magic_:p", 
            "try to find a way around it": "more_walking"
        },
    },

    "cave3":{
        "tekstas":"You go back to the cave. Your stomach growls again.\nYou decide to eat some fruit that you took earlier.\nThey still tasted great.\nYou sit around in the cave for a while and get bored.\nyou made a little doll out of some scraps you found tho.\nWhat do you do now?",
        "pasirinkimai": {
            "Walk around and see what you can find": "Walk"
        },
    },

    "Jumping_off2":{
        "tekstas":"I just feel bad for you at this point so I'll give you another chance \n(I know I'm so nice)",
        "pasirinkimai": {
            "Go back": "Walk"
        },
    },

    "magic_:p":{
        "tekstas":"+rolls a D20+ oh wow, an 18 you're lucky.\n Well, you try levitating off the cliff.\n You don't know anything about magic so you just wing it.\n It was somehow successful.\nYou slowly levitate off the cliff",
        "pasirinkimai": {
            "Start walking to the village": "jurney1Start"
        },
    },

    "more_walking":{
        "tekstas":"You look around you. \nThere seems to be a small path right next to you.\nYou start following it and it leads you off the cliff safely.",
        "pasirinkimai": {
            "Start walking to the village": "jurney1Start"
        },
    },

    "jurney1Start":{
        "tekstas":"You get off of the cliff and start walking towards the village.\nIt doesn't seem too far away and you can see it in the horizon,\n but it'll take you at least a day to get to it.\nYou ran out of food this morning so you'll have to deal with that too.\nUnless you find something on the way.\nDon't recommend eating stuff you don't know tho.\nWell its getting dark and you found a big tree that can shelter you if it rains.\n You lie down on the soft grass, its WAY more comfortable than the stone floor in the cave\nYou lie around until you find the perfect position to fall asleep.\nBut some thing is still bothering you.\nIs it the earrings?\n*What coud they be used for?*\n*Well thats a problem for tomorrow, now time to sleep.*\nYou slowly close your eyes and drift in to sleep",
        "pasirinkimai": {
            "Wake up": "jurney1"
        },
    },

    "JurneyWait":{
        "tekstas":"",
        "pasirinkimai": {
            "": "", 
            "": "", 
            "": ""
        },
    },

    "jurney1":{
        "tekstas":"You wake up.\nThe sun just started rising so thankfully you didint oversleep.\n*Well, time to get walking*\nThere's a path probably made by merchant carriages traveling in and out of the village.\nYou start following the path towards the village.\nNow that you have some time to kill you can think about why there were earrings in the box and what they are used for.\n*They are pretty tho, they'd fetch a pretty good price if sold to a jeweller* \n+DONT you dare sell them+\n anyway, ignore her... ah I haven't introdused you two yet have I?\n Well you arent supposed to meet until chapter two...\n so I dont know why she decided to talk to you now but you wont be seeing her for a while\nWell all I'm going to say is that she's the friend that gave you the gift\nI'll leave the rest of figuring out more to you.\nJust wait until you reach the village, until then you can think about it",
        "pasirinkimai": {
            "continue": "JurneyWait"
        },
    },

    "AfterWaiting":{
        "tekstas":"You finally reach the village, it is dark tho,\n about 1 am if you had to guess. The gate is closed so you have to find a place you can sleep the night.\n After some looking around you find another tree and decide to spend the night there.\n You lay down and drift off to sleep.",
        "pasirinkimai": {
            "Wake up": "bridge"
        },
    },

    "bridge":{
        "tekstas":"You walk around until you reach the gate. Its open now and there's a guard standing next to it.\nYou try walking inside the village but she confronts you.\n '⊑⟒⌰⌰⍜ ⌇⟟⍀, ⌿⌰⟒⏃⌇⟒ ⌇⊑⍜⍙ ⋔⟒ ⊬⍜⎍⍀ ⟟⎅ ☊⏃⍀⎅' she says to you in an unfamiliar language\n 'uhh... I don't....', *if I cant understand her she wont understand me eather, will she...*\n '⊬⍜⎍⍀ ⟟⎅ ⌇⟟⍀' she asks again.\n You walk away feeling awkward. You go behind the same tree you slept by tonight.\nHow will you solve this problem?",
        "pasirinkimai": {
            "Sit here doing nothing": "nothing", 
            "see what you have in your bag": "bag"
        },
    },

    "nothing":{
        "tekstas":"You sit down next to the tree and do nothing",
        "pasirinkimai": {
            "See what you have in your bag": "bag"
        },
    },

    "bag":{
        "tekstas":"in your inventory you have some potions, the damaged dagger.... oh right, the earrings!",
        "pasirinkimai": {
            "Put them on": "Puton"
        },
    },

    "Puton":{
        "tekstas":"You put on the earrings. You can feel a weird energy flowing from them\n Well there's no harm in trying to talk to the guard again, is there?",
        "pasirinkimai": {
            "Kay": "bridge1", 
            "Nahh, talking to women is scary": "sereusly?"
        },
    },

    "sereusly?":{
        "tekstas":"Oh come on...Just do it or I'll force you to",
        "pasirinkimai": {
            "No, you won't": "YouThinkSo?", 
            "FINE": "bridge1"
        },
    },

    "YouThinkSo?":{
        "tekstas":"...",
        "pasirinkimai": {
            "Go talk to her": "bridge1", 
            "Go talk to her ": "bridge1"
        },
    },

    "bridge1":{
        "tekstas":"You walk back to the bridge and she starts talking again.\n'Oh, it's you again' she said with an annoyed look on her face.\n'are you going to talk this time? 'she asks you\n*the earrings worked! I understand her now!* you think to yourself\nWhat do you say now?",
        "pasirinkimai": {
            "'Oh yea, sorry about that'": "FirstWords", 
            "'Yea, I'll talk this time'": "FirstWords",
            "'my deepest condolences, I'm truly sorry'": "FirstWords"
        },
    },

    "FirstWords":{
        "tekstas":"'Well at least you'll talk now... So anyway please show me your identification card' she tells you,\n'Uhhh about that... I.. don't have one...'\n'Hmm... then that'll cost 5 copper as an entry fee'\nYou take out your coin bag and pay the fee\n'Don't forget to get an id card when you're in the village or if you want a more... affordable option you can register with the adventurers guild'\n'Will do'\n'Now... since it's your first time in Caltia I'll have to check your bag' she told you\nYou hand over your bag to her.\nshe looked thruogh it 'okay, everything's good, have a great time in Caltia!' she said while handing your bag back to you",
        "pasirinkimai": {
            "Go thruogh the gate": "Caltia1"
        },
    },

    "Caltia1":{
        "tekstas":"You walk though the gate.\n*it kinda looks like a medieval, European village* you think. you look around\n your stomach growls.\nYou look around and see a tavern\nYou decide to go in and check it out, you do still have some money left.\nYou go in and look around, you spot an empty table and go sit down.\nYou order some stew, it's pretty bland but you're startving so you enjoi it.\nYou pay for your meal and go serch for an inn. It costed 3 copper, not too expensive.",
        "pasirinkimai": {
            "Go look for an inn": "inn"
        },
    },

    "inn":{
        "tekstas":"You walk aruond and find one that looks kinda run down.\nYou go in a receptionist greets you 'Hello sir are you looking to stay at our inn?', \n'Yea, I'd like a room please',\n 'That'll be 2 coppers a night and 1 more copper for breakfast',\n+You hand her 2 copper and 1 as payment+ \n'Okay two nights it is, follow me sir, I'll take you to your room'\nYou follow her and she leads you to a small room with one bed, a cupboard and a wardrobe",
        "pasirinkimai": {
            "CHAPTER ONE END": "Chapter1End"
        },
    },

    "Chapter1End":{
        "tekstas":"You finished chapter one! Congrats!\n\n\n\n(Chapter two is a wip... this already took too long T_T(in total this has 77 scenes I hope that's enough to make up for not finishing the game), Chapter two will come out in a few weeks... or never, we'll see)\n\n\nwe apologise for spelling errors and thank you for playing ~★~ Forest of Fate Chapter 1~★~",
        "pasirinkimai": {
            "Credits": "Credits"
        },
    },

    "Credits":{
        "tekstas":"\n\n\n\nCredits:\n\n\n\n Story made by - me\n\n programed by - code academy kids(Mykolas Aškelovičius) and ChatGPT (only a little by me)\n\n",
        "pasirinkimai": {
            "Quit": "End"
        },
    },
}

dabartine_scena = "Pradzia"
teksto_laukas = None
mygtukai = None
inventory = {}
inventory_label = None
coin_bag = {}
equipment = {
    "Weapon": None,
    "Armor": None,
    "Accessory": None
}


def add_item(item_name):
    if item_name in inventory:
        inventory[item_name] += 1
    else:
        inventory[item_name] = 1
    atnaujinti_inventoriu()

def remove_item(item_name):
    if item_name in inventory:
        inventory[item_name] -= 1
        if inventory[item_name] <= 0:
            del inventory[item_name]
    atnaujinti_inventoriu()

def atnaujinti_inventoriu():
    equipped_items = {item for item in equipment.values() if item}

    inventory_parts = []
    for item, count in inventory.items():
        if item in equipped_items:
            continue
        if count > 1:
            inventory_parts.append(f"{count}x {item}")
        else:
            inventory_parts.append(item)

    inventory_text = "Inventory: " + ", ".join(inventory_parts)
    if "Coin Bag" in inventory:
        coins_text = f" | Coins: {coin_bag.get('copper', 0)}c {coin_bag.get('silver', 0)}s {coin_bag.get('gold', 0)}g"
        inventory_text += coins_text

    inventory_label.config(text=inventory_text)


    equipment_parts = []
    for slot, item in equipment.items():
        if item:
            equipment_parts.append(f"{slot}: {item}")
        else:
            equipment_parts.append(f"{slot}: (empty)")

    equipment_text = "Equipment: " + " | ".join(equipment_parts)
    equipment_label.config(text=equipment_text)

    


def rodyti_scena():
    global dabartine_scena, teksto_laukas, mygtukai

    if dabartine_scena == "End":
        root.destroy()
        return

    for widget in mygtukai.winfo_children():
        widget.destroy()

    scena = istorija.get(dabartine_scena, {"tekstas": "", "pasirinkimai": {}})
    print("Available scenes:", list(istorija.keys()))
    print("Trying to load scene:", dabartine_scena)


    if dabartine_scena == "Safe food":
            add_item("Fruit")
    elif dabartine_scena == "Pradzia":
        inventory.clear()
        coin_bag.clear()
        for slot in equipment:
            equipment[slot] = None
    elif dabartine_scena == "slimes":
        add_item("Dagger")
    elif dabartine_scena == "SlimesF":
        remove_item("Dagger")
        add_item("Damaged Dagger")
    elif dabartine_scena == "2slimes":
        add_item("Green Stone")
    elif dabartine_scena == "Body":
        add_item("Coin Bag")
        add_item("Book")
        add_item("Card")
        add_item("Red Potion")
        add_item("Green Potion")
        add_item("Purple Potion")
        coin_bag['copper'] = 10
        coin_bag['silver'] = 5
        coin_bag['gold'] = 2
    elif dabartine_scena == "FirstWords":
        coin_bag["copper"] = max(0, coin_bag.get("copper", 0) - 5)
        atnaujinti_inventoriu()
    elif dabartine_scena == "Caltia1":
        coin_bag["copper"] = max(0, coin_bag.get("copper", 0) - 3)
        atnaujinti_inventoriu()
    elif dabartine_scena == "inn":
        coin_bag["copper"] = max(0, coin_bag.get("copper", 0) - 2)
        coin_bag["silver"] = max(0, coin_bag.get("silver", 0) - 1)
        atnaujinti_inventoriu()
    elif dabartine_scena == "ChestOpen":
        add_item("Cloud Earrings")
    elif dabartine_scena == "cave3":
        add_item("scrap doll")
    elif dabartine_scena == "Puton":
        if "Cloud Earrings" in inventory:
            equip_item("Cloud Earrings")
    elif dabartine_scena == "Walking":
        if "Fruit" in inventory:
            del inventory["Fruit"]

    atnaujinti_inventoriu()

    if dabartine_scena == "JurneyWait":
        teksto_laukas.config(text="You keep walking...")
        root.after(30000, rodyti_tesimo_mygtuka)
        return

    if dabartine_scena == "slimes":
        if "Dagger" not in inventory:
            add_item("Dagger")
        equip_item("Dagger")

    if dabartine_scena == "SlimesF":
        if "Dagger" in inventory:
            remove_item("Dagger")
        add_item("Damaged Dagger")
        equip_item("Damaged Dagger")

    if dabartine_scena == "Walk":
        remove_item("Fruit")

    if dabartine_scena == "ChestCodeU":
        atidaryti_kodo_ivedima()
        return

    scena = istorija.get(dabartine_scena, {"tekstas": "Scene not found", "pasirinkimai": {}})
    teksto_laukas.config(text=scena["tekstas"])


    for pasirinkimo_tekstas, kita_scena in scena["pasirinkimai"].items():
        mygtukas = tk.Button(mygtukai, bg="#8a8666", text=pasirinkimo_tekstas, width=30,
                             command=lambda ns=kita_scena: keisti_scena(ns))
        
        mygtukas.pack()

def keisti_scena(nauja_scena):
    global dabartine_scena
    dabartine_scena = nauja_scena
    rodyti_scena()


def atidaryti_kodo_ivedima():
    teisingas_kodas = "536470" 

    def tikrinti_koda():
        ivestas_kodas = kodas_entry.get()
        if ivestas_kodas == teisingas_kodas:
            kodas_popup.destroy()
            global dabartine_scena
            dabartine_scena = "ChestOpen"
            rodyti_scena()
        else:
            klaida_label.config(text="Wrong! Try again!")

    kodas_popup = tk.Toplevel(root)
    kodas_popup.title("Code:")
    kodas_popup.geometry("300x150")
    kodas_popup.configure(bg="#4e6196")

    tk.Label(kodas_popup, text="Input the code:", fg="#ccd9fc", bg="#4e6196").pack(pady=10)
    kodas_entry = tk.Entry(kodas_popup, bg="#203454", fg="#4a638a", width=20)
    kodas_entry.pack()

    klaida_label = tk.Label(kodas_popup, text="", fg="#b01515", bg="#4e6196")
    klaida_label.pack()

    tikrinti_btn = tk.Button(kodas_popup, text="Check", bg="#7b5da8", fg="#b9a0de", command=tikrinti_koda)
    tikrinti_btn.pack(pady=10)

    kodas_entry.focus()

def equip_item(item):
    if item in ["Dagger", "Damaged Dagger"]:
        equipment["Weapon"] = item
    elif item in ["Cloud Earrings"]:
        equipment["Accessory"] = item
    
    atnaujinti_inventoriu()


def rodyti_tesimo_mygtuka():
    for widget in mygtukai.winfo_children():
        widget.destroy()

    def testi():
        if dabartine_scena == "JurneyWait":
            keisti_scena("AfterWait")
        elif dabartine_scena == "ChestCodeU":
            keisti_scena("ChestOpen")
        else:
            keisti_scena("AfterWaiting")

    tesimo_mygtukas = tk.Button(mygtukai, text="Continue", bg="#b39a2d", fg="#dbcb86", width=30, command=testi)
    tesimo_mygtukas.pack()

def rodyti_tesimo_mygtuka():
    for widget in mygtukai.winfo_children():
        widget.destroy()

    def testi():
        if dabartine_scena == "JurneyWait":
            keisti_scena("AfterWait")  
        else:
            keisti_scena("AfterWaiting")

    tesimo_mygtukas = tk.Button(mygtukai, text="Continue", bg="#b39a2d", fg="#dbcb86", width=30, command=testi)
    tesimo_mygtukas.pack()



def rodyti_tesimo_mygtuka():
    def testi():
        keisti_scena("AfterWaiting")

    tesimo_mygtukas = tk.Button(mygtukai, text="Continue", bg="#b39a2d", fg="#dbcb86", width=30, command=testi)
    tesimo_mygtukas.pack()


def start():
    global root, teksto_laukas, mygtukai, inventory_label, equipment_label

    root = tk.Tk()
    root.title("~★~ Forest of Fate Chapter 1~★~")
    root.geometry("700x550")
    root.configure(bg='#4a5441')

    teksto_laukas = tk.Label(root, bg='#4a5441', fg="#9db378", wraplength=600)
    teksto_laukas.pack(pady=20)

    mygtukai = tk.Frame(root, bg='#4a5441')  
    mygtukai.pack()

    equipment_label = tk.Label(root, text="Equipment: ", bg='#4a5441', fg="#9db378")
    equipment_label.pack(side="bottom", pady=5)  

    inventory_label = tk.Label(root, text="Inventory: ", bg='#4a5441', fg="#9db378")
    inventory_label.pack(side="bottom", pady=5)  

    rodyti_scena() 

    root.mainloop()




if __name__ == "__main__":
    start()
