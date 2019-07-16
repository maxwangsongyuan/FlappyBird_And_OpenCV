import random
import sys
import pygame
import flappy

def main():
    global SCREEN, FPSCLOCK

    pygame.init()  # initialize pygame

    FPSCLOCK = pygame.time.Clock()  # control when to run a loop
    SCREEN = pygame.display.set_mode((flappy.SCREENWIDTH, flappy.SCREENHEIGHT))  #create a screen

    pygame.display.set_caption('Flappy Bird')

    # numbers sprites for score display
    # use pygame.image.load（）to load images （jpg,png,gif,bmp,pcx,tif,tga and etc）。
    # convert_alpha() to remove the background and keep the front image

    flappy.IMAGES['numbers'] = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha()
    )

    # game over sprite
    flappy.IMAGES['gameover'] = pygame.image.load('assets/sprites/gameover.png').convert_alpha()
    # message sprite for welcome screen
    flappy.IMAGES['message'] = pygame.image.load('assets/sprites/message.png').convert_alpha()
    # base (ground) sprite
    flappy.IMAGES['base'] = pygame.image.load('assets/sprites/base.png').convert_alpha()

    # sounds
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    flappy.SOUNDS['die']    = pygame.mixer.Sound('assets/audio/die' + soundExt)
    flappy.SOUNDS['hit']    = pygame.mixer.Sound('assets/audio/hit' + soundExt)
    flappy.SOUNDS['point']  = pygame.mixer.Sound('assets/audio/point' + soundExt)
    flappy.SOUNDS['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh' + soundExt)
    flappy.SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)

    while True:
        # select random background sprites

        randBg = random.randint(0, len(flappy.BACKGROUNDS_LIST) - 1)
        flappy.IMAGES['background'] = pygame.image.load(flappy.BACKGROUNDS_LIST[randBg]).convert()

        # select random player sprites

        randPlayer = random.randint(0, len(flappy.PLAYERS_LIST) - 1)
        flappy.IMAGES['player'] = (
            pygame.image.load(flappy.PLAYERS_LIST[randPlayer][0]).convert_alpha(),
            pygame.image.load(flappy.PLAYERS_LIST[randPlayer][1]).convert_alpha(),
            pygame.image.load(flappy.PLAYERS_LIST[randPlayer][2]).convert_alpha(),
        )

        # select random pipe sprites
        pipeindex = random.randint(0, len(flappy.PIPES_LIST) - 1)
        flappy.IMAGES['pipe'] = (
            pygame.transform.flip(
                pygame.image.load(flappy.PIPES_LIST[pipeindex]).convert_alpha(), False, True),
            pygame.image.load(flappy.PIPES_LIST[pipeindex]).convert_alpha(),
        )

        # hismask for pipes
        flappy.HITMASKS['pipe'] = (
            flappy.getHitmask(flappy.IMAGES['pipe'][0]),
            flappy.getHitmask(flappy.IMAGES['pipe'][1]),
        )

        # hitmask for player
        flappy.HITMASKS['player'] = (
            flappy.getHitmask(flappy.IMAGES['player'][0]),
            flappy.getHitmask(flappy.IMAGES['player'][1]),
            flappy.getHitmask(flappy.IMAGES['player'][2]),
        )

        movementInfo = flappy.showWelcomeAnimation()  #returnn 'playery'（player's location）,'basex'（base image's location） 'playerIndexGen'（flying position index）
        crashInfo = flappy.mainGame(movementInfo)
        flappy.showGameOverScreen(crashInfo)

if __name__ == '__main__':
    main()