import pygame
pygame.init()

""" Variabel global """
lebar_scene = 500
tinggi_scene = 500
judul_scene = "PING PONG GAME"
gambar_background = "fantasi_sky.jpg"
musik_background = "Battle_Music.mp3"
GAME_ON = True
GAME_FINISH = False

""" Merebut scene """
scene = pygame.display.set_mode((lebar_scene, tinggi_scene))
background = pygame.transform.scale(pygame.image.load(gambar_background),
    (lebar_scene, tinggi_scene))
pygame.display.set_caption(judul_scene)


""" Membuat musik """
pygame.mixer.init()
pygame.mixer.music.load(musik_background)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play()

""" Game on """
FPS = pygame.time.Clock()
while GAME_ON:
    """ event handler untuk QUIT """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_ON = False

    if GAME_FINISH == False:
        """ tampilkan """
        scene.blit(background, (0,0))

    """ penting """
    FPS.tick(60)
    pygame.display.update()




