from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivy.utils import get_color_from_hex as ku
from kivymd.uix.label import MDLabel
from kivy.lang.builder import Builder

kv = """
#:import ku kivy.utils.get_color_from_hex

Manager:
    Tela1:
        name: "tela1"

    Tela2:
        name: "tela2"

    Tela3:
        name: "tela3"

<Tela1>
    on_enter: root.adicionarMdCard()
    FloatLayout:
        ScrollView:
            MDBoxLayout:
                id: caixa
                spacing: 25
                padding: 15
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {"top": 1}

        MDFloatingActionButton:
            pos_hint: {"x": .7, "y": .05}
            icon: "plus"
            on_release: app.root.current = "tela2"

<Tela2>
    MDFloatLayout:

        MDTextField:
            id: texto_anotacao
            hint_text: "Anotação"
            size_hint_x: .8
            pos_hint: {"center_x": .5,"y": .64}

        MDRaisedButton:
            text: "Salvar"
            pos_hint: {"center_x": 0.5, "y": .5}
            on_release: root.apagarTexto()
            on_release: app.root.current = "tela3"


<Tela3>
    MDLabel:
        text: "Anotação salvada com sucesso!"
        bold: 1
        halign: 'center'
        pos_hint: {"y": .2}

    MDRaisedButton:
        text: "Voltar"
        pos_hint: {"center_y": .5,"center_x": .5}
        on_release: app.root.current = "tela1"
"""



listcard = []

class Manager(ScreenManager):
    pass


class Tela1(Screen):


    def adicionarMdCard(self):
        self.ids.caixa.add_widget(listcard[0])
        listcard.pop()


class Tela2(Screen):
    pass


    def apagarTexto(self):
        texto = self.ids.texto_anotacao
        mdcard = MDCard(size_hint=(0.6, None), height=100, md_bg_color=ku("#ebd936"),
                        pos_hint={"center_x": 0.5, "center_y": 0.85})
        mdcard.add_widget(MDLabel(text=texto.text, halign="center"))
        listcard.append(mdcard)

        texto.text = ""



class Tela3(Screen):
    pass




class Programa(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
    Programa().run()

