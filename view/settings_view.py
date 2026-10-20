import flet as ft
import components

# 디자인 확정 전 자리만 잡아둔 화면 (뒤로가기 버튼만 있음)
def settings_view(page:ft.Page):
    return ft.View(
        route="/settings",
        controls=[
            ft.Container(
                content=components.make_back_button({
                    "push_route": page.push_route,
                    "href": "/"
                }),
                padding=ft.Padding.symmetric(vertical=30, horizontal=40)
            )
        ]
    )
