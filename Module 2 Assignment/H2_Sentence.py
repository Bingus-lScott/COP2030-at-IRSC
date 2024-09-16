# Homework 2: Sentence Generator
# Program By: Landon Scott
# File Name: H2_Sentence.py
# Function: This program will generate a random sentence

import random

# The only 2 Engish Articles
articles = ("A", "THE")
# 3 Nouns for the random sentence generator
nouns = ("GUY", "GUEST","GIRL")
# 3 Verbs for the random sentence generator
verbs = ("RAN OVER", "ATE", "STOLE FROM")
# 3 Prepositions for the random sentence generator
prepositions = ("BY", "WITH", "AT")

# Get 3 noun phrases for use in the sentence
noun_Phrase1 = random.choice(articles) + " " + random.choice(nouns) + " "
noun_Phrase2 = random.choice(articles) + " " + random.choice(nouns) + " "
noun_Phrase3 = random.choice(articles) + " " + random.choice(nouns) + " "

# Make the verb phrase for the sentence
preposition_Phrase = random.choice(prepositions) + " " + noun_Phrase3 + " "
verb_Phrase = random.choice(verbs) + " " + noun_Phrase2 + preposition_Phrase + " "

# Combine the noun and verb phrase
sentence = noun_Phrase1 + verb_Phrase

# print out the randomly generated sentence
print(sentence)