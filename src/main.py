import flet as ft
from views.app import App


def main(page: ft.Page):
    App(page)


ft.run(main, assets_dir="assets")
