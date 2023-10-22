class Cliente:

    def __init__(self,endereco):
        self._endereco = endereco
        self.conta = []

    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)