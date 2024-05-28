pontos = 20

print("Olá seja bem vindo a FE Choices!!\nAqui voce pode dar seus palpites sobre a formula E\n")

userCadastro = input("Para começar vamos pedir para voce se cadastrar\nQual será seu user: ")
userSenha = input("Qual senha voce deseja cadastrar: ")

print("Faça o login para começar a dar seus palpites !")

user = input("Insira seu usuario: ")
senha = input("Insira sua senha: ")

while user != userCadastro or senha != userSenha:
    print("Usuario e ou senha incorretos, tente novamente")
    user = input("Insira seu usuario: ")
    senha = input("Insira sua senha: ")
print(f"Seja bem vindo {user}, voce possui {pontos} pontos")

#Roleta
import random

prizes = [
    "10 pontos em créditos",
    "20 pontos em créditos",
    "Sem premiação"
]

def spin_roulette():
    # Seleciona um prêmio aleatoriamente
    premio = random.choice(prizes)
    return premio

# Função principal para rodar a roleta diária
def daily_roulette():
    global pontos
    print("Bem-vindo à roleta diária!")
    input("Pressione Enter para rodar a roleta...")

    # Rodando a roleta
    premio = spin_roulette()

    # Exibindo o prêmio obtido
    print(f"Parabéns! Você ganhou: {premio}")

    if premio == prizes[0]:
        pontos += 10
    elif premio == prizes[1]:
        pontos += 20
    
    return pontos

# Executando a roleta diária
if __name__ == "__main__":
    daily_roulette()

#Palpites
# Dados de corridas e vencedores
races = {
    "Corrida 1": "Piloto A",
    "Corrida 2": "Piloto B",
    "Corrida 3": "Piloto C"
}

# Função verificar se os pontos são Numeros
def verificaPontos():
    num = input("Quantos pontos voce deseja colocar ? ")
    while not num.isnumeric():
        print("Valor Invalido")
        num = input("Quantos pontos voce deseja colocar ? ")
    num = int(num)
    return num

# Função para verificar se é numero
def verificaValor():
    global pontos
    num = verificaPontos()
    while num > pontos:
        print("Valor do palpite maior que quantidade de pontos")
        num = verificaPontos()
    return num

# Função para fazer palpites
def fazer_palpite():
    global pontos
    print("\nVamos fazer um palpite sobre a próxima corrida!")
    valorApostado = verificaValor()
    for corrida in races:
        print(corrida)
    
    corrida_escolhida = input("Escolha uma corrida: ")
    if corrida_escolhida not in races:
        print("Corrida inválida. Tente novamente.")
        return

    for piloto in races:
        print(races[piloto])
    palpite = input(f"Quem você acha que vai ganhar {corrida_escolhida}? ")

    if palpite == races[corrida_escolhida]:
        print(f"Parabéns! Você acertou o palpite! \nVocê tinha {pontos} pontos")
        valorApostado * 2
        pontos += valorApostado  # Ganhe 30 pontos por palpite correto
    else:
        print(f"Palpite errado. O vencedor foi {races[corrida_escolhida]}. \nVocê tinha {pontos} pontos")
        pontos -= valorApostado  # Perde 10 pontos por palpite errado

    print(f"Agora você tem {pontos} pontos")
    return pontos

fazer_palpite()

#Fantasy - Podio
races_podium = {
    "Corrida 1": ["Piloto A", "Piloto B", "Piloto C"],
    "Corrida 2": ["Piloto B", "Piloto C", "Piloto A"],
    "Corrida 3": ["Piloto C", "Piloto A", "Piloto B"]
}

# Função para fazer palpites de pódio
def fazer_palpite_podio():
    global pontos
    print("\nVamos fazer um palpite sobre o pódio da próxima corrida!")
    valor_apostado = verificaValor()
    
    print("Corridas disponíveis:")
    for corrida in races_podium:
        print(corrida)

    corrida_escolhida = input("Escolha uma corrida: ")
    if corrida_escolhida not in races_podium:
        print("Corrida inválida. Tente novamente.")
        return

    print("Pilotos disponíveis:")
    pilotos = set(piloto for podio in races_podium.values() for piloto in podio)
    for piloto in pilotos:
        print(piloto)

    palpite_primeiro = input("Quem você acha que ficará em primeiro lugar? ")
    palpite_segundo = input("Quem você acha que ficará em segundo lugar? ")
    palpite_terceiro = input("Quem você acha que ficará em terceiro lugar? ")

    palpite = [palpite_primeiro, palpite_segundo, palpite_terceiro]
    resultado = races_podium[corrida_escolhida]

    pontos_ganhos = 0
    for i in range(3):
        if palpite[i] == resultado[i]:
            pontos_ganhos += 10

    if pontos_ganhos > 0:
        print(f"Parabéns! Você acertou {pontos_ganhos // 10} posições!")
        pontos += pontos_ganhos
    else:
        print("Palpites errados. Nenhuma posição correta.")
        pontos -= valor_apostado

    print(f"Agora você tem {pontos} pontos.")
    return pontos

fazer_palpite_podio()
