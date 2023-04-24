import random
import string

#A função generate_password irá gerar uma senha com numeros e letras aleatorios
def generate_password(length):
    letters = string.ascii_letters + string.digits
    password = ''.join(random.choice(letters) for i in range(length))
    return password

#Aqui entra num loop para verificar se o usuario digitou o minimo de caracteres validos e verifica se digitou como ''int'' de verdade
while True:
    try:
        size_password = int(input('Digite o tamanho da senha que deseja: '))
        if size_password < 6:
            print('Digite um valor mínimo, de 6 pra cima.')
            continue
        break
    except ValueError:
        print('Digite apenas números inteiros.')

#aqui gera a senha do tamanho que o usuário pediu
password = generate_password(size_password)
print('A senha de tamanho {} gerada é: {}'.format(size_password, password))
