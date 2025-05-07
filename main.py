# main.py
import flet as ft

def main(page: ft.Page):
    page.title = "DGB COMEX - Sistema de Tecidos"
    page.theme_mode = "light"
    page.window_width = 1200
    
    # Layout com abas laterais e superiores
    rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(icon="home", label="Início"),
            ft.NavigationRailDestination(icon="settings", label="Configurações"),
            ft.NavigationRailDestination(icon="admin_panel_settings", label="Admin"),
        ],
        selected_index=0,
    )
    
    page.add(ft.Row([rail, ft.VerticalDivider(), ft.Column([ft.Text("Conteúdo")])]))

ft.app(target=main)