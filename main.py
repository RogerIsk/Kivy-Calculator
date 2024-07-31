from kivy.app import App  # libraries and dependencies
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

Window.size = (500, 700)  # this sets the size of the window

kv = '''
<Button>
    font_size: 34
    size_hint: (0.25,0.16)
    background_color: "white"

<MyLayout>
    FloatLayout:
        size: root.width, root.height
        orientation: "vertical"

        TextInput:
            id: calc_input
            text: "0"
            halign: "right"
            multiline: True
            font_size: 90
            pos_hint: {"x":0, "top": 1}
            size_hint: (1,0.20)

        Button:
            id: input_one
            on_press: root.press_button(1)
            text: "1"
            pos_hint: {"x":0, "top":0.32}
            background_color: (0.5, 0.5, 0.5, 1)
            
        Button:
            id: input_two
            on_press: root.press_button(2)
            text: "2"
            pos_hint: {"x":0.25, "top":0.32}
            background_color: (0.5, 0.5, 0.5, 1)
            
        Button:
            id: input_three
            on_press: root.press_button(3)
            text: "3"
            pos_hint: {"x":0.5, "top":0.32}
            background_color: (0.5, 0.5, 0.5, 1)
            
        Button:
            id: input_four
            on_press: root.press_button(4)
            text: "4"
            pos_hint: {"x":0, "top":0.48}
            background_color: (0.5, 0.5, 0.5, 1)
            
        Button:
            id: input_five
            on_press: root.press_button(5)
            text: "5"
            pos_hint: {"x":0.25, "top":0.48}
            background_color: (0.5, 0.5, 0.5, 1)

        Button:
            id: input_six
            on_press: root.press_button(6)
            text: "6"
            pos_hint: {"x":0.5, "top":0.48}
            background_color: (0.5, 0.5, 0.5, 1)
            
        Button:
            id: input_seven
            on_press: root.press_button(7)
            text: "7"
            pos_hint: {"x":0, "top":0.64}
            background_color: (0.5, 0.5, 0.5, 1)
            
        Button:
            id: input_eight
            on_press: root.press_button(8)
            text: "8"
            pos_hint: {"x":0.25, "top":0.64}
            background_color: (0.5, 0.5, 0.5, 1)
            
        Button:
            id: input_nine
            text: "9"
            pos_hint: {"x":0.5, "top":0.64}
            background_color: (0.5, 0.5, 0.5, 1)
            on_press: root.press_button(9)
            
        Button:
            id: input_zero
            on_press: root.press_button(0)
            text: "0"
            pos_hint: {"x":0.25, "top":0.16}
            background_color: (0.5, 0.5, 0.5, 1)
        
        Button:
            id: input_procentage
            text: "%"
            pos_hint: {"x":0, "top":0.80}
            on_press: root.procenate_button()

        Button:
            text: u"\u00AB"
            pos_hint: {"x":0.5, "top":0.80}
            on_press: root.delete_button()
            
        Button:
            id: clear
            text: "C"
            pos_hint: {"x":0.25, "top":0.80}
            on_press: root.clear()
            
        Button:
            id: input_divide
            text: "/"
            pos_hint: {"x":0.75, "top":0.80}
            on_press: root.math_sign("/")
            
        Button:
            id: input_multiply
            text: "*"
            pos_hint: {"x":0.75, "top":0.64}
            on_press: root.math_sign("*")

        Button:
            id: input_minus
            text: "-"
            pos_hint: {"x":0.75, "top":0.48}
            on_press: root.math_sign("-")

        Button:
            id: input_plus
            on_press: root.math_sign("+")
            text: "+"
            pos_hint: {"x":0.75, "top":0.32}

        Button:
            id: input_equals
            text: "="
            pos_hint: {"x":0.75, "top":0.16}
            on_press: root.equals_button()
            background_color: (0.1, 1, 0.1, 1)
            
        Button:
            id: input_dot
            text: "."
            pos_hint: {"x":0.5, "top":0.16}
            background_color: (0.5, 0.5, 0.5, 1)
            on_press: root.dot_button()
            
        Button:
            id: input_plus_minus
            text: "+/-"
            pos_hint: {"x":0, "top":0.16}
            background_color: (0.5, 0.5, 0.5, 1)
            on_press: root.pos_neg()
        
'''

Builder.load_string(kv)


class MyLayout(Widget):
    def adjust_font_size(self):
        text_length = len(self.ids.calc_input.text)
        if text_length > 22:
            self.ids.calc_input.font_size = 30
        elif text_length > 17:
            self.ids.calc_input.font_size = 40
        elif text_length > 9:
            self.ids.calc_input.font_size = 50
        else:
            self.ids.calc_input.font_size = 90

    def wrap_text(self):
        text = self.ids.calc_input.text.replace('\n', '')
        wrapped_text = ""
        
      
        
        wrapped_text += text
    
        # Check if the last line ends exactly at 22 characters
        if len(wrapped_text) > 0 and wrapped_text[-1] == '\n':
            wrapped_text = wrapped_text[:-1]
    
        self.ids.calc_input.text = wrapped_text

    def clear(self):
        self.ids.calc_input.text = '0'
        self.ids.calc_input.font_size = 90

    def press_button(self, button):
        prior = self.ids.calc_input.text

        if "Error" in prior:
            prior = ''

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
        
        self.wrap_text()
        self.adjust_font_size()

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}{sign}"
        self.wrap_text()
        self.adjust_font_size()

    def delete_button(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior
        self.wrap_text()
        self.adjust_font_size()

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = prior.replace("-", "")
        else:
            self.ids.calc_input.text = f'-{prior}'
        self.wrap_text()
        self.adjust_font_size()

    def procenate_button(self):
        prior = self.ids.calc_input.text
        if prior:
            try:
                result = float(prior) / 100
                self.ids.calc_input.text = str(result)
            except:
                self.ids.calc_input.text = "Error"
        self.wrap_text()
        self.adjust_font_size()

    def dot_button(self):
        prior = self.ids.calc_input.text

        if '.' not in prior.split()[-1]:
            self.ids.calc_input.text = f'{prior}.'
        
        self.wrap_text()
        self.adjust_font_size()

    def equals_button(self):
        prior = self.ids.calc_input.text

        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
        
        self.wrap_text()
        self.adjust_font_size()

class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()