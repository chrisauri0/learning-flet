import flet as ft

def data_input_view(page: ft.Page):
    return ft.Column(
        controls=[
            ft.Text("Cargar Datos", size=26, weight="bold"),
            ft.Text("Ingrese los datos necesarios para generar horarios."),
            ft.TextField(label="Número de estudiantes"),
            ft.TextField(label="Número de cursos"),
            ft.ElevatedButton(
                "Volver al inicio",
                on_click=lambda e: page.go("/")
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )