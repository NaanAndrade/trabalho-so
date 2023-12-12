import random

class Escalonador:
    def __init__(self):
        self.processList = []

    def add_process(self, processo):
        if self.processList is None:
            self.processList = []
        self.processList.append(processo)

    def fcfs(self):
        tempo_espera = 0
        t_p2 = 0

        for processo in self.processList:
            print(f"{processo}")
            print(f"Tempo de Espera: {tempo_espera}\n")
            tempo_espera += processo.tempo_execucao

            t_p2 = (self.processList[0].tempo_execucao * 2) + self.processList[1].tempo_execucao

        media_espera = t_p2 / len(self.processList)
        print(f"Tempo Médio de Espera: {media_espera:.2f}\n")

        self.imprime_stats()

    def sjf_nao_preemptivo(self):
        self.processList.sort(key=lambda x: x.tempo_execucao)
        tempo_espera = 0
        t_p2 = 0

        for processo in self.processList:
            print(f"{processo}")
            print(f"Tempo de Espera: {tempo_espera}\n")
            tempo_espera += processo.tempo_execucao

            t_p2 = (self.processList[0].tempo_execucao * 2) + self.processList[1].tempo_execucao

        media_espera = t_p2 / len(self.processList)
        print(f"Tempo Médio de Espera: {media_espera:.2f}\n")

        self.imprime_stats()

    def prioridade_nao_preemptivo(self):
        self.processList.sort(key=lambda x: x.prioridade)
        tempo_espera = 0
        t_p2 = 0

        for processo in self.processList:
            print(f"{processo}")
            print(f"Tempo de Espera: {tempo_espera}\n")
            tempo_espera += processo.tempo_execucao

            t_p2 = (self.processList[0].tempo_execucao * 2) + self.processList[1].tempo_execucao

        media_espera = t_p2 / len(self.processList)
        print(f"Tempo Médio de Espera: {media_espera:.2f}\n")

        self.imprime_stats()

    def imprime_stats(self):
        for processo in self.processList:
            print(f"{processo}")
            print(f"Tempo Execução: {processo.tempo_execucao}")
            print(f"Tempo Restante: {processo.tempo_execucao}")
            print(f"Tempo Chegada: {processo.tempo_chegada}")
            print(f"Prioridade: {processo.prioridade}\n")


class Processo:
    ids = 0

    def __init__(self, tempo_execucao, tempo_chegada, prioridade):
        Processo.ids += 1
        self.id = Processo.ids
        self.tempo_execucao = tempo_execucao
        self.tempo_chegada = tempo_chegada
        self.prioridade = prioridade

    def __str__(self):
        return f"Processo {self.id} [Tempo Execução: {self.tempo_execucao}, Tempo Chegada: {self.tempo_chegada}, Prioridade: {self.prioridade}]"


class Main:
    def __init__(self):
        self.inp = None
        self.escalonador = Escalonador()

    def main(self):
        print("=== Simulador de Escalonamento de Processos ===")
        self.inp = input("1: Automático\n2: Manual\n0: Sair\n: ")
        self.principal_menu()

    def principal_menu(self):
        op = int(self.inp)

        while op != 0:
            if op == 1:
                self.add_auto()
                self.menu()
                break
            elif op == 2:
                self.add_manual()
                self.menu()
                break
            elif op == 0:
                print("Código Finalizado.")
                break
            else:
                print("Esta opção não existe.")
                break

    def add_auto(self):
        quantidade_processos = 3
        print("\nAdicionando processos automaticamente:")
        for _ in range(quantidade_processos):
            tempo_execucao = random.randint(1, 20)
            tempo_chegada = random.randint(1, 10)
            prioridade = random.randint(1, 10)

            novo_processo = Processo(tempo_execucao, tempo_chegada, prioridade)
            self.escalonador.add_process(novo_processo)
            print(f"Processo adicionado: {novo_processo}")

    def add_manual(self):
        quantidade_processos = 3
        print("\nAdicionando processos manualmente:")
        for _ in range(quantidade_processos):
            tempo_execucao = int(input("Tempo de Execução: "))
            tempo_chegada = int(input("Tempo de Chegada: "))
            prioridade = int(input("Prioridade: "))

            novo_processo = Processo(tempo_execucao, tempo_chegada, prioridade)
            self.escalonador.add_process(novo_processo)
            print(f"Processo adicionado: {novo_processo}\n")

    def menu(self):
        op = int(input("\nEscolha uma opção:\n1: First-Come, First-Served\n2: Shortest Job First não-preemptivo\n3: Executar Prioridade Não-Preemptivo\n4: Imprimir Status\n0: Sair\n: "))

        while op != 0:
            if op == 1:
                print("\nExecutando FCFS:")
                self.escalonador.fcfs()
                break
            elif op == 2:
                print("\nExecutando SJF Não-Preemptivo:")
                self.escalonador.sjf_nao_preemptivo()
                break
            elif op == 3:
                print("\nExecutando Prioridade Não-Preemptivo:")
                self.escalonador.prioridade_nao_preemptivo()
                break
            elif op == 4:
                print("\nImprimindo Status:")
                self.escalonador.imprime_stats()
                break
            elif op == 0:
                print("\nCódigo finalizado.")
                break
            else:
                print("\nEsta opção não existe.")
                break

if __name__ == "__main__":
    main_obj = Main()
    main_obj.main()
