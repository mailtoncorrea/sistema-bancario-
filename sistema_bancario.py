# Sistema => Mailton Correa
menu = '''
1. Depositar
2. Sacar
3. Extrato
4. Sair    
=> '''
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)
    if opcao == "1":
        saldo_add = int(input("Informe o valor que deseja depositar: "))
        if saldo_add > 0:
            saldo += saldo_add
            extrato += f"Depósito: R$ {saldo_add}\n"
            print(f"{saldo_add} R$ Foi Depositado com Sucésso ")
        else:
            print("Valor inválido! O depósito deve ser maior que zero.")

    elif opcao == "2":
        if numero_saque >= LIMITE_SAQUES:
            print("Limites de saques diários atingido!") 
        else:
            saque = int(input("Informe o valor que deseja sacar: "))
            if saque > saldo:
                print("Saldo insuficiente.")
            elif saque > limite:
                print(f"O valor de saque excede o limite de R$ {limite}")
            elif saque > 0:
                saldo -= saque
                extrato += f"Saque: R$ {saque}\n"
                numero_saque += 1
                print(f"Saque de R$ {saque} realizado com sucésso.")
            else:
                print("Valor inválido! O saque deve ser maior que zero.")
                
        
    elif opcao == "3":
        print("=========EXTRATO=========")
        print(extrato if extrato else " Nenhuma Movimentação registrada.")
        print(f"Saldo atual: R$ {saldo}")
        print("========================")
        


    elif opcao == "4":
        print("Finalizando...")
        break
    else:
         print("Opção inválida! Escolha uma opção de 1 á 4.")
