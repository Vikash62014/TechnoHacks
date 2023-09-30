import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Currency codes
        self.currency_codes = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "INR"]

        # Variables
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.result_var = tk.StringVar()

        # GUI Components
        self.from_currency_label = ttk.Label(root, text="From Currency:")
        self.from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var, values=self.currency_codes)

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_entry = ttk.Entry(root, textvariable=self.amount_var)

        self.to_currency_label = ttk.Label(root, text="To Currency:")
        self.to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var, values=self.currency_codes)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_currency)

        self.result_label = ttk.Label(root, text="Result:")
        self.result_entry = ttk.Entry(root, textvariable=self.result_var, state="readonly")

        # Grid layout
        self.from_currency_label.grid(row=0, column=0, padx=10, pady=10)
        self.from_currency_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.amount_label.grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10)
        self.to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=4, column=0, padx=10, pady=10)
        self.result_entry.grid(row=4, column=1, padx=10, pady=10)

    def convert_currency(self):
        try:
            # Get user inputs
            amount = self.amount_var.get()
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            # Perform currency conversion
            c = CurrencyRates()

            if from_currency == "INR":
                # Convert from INR to the selected currency
                rate = c.get_rate("USD", to_currency)
                result = round(amount / rate, 2)
            elif to_currency == "INR":
                # Convert to INR from the selected currency
                rate = c.get_rate("USD", from_currency)
                result = round(amount * rate, 2)
            else:
                # Convert between two non-INR currencies
                rate = c.get_rate(from_currency, to_currency)
                result = round(amount * rate, 2)

            # Update result entry
            self.result_var.set(result)
        except Exception as e:
            # Handle exceptions (e.g., invalid input)
            self.result_var.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()
