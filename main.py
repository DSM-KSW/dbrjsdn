import flet as ft
import view

def main(page:ft.Page):
    page.title = "dsm ksw project"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "0x595959"
    page.padding = ft.Padding.all(16)

    page.window.width = 1280
    page.window.height = 720

    def route_change(e:ft.RouteChangeEvent | None = None):
        page.views.clear()

        # stack
        match page.route:
            case "/":
                page.views.append(view.home_view(page))

            case "/keyboard":
                page.views.append(view.home_view(page))
                page.views.append(view.keyboard_view(page))

            case "/mouse":
                page.views.append(view.home_view(page))
                page.views.append(view.mouse_view(page))

            case "/settings":
                page.views.append(view.home_view(page))
                page.views.append(view.settings_view(page))

        page.update()

    # 뒤로가기
    async def view_pop(e:ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # 맨 처음 이동할 때는 await page.push_route("/")가 안 되더라구요.
    # / -> /라서 변경 없음으로 처리한다나 뭐라나.
    route_change()

if __name__ == "__main__":
    ft.run(main)