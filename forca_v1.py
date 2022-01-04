# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
|
|
|
|
=========''', '''

+---+
|   |
|   O
|
|
|
=========''', '''

+---+
|   |
|   O
|   |
|
|
=========''', '''

+---+
|   |
|   O
|  /|
|
|
=========''', '''

+---+
|   |
|   O   
|  /|\  
|
|
=========''', '''

+---+
|   |
|   O   
|  /|\  
|  /   
|
=========''', '''

+---+
|   |   
|   O   
|  /|\  
|  / \  
|
=========''']


# Classe
class Hangman:
    # Método Construtor
    def __init__(self, word):
        
        self.palavra = word
        self.stringErrada = []
        self.stringCorreta = []
        self.stringEscondida = []
        self.listaElementos = []
        print(board[0]+"\n")

        self.sentence = [x for x in word]
        sent_str = ""
        for i in self.sentence:
            sent_str += str(i)
        print("Palavra:",sent_str)

        self.stringPalavra = self.sentence

    # Método para retornar a palavra correta
    def word(self):
        return self.palavra

    # Método para adivinhar a letra
    def guess(self, letter):
        a = self.stringPalavra.count(letter)
        print(self.palavra)
        if a >= 1:
            self.stringCorreta.append(letter)
            for i in range (1,(a+1)):
                b = self.stringPalavra.index(letter)
                print(b)
                self.listaElementos.append(b)
                self.stringPalavra.remove(letter)
                self.stringPalavra.insert(b,0)
        else:
            self.stringErrada.append(letter)
                        
                
    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if len(self.stringErrada) == 6:
            return True

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        pass
        #if len(self.stringCorreta)

    # Método para não mostrar a letra no board
    def hide_word(self):
        sent_udl = ""
        for x in self.stringPalavra:
            sent_udl += "_"
        print("Palavra:", sent_udl)
        self.stringEscondida = sent_udl

        '''
        for i in self.stringEscondida:
            for i in self.listaElementos:
                b = int(i)
            
            self.stringEscondida[b] = self.stringPalavra[b]

        return self.stringEscondida
        '''
        


    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        
        if len(self.stringCorreta) >= 1 or len(self.stringErrada) >= 1:
            print(board[len(self.stringErrada)])
        
        print("\nLetras erradas: ")
        for i in self.stringErrada:
            print(i)

        print("\nLetras corretas: ")
        for i in self.stringCorreta:
            print(i)
        print("\n")
        


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    palavra = bank[random.randint(0, len(bank))].strip()
    return palavra


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    while True:
        # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
        game.print_game_status()

        game.hide_word()
        a = str(input("Digite uma letra: \n"))
        print("----------------------------------")
        game.guess(a)
        
        # Verifica o status do jogo
        

        if game.hangman_over():
            break

    print(board[6])    
    
    print("\nLetras erradas: ")
    for i in game.stringErrada:
        print(i)

    print("\nLetras corretas: ")
    for i in game.stringCorreta:
        print(i)

    print("\n",game.stringPalavra)

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print("\nParabéns! Você venceu!!")
    else:
        print("\nGame over! Você perdeu.")
        print("A palavra era", game.word())

    print("\nFoi bom jogar com você! Agora vá estudar!\n")


# Executa o programa
if __name__ == "__main__":
    main()


