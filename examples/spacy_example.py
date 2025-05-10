import spacy

# Załaduj model językowy
nlp = spacy.load("en_core_web_sm")

# Przykładowy tekst
text = "Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University."

# Przetwarzanie tekstu
doc = nlp(text)

# Tokenizacja i części mowy
print("Tokeny i części mowy:")
for token in doc:
    print(f"{token.text:<15} {token.pos_}")

# Rozpoznawanie nazwanych encji
print("\nNazwane jednostki (NER):")
for ent in doc.ents:
    print(f"{ent.text:<30} {ent.label_}")
