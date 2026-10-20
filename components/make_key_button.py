
import flet as ft
from typing import TypedDict

class KeyButtonParameters(TypedDict):
    id:str
    name:str
    width:float
    height:float
    on_hover:ft.ControlEventHandler[ft.Button]
    on_out:ft.ControlEventHandler[ft.Button]

def make_key_button(param:KeyButtonParameters):
    def on_hover(e:ft.Event[ft.Button]):
        # 들어올 때 True, 나갈 때 False ("true"/"false" 문자열로 오는 경우도 처리)
        if e.data is True or e.data == "true":
            param["on_hover"](e)
        else:
            param["on_out"](e)

    return ft.Button(
        content=ft.Text(
            param["name"],
            size=12,
            color="0x000000"
        ),

        width=param["width"],
        height=param["height"],

        bgcolor=ft.Colors.GREY_300,

        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius.all(4)),
            # 1칸짜리 키에 "Delete" 같은 이름이 들어가도록 여백을 줄임
            padding=ft.Padding.all(4)
        ),

        data=param["id"],

        on_hover=on_hover
    )
