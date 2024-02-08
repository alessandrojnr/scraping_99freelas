from time import sleep
import flet as ft
from flet import Page, MainAxisAlignment, AlertDialog , Text, AppBar, TextField, ElevatedButton
from scrap_final import *
import subprocess

subprocess.call("Script1.py", shell=True)

def main(page: Page):
    page.title = 'Scraping 99Freelas'
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.padding = 100
    page.theme_mode = 'dark'
    page.vertical_alignment = MainAxisAlignment.CENTER

    def bt_click(e):

        dialogo = AlertDialog(
            title = Text(f'Bem vindo {name_input.value} , vamos fazer dinheiro !'))
        page.dialog = dialogo
        dialogo.open = True
        page.update()
        sleep(1)
        subprocess.call("scrap_final.py", shell=True)
    
    page.appbar = AppBar(title = Text('Scraping 99Freelas'), center_title = True)
    name_input = TextField(
        label = ' Nome', autofocus = True, hint_text = 'Digite seu nome')

    submit = ElevatedButton(
        text = 'Enviar', width = 600, on_click = bt_click
    )
    page.update()
    page.add(name_input, submit)


ft.app(target=main)