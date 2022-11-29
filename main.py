from func import *


#cursor.execute('CREATE TABLE pessoas(nome varchar(10) not null)')
# conn.commit()
loop = True
while loop == True:
    login = input("digite seu login")
    senha = input("digite sua senha")
    cursor.execute('SELECT * from login')
    resultado = cursor.fetchall()
    if login and senha in resultado[0]:
        print('login realizado com sucesso')
        while True:
            menu = input(
                '----- Bem vindo ao Menu.----- \n 1-inserir Aluno \n 2-ver a lista geral \n 3-sair \n 4- Criar tabela \n 5-Inserir Colunas em uma tabela \n 6-Deletar tabela')
            if menu == '1':
                aluno_para_insercao = input(
                    'digite nome do aluno par ser inserido')
                telefone_para_insercao = input(
                    'digite o telefone para ser inserido')
                inserir_aluno(aluno_para_insercao, telefone_para_insercao)
                print('----- ALUNO INSERIDO ----')
            if menu == '2':
                nomeTabela = input('qual lista voce deseja ver?')
                ver_lista(nomeTabela)
            if menu == '3':
                print('fechando programa')
                loop = False
                break

            if menu == '4':
                nomeTabela = input('Digite o nome da tabela a ser criada')
                criar_tabela(nomeTabela)
                insertColunas = input(
                    'deseja inserir colunas na sua nova tabela? [S/N]')
                if insertColunas in 'Ss':
                    inserir_colunas_na_tabela()
                else:
                    print('voltando ao menu')
            if menu == '5':
                inserir_colunas_na_tabela()
            if menu == '6':
                nome_tabela = input("digite o nome da tabela que quer DELETAR")
                deletar_tabela(nome_tabela)
    else:
        print('login ou senha incorreto, fechando programa...')
        break

cursor.close()
conn.close()
