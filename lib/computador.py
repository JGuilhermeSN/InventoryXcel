class Novo_computador:
    def __init__(self, setor, usuario, patrimonio, processador, memoria, armazenamento,
                  marca_processador, dispositivo, qualidade, situacao, gpu, placaderede,
                  marca_mouse, tipo_mouse, marca_teclado, tipo_teclado):
        self.setor = setor
        self.usuario = usuario
        self.patrimonio = patrimonio
        self.processador = processador
        self.memoria = memoria
        self.armazenamento = armazenamento
        self.marca_processador = marca_processador
        self.dispositivo = dispositivo
        self.qualidade = qualidade
        self.situacao = situacao
        self.gpu = gpu
        self.placaderede = placaderede
        self.marca_mouse = marca_mouse
        self.marca_teclado = marca_teclado
        self.tipo_mouse = tipo_mouse
        self.tipo_teclado = tipo_teclado


    def to_dict(self):
        return {
            'Patrimônio': self.patrimonio,
            'Setor': self.setor,
            'Usuário': self.usuario,
            'Processador': self.processador,
            'Memória': self.memoria,
            'Marca Processador': self.marca_processador,
            'Armazenamento': self.armazenamento,
            'Dispositivo': self.dispositivo,
            'Qualidade': self.qualidade,
            'Situação': self.situacao,
            'Placa de Video': self.gpu,
            'Placa de Rede': self.placaderede,
            'Marca Mouse': self.marca_mouse,
            'Tipo Mouse': self.tipo_mouse,
            'Marca Teclado': self.marca_teclado,
            'Tipo Teclado': self.tipo_teclado
    }

