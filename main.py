import kivy
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config

kivy.require("2.2.1")
Window.clearcolor = (0.6, 0.6, 0.8, 1)
Window.size = (720,1280)
#Config.set('graphics', 'width', '1920')
#Config.set('graphics', 'height', '1080')

class Manager(ScreenManager):
    pass
class Title(Screen):
    pass
class Intro_page(Screen):
    pass

class Index(Screen):
    pass
class parent_qna():
    def change(self,qp_img,ans_btn):

        if ans_btn.text == "Answer":
            ans_btn.text = "Question"
            qp_img.source = "Chapter-"+self.name[1:4]+"/Answers/A-"+self.name[1:4]+"-"+self.name[5:]+"-01.png"
        elif ans_btn.text == "Question":
            ans_btn.text = "Answer"
            qp_img.source = "Chapter-"+self.name[1:4]+"/Questions/Q-"+self.name[1:4]+'-'+self.name[5:]+"-01.png"

    def ans_next(self,qp_img,ans_btn):
        if ans_btn.text == "MORE":
            ans_btn.text = "BACK"
            qp_img.source = "Chapter-"+self.name[1:4]+"/Answers/A-"+self.name[1:4]+"-"+self.name[5:]+"-02.png"
        elif ans_btn.text == "BACK":
            ans_btn.text = "MORE"
            qp_img.source = "Chapter-"+self.name[1:4]+"/Answers/A-"+self.name[1:4]+"-"+self.name[5:]+"-01.png"

class Q01_pg(Screen):
    pass
class c1q1(Screen,parent_qna):
    pass

class c1q2(Screen,parent_qna):
    pass
class c1q3(Screen,parent_qna):
    pass
class c1q4(Screen,parent_qna):
    pass
class c1q5(Screen,parent_qna):
    pass




class Q02_pg(Screen):
    pass
class c2q1(Screen,parent_qna):
    pass
class c2q2(Screen,parent_qna):
    pass
class c2q3(Screen,parent_qna):
    pass
class c2q4(Screen,parent_qna):
    pass
class c2q5(Screen,parent_qna):
    pass
class c2q6(Screen,parent_qna):
    pass


class Q03_pg(Screen):
    pass
class c3q1(Screen,parent_qna):
    pass
class c3q2(Screen,parent_qna):
    pass
class c3q3(Screen,parent_qna):
    pass
class c3q4(Screen,parent_qna):
    pass
class c3q5(Screen,parent_qna):
    pass


class Q04_pg(Screen):
    pass
class c4q1(Screen,parent_qna):
    pass
class c4q2(Screen,parent_qna):
    pass
class c4q3(Screen,parent_qna):
    pass


class Q05_pg(Screen):
    pass
class c5q1(Screen,parent_qna):
    pass

class c5q2(Screen,parent_qna):
    pass
class c5q3(Screen,parent_qna):
    pass
class c5q4(Screen,parent_qna):
    pass
class c5q5(Screen,parent_qna):
    pass

class Q06_pg(Screen):
    pass
class c6q1(Screen,parent_qna):
    pass

class c6q2(Screen,parent_qna):
    pass
class c6q3(Screen,parent_qna):
    pass
class c6q4(Screen,parent_qna):
    pass
class c6q5(Screen,parent_qna):
    pass


class MyApp(App):
    def build(self):
        return file

file = Builder.load_file("main_kv.kv")
MyApp().run()