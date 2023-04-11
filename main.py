import PySimpleGUI as sg
import mysql.connector

sg.theme('Dark Blue 3')

layout = [
    [sg.Text('Nome'), sg.Input(key='nome')],
    [sg.Text('Email'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha')],
    [sg.FileBrowse('Selecionar imagem', key='imagem_path')],
    [sg.Button('Confirmar'), sg.Button('Sair')]
]

janela = sg.Window('aplicação do PySimpleGUI Kaio hehe', layout)

# Conectar ao banco de dados MySQL
db = mysql.connector.connect(
    host='*******',
    user='*******',
    password='*******',
    database='*******'
)

# Criou um cursor
cursor = db.cursor()

cursor.execute("alter table usuarios MODIFY column imagem LONGBLOB")

while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED or evento == 'Sair':
        break

    cursor = db.cursor()
    sql = 'select * from usuarios where email = %s'
    dados = (valores['email'],)
    cursor.execute(sql, dados)

    resultado = cursor.fetchone()

    if resultado:
        sg.popup('Já existe um usuário com esse e-mail!')

    else:
        with open(valores['imagem_path'], 'rb') as arquivo_imagem:
            imagem = arquivo_imagem.read()

        sql = 'INSERT INTO usuarios (nome, email, senha, imagem) VALUES (%s, %s, %s, %s)'
        dados = (valores['nome'], valores['email'], valores['senha'], imagem)
        cursor.execute(sql, dados)
        db.commit()
        sg.popup('Usuário cadastrado com sucesso!')

    cursor.close()

janela.close()
db.close()
