# import flet as ft


# def main(page: ft.Page):
#     None


# ft.run(main, assets_dir="assets")

from controllers.user import User

new_user = User.create(username='admin', master_password='1234') 
