#ATIVIDADE SEMANA 2 - SISTEMA PUC / MENU PRINCIPAL - PEDRO LUCAS GALVAO FRANCO OLIVEIRA 


def menu_principal():
    
    print ("\nMENU PRINCIPAL DO SISTEMA PUC")
    print ("--------------------------------")
    print ("(1) Gerenciar Estudantes")
    print ("(2) Gerenciar Disciplinas")
    print ("(3) Gerenciar Professores")
    print ("(4) Gerenciar Turmas")
    print ("(5) Gerenciar Matriculas")
    print ("(0) SAIR")
    print ("--------------------------------")
 
 # Não vimos ainda esse tipo de código, mas para facilitar tanto a execução quanto a reutilização do código nas proximas semanas
if __name__ == "__main__":
     
     menu_principal()
     
     opcao_princiapal = input("Digite a opcao desejada: ")
     
     if opcao_princiapal == '1':
         print ("\nVocê selecionou o Gerenciador de Estudantes!")
         print ("Ainda não desenvolvido :( ")
     elif opcao_princiapal == '2':
        print ("\nVocê selecionou o Gerenciador de Disciplinas!")
        print ("Ainda não desenvolvido :(")
     elif opcao_princiapal == '3':
        print ("\nVocê selecionou o Gerenciador de Professores!")
        print ("Ainda não desenvolvido :(")
     elif opcao_princiapal == '4':
        print ("\nVocê selecionou o Gerenciador de Turmas!")
        print ("Ainda não desenvolvido :(")
     elif opcao_princiapal == '5':
        print ("\nVocê selecionou o Gerenciador de Matriculas!")
        print ("Ainda não desenvolvido :(")
     elif opcao_princiapal == '0':
        print ("\nVocê selecionou para SAIR!")
        print ("Saindo do sistema...")
     else:
         print ("\nOpção invalida! Execute novamente :) ")
         
     print("\FIM DA EXECUCAO SEMANA 2")
         
        
        
     
