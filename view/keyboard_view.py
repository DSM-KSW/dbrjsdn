import flet as ft
import components
from typing import TypedDict, NotRequired

class KeyButtonData(TypedDict):
    id:str
    name:str
    width: NotRequired[int]
    height: NotRequired[int]

KEYBOARD_BUTTON_DATA:list[list[KeyButtonData]] = [
    [
        {
            "id": "esc",
            "name": "Esc",
        },
        {
            "id": "func-1",
            "name": "F1",
        },
        {
            "id": "func-2",
            "name": "F2",
        },
        {
            "id": "func-3",
            "name": "F3",
        },
        {
            "id": "func-4",
            "name": "F4",
        },
        {
            "id": "func-5",
            "name": "F5",
        },
        {
            "id": "func-6",
            "name": "F6",
        },
        {
            "id": "func-7",
            "name": "F7",
        },
        {
            "id": "func-8",
            "name": "F8",
        },
        {
            "id": "func-9",
            "name": "F9",
        },
        {
            "id": "func-10",
            "name": "F10",
        },
        {
            "id": "func-11",
            "name": "F11",
        },
        {
            "id": "func-12",
            "name": "F12",
        },
    ],
    [
        {
            "id": "backtick",
            "name": "`",
        },
        {
            "id": "one",
            "name": "1",
        },
        {
            "id": "two",
            "name": "2",
        },
        {
            "id": "three",
            "name": "3",
        },
        {
            "id": "four",
            "name": "4",
        },
        {
            "id": "five",
            "name": "5",
        },
        {
            "id": "six",
            "name": "6",
        },
        {
            "id": "seven",
            "name": "7",
        },
        {
            "id": "eight",
            "name": "8",
        },
        {
            "id": "nine",
            "name": "9",
        },
        {
            "id": "hyphen",
            "name": "-",
        },
        {
            "id": "equal-sign",
            "name": "=",
        },
        {
            "id": "backspace",
            "name": "Backspace",
            "width": 48
        },
    ]
]

def keyboard_view(page:ft.Page):
    back_button_container = ft.Container(
        content=ft.Column(
            controls=[
                components.make_back_button({
                    "push_route": page.push_route,
                    "href": "/"
                })
            ]
        ),
        padding=ft.Padding.symmetric(vertical=30, horizontal=40)
    )

    tooltip_thing = components.make_tooltip()

    tooltip_thing.visible = False

    tooltip_thing.top = 0
    tooltip_thing.left = 0

    key_buttons:list[ft.Row] = []

    for data_list in KEYBOARD_BUTTON_DATA:
        row = ft.Row(
            spacing=8
        )

        for data in data_list:
            def on_hover(e:ft.Event[ft.Button]):
                tooltip_thing.visible = True

                tooltip_thing.top = e.control.top - tooltip_thing.height - 2
                tooltip_thing.left = e.control.left - (tooltip_thing.width / 2)

                tooltip_thing.update()

            def on_out(e:ft.Event[ft.Button]):
                tooltip_thing.visible = False

                tooltip_thing.update()

            row.controls.append(components.make_key_button({
                "id": data["id"],
                "name": data["name"],
                "width": data.get("width", None),
                "height": data.get("height", None),
                "on_hover": on_hover,
                "on_out": on_out
            }))

        key_buttons.append(row)

    keyboard = ft.Container(
        content=ft.Column(
            controls=key_buttons
        ),

        bgcolor="0xFFFFFF",
        border=ft.Border.all(1, "0xB1B1B1"),
        border_radius=ft.BorderRadius.all(6),

        padding=ft.Padding.all(8),

        shadow=[
            ft.BoxShadow(  # inner
                blur_style=ft.BlurStyle.INNER,
                blur_radius=4,
                color=ft.Colors.with_opacity(0.8, "0x000000"),
                offset=ft.Offset(0.5, 0.5)
            ),
            ft.BoxShadow( # outer
                blur_radius=24,
                spread_radius=4,
                color=ft.Colors.with_opacity(0.25, "0x000000")
            )
        ]
    )
    keyboard_container = ft.Container(
        content=keyboard,
        padding=ft.Padding.all(24),
        alignment=ft.Alignment.CENTER
    )

    stack = ft.Stack(
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        back_button_container,
                        keyboard_container
                    ]
                )
            ),
            tooltip_thing
        ],
        expand=True
    )

    return ft.View(
        route="/keyboard",
        controls=[stack]
    )