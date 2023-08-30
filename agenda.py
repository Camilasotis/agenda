import os 
agenda=[]
sair=False
while(sair==False):
    print("Lista de opções: ")
    print("1-Inserir novo contato:")
    print("2-Exibir lista de contatos:")
    print("3-Editar um contato:")
    print("4-Remover um contato:")
    opcao=int(input("Digite a opção escolhida.... : "))

    if(opcao==1): 
        novo_contato=[]
        nome=input("Digite o nome do contato:")
        novo_contato.append(nome)
        telefone=input("Digite o telefone do contato:")
        novo_contato.append(telefone)
        agenda.append(novo_contato)
        os.system('cls')

    if(opcao==2):
        for novo_contato in agenda:
           print(novo_contato[0])
