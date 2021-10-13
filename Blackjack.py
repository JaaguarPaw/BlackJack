import pygame
import time
from random import randrange
pygame.init()
screen = pygame.display.set_mode((1600, 1000))
pygame.display.set_caption("Blackjack")
FPS = pygame.time.Clock()


def game_set(text):
    screen.blit(text, (950, 475))


def update_screen(card_list, score1, score2, filo_index, cords, case):
    pygame.draw.rect(screen, black, (0, 0, 2000, 1200))
    screen.blit(bg, (0,0))
    screen.blit(score1, (300,650))
    screen.blit(score2, (300, 250))
    screen.blit(case, (1200, 250))
    screen.blit(card_list[filo_index], cords)

    draw_card1(card_list, cords, filo_index)
    draw_card0(card_list, cords, filo_index)
    display_buttons()


def display_buttons():
    pygame.draw.rect(screen, black, (1100, 650, 150, 70), 5)
    pygame.draw.rect(screen, black, (1350, 650, 150, 70), 5)
    screen.blit(draw_button, (1100, 650))
    screen.blit(stop_button, (1357, 650))


def draw_card0(values, cords, x):
    if type(values[x]) == int:
        screen.blit(fila[x], cords)
        return x
    else:
        print("OTHER")
        return str(x)


def draw_card1(values, cords, x):
    if type(values[x]) == int:
        screen.blit(fila[x], cords)
        return x
    else:
        print("OTHER")
        return str(x)


black = (0, 0, 0); white = (245, 245, 245); brown = (210, 105, 30); blue = (0, 0, 205); dark_green = (0, 30, 0)

font = pygame.font.SysFont('Arial', 48, True,)
font2 = pygame.font.SysFont('ComicSans', 40, True)

play_again_button = font.render("Play Again", True, blue)
draw_button = font.render("DRAW", True, white)
stop_button = font.render("STOP", True, dark_green)

player1_win = font.render("Player 1 wins!", True, blue)
player2_win = font.render("Player 2 wins!", True, brown)
tie_text = font.render("Tie!", True, white)

ace_conversion = font.render("Convert Ace to:  1  or  10  ?", True, black)
nada = font.render("", True, black)


bg = pygame.image.load("./imges/bg.jpg")
asos_karo = pygame.image.load("./karo/asos_karo.png"); dio_karo = pygame.image.load("./karo/dio_karo.png"); tria_karo = pygame.image.load("./karo/tria_karo.png")
tesera_karo = pygame.image.load("./karo/tesera_karo.png"); pente_karo = pygame.image.load("./karo/pente_karo.png"); eksi_karo = pygame.image.load("./karo/eksi_karo.png")
epta_karo = pygame.image.load("./karo/epta_karo.png"); okto_karo = pygame.image.load("./karo/okto_karo.png"); ennia_karo = pygame.image.load("./karo/enia_karo.png")
deka_karo = pygame.image.load("./karo/deka_karo.png"); J_karo = pygame.image.load("./karo/J_karo.png"); Q_karo = pygame.image.load("./karo/Q_karo.png"); K_karo = pygame.image.load("./karo/K_karo.png")

asos_koupa = pygame.image.load("./koupes/asos_koupa.png"); dio_koupa = pygame.image.load("./koupes/dio_koupa.png"); tria_koupa = pygame.image.load("./koupes/tria_koupa.png")
tesera_koupa = pygame.image.load("./koupes/tesera_koupa.png"); pente_koupa = pygame.image.load("./koupes/pente_koupa.png"); eksi_koupa = pygame.image.load("./koupes/eksi_koupa.png")
epta_koupa = pygame.image.load("./koupes/epta_koupa.png"); okto_koupa = pygame.image.load("./koupes/okto_koupa.png"); ennia_koupa = pygame.image.load("./koupes/enia_koupa.png")
deka_koupa = pygame.image.load("./koupes/deka_koupa.png"); J_koupa = pygame.image.load("./koupes/J_koupa.png"); Q_koupa = pygame.image.load("./koupes/Q_koupa.png"); K_koupa = pygame.image.load("./koupes/K_koupa.png")

asos_spathi = pygame.image.load("./spathia/asos_spathi.png"); dio_spathi = pygame.image.load("./spathia/dio_spathi.png"); tria_spathi = pygame.image.load("./spathia/tria_spathi.png")
tesera_spathi = pygame.image.load("./spathia/tesera_spathi.png"); pente_spathi = pygame.image.load("./spathia/pente_spathi.png"); eksi_spathi = pygame.image.load("./spathia/eksi_spathi.png")
epta_spathi = pygame.image.load("./spathia/epta_spathi.png"); okto_spathi = pygame.image.load("./spathia/okto_spathi.png"); ennia_spathi = pygame.image.load("./spathia/enia_spathi.png")
deka_spathi = pygame.image.load("./spathia/deka_spathi.png"); J_spathi = pygame.image.load("./spathia/J_spathi.png"); Q_spathi = pygame.image.load("./spathia/Q_spathi.png"); K_spathi = pygame.image.load("./spathia/K_spathi.png")

