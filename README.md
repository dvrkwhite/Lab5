# Lab5: Przetwarzanie języka naturalnego w Pythonie

## Opis projektu

Repozytorium zawiera demonstracyjne przykłady użycia dwóch popularnych bibliotek do przetwarzania języka naturalnego (NLP) w języku Python:
- **spaCy** – wydajna, zaawansowana biblioteka NLP
- **TextBlob** – łatwa w użyciu, idealna dla początkujących

Projekt zrealizowany w ramach Laboratorium 5: "Poszukiwanie bibliotek o określonej funkcjonalności".

## Struktura katalogów

```
NLP-Lab5/
├── examples/           # Przykładowe skrypty z użyciem bibliotek
│   ├── spacy_example.py
│   └── textblob_example.py
├── raport.md           # Raport opisujący biblioteki
└── README.md           # Niniejszy plik
```

## Jak uruchomić

### Wymagania:
- Python 3.7+
- pip

### Instalacja:

```bash
pip install spacy textblob
python -m textblob.download_corpora
python -m spacy download en_core_web_sm
```

### Uruchomienie przykładów:
```bash
python examples/spacy_example.py
python examples/textblob_example.py
```

## Autor
Wykonano na potrzeby ćwiczeń z programowania w języku Python.

## Licencja
Ten projekt dostępny jest na licencji MIT.
