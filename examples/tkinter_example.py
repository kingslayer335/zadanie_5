import tkinter as tk
from tkinter import ttk
from currencyList import CurrencyList
import requests
# instacja klasy CurrencyList wywolujaca api przy pomocy podanego url
currency_list = CurrencyList("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json")

# wyjsciowe waluty
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
        result_label.config(text=f"1 {from_currency.upper()} = {value:.8f} {to_currency.upper()}")
        result_label2.config(text=f"{amount} {from_currency.upper()} = {result:.8f} {to_currency.upper()}")
    except Exception as e:
        result_label.config(text="Error fetching conversion.")
        result_label2.config(text=str(e))

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
    button.config(relief="sunken")
    button.after(100, lambda: button.config(relief="raised"))
    button.after(100, command)

root = tk.Tk()
root.title("Currency Converter")
root.geometry("800x500")


left_frame = tk.Frame(root, width=200)
center_frame = tk.Frame(root)
right_frame = tk.Frame(root, width=200)

left_frame.pack(side="left", fill="y", padx=10, pady=10)
center_frame.pack(side="left", expand=True, fill="both")
right_frame.pack(side="right", fill="y", padx=10, pady=10)

    
# Popularne kryptowaluty
tk.Label(left_frame, text="Popular Cryptocurrencies", font=("Arial", 12, "bold")).pack(pady=5)
for crypto in ["btc", "eth", "sol", "xrp"]:
    btn = tk.Button(left_frame, text=crypto.upper(), width=10)
    btn.pack(pady=2)
    btn.bind("<Button-1>", lambda e, c=crypto: set_from_currency(c))  # Left-click
    btn.bind("<Button-3>", lambda e, b=btn, c=crypto: simulate_right_click(b, lambda: set_to_currency(c))) # Right-click

tk.Label(left_frame, text="Left click -> upper currency\nRight click -> lower currency", font=("Arial", 10, "bold")).pack(pady=5)

# Popularne waluty
tk.Label(right_frame, text="Popular Currencies", font=("Arial", 12, "bold")).pack(pady=5)

for curr in ["eur", "usd", "pln", "gbp"]:
    btn = tk.Button(right_frame, text=curr.upper(), width=10)
    btn.pack(pady=2)
    
    # Correct lambda binding: capture btn and curr as default args
    btn.bind("<Button-1>", lambda e, c=curr: set_from_currency(c))
    btn.bind("<Button-3>", lambda e, b=btn, c=curr: simulate_right_click(b, lambda: set_to_currency(c)))


from_var = tk.StringVar(value=euro)
to_var = tk.StringVar(value=pln)
amount_var = tk.StringVar(value="1")

ttk.Label(center_frame, text="From:").pack(pady=5)
ttk.Combobox(center_frame, textvariable=from_var, values=currency_list.get_pairs(), state="readonly").pack()

ttk.Label(center_frame, text="To:").pack(pady=5)
ttk.Combobox(center_frame, textvariable=to_var, values=currency_list.get_pairs(), state="readonly").pack()

ttk.Label(center_frame, text="Amount:").pack(pady=5)
tk.Entry(center_frame, textvariable=amount_var).pack()

# przycisk reverse
tk.Button(center_frame, text="Reverse", command=reverse_currencies).pack(pady=5)

# przycisk konwersji
tk.Button(center_frame, text="Convert", command=currency_exchange).pack(pady=10)

# rezultaty
result_label = tk.Label(center_frame, text="", font=("Arial", 12))
result_label.pack()

result_label2 = tk.Label(center_frame, text="", font=("Arial", 12))
result_label2.pack()

root.mainloop()


if __name__ == "__main__":
    currency_exchange()