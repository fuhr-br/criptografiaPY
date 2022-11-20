import sys

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

    
if len(sys.argv) == 4:

    arquivo_recebido = sys.argv[1]
    chave = sys.argv[2]
    funcao = sys.argv[3]


    # valida se o segundo parametro he um arquivo de texto

    if arquivo_recebido[len(arquivo_recebido)-4:] != '.txt':
            
        print('Adicione um arquivo do tipo .txt')


    # valida se o terceiro parametro da chamada he um numero

    elif chave.isdecimal() == False:

        print('A chave precisa ser um número')
        

    # verifica qual o quarto parametro, se CRIPTO ou DECRIPTO

    elif funcao != 'CRIPTO' and funcao != 'DECRIPTO':
        
        print('O último parametro deve ser CRIPTO ou DECRIPTO')

    # se nao houver ao chamar o script, ele sera executado

    else:
        
        # declara os caracteres que substituirao os caracteres do arquivo
  
        tableau  = 'ABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇabcdefghijklmnopqrstuvwyzàáãâéêóôõíúç'

        # declara a variavel que ira receber o novo texto (criptografado ou decriptografado)

        novo_texto = ''      

        arquivo = open(arquivo_recebido)

        # faz a leitura do texto do arquivo e armazena em uma variavel temporaria

        texto = arquivo.read()
        
        arquivo.close()

        # percorre todos os caracteres que serao criptografados/decriptografados

        for c in texto:

            # procura pela letra lida do texto no alfabeto de substituicao

            posicao = tableau .find(c)
        
            if posicao == -1:
                
                # se nao localizar a letra, adiciona o proprio caracter no novo texto

                novo_texto += c

            else:
 
                # localizando a letra no tableau e o ultimo parametro da chamada for criptografar, nova_posicao recebe a posicao do caracter mais o valor da chave, se nao sera posicao menos o valor da chave

                nova_posicao = posicao + int(chave) if funcao == 'CRIPTO' else posicao - int(chave)

                # como o calculo para a substituicao pode ser maior do que o numero de letras da variavel alfabeto, sera feito um mod para garantir que o valor nao seja ultrapassado     
                       
                nova_posicao = nova_posicao % len(tableau )

                # o novo caracter calculado sera adicionado ao novo texto

                novo_texto += tableau [nova_posicao:nova_posicao + 1]
        
        # sera adicionado ao nome do arquivo modificado o final _cripto 

        arquivo_recebido = arquivo_recebido[:len(arquivo_recebido) - 4] + '.txt'

        # um novo arquivo .txt sera criado

        novo_arquivo = open(arquivo_recebido,'w+')

        # o novo texto sera salvo no novo arquivo

        novo_arquivo.write(novo_texto)

        # o novo arquivo sera fechado

        novo_arquivo.close()

else:

    # retorna mensagem de erro caso a quantidade de parametro esteja errada e apresenta a sintaxe correta

    print('Estão faltando parametros na chamada do script')
    print('Sintaxe correta: $<script> <arquivo.txt> <chave> <CRIPTO ou DECRIPTO>')
    sys.exit()
