from colorama import Fore, Style, init
init(autoreset=True)

pecas = []
caixas = []
caixa_atual = []


def avaliar_peca(peso, cor, comprimento):
    motivos = []

    if not (95 <= peso <= 105):
        motivos.append("Peso fora do padrão")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida")

    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do padrão")

    if len(motivos) == 0:
        return "Aprovada", None
    else:
        return "Reprovada", motivos


def cadastrar_peca():
    id_peca = input("ID da peça: ")
    peso = float(input("Peso (g): "))
    cor = input("Cor: ")
    comprimento = float(input("Comprimento (cm): "))

    status, motivos = avaliar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivos": motivos
    }

    pecas.append(peca)

    if status == "Aprovada":
        adicionar_na_caixa(peca)

    print(f"\nPeça {status}!")


def adicionar_na_caixa(peca):
    global caixa_atual

    caixa_atual.append(peca)

    if len(caixa_atual) == 10:
        caixas.append(caixa_atual)
        print("📦 Caixa fechada com 10 peças!")
        caixa_atual = []


def listar_pecas():
    if not pecas:
        print("\nNenhuma peça cadastrada.")
        return

    print(f"{Fore.GREEN}\n=== PEÇAS APROVADAS ==={Style.RESET_ALL}")
    for p in pecas:
        if p["status"] == "Aprovada":
            print(f'ID: {p["id"]} | Peso: {p["peso"]} | Cor: {p["cor"]} | Comprimento: {p["comprimento"]}')

    print(f"{Fore.RED}\n=== PEÇAS REPROVADAS ==={Style.RESET_ALL}")
    for p in pecas:
        if p["status"] == "Reprovada":
            print(f'ID: {p["id"]} | Motivos: {", ".join(p["motivos"])}')


def remover_peca():
    id_peca = input("Digite o ID da peça para remover: ")

    for p in pecas:
        if p["id"] == id_peca:
            pecas.remove(p)

            # remover da caixa atual
            if p in caixa_atual:
                caixa_atual.remove(p)

            # remover das caixas fechadas
            for caixa in caixas:
                if p in caixa:
                    caixa.remove(p)

            print(f"{Fore.YELLOW}Peça removida com sucesso!{Style.RESET_ALL}")
            return

    print(f"{Fore.RED}Peça não encontrada!{Style.RESET_ALL}")


def listar_caixas():
    
    if not caixas:
        print("\nNenhuma caixa fechada ainda.")
        return

    for i, caixa in enumerate(caixas, start=1):
        print(f"\n📦 Caixa {i}:")
        for p in caixa:
            print(f'ID: {p["id"]}')

def relatorio_final():
    aprovadas = 0
    reprovadas = 0
    motivos_reprovacao = {}

    for p in pecas:
        if p["status"] == "Aprovada":
            aprovadas += 1
        else:
            reprovadas += 1
            for motivo in p["motivos"]:
                if motivo in motivos_reprovacao:
                    motivos_reprovacao[motivo] += 1
                else:
                    motivos_reprovacao[motivo] = 1

    print(f"{Fore.YELLOW}\n=== RELATÓRIO FINAL ==={Style.RESET_ALL}")
    print(f"Total aprovadas: {aprovadas}")
    print(f"Total reprovadas: {reprovadas}")
    print(f"Caixas utilizadas: {len(caixas)}")
    print(f"Peças na caixa atual: {len(caixa_atual)}")

    print("\nMotivos de reprovação:")
    for motivo, qtd in motivos_reprovacao.items():
        print(f"{motivo}: {qtd}")


def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar peça")
        print("2 - Listar peças")
        print("3 - Remover peça")
        print("4 - Listar caixas fechadas")
        print("5 - Gerar relatório")
        print("6 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            relatorio_final()
        elif opcao == "6":
            print("Encerrando sistema...")
            break
        else:
            print(f'{Fore.RED}Opção inválida!{Style.RESET_ALL}')


menu()
