import pandas as pd
df = pd.read_csv('dane.csv')


kolumna = input("Podaj nazwę kolumny do sortowania (imię/wiek/wzrost): ")

while kolumna not in ['imię', 'wiek', 'wzrost']:
    kolumna = input("Nieprawidłowa nazwa kolumny. Podaj nazwę kolumny do sortowania: ")

kierunek = input("Podaj kierunek sortowania (rosnąco/malejąco): ")

while kierunek not in ['rosnąco', 'malejąco']:
    kierunek = input("Nieprawidłowy kierunek sortowania. Wybierz 'rosnąco' lub 'malejąco': ")


if kierunek == 'rosnąco':
    print(df.sort_values(by=kolumna, ascending=True))
else:
    print(df.sort_values(by=kolumna, ascending=False))