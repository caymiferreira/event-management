class HashTable:
    def __init__(self):
        self._tamanho = 100  # Inicializa o tamanho da tabela hash como 100
        self._slots = [None] * self._tamanho  # Inicializa a lista de slots com 'None'
        self._valores = [None] * self._tamanho  # Inicializa a lista de valores com 'None'

    def hashfunction(self, chave):
        total = 0
        for char in chave:
            total += ord(char)  # Calcula o valor hash somando as ordenadas dos caracteres na chave
        return total % self._tamanho  # Retorna o valor hash calculado

    def rehash(self, oldhash):
        return (oldhash + 1) % self._tamanho  # Lida com colisões, incrementando o valor hash

    def put(self, chave, valor):
        valor_hash = self.hashfunction(chave)  # Calcula o valor hash da chave

        while self._slots[valor_hash] is not None and self._slots[valor_hash] != chave:
            valor_hash = self.rehash(valor_hash)  # Lida com colisões e encontra um slot vazio
        self._slots[valor_hash] = chave  # Armazena a chave no slot correspondente
        self._valores[valor_hash] = valor  # Armazena o valor associado à chave

    def get(self, chave):  # Retorna a categoria do evento com base na chave
        valor_hash = self.hashfunction(chave)  # Calcula o valor hash da chave

        while self._slots[valor_hash] is not None:
            if self._slots[valor_hash] == chave:  # Encontra a chave correspondente
                return self._valores[valor_hash]  # Retorna o valor associado à chave
            valor_hash = self.rehash(valor_hash)  # Lida com colisões, se necessário

        return None  # Retorna 'None' se a chave não for encontrada

    def get_by_categoria(self, categoria):
        # Retorna uma lista de eventos associados a uma categoria específica
        eventos = [self._slots[i] for i in range(self._tamanho) if self._valores[i] == categoria]
        return eventos

    def remove(self, chave):
        valor_hash = self.hashfunction(chave)  # Calcula o valor hash da chave

        while self._slots[valor_hash] is not None:
            if self._slots[valor_hash] == chave:  # Encontra a chave correspondente
                self._slots[valor_hash] = None  # Remove a chave do slot
                self._valores[valor_hash] = None  # Remove o valor associado à chave
                return True  # Indica que a remoção foi bem-sucedida
            valor_hash = self.rehash(valor_hash)  # Lida com colisões, se necessário

        return False  # Indica que a chave não foi encontrada

    def redimensionar(self):
        novo_tamanho = self._tamanho * 2
        while not self.e_primo(novo_tamanho):  # Encontra um novo tamanho que seja um número primo
            novo_tamanho += 1

        novo_slots = [None] * novo_tamanho
        novo_valores = [None] * novo_tamanho

        for i in range(self._tamanho):
            if self._slots[i] is not None:
                novo_hash = self.hashfunction(self._slots[i]) % novo_tamanho
                while novo_slots[novo_hash] is not None:
                    novo_hash = self.rehash(novo_hash) % novo_tamanho
                novo_slots[novo_hash] = self._slots[i]
                novo_valores[novo_hash] = self._valores[i]

        self._tamanho = novo_tamanho  # Atualiza o tamanho
        self._slots = novo_slots  # Atualiza os slots
        self._valores = novo_valores  # Atualiza os valores

    def e_primo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:  # Verifica se o número é primo
                return False
        return True

    def __getitem__(self, chave):
        return self.get(chave)

    def __setitem__(self, chave, valor):
        self.put(chave, valor)

    def __str__(self):
        categorias = ""
        for categoria in self._valores:
            if categoria is not None and categoria not in categorias:
                categorias += str(categoria) + " "
        return str(categorias)
