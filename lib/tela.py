import flet as ft


def pagina (page: ft.Page, app):
    page.title = 'Gerador de Planilhas'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "auto"
    page.auto_scroll = True


    # Coleta os dados dos text fields
    def adicionar(e):
        if text_usuario.value == "":
            not_add_snackbar = ft.SnackBar(ft.Text("Preencha os dados do Computador"))
            page.overlay.append(not_add_snackbar)
            not_add_snackbar.open = True
            page.update()
        else:
            app.novocomputador(  # Instancia objeto novo computador,
                setor = text_setor.value,
                usuario = text_usuario.value,
                patrimonio = text_patrimonio.value,
                processador = text_processador.value,
                memoria = text_memoria.value,
                armazenamento = text_armazenamento.value,
                marca_processador = drop_marca_processador.value,
                dispositivo = drop_dispositivo.value,
                qualidade = drop_qualidade.value,
                situacao = drop_situacao.value,
                gpu = "Sim" if check_gpu.value else "Não",
                placaderede = "Sim" if check_placa_rede.value else "Não",
                marca_mouse = "N/E" if drop_dispositivo.value=="Notebook" else text_marca_mouse.value,
                tipo_mouse = drop_tipo_mouse.value,
                marca_teclado = "N/E" if drop_dispositivo.value=="Notebook" else text_marca_teclado.value,
                tipo_teclado = drop_tipo_teclado.value,
                )
            # Se computador for salvo corretamente
            add_snackbar = ft.SnackBar(ft.Text("Computador salvo com sucesso!"))
            page.overlay.append(add_snackbar)
            add_snackbar.open = True
            page.update()
            limpar_selecao(e)

    def limpar_selecao(e):
        text_setor.value = ""
        text_usuario.value = ""
        text_patrimonio.value = ""
        text_processador.value = ""
        text_memoria.value = ""
        text_armazenamento.value = ""
        text_marca_mouse.value = ""
        text_marca_teclado.value = ""
        check_gpu.value = False
        check_placa_rede.value = False
        page.update()

    def gerar_tabela(e):
        nome_planilha_sufix = text_nome_planilha.value
        if nome_planilha_sufix == '':
            tablename_snackbar = ft.SnackBar(ft.Text("Escreva o nome da planilha"))
            page.overlay.append(tablename_snackbar)
            tablename_snackbar.open = True
            page.update()
        else:
            if not nome_planilha_sufix.endswith('.xlsx'):
                nome_planilha_sufix += '.xlsx'
            file_path = app.gera_planilha(nome_planilha=nome_planilha_sufix)
            if file_path:
                tabledone_snackbar = ft.SnackBar(ft.Text("Planilha gerada com sucesso!"))
                page.overlay.append(tabledone_snackbar)
                tabledone_snackbar.open = True
            else:
                nottabledone_snackbar = ft.SnackBar(ft.Text("Erro ao gerar a planilha."))
                page.overlay.append(nottabledone_snackbar)
                nottabledone_snackbar.open = True
            page.update()

    # Itens da tela/ widgets
    # Text fields
    text_setor = ft.TextField(label='Setor',border_color=ft.colors.GREY_400, width=180, text_align=ft.TextAlign.LEFT)
    text_usuario = ft.TextField(label='Usuário/Função',border_color=ft.colors.GREY_400, width=365, text_align=ft.TextAlign.LEFT)
    text_patrimonio = ft.TextField(label='nº Patrimônio', width=180,border_color=ft.colors.GREY_400, text_align=ft.TextAlign.LEFT)
    text_processador = ft.TextField(label='Processador',border_color=ft.colors.GREY_400, width=230, text_align=ft.TextAlign.LEFT)
    text_memoria = ft.TextField(label='Memória (GB/DDR3/DDR4)', border_color=ft.colors.GREY_400,width=365, text_align=ft.TextAlign.LEFT)
    text_armazenamento = ft.TextField(label='Armazenamento (SSD/HDD)',border_color=ft.colors.GREY_400, width=365, text_align=ft.TextAlign.LEFT)
    text_marca_teclado = ft.TextField(label='Marca Teclado',border_color=ft.colors.GREY_400, width=230, text_align=ft.TextAlign.LEFT)
    text_marca_mouse = ft.TextField(label='Marca Mouse',border_color=ft.colors.GREY_400, width=230, text_align=ft.TextAlign.LEFT)
    text_nome_planilha = ft.TextField(label='Nome da Planilha',suffix_text='.xlsx', hint_text='Preencher ao Gerar Planilha',
                                      border_color=ft.colors.GREY_400, width=365, text_align=ft.TextAlign.LEFT)

    # Botões
    botao_adicionar = ft.ElevatedButton(text='Adicionar PC',icon=ft.icons.SAVE, color=ft.colors.BLACK,bgcolor=ft.colors.BLUE, on_click=adicionar)
    botao_limpar = ft.ElevatedButton(text='Limpar seleção',icon=ft.icons.DELETE, color=ft.colors.BLACK, bgcolor=ft.colors.RED, on_click=limpar_selecao)
    botao_gerar_tabela = ft.ElevatedButton(text='Gerar Tabela',icon=ft.icons.ADD_TASK, color=ft.colors.BLACK,bgcolor=ft.colors.GREEN, on_click=gerar_tabela)

    # Dropdowns
    drop_marca_processador = ft.Dropdown(label='Marca', border_color=ft.colors.GREY_400, width=130,
                                                                    options=[ft.dropdown.Option('Intel'),
                                                                            ft.dropdown.Option('AMD')])
    drop_dispositivo = ft.Dropdown(label='Dispositivo',border_color=ft.colors.GREY_400, width=160,
                                                                    options=[ft.dropdown.Option('Notebook'),
                                                                            ft.dropdown.Option('Desktop')])
    drop_qualidade = ft.Dropdown(label='Qualidade',border_color=ft.colors.GREY_400, width=160,
                                                                    options=[ft.dropdown.Option('Ótimo'),
                                                                            ft.dropdown.Option('Bom'),
                                                                            ft.dropdown.Option('Médio'),
                                                                            ft.dropdown.Option('Ruim'),])
    drop_situacao = ft.Dropdown(label='Situação',border_color=ft.colors.GREY_400, width=335,
                                                                    options=[ft.dropdown.Option('Atualizado'),
                                                                            ft.dropdown.Option('Aprimorável'),
                                                                            ft.dropdown.Option('Obsoleto'),
                                                                            ft.dropdown.Option('Descarte'),])
    drop_tipo_teclado = ft.Dropdown(label='Teclado Tipo:', border_color=ft.colors.GREY_400, width=130,
                                                                    options=[ft.dropdown.Option('USB'),
                                                                             ft.dropdown.Option('PS2'),
                                                                             ft.dropdown.Option('N/E'),
                                                                    ])
    drop_tipo_mouse = ft.Dropdown(label='Mouse Tipo:', border_color=ft.colors.GREY_400, width=130,
                                                                    options=[ft.dropdown.Option('USB'),
                                                                             ft.dropdown.Option('PS2'),
                                                                             ft.dropdown.Option('N/E'),
                                                                    ])
    # Checkbox
    check_gpu = ft.Checkbox(label='Possui Placa de Video',value=False)
    check_placa_rede = ft.Checkbox(label='Possui Placa de Rede', value=False)

    # Montagem do layout da tela
    page.add(
        ft.Container(height=50),
        ft.Text('InventoryXcel'),
        ft.Divider(),
        ft.Column([
            ft.Column(
                [ft.Row([
                    text_setor,
                    text_patrimonio,
                ],alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                text_usuario,
                ft.Row([
                    text_processador,
                    drop_marca_processador
                ],alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                text_memoria,
                text_armazenamento,
                ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=10),
            ft.Column([
                ft.Row([
                    drop_dispositivo,
                    check_gpu
                ],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    drop_qualidade,
                    check_placa_rede
                ],alignment=ft.MainAxisAlignment.CENTER),
                drop_situacao
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Row([
                text_marca_mouse,
                drop_tipo_mouse
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
            ft.Row([
                text_marca_teclado,
                drop_tipo_teclado
            ],alignment=ft.MainAxisAlignment.CENTER, spacing=5),
            ft.Row([
                botao_adicionar,
                botao_limpar
            ],alignment=ft.MainAxisAlignment.CENTER, spacing=5),
            ft.Divider(),
            ft.Text('Finalizar setor ?'),
            text_nome_planilha,
            botao_gerar_tabela,
            ft.Divider(),
            ft.Text('by José Guilherme Neves')
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

