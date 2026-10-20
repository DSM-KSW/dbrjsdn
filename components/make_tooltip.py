import flet as ft

def make_tooltip():
    remapping_arr:list[ft.Text] = []

    return ft.Container(
        content=ft.Column(
            controls=remapping_arr,
            spacing=4
        ),

        bgcolor="0xFFFFFF",

        padding=ft.Padding.all(16)
    )