
def main():
    import pyfightselection
    import pygame
    #definindo cores:
    cor_branca=(255,255,255)
    cor_azul=(0,0,255)
    cor_verde=(0,128,0)
    cor_preto=(0,0,0) 
    cor_vermelho=(255,0,0)

    #declarando a fonte
    pygame.font.init()
    fontearial=pygame.font.SysFont('Arial', 40)

    #Definições Dos Objetos(variaveis):
    pygame.init()                                   #inicia a classe pygame
    tela=pygame.display.set_mode([800,600])         #define o tamanho da tela
    pygame.display.set_caption("Pyfighter")         #titulo da janela
    relogio=pygame.time.Clock()                     #controle de frames
    superficie=pygame.Surface((800,600))            #cria uma superficie de 200x200, mas não a mostra na tela
    superficie.fill(cor_preto)                      #muda a cor da superficie
    cursor=pygame.Rect(1,1,1,1)
    playbutton=pygame.Rect(250,200,300,200)
    
    #condições de loopings:
    sair=False
    flag1=True

    while sair==False:                                  #resumidamente, mantem a janela aberta enquanto o looping se manter.
        (cursor.left,cursor.top)=pygame.mouse.get_pos()
        for event in pygame.event.get():                #busca qual evento está acontecendo na tela
            if event.type == pygame.QUIT:               #se o evento for o usuario clicando no X para fechar
                sair=True                               #seta sair para  True, dando fim ao looping e executando pygame.quit.
            if event.type == pygame.MOUSEBUTTONDOWN:    #detecta click do mouse
                if cursor.colliderect(playbutton):
                    flag1=False
        
        playbutton=pygame.draw.rect(tela,cor_branca,playbutton)
        playtext=fontearial.render('PLAY',1,cor_vermelho)
        tela.blit(playtext,(350,275))

        relogio.tick(30)                  #configuração da taxa de frames por segundo
        pygame.display.update()           #atualiza o display com novos eventos ao fim do ciclo

        if flag1==False:
            sair=True
            pygame.quit()
            pyfightselection.telaselecao()
        
    pygame.quit()           #o programa se fecha já que pygame.quit() fecha a janela.

main()