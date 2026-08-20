# ==============================================================================
# SISTEMA DE GERENCIAMENTO - COFFEE SHOPS TIA ROSA
# ==============================================================================

# Estoque de insumos/ingredientes em memória

estoque_ingredientes = {
    "café (g)": 5000,          # 1000g (1kg)
    "leite (ml)": 15000,        # 5000ml (5L)
    "água (ml)": 50000,
    "açúcar (g)": 7000,         # 1000g (1kg)
    "canela (g)": 250,          # 250g
    "chocolate (g)": 5000,      # 1000g (1kg)
    "polpa morango (un)": 60,
    "polpa laranja (un)": 60,
    "polpa abacaxi (un)": 60,
    "farinha (g)": 10000,        # 1000g (1kg)
    "ovos (un)": 200,
    "manteiga (g)": 5000,        # 1000g (1kg)
    "frango (g)": 7000,          # 1000g (1kg)
    "requeijão (g)": 2000        # 1000g (1kg)
}
# Lista de produtos (descrição do produto, preço e ingredientes)
cardapio = [
    {
        "nome": "Cappuccino",
        "preço": float(17.50),
        "ingredientes": "café, leite, canela e chocolate.",
        "receita": {
            "café (g)": 20,
            "leite (ml)": 150,
            "canela (g)": 5,
            "chocolate (g)": 15
        }
    },
    {
        "nome": "Café",
        "preço": float(8.00),
        "ingredientes": "café, água e açúcar.",
        "receita": {
            "café (g)": 10,
            "água (ml)": 100,
            "açúcar (g)": 5
        }
    },
    {
        "nome": "Suco",
        "preço": float(14.00),
        "ingredientes": "fruta/polpa, água e açúcar.",
        "tipos": "morango, laranja, abacaxi.",
        "receita": {
            "polpa morango (un)": 1,
            "polpa laranja (un)": 1,
            "polpa abacaxi (un)": 1,
            "água (ml)": 150,
            "açúcar (g)": 15
        }
    },
    {
        "nome": "Bolo",
        "preço": float(12.00),
        "ingredientes": "farinha de trigo, ovos, açúcar, leite, manteiga.",
        "tipos": "chocolate, baunilha.",
        "receita": {
            "farinha (g)": 200,
            "ovos (un)": 3,
            "açúcar (g)": 50,
            "leite (ml)": 150,
            "manteiga (g)": 30
         }
    },

    {
        "nome": "Coxinha de frango",
        "preço": float(16.00),
        "ingredientes": "farinha de trigo, água, frango, requeijão, temperos.",
        "receita": {
            "farinha (g)": 100,
            "água (ml)": 100,
            "frango (g)": 100,
            "requeijão (g)": 50,
          }
    }

]
# dicionário de cliente e histórico de vendas

clientes = {}
historico_vendas = []

# Funcionalidade do sistema de gerenciamento - COFFEE SHOPS TIA ROSA
# ------------------------------------------------------------------------------------------

def exibir_cabecalho(titulo):
    # Exibe um título formatado e centralizado no terminal.
    print("\n" + "=" * 60)
    print(f"{titulo:^60}")
    print("=" * 60)

def exibir_cardapio_completo():
    # Percorre e imprime os itens do cardápio detalhado
    exibir_cabecalho("COFFEE SHOPS TIA ROSA - CARDÁPIO DETALHADO")
    for i, produto in enumerate(cardapio, 1):
        print(f"[{i}] {produto['nome'].upper()} - R$ {produto['preço']:.2f}")
        print(f"    │ Ingredientes: {produto['ingredientes']}")
        if "tipos" in produto:
            print(f"    └ Tipos disponíveis: {produto['tipos']}")
        print("-" * 60)

