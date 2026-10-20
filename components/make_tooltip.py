import flet as ft

TOOLTIP_WIDTH = 160

def make_tooltip():
    remapping_arr:list[ft.Text] = []

    return ft.Container(
        content=ft.Column(
            controls=remapping_arr,
            spacing=4
        ),

        # 키 위 가운데에 놓기 위해 너비를 고정
        width=TOOLTIP_WIDTH,

        bgcolor="0xFFFFFF",
        # 흰 키보드 판 위에서도 보이도록 테두리 추가 (디자인 확정 전 임시)
        border=ft.Border.all(1, "0xB1B1B1"),
        border_radius=ft.BorderRadius.all(4),

        padding=ft.Padding.all(16)
    )
