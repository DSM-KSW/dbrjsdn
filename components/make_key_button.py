
import flet as ft
from typing import TypedDict, NotRequired

class KeyButtonParameters(TypedDict):
    id:str
    name:str
    width:NotRequired[int]
    height:NotRequired[int]
    on_hover:ft.ControlEventHandler[ft.Button]
    on_out:ft.ControlEventHandler[ft.Button]

def make_key_button(param:KeyButtonParameters):
    width = param.get("width", 100)
    height = param.get("height", 100)

    def on_hover(e:ft.Event[ft.Button]):
        match e.data:
            case "true":
                param["on_hover"](e)
            case "false":
                param["on_out"](e)

    return ft.Button(
        content=ft.Text(
            param["name"],
            size=12,
            color="0x000000"
        ),

        width=width,
        height=height,

        bgcolor=ft.Colors.GREY_300,

        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius.all(4)),
            padding=ft.Padding.all(8)
        ),

        on_hover=on_hover
    )