asos_mpastouni = pygame.image.load("./mpastounia/asos_mpastouni.png"); dio_mpastouni = pygame.image.load("./mpastounia/dio_mpastouni.png"); tria_mpastouni = pygame.image.load("./mpastounia/tria_mpastouni.png")
tesera_mpastouni = pygame.image.load("./mpastounia/tesera_mpastouni.png"); pente_mpastouni = pygame.image.load("./mpastounia/pente_mpastouni.png"); eksi_mpastouni = pygame.image.load("./mpastounia/eksi_mpastouni.png")
epta_mpastouni = pygame.image.load("./mpastounia/epta_mpastouni.png"); okto_mpastouni = pygame.image.load("./mpastounia/okto_mpastouni.png"); ennia_mpastouni = pygame.image.load("./mpastounia/enia_mpastouni.png")
deka_mpastouni = pygame.image.load("./mpastounia/deka_mpastouni.png"); J_mpastouni = pygame.image.load("./mpastounia/J_mpastouni.png"); Q_mpastouni = pygame.image.load("./mpastounia/Q_mpastouni.png"); K_mpastouni = pygame.image.load("./mpastounia/K_mpastouni.png")
klisto_filo = pygame.image.load("./imges/klisto_filo.png")

fila = [ asos_karo, dio_karo, tria_karo, tesera_karo, pente_karo, eksi_karo, epta_karo, okto_karo, ennia_karo, deka_karo, J_karo, Q_karo, K_karo,
         asos_spathi, dio_spathi, tria_spathi, tesera_spathi, pente_spathi, eksi_spathi,epta_spathi, okto_spathi, ennia_spathi,deka_spathi, J_spathi, Q_spathi, K_spathi,
         asos_koupa, dio_koupa, tria_koupa, tesera_koupa, pente_koupa, eksi_koupa, epta_koupa, okto_koupa, ennia_koupa, deka_koupa, J_koupa, Q_koupa, K_koupa,
         asos_mpastouni, dio_mpastouni, tria_mpastouni, tesera_mpastouni, pente_mpastouni, eksi_mpastouni, epta_mpastouni, okto_mpastouni, ennia_mpastouni, deka_mpastouni, J_mpastouni, Q_mpastouni, K_mpastouni, klisto_filo]

playerCardCords = (740, 750); opponentCardCords = (740, 250)
playerScore = 0; opponentScore = 0
mouse = (0, 0)


program = True
while program:
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    running = True
    gameOn = True

    case_win = False; case_lose = False; case_tie = False

    gameSet_Player = False
    gameSet_Opponent = False
    playerScore = 0
    opponentScore = 0
    resultPlayer = 52
    result_opponent = 52
    case = nada

    ace_choosing = False
#   Aces for player 1
    ace_ten_chosen_0 = False
    ace_one_chosen_0 = False
#   Aces for player 2
    ace_ten_chosen_1 = False
    ace_one_chosen_1 = False

    playerTurn = True

    pygame.draw.rect(screen, black, (0, 0, 2000, 1200))
    screen.blit(bg, (0, 0))
    while running:
        FPS.tick(10)
        Player1_Score = font.render(str(playerScore), True, blue)
        Player2_Score = font.render(str(opponentScore), True, black)
        display_buttons()

        if playerTurn:
            update_screen(fila, Player1_Score, Player2_Score, resultPlayer, playerCardCords, case)
        if not playerTurn:
            update_screen(fila, Player1_Score, Player2_Score, result_opponent, opponentCardCords, case)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                program = False
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()

        if gameOn:

