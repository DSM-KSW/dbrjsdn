import flet as ft
import components
from typing import TypedDict, NotRequired

class KeyButtonData(TypedDict):
    id:str
    name:str
    # 아래 값들은 모두 키 1칸(KEY_UNIT) 기준 배수
    x: NotRequired[float]  # 이 키 앞의 가로 간격
    y: NotRequired[float]  # 이 줄 위의 세로 간격 (줄의 첫 키에만 지정)
    width: NotRequired[float]
    height: NotRequired[float]

KEY_UNIT = 50  # 키 1칸의 크기(px)
KEY_GAP = 4  # 키 사이 여백(px)

# US ANSI 104키 풀배열
KEYBOARD_BUTTON_DATA:list[list[KeyButtonData]] = [
    [
        {"id": "esc", "name": "Esc"},
        {"id": "func-1", "name": "F1", "x": 1},
        {"id": "func-2", "name": "F2"},
        {"id": "func-3", "name": "F3"},
        {"id": "func-4", "name": "F4"},
        {"id": "func-5", "name": "F5", "x": 0.5},
        {"id": "func-6", "name": "F6"},
        {"id": "func-7", "name": "F7"},
        {"id": "func-8", "name": "F8"},
        {"id": "func-9", "name": "F9", "x": 0.5},
        {"id": "func-10", "name": "F10"},
        {"id": "func-11", "name": "F11"},
        {"id": "func-12", "name": "F12"},
        {"id": "print-screen", "name": "PrtSc", "x": 0.25},
        {"id": "scroll-lock", "name": "ScrLk"},
        {"id": "pause", "name": "Pause"},
    ],
    [
        {"id": "backtick", "name": "`", "y": 0.5},
        {"id": "one", "name": "1"},
        {"id": "two", "name": "2"},
        {"id": "three", "name": "3"},
        {"id": "four", "name": "4"},
        {"id": "five", "name": "5"},
        {"id": "six", "name": "6"},
        {"id": "seven", "name": "7"},
        {"id": "eight", "name": "8"},
        {"id": "nine", "name": "9"},
        {"id": "zero", "name": "0"},
        {"id": "hyphen", "name": "-"},
        {"id": "equal-sign", "name": "="},
        {"id": "backspace", "name": "Backspace", "width": 2},
        {"id": "insert", "name": "Insert", "x": 0.25},
        {"id": "home", "name": "Home"},
        {"id": "page-up", "name": "PgUp"},
        {"id": "num-lock", "name": "Num", "x": 0.25},
        {"id": "numpad-slash", "name": "/"},
        {"id": "numpad-asterisk", "name": "*"},
        {"id": "numpad-hyphen", "name": "-"},
    ],
    [
        {"id": "tab", "name": "Tab", "width": 1.5},
        {"id": "q", "name": "Q"},
        {"id": "w", "name": "W"},
        {"id": "e", "name": "E"},
        {"id": "r", "name": "R"},
        {"id": "t", "name": "T"},
        {"id": "y", "name": "Y"},
        {"id": "u", "name": "U"},
        {"id": "i", "name": "I"},
        {"id": "o", "name": "O"},
        {"id": "p", "name": "P"},
        {"id": "left-bracket", "name": "["},
        {"id": "right-bracket", "name": "]"},
        {"id": "backslash", "name": "\\", "width": 1.5},
        {"id": "delete", "name": "Delete", "x": 0.25},
        {"id": "end", "name": "End"},
        {"id": "page-down", "name": "PgDn"},
        {"id": "numpad-seven", "name": "7", "x": 0.25},
        {"id": "numpad-eight", "name": "8"},
        {"id": "numpad-nine", "name": "9"},
        {"id": "numpad-plus", "name": "+", "height": 2},
    ],
    [
        {"id": "caps-lock", "name": "Caps Lock", "width": 1.75},
        {"id": "a", "name": "A"},
        {"id": "s", "name": "S"},
        {"id": "d", "name": "D"},
        {"id": "f", "name": "F"},
        {"id": "g", "name": "G"},
        {"id": "h", "name": "H"},
        {"id": "j", "name": "J"},
        {"id": "k", "name": "K"},
        {"id": "l", "name": "L"},
        {"id": "semicolon", "name": ";"},
        {"id": "quote", "name": "'"},
        {"id": "enter", "name": "Enter", "width": 2.25},
        {"id": "numpad-four", "name": "4", "x": 3.5},
        {"id": "numpad-five", "name": "5"},
        {"id": "numpad-six", "name": "6"},
    ],
    [
        {"id": "left-shift", "name": "Shift", "width": 2.25},
        {"id": "z", "name": "Z"},
        {"id": "x", "name": "X"},
        {"id": "c", "name": "C"},
        {"id": "v", "name": "V"},
        {"id": "b", "name": "B"},
        {"id": "n", "name": "N"},
        {"id": "m", "name": "M"},
        {"id": "comma", "name": ","},
        {"id": "period", "name": "."},
        {"id": "slash", "name": "/"},
        {"id": "right-shift", "name": "Shift", "width": 2.75},
        {"id": "arrow-up", "name": "↑", "x": 1.25},
        {"id": "numpad-one", "name": "1", "x": 1.25},
        {"id": "numpad-two", "name": "2"},
        {"id": "numpad-three", "name": "3"},
        {"id": "numpad-enter", "name": "Enter", "height": 2},
    ],
    [
        {"id": "left-ctrl", "name": "Ctrl", "width": 1.25},
        {"id": "left-win", "name": "Win", "width": 1.25},
        {"id": "left-alt", "name": "Alt", "width": 1.25},
        {"id": "space", "name": "Space", "width": 6.25},
        {"id": "right-alt", "name": "Alt", "width": 1.25},
        {"id": "right-win", "name": "Win", "width": 1.25},
        {"id": "menu", "name": "Menu", "width": 1.25},
        {"id": "right-ctrl", "name": "Ctrl", "width": 1.25},
        {"id": "arrow-left", "name": "←", "x": 0.25},
        {"id": "arrow-down", "name": "↓"},
        {"id": "arrow-right", "name": "→"},
        {"id": "numpad-zero", "name": "0", "x": 0.25, "width": 2},
        {"id": "numpad-period", "name": "."},
    ],
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

    key_buttons:list[ft.Control] = []

    # 키를 KEY_UNIT 격자 위에 절대 위치로 배치
    # (넘패드 +, Enter처럼 두 줄짜리 키가 있어서 Row로는 배치할 수 없음)
    keyboard_width = 0.0
    keyboard_height = 0.0
    y = 0.0

    for data_list in KEYBOARD_BUTTON_DATA:
        x = 0.0
        y += data_list[0].get("y", 0)

        for data in data_list:
            x += data.get("x", 0)
            width = data.get("width", 1)
            height = data.get("height", 1)

            def on_hover(e:ft.Event[ft.Button]):
                tooltip_thing.visible = True

                # 키 바로 위, 가운데 정렬
                tooltip_thing.left = e.control.left + (e.control.width - tooltip_thing.width) / 2
                tooltip_thing.bottom = keyboard_height - e.control.top + KEY_GAP

                tooltip_thing.update()

            def on_out(e:ft.Event[ft.Button]):
                tooltip_thing.visible = False

                tooltip_thing.update()

            key_button = components.make_key_button({
                "id": data["id"],
                "name": data["name"],
                "width": width * KEY_UNIT - KEY_GAP,
                "height": height * KEY_UNIT - KEY_GAP,
                "on_hover": on_hover,
                "on_out": on_out
            })
            key_button.left = x * KEY_UNIT
            key_button.top = y * KEY_UNIT

            key_buttons.append(key_button)

            x += width
            keyboard_width = max(keyboard_width, x * KEY_UNIT - KEY_GAP)
            keyboard_height = max(keyboard_height, (y + height) * KEY_UNIT - KEY_GAP)

        y += 1

    keyboard = ft.Container(
        content=ft.Stack(
            controls=[*key_buttons, tooltip_thing],
            width=keyboard_width,
            height=keyboard_height,
            # 맨 윗줄 키의 툴팁이 키보드 밖으로 나가도 잘리지 않게
            clip_behavior=ft.ClipBehavior.NONE
        ),

        bgcolor="0xFFFFFF",
        border=ft.Border.all(1, "0xB1B1B1"),
        border_radius=ft.BorderRadius.all(6),
        clip_behavior=ft.ClipBehavior.NONE,

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

    return ft.View(
        route="/keyboard",
        controls=[
            ft.Column(
                controls=[
                    back_button_container,
                    keyboard_container
                ]
            )
        ]
    )
