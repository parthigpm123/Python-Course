import platform
import re
from kivy.config import Config

# On Android: fullscreen, On Windows: fixed size
if platform.system() == "Windows":
    from kivy.core.window import Window
    Window.size = (350, 550)
else:
    Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("calculator.kv")


class CalculatorWidget(Widget):
    # Clear the screen
    def clear(self):
        self.ids.input_box.text = "0"

    # Remove the last character
    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        if prev_number == "":
            prev_number = "0"
        self.ids.input_box.text = prev_number

    # Getting the button value
    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if "wrong equation" in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    # Getting the signs
    def signs(self, sign):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{sign}"

    # Getting decimal value
    def dot(self):
        prev_number = self.ids.input_box.text
        num_list = re.split(r"\+|\*|-|/|%", prev_number)

        if ("+" in prev_number or "-" in prev_number or "*" in prev_number or "/" in prev_number or "%" in prev_number) and "." not in num_list[-1]:
            prev_number = f"{prev_number}."
            self.ids.input_box.text = prev_number

        elif '.' in prev_number:
            pass
        else:
            prev_number = f'{prev_number}.'
            self.ids.input_box.text = prev_number

    # Calculate the result
    def results(self):
        prev_number = self.ids.input_box.text
        try:
            result = eval(prev_number)  # ⚠️ could be replaced with safer eval later
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "wrong equation"

    # Positive to negative toggle
    def positive_negative(self):
        prev_number = self.ids.input_box.text
        if prev_number.startswith("-"):
            self.ids.input_box.text = prev_number[1:]
        else:
            self.ids.input_box.text = f"-{prev_number}"


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
