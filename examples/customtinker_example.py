import customtkinter as ctk
from currencyList import CurrencyList
import requests

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# instacja klasy CurrencyList wywolujaca api przy pomocy podanego url
currency_list = CurrencyList("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json")

euro = currency_list.get_currency_code("euro")
pln = currency_list.get_currency_code("polish zloty")
# funkcja dajaca konwersje wszystkich walut dla danej waluty u gory, czyli "from_currency"
def currency_exchange():
    from_currency = from_var.get().split(":")[0].strip().lower()
    to_currency = to_var.get().split(":")[0].strip().lower()
    amount = amount_var.get()

    try:
        response = requests.get(
            f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency}.json"
        )
        data = response.json()
        value = data[from_currency][to_currency]

        result = float(value) * float(amount)
        result_label.configure(text=f"1 {from_currency.upper()} = {value} {to_currency.upper()}")
        result_label2.configure(text=f"{amount} {from_currency.upper()} = {result} {to_currency.upper()}")
    except Exception as e:
        result_label.configure(text="Error fetching conversion.")
        result_label2.configure(text=str(e))

# funkcja pozwalajaca na ustawienie waluty u gory 
def set_from_currency(code):
    for pair in currency_list.get_pairs():
        if pair.lower().startswith(code):
            from_var.set(pair)
            break
# funkcja pozwalajaca na ustawienie waluty na dole

def set_to_currency(code):
    for pair in currency_list.get_pairs():
        if pair.lower().startswith(code):
            to_var.set(pair)
            break

# funkcja pozwalajaca na przestawienie walut 
def reverse_currencies():
    from_value = from_var.get()
    to_value = to_var.get()
    from_var.set(to_value)
    to_var.set(from_value)

# funkcja dajaca animacje klikniecia prawym przyciskiem bo standardowo nie bylo takiej animacji
def simulate_right_click(button, command):
    button.configure(state="disabled")
    button.after(100, lambda: button.configure(state="normal"))
    button.after(100, command)

root = ctk.CTk()
root.title("Currency Converter")
root.geometry("800x500")

left_frame = ctk.CTkFrame(root, width=200)
center_frame = ctk.CTkFrame(root)
right_frame = ctk.CTkFrame(root, width=200)

left_frame.pack(side="left", fill="y", padx=10, pady=10)
center_frame.pack(side="left", expand=True, fill="both")
right_frame.pack(side="right", fill="y", padx=10, pady=10)
# Popularne kryptowaluty
ctk.CTkLabel(left_frame, text="Popular Cryptocurrencies", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
for crypto in ["btc", "eth", "sol", "xrp"]:
    btn = ctk.CTkButton(left_frame, text=crypto.upper(), width=120)
    btn.pack(pady=2)
    btn.bind("<Button-1>", lambda e, c=crypto: set_from_currency(c))
    btn.bind("<Button-3>", lambda e, b=btn, c=crypto: simulate_right_click(b, lambda: set_to_currency(c)))

ctk.CTkLabel(left_frame, text="Left click -> upper currency\nRight click -> lower currency", font=ctk.CTkFont(size=10, weight="bold")).pack(pady=5)

# Popularne waluty
ctk.CTkLabel(right_frame, text="Popular Currencies", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
for curr in ["eur", "usd", "pln", "gbp"]:
    btn = ctk.CTkButton(right_frame, text=curr.upper(), width=120)
    btn.pack(pady=2)
    btn.bind("<Button-1>", lambda e, c=curr: set_from_currency(c))
    btn.bind("<Button-3>", lambda e, b=btn, c=curr: simulate_right_click(b, lambda: set_to_currency(c)))

from_var = ctk.StringVar(value=euro)
to_var = ctk.StringVar(value=pln)
amount_var = ctk.StringVar(value="1")

ctk.CTkLabel(center_frame, text="From:").pack(pady=5)
ctk.CTkComboBox(center_frame, variable=from_var, values=currency_list.get_pairs(), width=300).pack()

ctk.CTkLabel(center_frame, text="To:").pack(pady=5)
ctk.CTkComboBox(center_frame, variable=to_var, values=currency_list.get_pairs(), width=300).pack()

ctk.CTkLabel(center_frame, text="Amount:").pack(pady=5)
ctk.CTkEntry(center_frame, textvariable=amount_var).pack()
# przycisk reverse
ctk.CTkButton(center_frame, text="Reverse", command=reverse_currencies).pack(pady=5)
# przycisk konwersji
ctk.CTkButton(center_frame, text="Convert", command=currency_exchange).pack(pady=10)
# rezultaty

result_label = ctk.CTkLabel(center_frame, text="", font=ctk.CTkFont(size=12))
result_label.pack()

result_label2 = ctk.CTkLabel(center_frame, text="", font=ctk.CTkFont(size=12))
result_label2.pack()

root.mainloop()
