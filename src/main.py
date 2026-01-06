import flet as ft
from ui.home import home_view
from ui.views.materias import materias_view
from ui.views.carreras import carreras_view
from db import init_db


def main(page: ft.Page):
    page.title = "Generador de Horarios"
    page.theme_mode = ft.ThemeMode.DARK
    init_db()

    # ---------- SWITCH DE TEMA ----------
    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    theme_switch = ft.Switch(
        value=False,
        on_change=toggle_theme,
        tooltip="Cambiar tema claro / oscuro"
    )

    # ---------- APP BAR GLOBAL ----------
    def get_appbar():
        return ft.AppBar(
            title=ft.Text("Generador de Horarios"),
            center_title=False,
            actions=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.LIGHT_MODE),
                        theme_switch,
                        ft.Icon(ft.Icons.DARK_MODE),
                    ]
                )
            ]
        )

    # ---------- RUTAS ----------
    def route_change(route):
        page.views.clear()

        if page.route == "/materias":
            page.views.append(
                ft.View(
                    "/materias",
                    controls=[materias_view(page)],
                    appbar=get_appbar()
                )
            )
        elif page.route == "/carreras":
            page.views.append(
                ft.View(
                    "/carreras",
                    controls=[carreras_view(page)],
                    appbar=get_appbar()
                )
            )
        else:
            page.views.append(
                ft.View(
                    "/",
                    controls=[home_view(page)],
                    appbar=get_appbar()
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main)
