import json
import os

# Caminho para o arquivo de dados
DATA_FILE = 'shopping_list.json'

def load_data():
    """Carrega a lista de compras do arquivo de dados, se existir."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    """Salva a lista de compras no arquivo de dados."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def display_list(shopping_list):
    """Exibe a lista de compras com os itens e seu status."""
    if not shopping_list:
        print("A lista de compras está vazia.")
        return

    for idx, (item, bought) in enumerate(shopping_list.items(), start=1):
        status = "Comprado" if bought else "Não comprado"
        print(f"{idx}. {item} - {status}")

def add_item(shopping_list):
    """Adiciona um novo item à lista de compras."""
    item = input("Digite o nome do item para adicionar: ").strip()
    if item:
        shopping_list[item] = False
        print(f"Item '{item}' adicionado à lista.")
    else:
        print("Nome do item não pode ser vazio.")

def mark_item_as_bought(shopping_list):
    """Marca um item da lista como comprado."""
    display_list(shopping_list)
    try:
        index = int(input("Digite o número do item para marcar como comprado: ")) - 1
        item = list(shopping_list.keys())[index]
        if item:
            shopping_list[item] = True
            print(f"Item '{item}' marcado como comprado.")
    except (IndexError, ValueError):
        print("Número de item inválido.")

def main():
    shopping_list = load_data()

    while True:
        print("\nMenu:")
        print("1. Exibir lista de compras")
        print("2. Adicionar item")
        print("3. Marcar item como comprado")
        print("4. Sair")

        choice = input("Escolha uma opção: ").strip()

        if choice == '1':
            display_list(shopping_list)
        elif choice == '2':
            add_item(shopping_list)
        elif choice == '3':
            mark_item_as_bought(shopping_list)
        elif choice == '4':
            save_data(shopping_list)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
