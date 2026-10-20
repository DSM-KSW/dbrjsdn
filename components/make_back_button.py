import flet as ft
from typing import TypedDict, Callable, Awaitable

class BackButtonParameters(TypedDict):
    push_route:Callable[[str], Awaitable[None]]
    href:str

def make_back_button(param:BackButtonParameters):
    async def on_click():
        await param["push_route"](param["href"])

    return ft.IconButton(
        bgcolor="0x3A3A3A",
        icon=ft.Icons.CHEVRON_RIGHT,
        icon_size=24,
        icon_color="0xFFFFFF",
        width=44,
        height=44,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius.all(4))
        ),
        on_click=on_click
    )