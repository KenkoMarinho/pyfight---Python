def pyfightgame(champion1name,champion2name):
    import pygame
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
    pygame.display.set_caption("Pyfighter")         #titulo da janela
    relogio=pygame.time.Clock()                     #controle de frames
    superficie=pygame.Surface((800,600))            #cria uma superficie de 200x200, mas não a mostra na tela
    superficie.fill(cor_preto)                      #muda a cor da superficie

    lutador1=pygame.Rect(200,300,50,50)
    lutador2=pygame.Rect(500,300,50,50)
    chao=pygame.Rect(0,450,800,150)

    #condições de loopings:
    sair=False
    antigravidade=False
    antigravidadecontador=0
    podedoublejump=True

    #declarando as cores e skins dos lutadores:
    if champion1name=="Pru":
        corlutador1=cor_amarelo
    if champion2name=="Pru":
        corlutador2=cor_amarelo

    if champion1name=="Maly":
        corlutador1=cor_laranja
    if champion2name=="Maly":
        corlutador2=cor_laranja

    if champion1name=="Kerkad":
        corlutador1=cor_roxo
    if champion2name=="Kerkad":
        corlutador2=cor_roxo

    if champion1name=="Vagus":
        corlutador1=cor_verde
    if champion2name=="Vagus":
        corlutador2=cor_verde

    if champion1name=="Kikky":
        corlutador1=cor_azul
    if champion2name=="Kikky":
        corlutador2=cor_azul

    if champion1name=="Adrian":
        corlutador1=cor_verde_claro
    if champion2name=="Adrian":
        corlutador2=cor_verde_claro

    if champion1name=="Mavis":
        corlutador1=cor_vermelho_escuro
    if champion2name=="Mavis":
        corlutador2=cor_vermelho_escuro

    if champion1name=="Melkior":
        corlutador1=cor_marrom
    if champion2name=="Melkior":
        corlutador2=cor_marrom

    if champion1name=="Kutsuo":
        corlutador1=cor_azul_claro
    if champion2name=="Kutsuo":
        corlutador2=cor_azul_claro

    while sair==False:                                          #resumidamente, mantem a janela aberta enquanto o looping se manter.
        tela.fill(cor_preto)                                    #reseta o fundo preto
        for event in pygame.event.get():                        #busca qual evento está acontecendo na tela
            if event.type == pygame.QUIT:                       #se o evento for o usuario clicando no X para fechar
                sair=True                                       #seta sair para  True, dando fim ao looping e executando pygame.quit.

            if event.type == pygame.KEYDOWN:                    #controlador esquerda-direita do retangulo
                if event.key==pygame.K_a and lutador1.left>15:              #andar esquerda
                    lutador1=lutador1.move(-15,0)
                if event.key==pygame.K_d and lutador1.left<730:             #andar direita
                    lutador1=lutador1.move(15,0)
                if event.key==pygame.K_w and lutador1.colliderect(chao):
                    antigravidade=True                                      #desabilita gravidade p/ pular
                    antigravidadecontador=45                                #tempo q vc pode ficar pulando em frames
                if event.key==pygame.K_w and podedoublejump and not(lutador1.colliderect(chao)): #doublejump
                    podedoublejump=False
                    antigravidadecontador=30

        if antigravidade==True:
            antigravidadecontador+=-1
            lutador1.top+=-2                                    #configurações de doublejump
            if antigravidadecontador==0:
                antigravidade=False
        
        if lutador1.colliderect(chao):                          #reseta o doublejump quando o personagem chega ao chao
            podedoublejump=True

        if lutador1.colliderect(lutador2):                      #configuração de empurrões
            if lutador1.left<=lutador2.left:                    #entre personagens
                lutador1.left+=-15
                lutador2.left+=15
            else:
                lutador1.left+=15
                lutador2.left+=-15


        if not(lutador1.colliderect(chao)):                     #gravidade
            if antigravidade==False:
                lutador1.top+=+3                                #velocidade de queda
        if not(lutador2.colliderect(chao)):
            if antigravidade==False:
                lutador2.top+=+3                                #velocidade de queda

        lutador1=pygame.draw.rect(tela,corlutador1,lutador1)
        lutador2=pygame.draw.rect(tela,corlutador2,lutador2)
        chao=pygame.draw.rect(tela,cor_branca,chao)

        relogio.tick(30)                  #configuração da taxa de frames por segundo
        pygame.display.update()           #atualiza o display com novos eventos ao fim do ciclo
        
    pygame.quit()           #o programa se fecha já que pygame.quit() fecha a janela.
