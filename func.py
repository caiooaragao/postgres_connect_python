
import psycopg2

try:
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='forestsky123',
        database='meu_db'
    )

except:
    print('erro ao conectar com a database')
cursor = conn.cursor()


def inserir_aluno(aluno, telefone):
    cursor.execute(
        'INSERT INTO alunos(nome, telefone) Values(%s, %s);', (aluno, telefone))
    conn.commit()
    cursor.close()


def ver_lista(nome_da_lista):
    cursor.execute('select * FROM {};'.format(nome_da_lista))
    print(cursor.fetchall())
    cursor.close()


def criar_tabela(nomeTabela):
    cursor.execute(
        'CREATE TABLE {} (ID SERIAL PRIMARY KEY NOT NULL);'.format(nomeTabela))
    print("essa tabalea foi criada usando ID como primary key e AUTO_INCREMENT")
    conn.commit()


def inserir_colunas_na_tabela():
    nomeTabela = input("digite o nome da tabela a ter a coluna inserida")
    nomeColuna = input("digite o nome da coluna a ser inserida")
    characterType = input(
        'digite o tipo de character a ser usado(VARCHAR/INT/ETC...')
    nullorNot = input("voce prefere: NULL OR NOT NULL?")
    cursor.execute('ALTER TABLE {} ADD COLUMN{} {} {};'.format(
        nomeTabela, nomeColuna, characterType, nullorNot))
    conn.commit()


def deletar_tabela(nome_tabela):
    cursor.execute('DROP TABLE {};'.format(nome_tabela))
    conn.commit()
    return print('Tabela {} deletada!'.format(nome_tabela))
