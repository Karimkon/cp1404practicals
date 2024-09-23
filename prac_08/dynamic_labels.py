from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        Builder.load_file('dynamic_labels.kv')
        layout = self.root.ids.main
        names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]  # Sample list of names

        for name in names:
            label = Label(text=name)
            layout.add_widget(label)  # Add each label to the layout

        return layout

if __name__ == '__main__':
    DynamicLabelsApp().run()
