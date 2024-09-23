from kivy.app import App
from kivy.lang import Builder

# Load the kv file
Builder.load_file('box_layout.kv')

class BoxLayoutDemoApp(App):
    def handle_greet(self):
        # Get the name from the text input and update the label
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        # Clear the text input and the label
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

if __name__ == '__main__':
    BoxLayoutDemoApp().run()