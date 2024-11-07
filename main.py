import flet as ft


def main (page: ft.Page):

    ############## Window Pro ###############

    page.window_width=390
    page.window_left=900
    page.window_height= 740
    page.title="Flash Light"
    page.scroll="auto"
    page.theme_mode="DARK"


    page.vertical_alignment="center"  # top - bottom
    page.horizontal_alignment="center" # left - right

    ############## AppBar Star ############

    def click(e):
        al= ft.AlertDialog(title=ft.Text("hello khalid"),bgcolor="green")
        page.overlay.append(al)
        al.open=True
        page.update()
    
    


    page.add(
        
        ft.AppBar(
            bgcolor="#fa8200",
            title=ft.Text("Flash Light Fatih",color="white"),
            center_title=True,
            leading=ft.Icon(ft.icons.HOME,color="white"),
            actions=[
                ft.IconButton(ft.icons.SETTINGS,icon_color="white",on_click=...)
            ]
        ),
        
        
        ft.Text(" \n\nمرحبا بكم في تطبيق خالد فاتح لتشغيل الفلاش\n"),
        ft.Image(src="flashlight.webp",width=300,border_radius=50),
        ft.Text("\n"),
        ft.Row([
            ft.ElevatedButton("ON",width=140,icon=ft.icons.PLAY_ARROW,style=ft.ButtonStyle(
                bgcolor="green",
                color="white",
                padding=15,
                shape=ft.ContinuousRectangleBorder(radius=100)
            ),on_click=click),
            ft.ElevatedButton("OFF",width=140,icon=ft.icons.PLAY_DISABLED_OUTLINED,style=ft.ButtonStyle(
                bgcolor="red",
                color="white",
                padding=15,
                shape=ft.ContinuousRectangleBorder(radius=100)
            ))
            
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Text("\n\n\n\n Khalid Fatih 2024"),
        

    )
    page.update()

ft.app(main)
