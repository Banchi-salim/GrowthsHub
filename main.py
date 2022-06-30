import kivy
import kivymd
from kivy.clock import Clock
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.properties import ObjectProperty, ListProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.core.window import Window
from kivymd.material_resources import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.stacklayout import MDStackLayout
import requests
from requests import Session
from pprint import pprint as pp
import mysql.connector as mc

Window.size = (300, 600)


class Profile(Screen):
    def on_press_back(self):
        sm.current = "mainline"


class Content(MDBoxLayout):
    def button_page(self, widget):
        sm.current = str(widget.text)


class Mainline(Screen):
    data = ListProperty()

    # mydb = mc.connect(host="localhost", user="root", passwd="", database="growthshub")

    def __init__(self, **kwargs):
        super(Mainline, self).__init__(**kwargs)
        """query = "SELECT * FROM requests"
        my_cursor.execute(query)
        self.data = my_cursor.fetchall()"""
        pass

    def uid(self):
        my_cursor = self.mydb.cursor()
        query_id = "SELECT user_id FROM requests"
        my_cursor.execute(query_id)
        u_id = (my_cursor.fetchone())
        for i in u_id:
            return str(i)

    def dis_time(self):
        time_cursor = self.mydb.cursor()
        query_time = "SELECT time FROM requests"
        time_cursor.execute(query_time)
        var = time_cursor.fetchone()
        for i in var:
            return i

    def link(self):
        pass

    def img_dir(self):
        pass

    def active_jobs(self):
        for i in self.data:
            print(i)

    def on_enter(self, *args):
        self.active_jobs()


class Splash(Screen):
    pass


class Login(Screen):

    def button_click(self):
        sm.current = "mainline"


class GrowthHub(MDApp):
    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(Builder.load_file("login.kv"))
        sm.add_widget(Builder.load_file("mainline.kv"))
        sm.add_widget(Builder.load_file("profile.kv"))
        # sm.add_widget(Builder.load_file("page2.kv"))
        sm.transition = FadeTransition()
        return sm

    def on_start(self):
        Clock.schedule_once(self.login, 5)

    def login(self, *args):
        sm.current = "login"


GrowthHub().run()
