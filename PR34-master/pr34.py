from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_file('calc.kv')
Window.size = (350, 550)

class CalculatorWidget(Widget):
    # Clear the screen
    def clear(self):
        self.ids.input_box.text = "0"

    # Remove the last character
    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    # Getting the button value
    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if "wrong equation" in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"

        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    # Getting the sings
    def sings(self, sing):
        prev_number: str = self.ids.input_box.text
        proverka = prev_number[len(prev_number)-1:]
        if proverka == '+' or proverka == '-' or proverka == '*' or proverka == '/':
            pass
        else:
            if sing != '%':
                self.ids.input_box.text = f"{prev_number}{sing}"
            else:
                if ("+" in prev_number or "-" in prev_number or "*" in prev_number or "/" in prev_number or "%" in prev_number):
                    num_list = re.split("\+|\*|-|/|%", prev_number)
                    if len(num_list) == 2:
                        res_old = prev_number[:-len(num_list[1])]
                        simvol = res_old[len(res_old)-1:]
                        if simvol == '+' or simvol == '-':
                            result = float(num_list[0]) * (float(num_list[1])/100)
                        else:
                            result = float(num_list[1])/100
                        #prev_number.replace(f'{num_list[1]}', '' )
                        self.ids.input_box.text = f"{res_old}{result}"
                    elif len(num_list)>2:
                        string = prev_number[:-len(num_list[-1])]
                        simvol = string[len(string)-1:]
                        if simvol == '+' or simvol == '-':
                            result_number = eval(string[:-1])
                            result = float(result_number) * (float(num_list[-1])/100)
                        else:
                            result = float(num_list[-1])/100
                        self.ids.input_box.text = f"{string}{result}"
                else:
                    result = float(prev_number)/100
                    self.ids.input_box.text = str(result)

    # Getting decimal value
    def dot(self):
        prev_number = self.ids.input_box.text
        num_list = re.split("\+|\*|-|/|%", prev_number)


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
            result = eval(prev_number)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "wrong equation"

    # Positive to negative
    def positive_negative(self):
        prev_number = self.ids.input_box.text
        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{prev_number}"


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()