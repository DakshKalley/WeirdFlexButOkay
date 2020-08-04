import random

# Synonym lists for each word
weirdSynonyms = ["weird", "odd", "bizarre", "eccentric", "funky", "kooky", "peculiar", "strange", "queer", "oddball", "uncanny", "outlandish"]
flexSynonyms = ["flex", "boast", "brag", "braggadocio", "exaggeration", "vaunt", "grandiloquence"]
butSynonyms = ["but", "yet"]
okaySynonyms = ["okay", "acceptable", "satisfactory", "alright", "approved", "correct", "fair", "fine", "permitted", "accurate", "adequate", "convenient", "passable", "tolerable", "let's toast", "👌", "🆗"]

# Generate the different phrase
wS = random.choice(weirdSynonyms)
fS = random.choice(flexSynonyms)
bS = random.choice(butSynonyms)
oS = random.choice(okaySynonyms)

# Print out the combined phrase
print(wS + " " + fS + " " + bS + " " + oS)