# Acesso e gerenciamento do cardápio
def cadastrar_produto():
    # Cadastra um novo produto no cardápio e mapeia sua receita de ingredientes.
    exibir_cabecalho("CADASTRO DE NOVO PRODUTO NO CARDÁPIO")

    nome = input("Digite o nome do produto: ").strip().capitalize()

    if not nome:
        print("O nome do produto não pode ser vazio.")
        return

    for item in cardapio:
        if item["nome"].lower() == nome.lower():
            print(f"O produto '{nome}' já existe no cardápio!")
            return

    try:
        preco = float(input(f"Digite o preço de '{nome}' (R$): "))
        if preco <= 0:
            print("O preço deve ser maior que zero.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número decimal (ex: 15.50).")
        return

    ingredientes_descricao = input("Descrição rápida dos ingredientes (para exibição no menu): ").strip()

    receita = {}
    print("\n--- MONTAGEM DA RECEITA DO PRODUTO ---")
    print("Selecione os ingredientes que este produto consome:")

    ingredientes_lista = list(estoque_ingredientes.keys())

    while True:
        if not ingredientes_lista:
            print("Não há ingredientes cadastrados no estoque.")
            break

        print("\nIngredientes disponíveis:")
        for idx, ing in enumerate(ingredientes_lista, 1):
            print(f"{idx}. {ing}")

        try:
            op_ing = int(input("\nDigite o número do ingrediente (ou 0 para finalizar a receita): "))
            if op_ing == 0:
                break
            elif 1 <= op_ing <= len(ingredientes_lista):
                ing_nome = ingredientes_lista[op_ing - 1]

                if ing_nome in receita:
                    print(f"'{ing_nome}' já foi adicionado a este produto.")
                    continue

                qtd_usada = float(input(f"Quantidade de '{ing_nome}' usada por porção: "))
                if qtd_usada > 0:
                    receita[ing_nome] = qtd_usada
                    print(f"Adicionado: {qtd_usada} de {ing_nome}")
                else:
                    print("A quantidade deve ser maior que zero.")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite apenas números válidos.")

    novo_item = {
        "nome": nome,
        "preço": preco,
        "ingredientes": ingredientes_descricao if ingredientes_descricao else "Não especificado.",
        "receita": receita
    }
    cardapio.append(novo_item)
    print(f"\n Produto '{nome}' cadastrado com sucesso por R$ {preco:.2f}!")


def gestao_cardapio():
    # Gerencia a visualização e cadastro do cardápio.
    while True:
        exibir_cabecalho("GESTÃO DO CARDÁPIO")
        print("1. Consultar Cardápio Completo")
        print("2. Cadastrar Novo Produto")
        print("0. Voltar ao Menu Principal")

        sub_opcao = input("\nEscolha uma opção: ").strip()

        if sub_opcao == "1":
            exibir_cardapio_completo()
            input("\nPressione ENTER para voltar...")
        elif sub_opcao == "2":
            cadastrar_produto()
            input("\nPressione ENTER para voltar...")
        elif sub_opcao == "0":
            break
        else:
            print("Opção inválida.")

def cadastrar_cliente():
    # Cadastra um novo cliente no sistema de fidelidade.
    # Garante as 3 perguntas: CPF, Nome e Telefone.
    exibir_cabecalho("CADASTRO DE CLIENTE")
    cpf = input("1. Digite o CPF: ").strip()

    if cpf in clientes:
        print(f"\n Cliente já cadastrado! Nome: {clientes[cpf]['nome']}")

    else:
        nome = input("2. Digite o nome completo do cliente: ").strip()
        telefone = input("3. Digite o número do telefone (com DDD): ").strip()

        clientes[cpf] = {
            "nome": nome,
            "telefone": telefone,
            "pontos": 0
        }
        print(f"\n Cliente '{nome}' cadastrado com sucesso!")


def consultar_cliente():
    # Busca e exibe as informações de um cliente pelo CPF.
    exibir_cabecalho("CONSULTAR CLIENTE")

    if not clientes:
        print("Nenhum cliente cadastrado no sistema até o momento.")
        return

    cpf = input("Digite o CPF do cliente para busca (apenas números): ").strip()

    if cpf in clientes:
        dados = clientes[cpf]
        print("\n" + "-" * 40)
        print("DADOS DO CLIENTE ENCONTRADO")
        print("-" * 40)
        print(f"• CPF: {cpf}")
        print(f"• Nome: {dados['nome']}")
        print(f"• Telefone: {dados['telefone']}")
        print(f"• Pontos Acumulados: {dados['pontos']} ponto(s)")
        print("-" * 40)
    else:
        print("\n Cliente não localizado no sistema.")

# gerenciamento de vendas e estoque
#  Percorre o carrinho e reduz do estoque os ingredientes de cada produto.
def dar_baixa_estoque(carrinho):
    for item_carrinho in carrinho:
        produto_ref = item_carrinho["produto_ref"]
        qtd_comprada = item_carrinho["qtd"]
        nome_completo = item_carrinho["item"].lower()

        if "receita" in produto_ref:
            for ingrediente, qtd_unidade in produto_ref["receita"].items():

                # Desconsidera polpas que não correspondem ao sabor escolhido
                if "polpa" in ingrediente:
                    if "morango" in ingrediente and "morango" not in nome_completo:
                        continue
                    if "laranja" in ingrediente and "laranja" not in nome_completo:
                        continue
                    if "abacaxi" in ingrediente and "abacaxi" not in nome_completo:
                        continue

                # Abate do estoque
                if ingrediente in estoque_ingredientes:
                    qtd_total_consumida = qtd_unidade * qtd_comprada
                    estoque_ingredientes[ingrediente] -= qtd_total_consumida

                    if estoque_ingredientes[ingrediente] < 0:
                        estoque_ingredientes[ingrediente] = 0

