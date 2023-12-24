import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        # Variables
        self.from_unit_var = tk.StringVar()
        self.to_unit_var = tk.StringVar()
        self.temperature_var = tk.DoubleVar()
        self.result_var = tk.StringVar()

        # GUI elements
        label_from = tk.Label(root, text="From:",font=("Arial",12))
        label_from.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.from_unit_combobox = ttk.Combobox(root, textvariable=self.from_unit_var, values=["Fahrenheit", "Celsius"],font=("Arial",12))
        self.from_unit_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.from_unit_combobox.current(0)

        label_to = tk.Label(root, text="To:",font=("Arial",12))
        label_to.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.to_unit_combobox = ttk.Combobox(root, textvariable=self.to_unit_var, values=["Fahrenheit", "Celsius"],font=("Arial",12))
        self.to_unit_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.to_unit_combobox.current(1)

        label_temperature = tk.Label(root, text="Temperature:",font=("Arial",12))
        label_temperature.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.temperature_entry = tk.Entry(root, textvariable=self.temperature_var,font=("Arial",12))
        self.temperature_entry.grid(row=2, column=1, padx=10, pady=10)

        convert_button = tk.Button(root, text="Convert", command=self.convert_temperature, font=("Arial",12))
        convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        result_label = tk.Label(root, textvariable=self.result_var, font=("Helvetica", 14, "bold"))
        result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def convert_temperature(self):
        try:
            temperature = self.temperature_var.get()
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()

            if from_unit == to_unit:
                result = f"The temperature is already in {to_unit}."
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = f"{temperature:.2f} °F is {(temperature - 32) * 5/9:.2f} °C."
            elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = f"{temperature:.2f} °C is {(temperature * 9/5) + 32:.2f} °F."
            else:
                result = "Invalid conversion units."

            self.result_var.set(result)

        except ValueError:
            self.result_var.set("Invalid temperature value.")

def main():
    root = tk.Tk()
    root.geometry('400x300+600+200')
    root.resizable(False, False)
    app = TemperatureConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
