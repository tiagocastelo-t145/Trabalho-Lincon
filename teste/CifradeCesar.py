TAM_MAX_CH = 26

def recebeModo():
   """
    Função que pergunta se o usuário quer criptografar ou
    decriptografar e garante que uma entrada válida foi recebida
    """

   while True:
    modo = input ("Você deseja criptografar ou decriptografar?\n").lower()
    if modo in 'criptografar c decriptografar d'.split():
        return modo
    else:
        print("Digite 'criptografar' ou 'c' ou 'descriptografar' ou 'd'.")


   
    

def recebeChave():
    "Usuário insere a chave"

    global TAM_MAX_CH
    chave = 0

    while True:
        chave = int(input("Digite um valor (1-%s)\n"%TAM_MAX_CH))

        if 1 <= chave <= TAM_MAX_CH:
            return chave

def geraMsgTraduzida(modo, mensagem, chave):
    "Traduz a frase iinserida pelo usuário"
    if modo[0] == 'd':
        chave *= -1

    traduzido = ''

    for simbolo in mensagem:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= TAM_MAX_CH
                elif num < ord('A'):
                    num += TAM_MAX_CH
                elif simbolo.islower():
                     if num > ord('z'):
                        num -= TAM_MAX_CH
                elif num < ord('a'):
                    num += TAM_MAX_CH
                    
            traduzido += chr(num)
        else:
            traduzido += simbolo

        return traduzido

def main():

    modo = recebeModo()
    mensagem = input("Digite sua mensagem\n")
    chave = recebeChave()

    print("A sua tradução é:")
    print(geraMsgTraduzida(modo, mensagem, chave))

main()
    
    
