# link do githuba: https://github.com/kingslayer335/zadanie_5
## Autor

Imię i nazwisko: Piotr Artym  
Nr albumu: 122212

## Projekt: Przegląd bibliotek GUI w Pythonie

W ramach laboratorium nr 5 zainteresowalem sie tworzeniem graficznych interfejsow uzytkownika (GUI).  
Biblioteki GUI są szczególnie przydatne przy tworzeniu aplikacji okienkowych, umożliwiających interakcję użytkownika z programem bez użycia terminala.  
Na potrzeby tego zadania przygotowalem aplikacje do konwersji walut w jezyku Python.  
API do konwersji walut oraz pobierania kursów zostało zaczerpnięte z GitHuba: https://github.com/fawazahmed0/exchange-api  
Uzylem dwoch bibliotek do stworzenia GUI, ktore maja prawie identyczny syntax ale mimo to roznice w wygladzie mozna zauwazyc golym okiem.  

- `tkinter` – standardowa biblioteka GUI w Pythonie
- `customtkinter` – nowoczesna nakładka na `tkinter`, umożliwiająca tworzenie estetycznych i responsywnych interfejsów

W folderze `examples/` znajduja sie dwa programy do wymiany walut obie wykorzystujace po jednej z tych bibliotek.

## Struktura repozytorium

```
├── examples
│   ├── tkinter_example.py   # Wykorzystuje biblioteke tkinter
│   ├── customtinker_example.py        # wykorzystuje biblioteke CustomKinter
|   └── currencyList.py                        # ta klasa wykonuje API Call, zwraca liste z danymi walut
├── raport.md                                           # Raport opisujący biblioteki

```

## Opis bibliotek

### 1. Biblioteka `tkinter`

**Przeznaczenie:**

tkinter to standardowa biblioteka GUI dostępna we wszystkich instalacjach Pythona. Umożliwia tworzenie okien, przycisków, pól tekstowych i innych podstawowych komponentów GUI.

**Przykład użycia:**

# ![image](https://github.com/user-attachments/assets/e40d3ff8-ef10-4ceb-ab8c-631ab0e6ebaa)

**Zalety:**
- Wbudowana w Pythona (brak potrzeby instalacji)
- Dobrze udokumentowana
- Odpowiednia do prostych aplikacji

**Wady:**
- Przestarzały wygląd
- Brak natywnego wsparcia dla ciemnego motywu

**Wersja:**

Programy dzialaja na wersji pythona
```bash
python 3.13.2
```

**Instalacja:**
```bash
-do dzialania api potrzebna jest biblioteka requests

pip install requests

```

**Dokumentacja:**
https://docs.python.org/3/library/tkinter.html

### 2. Biblioteka `customtkinter`

**Przeznaczenie:**

customtkinter to nowoczesna biblioteka oparta na tkinter, która umożliwia tworzenie atrakcyjnych interfejsów użytkownika, wspierających motywy (jasny/ciemny) i styl zgodny z nowoczesnymi trendami.

**Przykład użycia:**

# ![image](https://github.com/user-attachments/assets/454b3586-6afd-4ccf-adfc-d4414c2e1246)

**Zalety:**
- Nowoczesny wygląd
- Tryb ciemny i jasny
- Łatwość użycia (interfejs podobny do tkinter)

**Wady:**
- Wymaga instalacji zewnętrznej biblioteki
- Mniej popularna niż tkinter

**Instalacja:**
```bash
pip install requests

pip install customtkinter

-jeżeli nie działa można spròbować

pip install customtkinter --upgrade

-lub

python3 -m pip install --upgrade customtkinter

```

**Dokumentacja:**
https://github.com/TomSchimansky/CustomTkinter


