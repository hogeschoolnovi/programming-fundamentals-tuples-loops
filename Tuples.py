
steden = ("Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Eindhoven", "Groningen")
# Loop door de tuple en print elk element afzonderlijk

# --------------------------------------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combineer de twee tuples tot één nieuwe tuple


# --------------------------------------------------------------------------------------------


# Definieer een tuple met verschillende soorten gegevens (bijvoorbeeld getallen, strings, booleans, etc.)
mijn_tuple = (10, 20, 30, 40, "a", "b", "c", "d", True, False, None, 3.14)

# Print enkele elementen van de tuple namelijk het eerste, een subset (vanaf index 2 tot index 5) en het laatste element
print(mijn_tuple[0])  # Print het eerste element
print(mijn_tuple[2:5])  # Print een subset van de tuple
print(mijn_tuple[-1])  # Print het laatste element

# --------------------------------------------------------------------------------------------


# Maak een tuple met een naam en een leeftijd
persoon_tuple = ("Karel", 30)

# Pak de gegevens uit de tuple en sla ze op in afzonderlijke variabelen (Wat gebeurt er als je de variabelen in de verkeerde volgorde definieert?)
naam, leeftijd = persoon_tuple

# Print de uitgepakte variabelen
print("Naam:", naam)
print("Leeftijd:", leeftijd)
