# interface

print ("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷")
print ('Welcome to The Alchemist’s Trial...')
print ()
print ('Please make sure that you are fully ready for this adventure {¬ºཀ°}¬')
readiness = input("Are you ready? (yes/no)").lower()
print()
if readiness == "yes":
    print ("You are a lone adventurer skilled in the art of potion-making. ")
    print("One night, you arrive at the gates of a long-abandoned castle.")
else:
    print ("You coward! You have to be ready.")
    print ("You will still have to continue play this game, so better be ready by now.")
print()

username = input('Before we start, please enter your nickname:')
print (f'Hello {username}... (㇏(•̀ᢍ•́)ノ)')
print ("Please make sure to understand the gameflow, or else... (っ҂ཀ•)っ")

#opening story

print("⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘")
print()
print("Legends speak of a hidden treasure sealed deep within an abandoned castle. Drawn by curiosity — and greed — you step inside, only to discover that the castle is far from empty.")
print()
print("The castle consists of three dangerous floors, each protected by its own obstacles and guardians.")
print()
print("To reach the treasure chest at the top, you must survive every floor — using your knowledge of potion-making to overcome what lies ahead.")
print()
print("Only those who brew wisely will leave the castle alive.")
print("⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘")
print()
print("Level 1: First Floor ִֶָ𓂃 ࣪˖𓉸ִֶָྀི ִֶָ་༘࿐")
print()
print("The air grows damp and heavy as you step into the lower halls.")
print("Something lurks in the shadows, and a wrong move could be fatal.")
print('A faceless ghost appears in front of you (but this is a weak one)') 
print("In order to pass this level, you have to create a basic potion using ONLY the BASE ingredients that will be given below:")

#ingredients list

ingredients = {
    "nightshade berry": "base",
    "moon dew": "base",
    "ashroot": "base",
    "dragon scale dust": "rare",
    "venom fang": "rare"
}

# ingredient input
item1 = input("Enter first ingredient: ").lower()
item2 = input("Enter second ingredient: ").lower()
 
type1 = ingredients.get(item1)
type2 = ingredients.get(item2)

# potion name
if {item1,item2} == {"nightshade berry","dragon scale dust"}:
    print("Name: Drakeshadow Toxin")
elif {item1,item2} == {"nightshade berry","venom fang"}:
    print("Name: Assassin’s Bloom")
elif {item1,item2} == {"nightshade berry","moon dew"}:
    print("Name: Lunar Venom Elixir")
elif {item1,item2} == {"nightshade berry","ashroot"}:
    print("Name: Elixir of Withering Shadows")
elif {item1,item2} == {"moon dew","ashroot"}:
    print("Name: Mist of Ancient Roots")
elif {item1,item2} == {"moon dew","dragon scale dust"}:
    print("Name: Celestial Scale Draught")
elif {item1,item2} == {"moon dew","venom fang"}:
    print("Name: Moonbite Serum")
elif {item1,item2} == {"ashroot","dragon scale dust"}:
    print("Name: Emberhide Tonic")
elif {item1,item2} == {"ashroot","venom fang"}:
    print("Name: Gravefang Brew")
elif {item1,item2} == {"ashroot","dragon scale dust"}:
    print("Name: Wyrmfang Concoction")

# potion strength
if {type1,type2} == {'base','base'}:
    print("Strength: Weak Poison")
elif {type1,type2} == {'base','rare'}:
    print("Strength: Strong Poison")
elif {type1,type2} == {'rare','rare'}:
    print("Strength: Unstable Poison")
else:
    print("Invalid ingredients")


