import flet as ft

def home_view(page:ft.Page):
    async def on_click():
        await page.push_route("/keyboard")

    return ft.View(
        route="/",
        controls=[
            ft.Button(content="test", on_click=on_click)
        ]
    )