def registrar_pedido():
    exibir_cabecalho("NOVO PEDIDO")
# Registro de pedidos dos clientes.
# Registra uma venda, pergunta o tipo do produto (se houver) e acumula pontos.

    cpf = input("CPF do cliente (ou pressione ENTER para consumidor não identificado): ").strip()
    cliente_nome = "Consumidor Não Identificado"

    if cpf in clientes:
        cliente_nome = clientes[cpf]["nome"]
        print(f" Cliente identificado: {cliente_nome}")
    elif cpf:
        print("CPF não encontrado. O pedido será registrado sem acúmulo de pontos.")

    carrinho = []
    total_pedido = 0.0

    exibir_cardapio_completo()

    while True:
        entrada_opcao = input("\nDigite o número do produto desejado (ou 0 para finalizar a seleção): ").strip()
        
        if not entrada_opcao.isdigit():
            print("Entrada inválida. Digite apenas o número correspondente ao item no cardápio.")
            continue

        opcao = int(entrada_opcao)

        if opcao == 0:
            break
        elif 1 <= opcao <= len(cardapio):
            item = cardapio[opcao - 1]              
            nome_item = item['nome']

            if "tipos" in item:
                print(f"Tipos disponíveis para {item['nome']}: {item['tipos']}")
                tipo_escolhido = input(f"Qual o tipo/sabor do {item['nome']}? ").strip()
                if tipo_escolhido:
                    nome_item = f"{item['nome']} ({tipo_escolhido})"

            entrada_qtd = input(f"Quantidade de '{nome_item}': ").strip()
            
            if not entrada_qtd.isdigit() or int(entrada_qtd) <= 0:
                print("Quantidade inválida! Por favor, insira um número maior que zero.")
                continue

            qtd = int(entrada_qtd)
            subtotal = item['preço'] * qtd

            carrinho.append({
                "produto_ref": item,
                "item": nome_item, 
                "qtd": qtd, 
                "subtotal": subtotal
            })
            total_pedido += subtotal
            print(f"{qtd}x {nome_item} adicionado(s) ao carrinho!")
        else:
            print("Opção inválida. Escolha um número que exista no cardápio.")

    if not carrinho:
        print("\n Pedido cancelado. Nenhum item foi selecionado.")
        return

    # Resumo do Pedido
    exibir_cabecalho("RESUMO DO PEDIDO")
    print(f"Cliente: {cliente_nome}")
    for item in carrinho:
        print(f"- {item['qtd']}x {item['item']} | Subtotal: R$ {item['subtotal']:.2f}")
    print(f"\nTotal do Pedido: R$ {total_pedido:.2f}")

    # Pontuação (1 ponto a cada R$ 10,00)
    if cpf in clientes:
        pontos_ganhos = int(total_pedido // 10)
        clientes[cpf]["pontos"] += pontos_ganhos
        print(f"Pontos acumulados nesta compra: {pontos_ganhos}")
        print(f"Total de pontos atualizados: {clientes[cpf]['pontos']}")

    # Executa a baixa e armazena no histórico. 
    dar_baixa_estoque(carrinho)

    historico_vendas.append({
        "cliente": cliente_nome,
        "itens": carrinho.copy(),
        "total": total_pedido
    })    
    print("\n Pedido finalizado com sucesso!")

# Exibe o histórico de vendas diárias
def exibir_relatorio_vendas():
    # Apresenta o resumo das vendas efetuadas.
    exibir_cabecalho("RELATÓRIO DE VENDAS DIÁRIAS")
    if not historico_vendas:
        print("Nenhuma venda realizada até o momento.")
        return

    faturamento_total = 0.0
    for i, venda in enumerate(historico_vendas, 1):
        print(f"Pedido #{i} | Cliente: {venda['cliente']} | Total: R$ {venda['total']:.2f}")
        faturamento_total += venda["total"]

    print("-" * 60)
    print(f"TOTAL DE PEDIDOS: {len(historico_vendas)}")
    print(f"FATURAMENTO TOTAL: R$ {faturamento_total:.2f}")

# Gerenciamento do estoque e cadastro de novos ingredientes (exibe o relatório de estoque do estabelecimento).
def relatorio_estoque_ingredientes():
    # Exibe o estoque atual de cada ingrediente e seu status ajustado por unidade.
    exibir_cabecalho("RELATÓRIO DE ESTOQUE DE INGREDIENTES")

    if not estoque_ingredientes:
        print("Nenhum ingrediente cadastrado.")
        return

    print(f"{'INGREDIENTE':<25} | {'QTD DISPONÍVEL':<15} | {'SITUAÇÃO'}")
    print("-" * 60)

    for ing, qtd in estoque_ingredientes.items():
        # Define limites críticos condizentes com cada unidade de medida
        if "canela" in ing:
            limite_critico = 50      # Especiaria de baixo consumo (50g) 
        elif "(un)" in ing:
            limite_critico = 10      # Menos de 10 unidades
        elif "(g)" in ing:
            limite_critico = 1000    # Menos de 1000g (1kg)
        elif "(ml)" in ing:
            limite_critico = 2000    # Menos de 2000ml (2L)
        else:
            limite_critico = 100

        if qtd <= 0:
            situacao = "ESGOTADO"
        elif qtd <= limite_critico:
            situacao = "CRÍTICO (REPOR)"
        else:
            situacao = "OK"

        print(f"{ing:<25} | {qtd:<15} | {situacao}")

    print("-" * 60)

def abastecer_estoque():
    # Permite ao usuário inserir/adicionar quantidades ao estoque existente.
    exibir_cabecalho("REPOSIÇÃO DE ESTOQUE DE INGREDIENTES")

    print("Ingredientes disponíveis para reposição:\n")
    ingredientes_lista = list(estoque_ingredientes.keys())

    for idx, ing in enumerate(ingredientes_lista, 1):
        print(f"{idx}. {ing} (Atual: {estoque_ingredientes[ing]})")

    try:
        opcao = int(input("\n Digite o número do ingrediente que deseja repor (ou 0 para voltar): "))
        if opcao == 0:
            return
        elif 1 <= opcao <= len(ingredientes_lista):
            ing_selecionado = ingredientes_lista[opcao - 1]
            qtd_adicionar = float(input(f"Digite a quantidade a ADICIONAR em '{ing_selecionado}': "))

            if qtd_adicionar > 0:
                estoque_ingredientes[ing_selecionado] += qtd_adicionar
                print(f"\n Sucesso! Novo saldo de '{ing_selecionado}': {estoque_ingredientes[ing_selecionado]}")
            else:
                print("A quantidade deve ser maior que zero.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")


def cadastrar_novo_ingrediente():
    # Permite cadastrar um ingrediente totalmente novo no sistema.
    exibir_cabecalho("CADASTRO DE NOVO INGREDIENTE")

    nome = input("Digite o nome do ingrediente com a unidade (ex: farinha (g), ovos (un)): ").strip().lower()

    if not nome:
        print("O nome do ingrediente não pode ser vazio.")
        return

    if nome in estoque_ingredientes:
        print(f" O ingrediente '{nome}' já está cadastrado no sistema!")
        return

    try:
        qtd_inicial = float(input(f"Digite a quantidade inicial em estoque para '{nome}': "))
        if qtd_inicial < 0:
            print("A quantidade inicial não pode ser negativa.")
            return

        estoque_ingredientes[nome] = qtd_inicial
        print(f"\n Ingrediente '{nome}' cadastrado com sucesso! Qtd inicial: {qtd_inicial}")
    except ValueError:
        print(" Digite apenas números válidos para a quantidade.")


def gestao_estoque():
    # Gerencia as ações do relatório, reposição e cadastro de ingredientes.
    while True:
        exibir_cabecalho("GESTÃO E RELATÓRIO DE ESTOQUE")
        print("1. Visualizar Situação do Estoque")
        print("2. Adicionar/Repor Quantidade de Ingrediente")
        print("3. Cadastrar Novo Ingrediente")
        print("0. Voltar ao Menu Principal")

        sub_opcao = input("\nEscolha uma opção: ").strip()

        if sub_opcao == "1":
            relatorio_estoque_ingredientes()
            input("\nPressione ENTER para voltar...")
        elif sub_opcao == "2":
            abastecer_estoque()
            input("\nPressione ENTER para voltar...")
        elif sub_opcao == "3":
            cadastrar_novo_ingrediente()
            input("\nPressione ENTER para voltar...")
        elif sub_opcao == "0":
            break
        else:
            print("Opção inválida.")

#  Menu Pincipal (tela exibida para interação com o usuário)
def menu_principal():
    # Gere a navegação do usuário através do menu.
    while True:
        exibir_cabecalho("COFFEE SHOPS TIA ROSA - SISTEMA DE GERENCIAMENTO")
        print("1. Consultar Cardápio")
        print("2. Cadastrar Cliente")
        print("3. Consultar Dados de Cliente")
        print("4. Registrar Novo Pedido")
        print("5. Relatório de Vendas")
        print("6. Relatório de Estoque")
        print("0. Sair do Sistema")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            gestao_cardapio()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "2":
            cadastrar_cliente()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "3":
            consultar_cliente()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "4":
            registrar_pedido()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "5":
            exibir_relatorio_vendas()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "6":
            gestao_estoque()  
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "0":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()


