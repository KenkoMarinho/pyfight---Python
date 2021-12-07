def telaselecao():
    import pygame
    import pyfightgame
    #definindo cores:
    cor_branca=(255,255,255)
    cor_azul=(0,0,255)
    cor_verde=(0,128,0)
    cor_preto=(0,0,0) 
    cor_vermelho=(255,0,0)
    cor_laranja=(255, 165, 0)
    cor_amarelo=(255,255,0)
    cor_roxo=(153,51,153)
    cor_verde_claro=(144,238,144)
    cor_vermelho_escuro=(139,0,0)
    cor_azul_claro=(176,224,230)
    cor_marrom=(165,42,42)
    #declarando a fonte
    pygame.font.init()
    fontearial=pygame.font.SysFont('Arial', 40)

    #Definições Dos Objetos(variaveis):
    pygame.init()                                   #inicia a classe pygame
    tela=pygame.display.set_mode([800,600])         #define o tamanho da tela
    pygame.display.set_caption("Pyfighter Tela de Seleção")         #titulo da janela
    relogio=pygame.time.Clock()                     #controle de frames
    superficie=pygame.Surface((800,600))            #cria uma superficie de 200x200, mas não a mostra na tela
    superficie.fill(cor_preto)                      #muda a cor da superficie
    cursor=pygame.Rect(1,1,1,1)
    champion1mostrar=pygame.Rect(600,0,400,300)
    champion2mostrar=pygame.Rect(600,300,400,300)

    malybutton=pygame.Rect(0,0,200,200)
    prubutton=pygame.Rect(200,0,200,200)
    kerkadbutton=pygame.Rect(400,0,200,200)
    vagusbutton=pygame.Rect(0,200,200,200)
    kikkybutton=pygame.Rect(200,200,200,200)
    adrianbutton=pygame.Rect(400,200,200,200)
    mavisbutton=pygame.Rect(0,400,200,200)
    melkiorbutton=pygame.Rect(200,400,200,200)
    kutsuobutton=pygame.Rect(400,400,200,200)

    #condições de loopings:
    sair=False
    champion1escolhido=False
    champion2escolhido=False
    champion1name=""
    champion2name=""
    transicao=0

    while sair==False:                                  #resumidamente, mantem a janela aberta enquanto o looping se manter.
        (cursor.left,cursor.top)=pygame.mouse.get_pos()
        for event in pygame.event.get():                #busca qual evento está acontecendo na tela
            if event.type == pygame.QUIT:               #se o evento for o usuario clicando no X para fechar
                sair=True                               #seta sair para  True, dando fim ao looping e executando pygame.quit.
            if event.type == pygame.MOUSEBUTTONDOWN:    #detecta click do mouse
                if cursor.colliderect(malybutton):
                    if champion1escolhido==False:
                        champion1escolhido=True
                        champion1name="Maly"
                        print("Player 1 Escolheu Maly!")
                    elif champion2escolhido==False:
                        champion2escolhido=True
                        champion2name="Maly"
                        print("Player 2 Escolheu Maly!")
                    
                if cursor.colliderect(prubutton):
                    if champion1escolhido==False:
                        champion1escolhido=True
                        champion1name="Pru"
                        print("Player 1 Escolheu Pru!")
                    elif champion2escolhido==False:
                        champion2escolhido=True
                        champion2name="Pru"
                        print("Player 2 Escolheu Pru!")
                if cursor.colliderect(kerkadbutton):
                    if champion1escolhido==False:
                        champion1escolhido=True
                        champion1name="Kerkad"
                        print("Player 1 Escolheu Kerkad!")
                    elif champion2escolhido==False:
                        champion2escolhido=True
                        champion2name="Kerkad"
                        print("Player 2 Escolheu Kerkad!")
                if cursor.colliderect(vagusbutton):
                    if champion1escolhido==False:
                        champion1escolhido=True
                        champion1name="Vagus"
                        print("Player 1 Escolheu Vagus!")
                    elif champion2escolhido==False:
                        champion2escolhido=True
                        champion2name="Vagus"
                        print("Player 2 Escolheu Vagus!")
                if cursor.colliderect(kikkybutton):
                    if champion1escolhido==False:
                        champion1escolhido=True
                        champion1name="Kikky"
                        print("Player 1 Escolheu Kikky!")
                    elif champion2escolhido==False:
                        champion2escolhido=True
                        champion2name="Kikky"
                        print("Player 2 Escolheu Kikky!")
                if cursor.colliderect(adrianbutton):
                    if champion1escolhido==False:
                        champion1escolhido=True
                        champion1name="Adrian"
                        print("Player 1 Escolheu Adrian!")
                    elif champion2escolhido==False:
                        champion2escolhido=True
                        champion2name="Adrian"
                        print("Player 2 Escolheu Adrian!")
                if cursor.colliderect(mavisbutton):
                    if champion1escolhido==False:
                        champion1escolhido=True
                        champion1name="Mavis"
                        print("Player 1 Escolheu Mavis!")
                    elif champion2escolhido==False:
                        champion2escolhido=True
                        champion2name="Mavis"
                        print("Player 2 Escolheu Mavis!")
                if cursor.colliderect(melkiorbutton):
                    if champion1escolhido==False:
                        champion1escolhido=True
                        champion1name="Melkior"
                        print("Player 1 Escolheu Melkior!")
                    elif champion2escolhido==False:
                        champion2escolhido=True
                        champion2name="Melkior"
                        print("Player 2 Escolheu Melkior!")
                if cursor.colliderect(kutsuobutton):
                    if champion1escolhido==False:
                        champion1escolhido=True
                        champion1name="Kutsuo"
                        print("Player 1 Escolheu Kutsuo!")
                    elif champion2escolhido==False:
                        champion2escolhido=True
                        champion2name="Kutsuo"
                        print("Player 2 Escolheu Kutsuo!")

        prubutton=pygame.draw.rect(tela,cor_amarelo,prubutton)
        prutext=fontearial.render('Pru',1,cor_vermelho)
        tela.blit(prutext,(230,30)) 

        malybutton=pygame.draw.rect(tela,cor_laranja,malybutton)
        malytext=fontearial.render('Maly',1,cor_marrom)
        tela.blit(malytext,(30,30))

        kerkadbutton=pygame.draw.rect(tela,cor_roxo,kerkadbutton)
        kerkadtext=fontearial.render('Kerkad',1,cor_azul)
        tela.blit(kerkadtext,(450,30))

        vagusbutton=pygame.draw.rect(tela,cor_verde,vagusbutton)
        vagustext=fontearial.render('Vagus',1,cor_amarelo)
        tela.blit(vagustext,(30,250))

        kikkybutton=pygame.draw.rect(tela,cor_azul,kikkybutton)
        kikkytext=fontearial.render('Kikky',1,cor_marrom)
        tela.blit(kikkytext,(230,250))

        adrianbutton=pygame.draw.rect(tela,cor_verde_claro,adrianbutton)
        adriantext=fontearial.render('Adrian',1,cor_branca)
        tela.blit(adriantext,(430,250))

        mavisbutton=pygame.draw.rect(tela,cor_vermelho_escuro,mavisbutton)
        mavistext=fontearial.render('Mavis',1,cor_preto)
        tela.blit(mavistext,(30,450))

        melkiorbutton=pygame.draw.rect(tela,cor_branca,melkiorbutton)
        melkiortext=fontearial.render('Melkior',1,cor_azul)
        tela.blit(melkiortext,(230,450))

        kutsuobutton=pygame.draw.rect(tela,cor_azul_claro,kutsuobutton)
        kutsuotext=fontearial.render('Kutsuo',1,cor_verde)
        tela.blit(kutsuotext,(430,450))

        if champion1escolhido==True:
            champion1mostrar=pygame.draw.rect(tela,cor_branca,champion1mostrar)
            champion1nome=fontearial.render(champion1name,1,cor_vermelho)
            tela.blit(champion1nome,(620,20))
        if champion2escolhido==True:
            champion2mostrar=pygame.draw.rect(tela,cor_vermelho,champion2mostrar)
            champion2nome=fontearial.render(champion2name,1,cor_branca)
            tela.blit(champion2nome,(620,320))

        if champion2escolhido==True:
            transicao+=1
            if transicao==75:
                pygame.quit()
                pyfightgame.pyfightgame(champion1name,champion2name)


        relogio.tick(30)                  #configuração da taxa de frames por segundo
        pygame.display.update()           #atualiza o display com novos eventos ao fim do ciclo
        
    pygame.quit()           #o programa se fecha já que pygame.quit() fecha a janela.