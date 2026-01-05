import flet as ft


def home_view(page: ft.Page):

    def step(text, route=None, highlight=False):
        link = ft.Text(
            text,
           
            weight="bold" if highlight else "normal"
        )

        if route:
            link = ft.TextButton(
                text,
                on_click=lambda e: page.go(route)
            )

        return ft.Row(
            controls=[
                ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE, size=18),
                link
            ],
            spacing=10
        )

    return ft.Container(
        expand=True,
        padding=30,
        content=ft.Column(
            spacing=25,
            controls=[

                # ---------- HEADER ----------
                ft.Column(
                    spacing=8,
                    controls=[
                        ft.Text(
                            "Bienvenido al Generador de Horarios",
                            size=28,
                            weight="bold"
                        ),
                        ft.Text(
                            "Organiza y visualiza los horarios de tu división de manera eficiente.",
                            color=ft.Colors.GREY_700
                        )
                    ]
                ),

                ft.Divider(),

                # ---------- PASOS ----------
                ft.Column(
                    spacing=15,
                    controls=[
                        ft.Text("¿Cómo empezar?", size=22, weight="bold"),

                        step("Carreras: Añade las carreras de tu división.", "/carreras"),
                        step("Gestión de Salones: Añade todos los salones disponibles.", "/salones"),
                        step("Gestión de Materias: Agrega todas las materias.", "/materias"),
                        step("Profesores: Asigna profesores a materias.", "/profesores"),
                        step("Gestión de Grupos: Crea los grupos correspondientes.", "/grupos"),
                        step(
                            "Generar Horarios: Selecciona grados y genera automáticamente.",
                            "/horarios/nuevo",
                            highlight=True
                        ),
                        step(
                            "Visualizar: Visualiza o exporta los horarios generados en PDF.",
                            highlight=True
                        ),
                    ]
                ),

                # ---------- INFO CARD ----------
                ft.Container(
                    margin=ft.margin.only(top=20),
                    width=400,
                    padding=15,
                    bgcolor=ft.Colors.AMBER_100,
                    border_radius=10,
                    content=ft.Row(
                        spacing=12,
                        controls=[
                            ft.Icon(
                                ft.Icons.INFO,
                                color=ft.Colors.AMBER_700
                            ),
                            ft.Text(
                                "Recuerda: Puedes modificar la información en cualquier momento "
                                "desde las secciones correspondientes.",
                                expand=True,
                                color=ft.Colors.BLACK
                            )
                        ]
                    )
                )
            ]
        )
    )
