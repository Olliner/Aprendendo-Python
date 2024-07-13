from colorama import Fore, Style
import time
import random

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
res = Style.RESET_ALL

opcoes = ['✊', '🖐️', '✌️']
pontos = 0


def determinar_vencedor(player, robo):
    if player == robo:
        return "Empate!"
    elif (player == '✊' and robo == '✌️') or (player == '🖐️' and robo == '✊') or (player == '✌️' and robo == '🖐️'):
        return "Vitória do jogador!"
    else:
        return "Vitória do robô!"

# Interação
print(f'{yellow}🤖 = Olá Tudo bem!')

nome_robo = str(input(f'{yellow}🤖 = Me dê um nome para que possamos jogar: {res}'))

print(f'{res}{nome_robo}{yellow}🤖 = Vamos ao que interessa!')

inicio_game = str(input(f'{res}{nome_robo}🤖 = Quer jogar Jokenpo (s/n): {res}').lower())

if inicio_game == 's':
    print(f'{res}{nome_robo}🤖{yellow} = Ótimo, vamos começar!')

    qtd_partida = int(input(f'{res}{nome_robo}{yellow}🤖 = Quantas partidas você quer: '))

    print(f'{res}{nome_robo}{yellow}🤖 = Ótimo, faremos {qtd_partida} partidas!')
    
    print(' ')

    print(f'{res}{nome_robo}{yellow}🤖 = Para escolher uma das opções vá de acordo com a tabela: \n ✊ (pedra) = 1\n 🖐️ (papel) = 2\n ✌️ (tesoura) = 3') 

    print(' ')

    for v in range(1, qtd_partida + 1):
        escolha = random.choice(opcoes)
        print(' *  - ' * 20)
        print(' ')
        print(f'{res}{nome_robo}{yellow}🤖 = {v}ª Partida')
        player_escolha_num = int(input(f'{blue}Escolha >> '))
        print(' ')
        
        if player_escolha_num == 1:
            player_escolha = opcoes[0]
        elif player_escolha_num == 2:
            player_escolha = opcoes[1]
        elif player_escolha_num == 3:
            player_escolha = opcoes[2]
        else:
            print(f'{res}{nome_robo}{yellow}🤖 = Opção inexistente jogador')
            continue

        print(f'{blue}Player:{res} {player_escolha}')
        print(f'{res}{nome_robo}{yellow}🤖 = JÓ KEN PO! {escolha}')
        print('')

        resultado = determinar_vencedor(player_escolha, escolha)
        print(f'{yellow}{resultado}{res}')
else:
    print(f'{res}{nome_robo}🤖{yellow} = Ah, que pena. Até a próxima... 👋')