#         Player 1 Turn
            if playerTurn and gameOn and (not gameSet_Player):

                if (mouse[0] > 1100 and mouse[1] > 650) and (mouse[0] < 1250 and mouse[1] < 720):
                    x = randrange(51)
                    if True:
                        resultPlayer = draw_card0(values, playerCardCords, x)
                    if type(resultPlayer) == int:
                        if (resultPlayer == 0) or (resultPlayer == 13) or (resultPlayer == 26) or (resultPlayer == 39):
                            values[resultPlayer] = False
                            if (ace_one_chosen_0 == False) and (ace_ten_chosen_0 == False):
                                ace_choosing = True

                                while ace_choosing:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            choosing = False
                                            running = False
                                            program = False
                                    screen.blit(ace_conversion, (100, 800))
                                    pygame.draw.rect(screen, brown, (462, 800, 65, 60), 4)
                                    pygame.draw.rect(screen, brown, (602, 800, 65, 60), 4)
                                    if pygame.mouse.get_pressed()[0]:
                                        mouse = pygame.mouse.get_pos()

                                    if (mouse[0] > 462 and mouse[1] > 800) and (mouse[0] < 527 and mouse[1] < 860) or ace_ten_chosen_0:
                                        mouse = (0,0)
                                        playerScore += 1
                                        ace_one_chosen_0 = True
                                        ace_choosing = False
                                    elif (mouse[0] > 602 and mouse[1] > 800) and (mouse[0] < 667 and mouse[0] < 860) or ace_one_chosen_0:
                                        mouse = (0, 0)
                                        playerScore += 10
                                        ace_ten_chosen = True
                                        ace_choosing = False
                                    pygame.display.update()

                            elif ace_ten_chosen_0:
                                playerScore += 1
                            elif ace_one_chosen_0:
                                playerScore += 10
                        playerScore += values[resultPlayer]
                        values[resultPlayer] = False
                        mouse = (0, 0)
                    else:
                        values[int(resultPlayer)] = False
                elif (mouse[0] > 1350 and mouse[1] > 650) and (mouse[0] < 1500 and mouse[1] < 720):
                    playerTurn = False
                    gameSet_Player = True
                    mouse = (0, 0)

#         Player 2 Turn
            elif (not playerTurn) and gameOn and (not gameSet_Opponent):

                if (mouse[0] > 1100 and mouse[1] > 650) and (mouse[0] < 1250 and mouse[1] < 720):
                    x = randrange(51)
                    if True:
                        result_opponent = draw_card1(values, opponentCardCords, x)
                    if type(result_opponent) == int:
                        if (result_opponent == 0) or (result_opponent == 13) or (result_opponent == 26) or (result_opponent == 39):
                            values[result_opponent] = False
                            if (ace_one_chosen_1 == False) and (ace_ten_chosen_1 == False):
                                ace_choosing = True

                                while ace_choosing:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            ace_choosing = False
                                            running = False
                                            program = False
                                    screen.blit(ace_conversion, (100, 800))
                                    pygame.draw.rect(screen, brown, (462, 800, 65, 60), 4)
                                    pygame.draw.rect(screen, brown, (602, 800, 65, 60), 4)
                                    if pygame.mouse.get_pressed()[0]:
                                        mouse = pygame.mouse.get_pos()
                                    if (mouse[0] > 462 and mouse[1] > 800) and (mouse[0] < 527 and mouse[1] < 860) or ace_ten_chosen_1:
                                        mouse = (0, 0)
                                        opponentScore += 1
                                        ace_one_chosen_1 = True
                                        ace_choosing = False
                                    elif (mouse[0] > 602 and mouse[1] > 800) and (mouse[0] < 667 and mouse[0] < 860) or ace_one_chosen_1:
                                        mouse = (0, 0)
                                        opponentScore += 10
                                        ace_ten_chosen_1 = True
                                        ace_choosing = False
                                    pygame.display.update()

                            elif ace_ten_chosen_1:
                                opponentScore += 1
                            elif ace_one_chosen_1:
                                opponentScore += 10
                        opponentScore += values[result_opponent]
                        values[result_opponent] = False
                        mouse = (0, 0)
                    else:
                        values[int(result_opponent)] = False
                elif (mouse[0] > 1350 and mouse[1] > 650) and (mouse[0] < 1500 and mouse[1] < 720):
                    gameSet_Oponent = True

            playerScore = int(playerScore)
            opponentScore = int(opponentScore)
            if (playerScore == 21) or (opponentScore > 21) or (gameSet_Opponent and gameSet_Player and playerScore > opponentScore):
                case = player1_win
                gameOn = False
            elif (playerScore > 21) or (opponentScore == 21) or (gameSet_Player and gameSet_Opponent and playerScore < opponentScore):
                case = player2_win
                gameOn = False
            elif (playerScore == opponentCardCords) or (gameSet_Opponent and gameSet_Player):
                case = tie_text
                gameOn = False
#    End of game
        else:
            pygame.draw.rect(screen, black, (700, 100, 245, 60), 5)
            screen.blit(play_again_button, (700, 100))
#    Play again option
            if (mouse[0] > 700 and mouse[1] > 100) and (mouse[0] < 945 and mouse[1] < 160):
                mouse = (0, 0)
                running = False
                case = ""

        pygame.display.update()
pygame.quit()
