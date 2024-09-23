"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""
from kivy.app import App
from kivy.lang import Builder

# Load the kv file
Builder.load_file('squaring.kv')

class SquaringApp(App):
    def square_number(self):
        try:
            number = float(self.root.ids.input_number.text)
            result = number ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Please enter a valid number."

if __name__ == '__main__':
    SquaringApp().run()
