import time

class TarefasDiarias:
    def __init__(self, tarefa, menu):
        self.tarefas = []
        self.tarefas_concluidas = []
        self.tarefa = tarefa
        self.menu = menu

    def mostrar_menu(self):
        self.menu = int(input("""
        selecione o que você deseja fazer:

        [1] adicionar nova tarefa
        [2] visualizar todas as tarefas
        [3] macar tarefa como concluida
        [4] remover uma tarefa
        [5] sair
        """))
        if self.menu == 1:
            return self.adicionar_tarefa()

        elif self.menu == 2:
            return self.visualizar_tarefas()

        elif self.menu == 3:
            return self.concluir_tarefa([])

        elif self.menu == 4:
            return self.remover_tarefa()

        else:
            return self.sair()

    def adicionar_tarefa(self):
        self.tarefa = input("adicione uma nova tarefa: ")
        self.tarefas.append(self.tarefa)
        print(f"tarefa adicionada com sucesso \n\n[1] visualizar todas as tarefas \n[2] adicionar nova tarefa \n[3] voltar ao menu \n")
        menu_adicionar = int(input())

        if menu_adicionar == 1:
            return self.visualizar_tarefas()

        elif menu_adicionar == 2:
            return self.adicionar_tarefa()

        else:
            return self.mostrar_menu()

    def visualizar_tarefas(self):
        i = 1
        if self.tarefas == []:
            print("lista de tarefas ainda está vazia \n[1] adcionar tarefa \n[2] voltar ao menu")
            menu_tarefas = int(input())

            if menu_tarefas == 1:
                return self.adicionar_tarefa
            else:
                return self.mostrar_menu

        for self.tarefa in self.tarefas:
            print(i, self.tarefa, sep=" - ")
            i += 1
        
        print()
        print(f"menu: \n[1] adicionar uma tarefa \n[2] marcar como concluida \n[3] excluir tarefa \n[4] voltar ao menu")
        menu_tarefas = int(input())

        if menu_tarefas == 1:
            return self.adicionar_tarefa()
        
        elif menu_tarefas == 2:
            return self.concluir_tarefa()

        elif menu_tarefas == 3:
            return self.remover_tarefa()

        else:
            return self.mostrar_menu()

    def concluir_tarefa(self, tarefas_concluidas):
        i = 1
        for self.tarefa in self.tarefas:
            print(i, self.tarefa, sep=" - ")

            i += 1

        escolher_tarefa_concluida = int(input("qual tarefa você concluiu? "))

        self.tarefas_concluidas.append(self.tarefas[escolher_tarefa_concluida - 1])
        self.tarefas.pop(escolher_tarefa_concluida - 1)

        print()
        print(f"tarefa marcada como concluída. \n[1] visualizar tarefas concluidas \n[2] voltar ao menu")
        menu_concluir = int(input())

        if menu_concluir == 1:
            return self.visualizar_tarefas_concluidas()

        elif menu_concluir == 2:
            return self.mostrar_menu()
    
    def visualizar_tarefas_concluidas(self):
        i = 1
        print("TAREFAS CONCLUÍDAS")
        for tarefa in self.tarefas_concluidas:
            print(i, tarefa, sep=" - ")
            i += 1
        print()
        print(f"[1] voltar ao menu")
        menu_concluir = int(input())

        if menu_concluir == 1:
            return self.mostrar_menu()

    def remover_tarefa(self):
        i = 1
        for self.tarefa in self.tarefas:
            print(i, self.tarefa, sep=" - ")
            i += 1
        print()
        print("qual tarefa você deseja excluir?")
        menu_remover = int(input())
        self.tarefas.pop(menu_remover -1)

        print()
        print("tarefa removida com sucesso! \n\n[1] voltar ao menu \n[2] adicionar nova tarefa \n[3] visualiza tarefas")
        menu_remover = int(input())

        if menu_remover == 1:
            return self.mostrar_menu()

        elif menu_remover == 2:
            return self.adicionar_tarefa()
          
        elif menu_remover == 3:
            return self.visualizar_tarefas()

    def sair(self):
        print("saindo...")
        time.sleep(2)
        print("sistema finalizado.")
        return None

def main():
    tarefas_diarias = TarefasDiarias("", 0)
    tarefas_diarias.mostrar_menu()

if __name__ == '__main__':
    main()