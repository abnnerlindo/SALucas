class Agendamento:

    def __init__(
        self,
        cliente,
        telefone,
        servico,
        preco,
        barbeiro,
        data,
        horario,
        status='Pendente',
        id=None,
    ):
        self.id = id
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.status = status

    def converte_tupla(self):
        # Retorna apenas os dados para gravação (sem o ID auto-increment)
        return (
            self.cliente,
            self.telefone,
            self.servico,
            self.preco,
            self.barbeiro,
            self.data,
            self.horario,
            self.status,
        )

    @classmethod
    def reverte_tupla(cls, linha):
        # Mapeia a linha do banco (id, cliente, telefone, ...) de volta para o objeto
        return cls(
            id=linha[0],
            cliente=linha[1],
            telefone=linha[2],
            servico=linha[3],
            preco=linha[4],
            barbeiro=linha[5],
            data=linha[6],
            horario=linha[7],
            status=linha[8],
        )