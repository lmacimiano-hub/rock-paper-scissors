import random

class Jogador:
    def __init__(self, nome):
        # Aqui definimos os ATRIBUTOS (características) do jogador
        self.nome = nome
        self.pontos = 0  # Todo jogador começa com 0 pontos

    def adicionar_ponto(self):
        # Aqui definimos um MÉTODO (uma ação)
        self.pontos += 1

def jogar():
    print("--- Jokenpô com Placar ---")
    
    # CRIANDO OS OBJETOS (Instanciando a classe)
    # Estamos criando dois jogadores reais baseados no molde "Jogador"
    humano = Jogador("Você")
    computador = Jogador("Computador")

    opcoes = ['pedra', 'papel', 'tesoura']

    while True:
        print(f"\nPLACAR: {humano.nome} {humano.pontos} x {computador.pontos} {computador.nome}")
        
        escolha_humano = input("Escolha (pedra, papel, tesoura) ou 'sair': ").lower()

        if escolha_humano == 'sair':
            break
        
        if escolha_humano not in opcoes:
            print("Opção inválida.")
            continue

        escolha_pc = random.choice(opcoes)
        
        print(f"--> {humano.nome} jogou: {escolha_humano}")
        print(f"--> {computador.nome} jogou: {escolha_pc}")

        # Lógica de vitória
        if escolha_humano == escolha_pc:
            print("Resultado: EMPATE")
        
        elif (escolha_humano == 'pedra' and escolha_pc == 'tesoura') or \
             (escolha_humano == 'papel' and escolha_pc == 'pedra') or \
             (escolha_humano == 'tesoura' and escolha_pc == 'papel'):
            print(f"Resultado: {humano.nome} venceu a rodada!")
            # Chamamos o método da classe para dar o ponto
            humano.adicionar_ponto()
            
        else:
            print(f"Resultado: {computador.nome} venceu a rodada!")
            computador.adicionar_ponto()

    print("\n--- Fim de Jogo ---")
    print(f"Placar Final -> {humano.nome}: {humano.pontos} | {computador.nome}: {computador.pontos}")

if __name__ == "__main__":
    jogar()
