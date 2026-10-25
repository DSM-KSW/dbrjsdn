import flet as ft
from typing import TypedDict, Callable
from components.make_hover_icon import make_hover_icon, is_hover_enter

TOOLTIP_WIDTH = 216

class TooltipParameters(TypedDict):
    on_hover:Callable[[], None]
    on_out:Callable[[], None]

class RemappingListParameters(TypedDict):
    labels:list[str]  # "리매핑 1: Ctrl+G+C" 같은 표시용 문자열
    on_add:Callable[[], None]
    on_edit:Callable[[int], None]
    on_delete:Callable[[int], None]
    on_row_hover:Callable[[int], None]
    on_row_out:Callable[[int], None]

# 키 위에 뜨는 리매핑 목록 (내용은 set_tooltip_remappings로 채움)
def make_tooltip(param:TooltipParameters):
    def on_hover(e:ft.Event[ft.Container]):
        if is_hover_enter(e):
            param["on_hover"]()
        else:
            param["on_out"]()

    return ft.Container(
        content=ft.Column(
            controls=[],
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),

        width=TOOLTIP_WIDTH,

        bgcolor="#FFFFFF",
        border_radius=ft.BorderRadius.all(10),
        padding=ft.Padding.symmetric(horizontal=10, vertical=8),
        shadow=ft.BoxShadow(
            blur_radius=10,
            spread_radius=6,
            color=ft.Colors.with_opacity(0.25, "#000000"),
            offset=ft.Offset(0, 4)
        ),

        on_hover=on_hover
    )

def _make_remapping_row(index:int, label:str, param:RemappingListParameters):
    def on_hover(e:ft.Event[ft.Container]):
        if is_hover_enter(e):
            param["on_row_hover"](index)
        else:
            param["on_row_out"](index)

    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    label,
                    size=16,
                    color="#000000",
                    width=140,
                    max_lines=1,
                    overflow=ft.TextOverflow.ELLIPSIS
                ),
                ft.Row(
                    controls=[
                        make_hover_icon({
                            "src": "icons/setting-off.svg",
                            "hover_src": "icons/setting-on.svg",
                            "width": 22,
                            "height": 22,
                            "on_click": lambda: param["on_edit"](index)
                        }),
                        make_hover_icon({
                            "src": "icons/delete-off.svg",
                            "hover_src": "icons/delete-on.svg",
                            "width": 24,
                            "height": 24,
                            "on_click": lambda: param["on_delete"](index)
                        })
                    ],
                    spacing=4
                )
            ],
            spacing=8
        ),
        on_hover=on_hover
    )

def set_tooltip_remappings(tooltip:ft.Container, param:RemappingListParameters):
    rows:list[ft.Control] = [
        _make_remapping_row(i, label, param) for i, label in enumerate(param["labels"])
    ]

    rows.append(make_hover_icon({
        "src": "icons/add-off.svg",
        "hover_src": "icons/add-on.svg",
        "width": 196,
        "height": 24,
        "on_click": param["on_add"]
    }))

    tooltip.content.controls = rows
