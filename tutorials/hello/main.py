#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.app import Widget
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from plyer import vibrator

kivy.require('1.8.0')

__version__ = "0.1"


class PaginaInicial(Screen):
    pass


class LabelConfig(Screen):
    pass


class Logo(Image):
    pass


class ScreenManagement(ScreenManager):
    def switch_to_labelConfig(self):
        self.current = 'labelConfig'

    def switch_to_paginaInicial(self):
        self.current = 'paginaInicial'
        self.logo = Logo(source='teste.jpg',
                         pos=(0, 0),
                         size=(51, 51))

    def vibrate(self):
        try:
            #vibramos por 5 segundos)
            vibrator.vibrate(time=5)
        except:
            print 'Este dispositivo não possui um vibrador'    


class kivyWizardApp(App):
    def build(self):
        self.root = ScreenManagement()
        return self.root

if __name__ == '__main__':
    kivyWizardApp().run()
