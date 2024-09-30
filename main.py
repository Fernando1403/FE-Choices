import logging
import random
import sys
import unittest

# Config log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)

# Código original
pontos = 20

def main():
    global pontos
    logging.info("Olá, seja bem-vindo à FE Choices!")

    userCadastro = input("Para começar, vamos pedir para você se cadastrar\nQual será seu user: ")
    userSenha = input("Qual senha você deseja cadastrar: ")

    while True:
        try:
            logging.info("Solicitando login.")
            user = input("Insira seu usuário: ")
            senha = input("Insira sua senha: ")

            if user != userCadastro or senha != userSenha:
                logging.warning("Tentativa de login falhou.")
                raise ValueError("Usuário e/ou senha incorretos, tente novamente.")

            logging.info(f"Usuário {user} logado com sucesso.")
            break
        except ValueError as erro:
            print(erro)

    # Roleta Opções
    prizes = ["10 pontos em créditos", "20 pontos em créditos", "Sem premiação"]

    def spin_roulette():
        return random.choice(prizes)

    def daily_roulette():
        global pontos
        logging.info("Iniciando a roleta diária.")
        input("Pressione Enter para rodar a roleta...")

        premio = spin_roulette()
        if premio == "10 pontos em créditos":
            pontos += 10
        elif premio == "20 pontos em créditos":
            pontos += 20

        logging.info(f"Prêmio obtido: {premio}. Pontos totais: {pontos}.")
        print(f"Você ganhou: {premio} e agora possui no total {pontos} pontos.")

    daily_roulette()

    # Funções de palpites
    races = {
        "Corrida 1": "Piloto A",
        "Corrida 2": "Piloto B",
        "Corrida 3": "Piloto C"
    }

    def verificaPontos():
        while True:
            try:
                num = input("Quantos pontos você deseja colocar? ")
                if not num.isnumeric():
                    raise ValueError("Valor inválido.")
                return int(num)
            except ValueError as erro:
                print(erro)

    def verificaValor():
        global pontos
        while True:
            num = verificaPontos()
            if num > pontos:
                print("Valor do palpite maior que a quantidade de pontos")
            else:
                return num

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

        palpite = input(f"Quem você acha que vai ganhar {corrida_escolhida}? ")

        if palpite == races[corrida_escolhida]:
            print(f"Parabéns! Você acertou o palpite!")
            pontos += valorApostado * 2
        else:
            print(f"Palpite errado. O vencedor foi {races[corrida_escolhida]}.")
            pontos -= valorApostado

        print(f"Agora você tem {pontos} pontos")
        return pontos

    fazer_palpite()

    # Palpites de pódio
    races_podium = {
        "Corrida 1": ["Piloto A", "Piloto B", "Piloto C"],
        "Corrida 2": ["Piloto B", "Piloto C", "Piloto A"],
        "Corrida 3": ["Piloto C", "Piloto A", "Piloto B"]
    }

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

        palpite = []
        for i in range(3):
            palpite.append(input(f"Quem você acha que ficará em {['primeiro', 'segundo', 'terceiro'][i]} lugar? "))

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

    # Fantasy
    pilotosFantasy = ["Piloto 1", "Piloto 2", "Piloto 3", "Piloto 4", "Piloto 5", "Piloto 6", "Piloto 7", "Piloto 8",
                      "Piloto 9", "Piloto 10"]
    escuderiasFantasy = ["Escuderia 1", "Escuderia 2", "Escuderia 3", "Escuderia 4", "Escuderia 5"]

    selecao_pilotos = []
    selecao_escuderias = []

    resultado_pilotosFantasy = ["Piloto 1", "Piloto 2", "Piloto 3", "Piloto 4", "Piloto 5"]
    resultado_escuderiasFantasy = ["Escuderia 1", "Escuderia 2"]

    # Escolha dos pilotos
    print("Escolha 5 pilotos para montar o seu Fantasy:")
    print(pilotosFantasy)
    for i in range(5):
        while True:
            try:
                piloto = input(f"Escolha o piloto {i + 1}: ")
                if piloto not in pilotosFantasy:
                    raise ValueError("Piloto inválido. Tente novamente.")
                selecao_pilotos.append(piloto)
                break
            except ValueError as erro:
                print(erro)

    # Escolha das escuderias
    print("Escolha 2 escuderias:")
    print(escuderiasFantasy)
    for i in range(2):
        while True:
            try:
                escuderia = input(f"Escolha a escuderia {i + 1}: ")
                if escuderia not in escuderiasFantasy:
                    raise ValueError("Escuderia inválida. Tente novamente.")
                selecao_escuderias.append(escuderia)
                break
            except ValueError as erro:
                print(erro)

    # Verificar os resultados
    for piloto in selecao_pilotos:
        if piloto in resultado_pilotosFantasy[:5]:
            pontos += 20
        else:
            pontos -= 10

    for escuderia in selecao_escuderias:
        if escuderia in resultado_escuderiasFantasy[:2]:
            pontos += 10
        else:
            pontos -= 10

    print(f"O resultado dos pilotos do Fantasy foi {resultado_pilotosFantasy}. A cada acerto você ganha 20 e a cada erro perde 10.")
    print(f"O resultado das escuderias do Fantasy foi {resultado_escuderiasFantasy}. A cada acerto você ganha 10 e a cada erro perde 10.")
    print(f"Você terminou a rodada fantasy com {pontos} pontos.")

if __name__ == "__main__":
    main()

# Testes
'''class Teste(unittest.TestCase):
    def setUp(self):
        self.pontos = 20
        self.userCadastro = "usuario"
        self.userSenha = "senha"

    def test_login_success(self):
        user = self.userCadastro
        senha = self.userSenha
        self.assertEqual(user, self.userCadastro)
        self.assertEqual(senha, self.userSenha)

    def test_login_failure(self):
        user = "usuario_errado"
        senha = "senha"
        with self.assertRaises(ValueError):
            if user != self.userCadastro or senha != self.userSenha:
                raise ValueError("Usuário e/ou senha incorretos, tente novamente.")

    def test_daily_roulette(self):
        global pontos
        original_points = self.pontos
        premio = "10 pontos em créditos"  # Simulando resultado da roleta
        if premio == "10 pontos em créditos":
            self.pontos += 10
        self.assertEqual(self.pontos, original_points + 10)

    def test_fazer_palpite_errado(self):
        global pontos
        corrida = "Corrida 1"
        palpite = "Piloto B"
        valor_apostado = 10
        vencedor = "Piloto A"
        if palpite != vencedor:
            self.pontos -= valor_apostado
        self.assertEqual(self.pontos, pontos - 10)'''

if __name__ == "__main__":
    unittest.main()
