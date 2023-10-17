from hashmap import *  # Importa a classe HashTable do módulo "hashmap"

def main():
    eventos = HashTable()  # Cria uma instância da classe HashTable para armazenar eventos
    
    while True:
        # Exibe um menu de opções para o usuário
        print("\nMenu:\n1. Adicionar Evento\n2. Mostrar Eventos por Categoria\n3. Listar Categorias\n4. Remover Evento\n5. Sair")
        escolha = input("Escolha uma opção: ")  # Solicita a escolha do usuário
        
        if escolha == "1":
            # Opção 1: Adicionar um evento à tabela hash
            nome = input("Digite o nome do evento: ")
            categoria = input("Digite a categoria do evento: ")
            descricao = input("Digite a descrição do evento: ")
            evento = (nome, descricao)  # Cria uma tupla com o nome e descrição do evento
            eventos.put(nome, categoria)  # Adiciona o evento à tabela hash
            print("Evento adicionado com sucesso!")
        
        elif escolha == "2":
            # Opção 2: Mostrar eventos com base em uma categoria específica
            categoria = input("Digite a categoria do evento: ")
            eventos_categoria = eventos.get_by_categoria(categoria)  # Obtém eventos por categoria
            
            if not eventos_categoria:
                print(f"Nenhum evento encontrado na categoria '{categoria}'.")
            else:
                print(f"Eventos na categoria '{categoria}': {', '.join(eventos_categoria)}")
                # Exibe os eventos na categoria especificada
        elif escolha == "3":
            # Opção 3: Listar as categorias disponíveis na tabela hash
            print("\nCategorias disponíveis:")
            print(eventos)  # Chama o método __str__ da classe para listar as categorias
            
        
        elif escolha == "4":
            # Opção 4: Remover um evento da tabela hash
            evento = input("Digite o nome do evento: ")
            if eventos.remove(evento):
                print("Evento removido com sucesso!")
            else:
                print("Evento não encontrado.")
        
        elif escolha == "5":
            # Opção 5: Sair do programa
            print('Saindo...')
            break  # Encerra o loop e finaliza o programa
        
        else:
            print("Opção inválida.")  # Mensagem de erro para opções inválidas

if __name__ == "__main__":
    main()  # Chama a função principal "main" quando o script é executado