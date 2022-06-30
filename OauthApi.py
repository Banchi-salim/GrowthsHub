import urllib
import kivy
import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.network.urlrequest import UrlRequest
from kivyauth import facebook_auth
kivyauth

Builder.load_string("""
<test>
    MDFlatButton:
        text:"click me!!!"
        on_press:root.open()
    
    
    """)


class Test(BoxLayout):
    param = {'?client_id': '415784697103215', '&redirect_uri': 'https://instafollowpanel.com/',
             '&scope': 'user_profile, user_media', '&response_type': 'code'}

    def open(self):
        # urllib.request.urlopen('https://api.instagram.com/oauth/authorize', self.params())
        # view = ModalView(size_hint = (.8, .8))
        # webview.()
        UrlRequest('https://api.instagram.com/oauth/authorize', req_headers=self.param)
        # print(req)

    """def params(self):
        param = {'?client_id': '415784697103215', '&redirect_uri': 'https://instafollowpanel.com/',
                 '&scope': 'user_profile, user_media', '&response_type': 'code'}"""

    # req = requests.get('https://api.instagram.com/oauth/authorize', params)
    # urllib.request.urlopen('https://api.instagram.com/oauth/authorize', params())

    # print(req)


class apiopen(MDApp):
    def build(self):
        return Test()


apiopen().run()
