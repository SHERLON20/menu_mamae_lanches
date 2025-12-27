import flet as ft
import psycopg2
def main(page:ft.Page):
    url_pedidos="http://127.0.0.1:8000/pedidos/"
    page.theme_mode = ft.ThemeMode.LIGHT
    dados_lanche = [{'id': 1, 'nome': 'farol', 'preco': '24,00', 'descricao': 'pão da casa, carne 100g, queijo, presunto, bacon triturado, tomate, alface, molho.', 'classe': 'lanche_artesanal'},
                        {'id': 2, 'nome': 'cruzeirinho', 'preco': '24,00', 'descricao': 'pão da casa, carne 100g, frango, queijo, catupiry, tomate, alface, molho.', 'classe': 'lanche_artesanal'},
                        {'id': 3, 'nome': 'nativo', 'preco': '25,00', 'descricao': 'pão da casa, carne 100g, calabresa, queijo, ovo, cebola caramelizada, tomate, alface, molho.', 'classe': 'lanche_artesanal'},
                        {'id': 4, 'nome': 'atanagildo', 'preco': '28,00', 'descricao': 'pão da casa, carne 100g, farofa de calabresa e bacon, queijo, presunto, ovo, tomate, alface, molho.', 'classe': 'lanche_artesanal'},
                        {'id': 5, 'nome': 'crumaí', 'preco': '38,00', 'descricao': 'pão da casa, 2 carnes de 100g, calabresa, bacon, frango, cheddar, queijo, cebola caramelizada, tomate, alface, molho.', 'classe': 'lanche_artesanal'},
                        {'id': 6, 'nome': 'mistão', 'preco': '10,00', 'descricao': 'pão da casa, queijo e presunto.', 'classe': 'lanche_tradicional'},
                        {'id': 7, 'nome': 'hamburguinho', 'preco': '10,00', 'descricao': 'pão da casa, hambúrguer, tomate, alface, molho.', 'classe': 'lanche_tradicional'},
                        {'id': 8, 'nome': 'x-salada', 'preco': '15,00', 'descricao': 'pão da casa, hambúrguer, queijo, milho verde, tomate, alface, molho.', 'classe': 'lanche_tradicional'},
                        {'id': 9, 'nome': 'x-calabresa', 'preco': '20,00', 'descricao': 'pão da casa, hãe', 'preco': '25,00', 'descricao': 'pão da casa, hambúrguer, calabresa, ovo, bacon, frango,  queijo, presunto, tomate, alface, molho.', 'classe': 'lanche_tradicional'},
                        {'id':10,'nome':'x-bacon',"preco": "20,00","descricao": "pão da casa, hambúrguer, bacon, queijo, presunto, tomate, alface, molho.","classe": "lanche_tradicional"},
                        {"id": 11, "nome": "x-frangão", "preco": "20,00", "descricao": "pão da casa, hambúrguer, frango,  queijo, presunto, tomate, alface, molho.", "classe": "lanche_tradicional"},
                        {"id": 12, "nome": "x-mamãe", "preco": "25,00", "descricao": "pão da casa, hambúrguer, calabresa, ovo, bacon, frango,  queijo, presunto, tomate, alface, molho.", "classe": "lanche_tradicional"}

                        ]
    dados_porcao_e_bebida = [{'id': 1, 'value': 'Batata Frita Com Bacon', 'preco': '30,00', 'classe': 'porcao'},
                        {'id': 2, 'value': 'Batata Frita Com Queijo \r\n(catupiry ou cheddar)', 'preco': '30,00', 'classe': 'porcao'},
                        {'id': 3, 'value': 'Batata Frita Completa\r\n(Queijo, Calabresa e Bacon)', 'preco': '40,00', 'classe': 'porcao'},
                        {'id': 4, 'value': 'Batata Frita Com Calabresa', 'preco': '30,00', 'classe': 'porcao'},
                        {'id': 5, 'value': 'Suco copo 300ml', 'preco': '6,00', 'classe': 'bebida'},
                        {'id': 6, 'value': 'Refrigerante Lata', 'preco': '6,00', 'classe': 'bebida'},
                        {'id': 7, 'value': 'Refrigerante 1LT', 'preco': '10,00', 'classe': 'bebida'},
                        {'id': 8, 'value': 'Energético 2LT', 'preco': '15,00', 'classe': 'bebida'},
                        {'id': 9, 'value': 'Água 500ml', 'preco': '4,00', 'classe': 'bebida'},
                        {'id': 10, 'value': 'Água com Gás', 'preco': '5,00', 'classe': 'bebida'}
                        ]
    dados_pastel =[
        {'value': 'frango', 'preco': '15,00',},
        {'value': 'carne', 'preco': '15,00',},
        {'value': 'misto', 'preco': '15,00',},
        {'value': 'romeu e julieta', 'preco': '15,00',},
        {'value': 'doce de leite com banana', 'preco': '15,00',},
        {'value': 'brigadeiro com morango', 'preco': '15,00',},
        {'value': 'frango com queijo', 'preco': '20,00',},
        {'value': 'carne com queijo', 'preco': '20,00',},
        {'value': 'frango com catupiry', 'preco': '20,00',},
        {'value': 'frango com cheddar', 'preco': '20,00',},
        {'value': 'calabresa com queijo', 'preco': '20,00',},
        {'value': 'camarão cremoso', 'preco': '20,00',},
    ]

    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # função para voltar a tela principal da aplicação 
    def voltar_pricipal(e):
        tela_enviar_pedido.col= 0
        tela_principal.col = 12
        page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.SHOPPING_CART,
        bgcolor=ft.Colors.LIGHT_GREEN_ACCENT_700,
        foreground_color=ft.Colors.BLACK,
        focus_color=ft.Colors.YELLOW,
        on_click=mudar_tela
    )
        page.bgcolor= ft.Colors.BLACK
        page.update()
    def mensagem_confirmado(texto):
        def fechar_tela_confirmado(e):
            tela_confirmado.open = False
            tela_confirmado.update()
            page.update()
        tela_confirmado = ft.AlertDialog(
            content_padding=ft.padding.only(bottom=-10),
            open=True,
            bgcolor=ft.Colors.WHITE,
            content=ft.Container(
                width=100,
                height=300,
                padding=ft.padding.all(10), 
                content=ft.Column(
                controls=[
                    ft.Container(
                        image=ft.DecorationImage(src='confirmado.webp',fit=ft.ImageFit.FILL),
                        width=200,
                        height=150,
                        bgcolor=ft.Colors.WHITE
                    ),
                    ft.Text(value=texto.upper(),text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,italic=True),
                    ft.ElevatedButton(
                text='ok',
                bgcolor=ft.Colors.BLACK,
                color=ft.Colors.WHITE,
                width=300,
                on_click=fechar_tela_confirmado
            )
                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
            )
        )
        page.open(tela_confirmado)
    # função para separar as colunas de lanches corretamente
    def coluna_nome_lanche(value,color:ft.ColorValue):
        return ft.Container(
            #expand=True,
            bgcolor=ft.Colors.BLACK,
            alignment=ft.alignment.center,
            padding=ft.padding.symmetric(horizontal=20),
            content=ft.Row(
                #vertical_alignment=ft.MainAxisAlignment.CENTER,
                spacing=-10,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_RIGHT,
                        icon_color=color,
                        icon_size=40,
                        ),
                        ft.Text(
                            value=value.upper(),
                            color=color,
                            size=25
                            ),
                            ft.IconButton(
                        icon=ft.Icons.ARROW_LEFT,
                        icon_color=color,
                        icon_size=40,
                        ),
                ]
            )
        )
    # função para gerar os conteiner da area de select
    def opcao(nome):
        return ft.Container(
            #expand=True,
            bgcolor=ft.Colors.BLACK87,
            shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.YELLOW),
            padding=ft.padding.symmetric(horizontal=10,vertical=5),
            border_radius=ft.border_radius.all(20),
            content=ft.Text(value=nome.upper(),color=ft.Colors.YELLOW),
            on_click=scrool
        )
    # função para rolar a tela ate o item correto
    def scrool(e):
        if e.control.content.value == "TRADICIONAL":
            tela_principal.content.controls = [
                logo,
                select,
                coluna_nome_lanche(value="lanche tradicional",color=ft.Colors.YELLOW),
                lanches,
                coluna_nome_lanche(value='lanche artesanal',color=ft.Colors.AMBER),
                lanches_artesanais,
                coluna_nome_lanche(value='pastel',color=ft.Colors.RED),
                pasteis,
                coluna_nome_lanche(value='porções',color=ft.Colors.WHITE),
                porcoes,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT),
                bebidas,
                footer
            ]
            tela_principal.update()
        elif e.control.content.value == "ARTESANAL":
            tela_principal.content.controls = [
                logo,
                select,
                coluna_nome_lanche(value='lanche artesanal',color=ft.Colors.AMBER),
                lanches_artesanais,
                coluna_nome_lanche(value="lanche tradicional",color=ft.Colors.YELLOW),
                lanches,
                coluna_nome_lanche(value='pastel',color=ft.Colors.RED),
                pasteis,
                coluna_nome_lanche(value='porções',color=ft.Colors.WHITE),
                porcoes,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT),
                bebidas,
                footer
            ]
            tela_principal.update()
        elif e.control.content.value == "PASTEL":
            tela_principal.content.controls = [
                logo,
                select,
                coluna_nome_lanche(value='pastel',color=ft.Colors.RED),
                pasteis,
                coluna_nome_lanche(value="lanche tradicional",color=ft.Colors.YELLOW),
                lanches,
                coluna_nome_lanche(value='lanche artesanal',color=ft.Colors.AMBER),
                lanches_artesanais,
                coluna_nome_lanche(value='porções',color=ft.Colors.WHITE),
                porcoes,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT),
                bebidas,
                footer
            ]
            tela_principal.update()
        elif e.control.content.value == "PORÇÕES":
            tela_principal.content.controls = [
                logo,
                select,
                coluna_nome_lanche(value='porções',color=ft.Colors.WHITE),
                porcoes,
                coluna_nome_lanche(value="lanche tradicional",color=ft.Colors.YELLOW),
                lanches,
                coluna_nome_lanche(value='lanche artesanal',color=ft.Colors.AMBER),
                lanches_artesanais,
                coluna_nome_lanche(value='pastel',color=ft.Colors.RED),
                pasteis,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT),
                bebidas,
                footer
            ]
            tela_principal.update()
        elif e.control.content.value == "BEBIDAS":
            tela_principal.content.controls = [
                logo,
                select,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT),
                bebidas,
                coluna_nome_lanche(value="lanche tradicional",color=ft.Colors.YELLOW),
                lanches,
                coluna_nome_lanche(value='lanche artesanal',color=ft.Colors.AMBER),
                lanches_artesanais,
                coluna_nome_lanche(value='pastel',color=ft.Colors.RED),
                pasteis,
                coluna_nome_lanche(value='porções',color=ft.Colors.WHITE),
                porcoes,
                footer
            ]
            tela_principal.update()
    # função para amostrar o alert diologo de adicionar o lanche na lista
    def tela_lanche(e):
        fundo_amarelo = False
        if e.control.shadow.color == ft.Colors.YELLOW:
            fundo_amarelo = True
        lanche=e.control.content.controls[2].value
        lista = lanche.split()
        numero_convertido= lista[1].replace(",",".")
        numero=float(numero_convertido)
        def fechar_tela(e):
            tela_aberta.open=False
            page.update()
        def excluir_do_carrinho(e):
            lista_string = e.control.parent.controls[0].content.value.split()
            total.spans[1].text -= float(lista_string[-1])
            total.update()
            for item in lista_lanches.content.controls:
                if item.content.controls[0].content.value == e.control.parent.controls[0].content.value:
                    lista_lanches.content.controls.remove(item)
                    lista_lanches.update()
                    break
        def adicionar_ao_carrinho(e):
            valor_reais = int(drop.value) * numero
            nome_lanche_separado = nome_lanche.value.split()
            total.spans[1].text += int(drop.value) * numero
            total.update()
            string=f"{drop.value}-LANCHE TRAD\n{nome_lanche_separado[-3]} {nome_lanche_separado[-2]} {valor_reais}" if fundo_amarelo == True else f"{drop.value}-LANCHE ART\n{nome_lanche_separado[-3]} {nome_lanche_separado[-2]} {valor_reais}"
            lista_lanches.content.controls.append(ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.all(15),
                    border_radius=ft.border_radius.all(10),
                    content=ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col=10,
                    padding=ft.padding.symmetric(vertical=10,horizontal=20),
                    content=ft.Text(value=string,size=15,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                    bgcolor=ft.Colors.WHITE,
                    shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.BLACK),
                    border_radius=ft.border_radius.all(10),
                ),
                ft.IconButton(
                    col=2,
                    bgcolor=ft.Colors.WHITE,
                    icon=ft.Icons.DELETE_OUTLINE,
                    icon_color=ft.Colors.RED_900,
                    alignment=ft.alignment.center,
                    on_click=excluir_do_carrinho
                )
                    ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
                ))
            lista_lanches.update()
            mensagem_confirmado(texto='lanche adicionado ao carrinho com sucesso!')
        tela_aberta = ft.AlertDialog(
            inset_padding=ft.padding.symmetric(vertical=100),
            content_padding=ft.padding.all(10),
            bgcolor=ft.Colors.WHITE,
                content=ft.Column(
                        controls=[
                            ft.Container(
                                expand=False,
                                width=320,
                                bgcolor=ft.Colors.WHITE10,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value='lanche tradicional'.upper() if e.control.content.controls[1].color == ft.Colors.YELLOW else 'lanche artesanal'.upper(),text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD),
                                        ft.Container(
                                            alignment=ft.alignment.top_center,
                                            content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Container(col=1),
                                               drop:= ft.Dropdown(options=[ft.dropdown.Option(text=f'{num}')for num in range(1,5)],col=3,icon=None,label='QTD',value=1),
                                               nome_lanche:= ft.Text(value=f'{e.control.content.controls[1].value} {e.control.content.controls[2].value}'.upper(),text_align=ft.TextAlign.LEFT,size=15,weight=ft.FontWeight.BOLD,col=8),
                                            ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ),
                                        ft.Text(value='ingredientes'.upper(),text_align=ft.TextAlign.CENTER,size=20,weight=ft.FontWeight.BOLD),
                                        ft.Text(value=f'{e.control.content.controls[4].value}'.upper(),text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.BOLD),
                                    ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5
                                )
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.ElevatedButton(
                                            text='Adicionar ao Carrinho',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=adicionar_ao_carrinho
                                        ),
                                        ft.ElevatedButton(
                                            text='voltar',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=fechar_tela
                                        )
                                    ],spacing=5
                                )
                            )
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.SPACE_BETWEEN,expand=True
                    ),
                open=True
            )
        
        page.open(tela_aberta)
    # função para amostrar o alertadiolog de pasteis na lista
    def tela_pastel(e):
        string_valor = e.control.content.controls[1].value
        valor_separado = string_valor.split()
        valor_solto = valor_separado[1]
        valor_float = valor_solto.replace(',','.')
        valor_float_final = float(valor_float)
        def excluir_do_carrinho(e):
            lista_string = e.control.parent.controls[0].content.value.split()
            total.spans[1].text -= float(lista_string[-1])
            total.update()
            for item in lista_lanches.content.controls:
                if item.content.controls[0].content.value == e.control.parent.controls[0].content.value:
                    lista_lanches.content.controls.remove(item)
                    lista_lanches.update()
                    break
        def fechar_tela(e):
            tela_aberta.open=False
            tela_aberta.update()
            page.update()
        def adicionar_ao_carrinho(e):
            valor_reais = int(drop.value) * valor_float_final
            total.spans[1].text += float(valor_reais)
            total.update()
            string=f"{drop.value}-PASTEL\n{nome_pastel.value} R$ {valor_reais}"
            lista_lanches.content.controls.append(ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.all(15),
                    border_radius=ft.border_radius.all(10),
                    content=ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col=10,
                    padding=ft.padding.symmetric(vertical=10,horizontal=20),
                    content=ft.Text(value=string,size=15,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                    bgcolor=ft.Colors.WHITE,
                    shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.BLACK),
                    border_radius=ft.border_radius.all(10),
                ),
                ft.IconButton(
                    col=2,
                    bgcolor=ft.Colors.WHITE,
                    icon=ft.Icons.DELETE_OUTLINE,
                    icon_color=ft.Colors.RED_900,
                    alignment=ft.alignment.center,
                    on_click=excluir_do_carrinho
                )
                    ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
                ))
            lista_lanches.update()
            mensagem_confirmado(texto='pastel adicionada ao carrinho com sucesso!')
        tela_aberta = ft.AlertDialog(
            inset_padding=ft.padding.symmetric(vertical=100),
            content_padding=ft.padding.only(bottom=10,left=10,right=10,top=20),
            bgcolor=ft.Colors.WHITE,
                content=ft.Column(
                        controls=[
                            ft.Container(
                                expand=False,
                                width=320,
                                bgcolor=ft.Colors.WHITE10,
                                content=ft.Column(
                                    controls=[
                                       porcao_ou_bebida:= ft.Text(value='pastel'.upper(),
                                                text_align=ft.TextAlign.CENTER,
                                                size=20,weight=ft.FontWeight.BOLD
                                                ),
                                                ft.Container(
                                            alignment=ft.alignment.top_center,
                                            content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Container(col=1),
                                               drop:= ft.Dropdown(options=[ft.dropdown.Option(text=f'{num}')for num in range(1,5)],col=3,icon=None,label='QTD',value=1),
                                               nome_pastel:= ft.Text(value=f'{e.control.content.controls[0].value}'.upper(),text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.BOLD,col=8),
                                            ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ),
                                       preco:= ft.Text(value=f'preço: {e.control.content.controls[1].value}'.upper(),text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.BOLD,offset=ft.Offset(x=0,y=1.5))
                                    ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5
                                )
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.ElevatedButton(
                                            text='Adicionar ao Carrinho',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=adicionar_ao_carrinho
                                        ),
                                        ft.ElevatedButton(
                                            text='voltar',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=fechar_tela
                                        )
                                    ],spacing=5
                                )
                            )
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.SPACE_BETWEEN,expand=True
                    ),
                open=True
            )
        
        page.open(tela_aberta)
    # função para mostrar a descrição da bibida ou porção e colocar na lista de pedidos.

    def tela_bebida_ou_porcao(e):
        fundo_azul = False
        if e.control.content.controls[0].color == ft.Colors.BLUE_ACCENT:
            fundo_azul =True
        string_valor = e.control.content.controls[1].value
        valor_separado = string_valor.split()
        valor_solto = valor_separado[1]
        valor_float = valor_solto.replace(',','.')
        valor_float_final = float(valor_float)
        def excluir_do_carrinho(e):
            lista_string = e.control.parent.controls[0].content.value.split()
            total.spans[1].text -= float(lista_string[-1])
            total.update()
            for item in lista_lanches.content.controls:
                if item.content.controls[0].content.value == e.control.parent.controls[0].content.value:
                    lista_lanches.content.controls.remove(item)
                    lista_lanches.update()
                    break
        def fechar_tela(e):
            tela_aberta.open=False
            tela_aberta.update()
            page.update()
        def adicionar_ao_carrinho(e):
            valor_reais = int(drop.value) * valor_float_final
            total.spans[1].text += float(valor_reais)
            total.update()
            string=f"{drop.value}-BEBIDA\n{nome_bebida.value} R$ {valor_reais}" if fundo_azul == True else f"{drop.value}-PORÇÃO\n{nome_bebida.value} R$ {valor_reais}"
            lista_lanches.content.controls.append(ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.all(15),
                    border_radius=ft.border_radius.all(10),
                    content=ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col=10,
                    padding=ft.padding.symmetric(vertical=10,horizontal=20),
                    content=ft.Text(value=string,size=15,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                    bgcolor=ft.Colors.WHITE,
                    shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.BLACK),
                    border_radius=ft.border_radius.all(10),
                ),
                ft.IconButton(
                    col=2,
                    bgcolor=ft.Colors.WHITE,
                    icon=ft.Icons.DELETE_OUTLINE,
                    icon_color=ft.Colors.RED_900,
                    alignment=ft.alignment.center,
                    on_click=excluir_do_carrinho
                )
                    ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
                ))
            lista_lanches.update()
            mensagem_confirmado(texto='bebida adicionada ao carrinho com sucesso!') if porcao_ou_bebida.value == 'BEBIDA' else mensagem_confirmado(texto='porção adicionada ao carrinho com sucesso!')
        tela_aberta = ft.AlertDialog(
            inset_padding=ft.padding.symmetric(vertical=100),
            content_padding=ft.padding.only(bottom=10,left=10,right=10,top=20),
            bgcolor=ft.Colors.WHITE,
                content=ft.Column(
                        controls=[
                            ft.Container(
                                expand=False,
                                width=320,
                                bgcolor=ft.Colors.WHITE10,
                                content=ft.Column(
                                    controls=[
                                       porcao_ou_bebida:= ft.Text(value='bebida'.upper() if e.control.content.controls[0].color == ft.Colors.BLUE_ACCENT else 'PORÇÃO'.upper(),
                                                text_align=ft.TextAlign.CENTER,
                                                size=20,weight=ft.FontWeight.BOLD
                                                ),
                                                ft.Container(
                                            alignment=ft.alignment.top_center,
                                            content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Container(col=1),
                                               drop:= ft.Dropdown(options=[ft.dropdown.Option(text=f'{num}')for num in range(1,5)],col=3,icon=None,label='QTD',value=1),
                                               nome_bebida:= ft.Text(value=f'{e.control.content.controls[0].value}'.upper(),text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.BOLD,col=8),
                                            ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ),
                                       preco:= ft.Text(value=f'preço: {e.control.content.controls[1].value}'.upper(),text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.BOLD,offset=ft.Offset(x=0,y=1.5))
                                    ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5
                                )
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.ElevatedButton(
                                            text='Adicionar ao Carrinho',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=adicionar_ao_carrinho
                                        ),
                                        ft.ElevatedButton(
                                            text='voltar',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=fechar_tela
                                        )
                                    ],spacing=5
                                )
                            )
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.SPACE_BETWEEN,expand=True
                    ),
                open=True
            )
        
        page.open(tela_aberta)
    # função para abrir a tela de fazer pedido
    def tela_fazer_pedido(e):
        if lista_lanches.content.controls == []:
            def fechar_tela_alerta(e):
                tela_alerta.open = False
                tela_alerta.update()
                page.update()
            tela_alerta = ft.AlertDialog(
                content_padding=ft.padding.only(bottom=-10),
                open=True,
                content=ft.Container(
                    width=100,
                    height=150,
                    padding=ft.padding.all(10), 
                    content=ft.Column(
                    controls=[
                        ft.Text(value='carrinho vazio, por favor adicione algum alimento ao carrinho!'.upper(),text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,italic=True),
                        ft.ElevatedButton(
                    text='ok',
                    bgcolor=ft.Colors.BLACK,
                    color=ft.Colors.WHITE,
                    width=300,
                    on_click=fechar_tela_alerta
                )
                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
                )
            )
            page.open(tela_alerta)
        else:
            def voltar_tela(e):
                tela.open = False
                tela.update()
                page.update()
            def mudar_endereco(e):
                if e.control.bgcolor == ft.Colors.RED:
                    e.control.bgcolor = ft.Colors.GREEN
                    e.control.update()
                    tela.content.content.controls.remove(mesa)
                    tela.content.content.controls.insert(1,endereco)
                    tela.update()
                elif e.control.bgcolor == ft.Colors.GREEN:
                    e.control.bgcolor = ft.Colors.RED
                    e.control.update()
                    tela.content.content.controls.remove(endereco)
                    tela.content.content.controls.insert(1,mesa)
                    tela.update()
            def confirmar(e):
                string_pedido = ''
                numero_mesa = ''
                if nome.content.controls[1].controls[1].value == '':
                    nome.content.controls[0].value = 'você esqueceu de colocar seu nome'.upper()
                    nome.content.controls[0].color = ft.Colors.RED
                    nome.update()
                else:
                    nome.content.controls[0] = ft.Text(value='por favor digite seu nome abaixo.'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True)
                    nome.update()
                    string_pedido+=f'NOME: {nome.content.controls[1].controls[1].value}'
                if delivery.content.controls[1].bgcolor == ft.Colors.RED:
                    if num_mesa.value == None:
                        mesa.content.controls[0].value = 'você esqueceu de selecionar o numero da mesa'.upper()
                        mesa.content.controls[0].color = ft.Colors.RED
                        mesa.update()
                    else:
                        mesa.content.controls[0].value = 'selecione o numero da mesa abaixo.'.upper()
                        mesa.content.controls[0].color = ft.Colors.BLACK
                        mesa.update()
                        string_pedido +=f'\nMESA: {num_mesa.value}'
                        for item in lista_lanches.content.controls:
                            string_pedido +=f'\n{item.content.controls[0].content.value}'
                        string_pedido +=f'\nVALOR TOTAL: {total.spans[1].text}'
                else:
                    if campo_endereco.controls[1].value == '':
                        endereco.content.controls[0].value = 'você esqueceu de colocar o endereço'.upper()
                        endereco.content.controls[0].color = ft.Colors.RED
                        endereco.update()
                    else:
                        endereco.content.controls[0].value = 'digite o endereço da entrega abaixo.'.upper()
                        endereco.content.controls[0].color = ft.Colors.BLACK
                        endereco.update()
                        string_pedido +=f'\nENDEREÇO: {campo_endereco.controls[1].value}'
                        for item in lista_lanches.content.controls:
                            string_pedido +=f'\n{item.content.controls[0].content.value}'
                        string_pedido +=f'\nVALOR TOTAL: {total.spans[1].text}'
                def enviar_dados(e):
                    # dados ={
                    #     "numero_mesa" : num_mesa.value,
                    #     "pedidos":string_pedido,
                    #     "visivel":True,
                    #     "delete":False,
                    #     "total":total.spans[1].text
                    # }
                    # try:
                    #     response = requests.post(url=url_pedidos, json=dados, timeout=10)  # Timeout de 10 segundos
                    #     response.raise_for_status()  # Levanta erro se status não for 2xx
                    #     print("Sucesso:", response.json())
                    #     lista_lanches.content.controls = []
                    #     total.spans[1].text = 0.00
                    #     lista_lanches.update()
                    #     total.update()
                    #     mensagem_confirmado(texto='pedido realizado com sucesso!')
                    # except requests.exceptions.RequestException as e:
                    #     print("Erro na requisição:", e)
                    tela_confirmar_envio_dados.open = False
                    tela_confirmar_envio_dados.update()
                    page.update()
                    try:
                        dados = (f"{num_mesa.value}", string_pedido, True, False, f"{total.spans[1].text}")
                        # Conexão (use os mesmos parâmetros do seu script)
                        conn = psycopg2.connect(
                            host="dpg-d57jh96uk2gs73d3dbk0-a.oregon-postgres.render.com",
                            port="5432",
                            database="bd_sherlon_ulac",
                            user="bd_sherlon_ulac_user",
                            password="synMXbst2UAOQJQJMWKNvUlRFHSGnfBd"
                        )
                        cursor = conn.cursor()
                        # Comando SQL
                        sql = """
                        INSERT INTO pedidos_mamae (numero_mesa, pedido, visivel, is_delete, total)
                        VALUES (%s, %s, %s, %s, %s);
                        """
                        # Executar o INSERT com os dados
                        cursor.execute(sql, dados)
                        # Confirmar a transação
                        conn.commit()
                        mensagem_confirmado(texto='pedido enviado com sucesso!')
                        total.spans[1].text = 0
                        total.update()
                    except psycopg2.Error as e:
                        def fechar_tela_confirmado(e):
                            tela_confirmado1.open = False
                            tela_confirmado1.update()
                            page.update()
                        tela_confirmado1 = ft.AlertDialog(
                            content_padding=ft.padding.only(bottom=-10),
                            open=True,
                            bgcolor=ft.Colors.WHITE,
                            content=ft.Container(
                                width=100,
                                height=300,
                                padding=ft.padding.all(10), 
                                content=ft.Column(
                                controls=[
                                    ft.Container(
                                        image=ft.DecorationImage(src='negado.webp',fit=ft.ImageFit.FILL),
                                        width=200,
                                        height=150,
                                        bgcolor=ft.Colors.WHITE
                                    ),
                                    ft.Text(value='erro interno ao enviar pedido por favor chame o garçon para te atender melhor'.upper(),text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,italic=True),
                                    ft.ElevatedButton(
                                text='ok',
                                bgcolor=ft.Colors.BLACK,
                                color=ft.Colors.WHITE,
                                width=300,
                                on_click=fechar_tela_confirmado
                            )
                                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                            )
                        )
                        page.open(tela_confirmado1)
                    lista_lanches.content.controls = []
                    total.spans[1].text = 0.00
                    lista_lanches.update()
                def fechar_tela_confirmado(e):
                    tela_confirmar_envio_dados.open = False
                    tela_confirmar_envio_dados.update()
                    page.update()
                tela_confirmar_envio_dados = ft.AlertDialog(
                    content_padding=ft.padding.only(bottom=-10),
                    open=True,
                    bgcolor=ft.Colors.WHITE,
                    content=ft.Container(
                        width=100,
                        height=150,
                        padding=ft.padding.only(bottom=10,left=10,right=10,top=30), 
                        content=ft.Column(
                        controls=[
                            ft.Text(value='tem certeza que deseja finalizar o pedido?'.upper(),text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,italic=True),
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                        text='não',
                        bgcolor=ft.Colors.BLACK,
                        color=ft.Colors.WHITE,
                        width=100,
                        on_click=fechar_tela_confirmado
                    ),
                    ft.ElevatedButton(
                        text='sim',
                        bgcolor=ft.Colors.BLACK,
                        color=ft.Colors.WHITE,
                        width=100,
                        on_click=enviar_dados
                    )
                                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            )
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                    )
                )
                page.open(tela_confirmar_envio_dados)

            nome = ft.Container(
                #bgcolor=ft.Colors.RED,
                content=ft.Column(
                    controls=[
                        ft.Text(value='por favor digite seu nome abaixo.'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                        ft.Row(
                            controls=[
                                ft.Text(value='nome:'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                                ft.TextField(width=200,border=ft.InputBorder.UNDERLINE,height=40,hint_text='digite seu nome aqui.'.upper())
                            ],vertical_alignment=ft.CrossAxisAlignment.END
                        )
                    ]
                )
            )
            mesa = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(value='selecione o numero da mesa abaixo.'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                        ft.Row(
                            controls=[
                                ft.Text(value='mesa:'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                            num_mesa:= ft.Dropdown(
                                    width=80,
                                    color=ft.Colors.BLACK,
                                    select_icon=None,
                                    options=[ft.dropdown.Option(text=f'{num}') for num in range(1,11)],
                                    
                                )
                            ],vertical_alignment=ft.CrossAxisAlignment.END
                        )
                    ]
                )
            )
            endereco = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(value='digite o endereço da entrega abaixo.'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                    campo_endereco:= ft.Row(
                            controls=[
                                ft.Text(value='endereço:'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                                ft.TextField(width=200,border=ft.InputBorder.UNDERLINE,height=40,hint_text='digite seu endereço aqui.'.upper())
                            ],vertical_alignment=ft.CrossAxisAlignment.END
                        )
                    ]
                )
            )
            delivery = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(value='delivery?'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Text(value='clique aqui'.upper(),weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.RED,
                            border_radius=ft.border_radius.all(20),
                            on_click=mudar_endereco
                        )
                    ]
                )
            )
            botoes_2 = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton(
                            text='confirmar'.upper(),
                            width=600,
                            bgcolor=ft.Colors.BLACK,
                            color=ft.Colors.WHITE,
                            on_click=confirmar
                        ),
                        ft.ElevatedButton(
                            text='voltar'.upper(),
                            width=600,
                            bgcolor=ft.Colors.BLACK,
                            color=ft.Colors.WHITE,
                            on_click=voltar_tela
                        ),
                    ],spacing=5
                )
            )
            tela=ft.AlertDialog(
                open=True,
                content_padding=ft.padding.only(top=10,left=10,right=10,bottom=-10),
                content=ft.Container(
                    width=320,
                    height=400,
                    padding=ft.padding.only(top=10,left=10,right=10,bottom=10),
                    content=ft.Column(
                        controls=[
                            nome,
                            mesa,
                            delivery,
                            botoes_2
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
                
            )
            page.open(tela)
    #parte de cima da aplicação ou o logo        
    logo=ft.Container(
        #expand=True,
        height=150,
        image=ft.DecorationImage(src='logo.jpeg',fit=ft.ImageFit.FILL),
        border_radius=ft.border_radius.all(30)
    )
    # area de selecionar qual as opções de pedido vai quer que apareca na tela
    select=ft.Row(
        controls=[
            ft.Container(height=20,width=5,bgcolor=ft.Colors.BLACK),
            opcao(nome='tradicional'),
            opcao(nome="artesanal"),
            opcao(nome="pastel"),
            opcao(nome="porções"),
            opcao(nome="bebidas"),
            ],scroll=ft.ScrollMode.HIDDEN,height=40,expand=True,adaptive=True
    )
    # area de lanches normais
    #e.control.content.controls[1].value
    lanches=ft.Container(
        padding=ft.padding.all(10),
        content=ft.Column(
            controls=[
                ft.Container(
            bgcolor=ft.Colors.BLACK,
            on_click=tela_lanche,
            scale=0.99,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.YELLOW),
            padding=ft.padding.all(10),
            content=ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                run_spacing=-8,
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_RIGHT,
                        icon_size=35,
                        icon_color=ft.Colors.YELLOW,
                        col=1.25,
                    ),
                    ft.Text(
                        value=item['nome'].upper(),
                        col=6.75,
                        color=ft.Colors.YELLOW,
                        weight=ft.FontWeight.BOLD,
                        italic=True
                        ),
                        ft.Text(
                            value=f"R$ {item['preco']}".upper(),
                            color=ft.Colors.LIGHT_GREEN_ACCENT_700,
                            weight=ft.FontWeight.BOLD,
                            col=4
                        ),
                        ft.Container(col=0.40),
                        ft.Text(
                            value=item['descricao'].upper(),
                            col=11.60,
                            color=ft.Colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                        )
                ]
            )
        ) for item in sorted(
                [item for item in dados_lanche if item['classe'] == "lanche_tradicional"],
                key=lambda x: float(x['preco'].replace(',', '.')))
            ] 
        )

    )
    # area de lanches artesanais
    lanches_artesanais=ft.Container(
        padding=ft.padding.all(10),
        content=ft.Column(
            controls=[
                ft.Container(
            bgcolor=ft.Colors.BLACK,
            on_click=tela_lanche,
            scale=0.99,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.AMBER),
            padding=ft.padding.all(10),
            content=ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                run_spacing=-8,
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_RIGHT,
                        icon_size=35,
                        icon_color=ft.Colors.AMBER,
                        col=1.25,
                    ),
                    ft.Text(
                        value=item['nome'].upper(),
                        col=6.75,
                        color=ft.Colors.AMBER,
                        weight=ft.FontWeight.BOLD,
                        italic=True
                        ),
                        ft.Text(
                            value=f"R$ {item['preco']}".upper(),
                            color=ft.Colors.LIGHT_GREEN_ACCENT_700,
                            weight=ft.FontWeight.BOLD,
                            col=4
                        ),
                        ft.Container(col=0.40),
                        ft.Text(
                            value=item['descricao'].upper(),
                            col=11.60,
                            color=ft.Colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                        )
                ]
            )
        ) for item in sorted(
                [item for item in dados_lanche if item['classe'] == "lanche_artesanal"],
                key=lambda x: float(x['preco'].replace(',', '.')))
            ]
        )
    )
    # area de pasteis
    pasteis=ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
            bgcolor=ft.Colors.BLACK,
            on_click=tela_pastel,
            scale=0.98,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.RED),
            padding=ft.padding.only(left=30,right=0,bottom=10,top=10),
            content=ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                run_spacing=0,
                controls=[
                    # ft.Container(
                    #     col=1,
                    #     height=50
                    # ),
                    ft.Text(
                        value=item['value'].upper(),
                        col=7,
                        color=ft.Colors.RED,
                        weight=ft.FontWeight.BOLD,
                        italic=True,
                        size=17
                        ),
                        ft.Text(
                            value=f"R$ {item['preco']}".upper(),
                            color=ft.Colors.LIGHT_GREEN_ACCENT_700,
                            weight=ft.FontWeight.BOLD,
                            col=4
                        ),
                        ft.Container(col=0.40),
                        # ft.Text(
                        #     value=item['descricao'].upper(),
                        #     col=11.60,
                        #     color=ft.Colors.YELLOW,
                        #     weight=ft.FontWeight.BOLD,
                        # )
                ]
            )
        ) for item in sorted(
                [item for item in dados_pastel ],
                key=lambda x: float(x['preco'].replace(',', '.')))
            ]
        )
    )
    # area de combos
    porcoes=ft.Container(
        ft.Column(
            controls=[
                ft.Container(
            bgcolor=ft.Colors.BLACK,
            on_click=tela_bebida_ou_porcao,
            scale=0.98,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.WHITE),
            padding=ft.padding.symmetric(horizontal=30,vertical=10),
            content=ft.ResponsiveRow(
                controls=[
                    ft.Text(
                        value=item['value'],
                        col=8,
                        color=ft.Colors.WHITE,
                        size=18
                            ),
                    ft.Text(
                        value=f"R$ {item['preco']}",
                        col=4,
                        color=ft.Colors.LIGHT_GREEN_ACCENT_700,
                        size=18
                        ),
                ]
            )
        ) for item in sorted(
                [item for item in dados_porcao_e_bebida if item['classe'] == "porcao"],
                key=lambda x: float(x['preco'].replace(',', '.')))
            ]
        )
    )
    # parte de bebidas da tela e eu estou reutilizando a funçao de porcoes
    bebidas=ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
            bgcolor=ft.Colors.BLACK,
            on_click=tela_bebida_ou_porcao,
            scale=0.98,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLUE_ACCENT),
            padding=ft.padding.symmetric(horizontal=30,vertical=10),
            content=ft.ResponsiveRow(
                controls=[
                    ft.Text(
                        value=item['value'],
                        col=8,
                        color=ft.Colors.BLUE_ACCENT,
                        size=18
                            ),
                    ft.Text(
                        value=f"R$ {item['preco']}",
                        col=4,
                        color=ft.Colors.LIGHT_GREEN_ACCENT_700,
                        size=18
                        ),
                ]
            )
        ) for item in sorted(
                [item for item in dados_porcao_e_bebida if item['classe'] == "bebida"],
                key=lambda x: float(x['preco'].replace(',', '.')))
            ]
        )
    )
    logo_enviar=ft.Container(
        padding=ft.padding.only(top=20,bottom=5,right=10,left=10),
        content=ft.Text(value='carrinho de alimentos'.upper(),size=30,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_900,italic=True)
    )

    lista_lanches = ft.Container(
        padding=ft.padding.symmetric(vertical=20,horizontal=20),
        bgcolor=ft.Colors.WHITE,
        height=300,
        expand=True,
        width=400,
        border_radius=ft.border_radius.all(10),
        shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLACK),
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            #expand=True,
            controls=[
                # ft.Container(
                #     bgcolor=ft.Colors.WHITE,
                #     padding=ft.padding.all(15),
                #     border_radius=ft.border_radius.all(10),
                #     content=ft.ResponsiveRow(
                #     controls=[
                #         ft.Container(
                #             col=10,
                #     padding=ft.padding.symmetric(vertical=10,horizontal=30),
                #     content=ft.Text(value='1x hamburguinho R$ 10,00',size=15,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                #     bgcolor=ft.Colors.WHITE,
                #     shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.BLACK),
                #     border_radius=ft.border_radius.all(10),
                # ),
                # ft.IconButton(
                #     col=2,
                #     bgcolor=ft.Colors.WHITE,
                #     icon=ft.Icons.DELETE_OUTLINE,
                #     icon_color=ft.Colors.RED_900,
                #     alignment=ft.alignment.center,
                    
                # )
                #     ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                # )
                # )  for l in range(5)
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.CENTER,spacing=0
        )
    )
    total = ft.Text(
        spans=[
            ft.TextSpan(text='valor total r$ '.upper(),style=ft.TextStyle(size=15,weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)),
            ft.TextSpan(text=0.00,style=ft.TextStyle(size=15,weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)),
        ]
    )
    # total.spans[1].text += 15.00
    
    # print(total.spans[1])
    botoes = ft.Container(
        content=ft.Column(
            controls=[
                ft.ElevatedButton(text='fazer pedido'.upper(),width=400,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=tela_fazer_pedido),
                ft.ElevatedButton(text='voltar'.upper(),width=400,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=voltar_pricipal),
            ]
        )
    )
    footer = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    col=6,
                    url='https://wa.me/<5575998621227>',
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                
                    image=ft.DecorationImage(src='whatsapp.webp',fit=ft.ImageFit.FILL),
                    width=100,
                    height=100,
                            ),
                            ft.Text(value='75 998621227',color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=-20
                    )
                    
                ),
                ft.Container(
                    col=6,
                    url='https://www.instagram.com/mamae_lanches_e_drinks_/',
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                image=ft.DecorationImage(src='instagran.webp',fit=ft.ImageFit.FILL),
                                width=100,
                                height=100,
                            ),
                            ft.Text(value='@mamae_lanches_e_drinks',color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=-15
                    )
                    
                ),
            ]
        )
    )
    # tela principal da aplicação
    tela_principal=ft.Container(
        expand=True,
        col=12,
        bgcolor=ft.Colors.BLACK,
        #width=400,
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                logo,
                select,
                coluna_nome_lanche(value="lanche tradicional",color=ft.Colors.YELLOW),
                lanches,
                coluna_nome_lanche(value='lanche artesanal',color=ft.Colors.AMBER),
                lanches_artesanais,
                coluna_nome_lanche(value='pastel',color=ft.Colors.RED),
                pasteis,
                coluna_nome_lanche(value='porções',color=ft.Colors.WHITE),
                porcoes,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT),
                bebidas,
                footer

            ],alignment=ft.MainAxisAlignment.CENTER
        )
    )
    tela_enviar_pedido = ft.Container(
        #width=800,
        border_radius=ft.border_radius.all(10),
        col=0,
        padding=ft.padding.all(10),
        bgcolor=ft.Colors.WHITE,
        expand=True,
        content=ft.Column(
            # expand=True,
            # width=600,
            controls=[
                logo_enviar,
                lista_lanches,
                total,
                botoes,
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    layout = ft.ResponsiveRow(
        expand=True,
        controls=[
            tela_principal,
            tela_enviar_pedido
        ]
    )
    def mudar_tela(e):
        tela_principal.col = 0
        tela_enviar_pedido.col = 12
        page.floating_action_button = None 
        page.bgcolor = ft.Colors.WHITE
        page.update()
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.SHOPPING_CART,
        bgcolor=ft.Colors.LIGHT_GREEN_ACCENT_700,
        foreground_color=ft.Colors.BLACK,
        focus_color=ft.Colors.YELLOW,
        on_click=mudar_tela
    )
    page.add(layout)
if __name__ == "__main__":
    ft.app(target=main,assets_dir='assets')