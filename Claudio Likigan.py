lbs = 250
kg =  lbs/2.205
kg = round(kg,2)
lbs = str(lbs)
kg = str(kg)
print("Weight in Pounds (lbs) = " + lbs)
print("Weight converted to Kilogram (kg) = " + kg)

print("==================================")

mi = 25
km = mi*1.609
km = round(km,2)
mi = str(mi)
km = str(km)
print("Length in Miles (mi) " + mi)
print("Length in Kilometer (km) " + km)

print("==================================")

Fahrenheit = 50000
Celsius = (5/9)*(Fahrenheit - 32)
Fahrenheit = str(Fahrenheit)
Celsius = round(Celsius)
Celsius = str(Celsius)
print("Temperature to Fahrenheit (°F)" + Fahrenheit)
print("Temperature to Celsius (°C)" + Celsius)

print("==================================")

print("2. Student Ages:")
Student1 = "18"
Student2 = "20"
Student3 = "21"
Student4 = "19"
Student5 = "18"
Student6 = "25"
Student7 = "18"
Student8 = "19"
Student9 = "24"
Student10 = "23"
average = "20.5"

print("Age of Student 1: " + Student1)
print("Age of Student 2: " + Student2)
print("Age of Student 3: " + Student3)
print("Age of Student 4: " + Student4)
print("Age of Student 5: " + Student5)
print("Age of Student 6: " + Student6)
print("Age of Student 7: " + Student7)
print("Age of Student 8: " + Student8)
print("Age of Student 9: " + Student9)
print("Age of Student 10: " + Student10)
print("The average age of the students is: " + average)

print("==================================")

character1 = "Hellion"
character2 = "Arkin"
character3 = "Zen"
character4 = "Zhene"
character5 = "Ryou"

equipment1 = "<Enchanted sword>"
equipment2 = "<Enhcanted Bow>"
equipment3 = "<Gondr's Staff>"
equipment4 = "<Dorans Ring>"
equipment5 =  "<Dorans Spear"

item1 = "Amulet of Power"
item2 = "Elixir of Immortality"
item3 = "Phoenix Feather"
item4 = "Sorcerer's Tome"
item5 = "Gem of Invisibility"

ability1 = "Fire Manipulation"
ability2 = "Telekinesis"
ability3 = "Ice Magic"
ability4 = "Healing Touch"
ability5 = "Time Manipulation"

monster = "dragon"

story = f"""
Once upon a time in a mystical land, there lived five brave adventurers:
1. {character1}, wielding an {equipment1}, 
2. {character2}, carrying a mysterious {item1},
3. {character3}, with the incredible ability of {ability1},
4. {character4}, known for her agility and grace,
5. {character5}, on a quest to defeat the fearsome {monster}.

In the mystical land of Eldoria, five brave adventurers known as {character1}, {character2}, {character3}, {character4}, and {character5} embarked on an epic quest. Each possessed a unique ability and wielded a legendary piece of equipment.

{character1}, with the power of {ability1}, carried the mighty {equipment1}, a sword said to have been forged by the gods themselves. {character2}, the archer of the group, used her {equipment2}, the enchanted {item2} hanging around her neck, granting her immortality.

{character3}, a wise mage, harnessed the ancient arts of {ability3} using his {equipment3}, the {item3}-tipped staff. {character4}, the healer, wore the resilient {equipment4} and had the gift of {ability4}, capable of mending wounds with a simple touch.

And lastly, {character5}, the enigmatic rogue, donned the {equipment5}, a cloak that granted him the power of {ability5}, allowing him to manipulate time itself. Together, they ventured into the unknown, seeking to vanquish the dark forces threatening Eldoria and protect the realm from eternal darkness.
"""
print(story)
