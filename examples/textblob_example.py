from textblob import TextBlob

# Przykładowy tekst
text = "Python is an amazing programming language. However, sometimes it can be a bit confusing for beginners."

# Tworzenie obiektu TextBlob
blob = TextBlob(text)

# Analiza sentymentu
print("Analiza sentymentu:")
print(f"Polaryzacja: {blob.sentiment.polarity}")
print(f"Subiektywność: {blob.sentiment.subjectivity}")

# Tłumaczenie (jeśli masz połączenie z internetem)
# print("\nTłumaczenie na francuski:")
# print(blob.translate(to='fr'))

# Tokenizacja
print("\nTokeny:")
print(blob.words)

# Części mowy
print("\nCzęści mowy:")
print(blob.tags)
