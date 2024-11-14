#A senha do Adm é 1234 ;)
clientes = []

#Para entrar no programa confirme que você é um administrador
print("----- <<< Confirme que você é um administrador >>> -----")
senha = int(input("Senha: "))
if (senha == 1234):
    while True:

        print("====== <<< Pet Lover >>> ======")
        print("|   [1] Cadastrar Cliente     |")
        print("|   [2] Login                 |")
        print("|   [3] Ver cadastros         |")
        print("|   [0] Sair                  |")
        print("===============================")

        opcao = int(input("Informe sua escolha: "))

        if(opcao == 1):
            
            print("=====================")
            print("| Cadastro Cliente  |")
            print("=====================")
            
            nome = input("Nome completo: ")
            email = input("Email: ")
            cpfCadastro = int(input("Cpf: "))
            clientes.append(["Cliente",nome, email, cpfCadastro])

            print("=====================")
            print("|   Cadastro Pet    |")
            print("=====================")    
            nomePet = input("Nome do pet: ")
            idade = input("Idade do pet: ")
            
            print("====== <<< Classificação >>> ======")
            print("|   [1] Felino                    |")
            print("|   [2] Canídeo                   |")
            print("|   [3] Ave                       |")
            print("|   [0] Sair                      |")
            print("===================================")

            classificacao = int(input("Classificação do pet: "))
            if (classificacao == 1):
                classificacao = ("Felino")
            
            if (classificacao == 2):
                classificacao = ("Canídeo")
            
            if (classificacao == 3):
                classificacao = ("Ave")
            
            clientes.append(["Pet", nomePet, idade, classificacao])
            
            with open("cadastros.txt", "w") as arquivo:
                for lista in clientes:
                    arquivo.write(str(lista) + "\n")

            arquivo.close()

            print("Cadastros realizados!")

            if (classificacao == 0):
                break


        if(opcao == 2):
            print("===================")
            print("|      Login      |")
            print("===================") 
            
            #Pede o cpf do cliente e a senha do Adm
            cpf = input("Cpf do cliente: ")

            senha = input("Senha do adm:  ")
            if(senha == 1234): 
            
                print("================================")
                print("|   [1] Marcar consulta        |")
                print("|   [2] Marcar banho/tosa      |")
                print("|   [0] Sair                   |")
                print("================================")
                opcaoLogin = int(input("Informe sua escolha: "))
                
                if(opcaoLogin == 1):
                    input("Data: ")
                    print("Consulta realizada!")

                if(opcaoLogin == 2):
                    print("================================")
                    print("|   [1] Banho                  |")
                    print("|   [2] Banho e tosa           |")
                    print("|   [0] Sair                   |")
                    print("================================")

                    banho = int(input("Informe sua escolha: "))
                    if (banho == 1): 
                        input("Data: ")
                        print("Banho marcado!")
                    
                    if(banho == 2):
                        input("Data: ")
                        print("Banho e tosa marcados!")
                
                if(opcaoLogin == 0):
                    break
                
            else:
                print("Senha incorreta!")
        
        if(opcao == 3):
        #consultar todos os dados
            print("===================")
            print("|    Cadastros    |")
            print("===================")
            
            arquivo = open("cadastros.txt", "r")
            dados = arquivo.readlines()
            for linha in dados:
                print(linha.strip())

            arquivo.close()
        
        if (opcao == 0):
            break
    
else:
    print("Acesso negado!")
    