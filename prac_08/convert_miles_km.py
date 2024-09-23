from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

# Constants for conversion
MILES_TO_KM_CONVERSION = 1.60934

class MilesToKmConverterApp(App):
    output_km = StringProperty("0.0")  # StringProperty for output

    def build(self):
        Builder.load_file('convert_miles_km.kv')
        return self

    def convert_miles_to_km(self, miles):
        try:
            miles = float(miles)
            self.output_km = str(miles * MILES_TO_KM_CONVERSION)  # Calculate and update
        except ValueError:
            self.output_km = "0.0"  # Handle invalid input

    def increment_miles(self, increment):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0  # Default to 0 if invalid
        miles += increment
        self.root.ids.input_miles.text = str(int(miles))  # Update the input field
        self.convert_miles_to_km(miles)

if __name__ == '__main__':
    MilesToKmConverterApp().run()
