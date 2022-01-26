from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class éPrimo(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}


        self.window.add_widget(Image(
                                source="logo.png",
                                size_hint = (2, 2)
                                ))

        self.greeting = Label(
                        text="Digite um número para verificar se ele é primo ou não: ",
                        font_size = 25,
                        font_name = 'SinkinSans-100Thin.otf',
                        color = '#FF08EF',
                        )

        self.window.add_widget(self.greeting)

        self.user = TextInput(
                    multiline=False,
                    input_filter='int',
                    padding_y = (20, 20),
                    padding_x = (220, 50),
                    size_hint = (1, 0.8),
                    font_size = 35

                    )
        self.window.add_widget(self.user)

        self.button = Button(
                    text="VERIFICAR",
                    size_hint = (1, 0.5),
                    bold = True,
                    background_color = '#9B177F'
                    )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window



    def callback(self, instance):
        x = int(self.user.text)
        count = 0

        for i in range(2, int(x / 2)):
            resto = x % i
            if resto != 0:
                count += 1

        if count == len(range(2, int(x / 2))):
            self.greeting.text = self.user.text + " é primo!"
        else:
            self.greeting.text = self.user.text + " não é primo!"





if __name__ == "__main__":
    éPrimo().run()
