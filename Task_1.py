
import ipywidgets as widgets
from IPython.display import display

def convert_temperature(initial_temp, temp_value):
    try:
        if initial_temp == "Celsius":
            celsius = temp_value
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
        elif initial_temp == "Fahrenheit":
            fahrenheit = temp_value
            celsius = (fahrenheit - 32) * 5/9
            kelvin = (fahrenheit - 32) * 5/9 + 273.15
        elif initial_temp == "Kelvin":
            kelvin = temp_value
            celsius = kelvin - 273.15
            fahrenheit = (kelvin - 273.15) * 9/5 + 32

        fahrenheit_label.value = f"{fahrenheit:.2f} °F"
        celsius_label.value = f"{celsius:.2f} °C"
        kelvin_label.value = f"{kelvin:.2f} K"
    except ValueError:
        fahrenheit_label.value = "Invalid input"
        celsius_label.value = "Invalid input"
        kelvin_label.value = "Invalid input"

# Initial Temperature Unit Dropdown
initial_temp_dropdown = widgets.Dropdown(
    options=["Celsius", "Fahrenheit", "Kelvin"],
    value="Celsius",
    description="Initial Temp Unit:"
)
display(initial_temp_dropdown)

# Temperature Value Entry
temp_value = widgets.FloatText(description="Temperature:")
display(temp_value)

# Fahrenheit Result
fahrenheit_label = widgets.Label(value="")
display(fahrenheit_label)

# Celsius Result
celsius_label = widgets.Label(value="")
display(celsius_label)

# Kelvin Result
kelvin_label = widgets.Label(value="")
display(kelvin_label)

# Convert Button
convert_button = widgets.Button(description="Convert")
display(convert_button)

def on_convert_button_clicked(b):
    convert_temperature(initial_temp_dropdown.value, temp_value.value)

convert_button.on_click(on_convert_button_clicked)
