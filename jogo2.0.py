#Maria Eduarda Nogueira Freitas   #536868

import turtle
import random

#Comandos para a criação da janela
janela = turtle.Screen()
janela.bgpic('ceu.gif')#Importação da imagem de fundo
janela.bgcolor('#EE82EE')#Cor do fundo para completar o cenário
janela.tracer(0)

#Importação dos ítens do jogo
nave = 'nave.gif'
cow = 'cow.gif'
alien = 'alien.gif'
star1 = 'starsR2.gif'
start= 'picwish.gif'
gameover='gameOver2.gif'

#Comandos para executar a entrada dos GIF's na janela do jogo
janela.addshape(nave)
janela.addshape(cow)
janela.addshape(alien)
janela.addshape(star1)
janela.addshape(start)  
janela.addshape(gameover)

#Start no início do jogo
pstart=turtle.Turtle()
pstart.shape(start)
janela.update()

#Criação do personagem principal (nave)
pers = turtle.Turtle()
pers.shape(nave)#A forma do ítem
pers.left(90)#Angulação
pers.up()#Comando para o persongem não riscar a tela
pers.goto(0, -150)#Posição inicial

#Criação do ítem para a pontuação(gasolina)
bom = turtle.Turtle()
bom.up()
bom.shape(cow)
bom.right(90)
bom.goto(random.randint(-100, 100), random.randint(-100, 100))#Utilização da blt randon para a movimentação do ítem de forma aleatória e dentro destas coordenadas

#Criaçao do obstáculo
ruim = turtle.Turtle()
ruim.up()
ruim.shape(alien)
ruim.right(90)
ruim.goto(random.randint(-100, 100), random.randint(-100, 100))

#Mensagem de 'game over'
go=turtle.Turtle()
go.shape(gameover)
go.ht()

#Bordas de colisão
borda1D = turtle.Turtle()
borda1D.up()
borda1D.shape(star1)
borda1D.goto(350, -10)

borda2E = turtle.Turtle()
borda2E.up()
borda2E.shape(star1)
borda2E.goto(-360, -90)

#Funções para a movimentação do personagem e colisão com as bordas
def personagemDireita():
    global gasolina
    global km
    if pers.xcor() <= 119:
        x = pers.xcor()
        x += 8
        pers.setx(x)
    else:
        pontuacao.clear()
        turtle.done()

def personagemEsquerda():
    if pers.xcor() >= -119:
        x = pers.xcor()
        x += -8
        pers.setx(x)
    else:
        pontuacao.clear()
        turtle.done()

#Linhas criadas para o maior delimitação das bordas
#Lado direito
linhad = turtle.Turtle()
linhad.pensize(3)
linhad.color('#B0C4DE')
linhad.up()
linhad.goto(150, -450)
linhad.down()
linhad.goto(150, 450)
linhad.left(90)
#Lado esquerdo
linhae = turtle.Turtle()
linhae.pensize(3)
linhae.color('#B0C4DE')
linhae.up()
linhae.goto(-150, -450)
linhae.down()
linhae.goto(-150, 450)
linhae.left(90)

def andar():#Função para a movimentação dos ítens de pontuação e obstáculo
    if bom.ycor() >= -450:#Se 'bom' estiver entre a coordenada, irá andar na velocidade definida
        bom.forward(6)#Velocidade menor que o a do obstáculo
    else:#Senão, voltará a andar aleatóriamente dentro dessas coordenadas, na velocidade '0'
        bom.goto(random.randint(-100, 100), random.randint(310, 450))

    if ruim.ycor() >= -450:
        ruim.forward(10)
    else:
        ruim.goto(random.randint(-100, 100), random.randint(310, 450))
    #Condição para haver uma pausa no jogo caso o personagem colidir com o obstáculo
    if ruim.ycor() + 20 >= pers.ycor() - 20 and ruim.ycor() - 20 <= pers.ycor() - 20 and pers.xcor() + 20 >= ruim.xcor() - 20 and pers.xcor() - 20 <= ruim.xcor() + 20:
        go.st()
        janela.update()
        turtle.done()

    janela.update()#Atualização da janela
    pontuacoes()#Chamada da função de pontuação
    turtle.ontimer(andar, 1000 // 60)

#Somatória de pontos e quilometragem
gasolina = 50 #Varlores iniciais das variáveis
km = 0

pontuacao = turtle.Turtle()#Criação do ítem que vai receber a pontuação
pontuacao.up()
pontuacao.pencolor('#FFF0F5')
pontuacao.goto(-320,250)
pontuacao.ht()#Comando para sumir asim que executar

def pontuacoes():
    global gasolina#Declaração de variáveis globais
    global km

    if bom.ycor() + 15 >= pers.ycor() - 15 and bom.ycor() - 15 <= pers.ycor() - 15 and pers.xcor() + 15 >= bom.xcor() - 15 and pers.xcor() - 15 <= bom.xcor() + 15:
        bom.goto(random.randint(-100, 100), random.randint(310, 450))
        gasolina += 10

    gasolina -= 0.08#Subtração dos pontos para que o jogo encerre
    km += 0.05

    pontuacao.clear()
    pontuacao.write(
        '''SCORE: {:.1f}\n
KM/H: {:.1f} '''.format(gasolina, km), font=('Verdana',13,'normal'))

    if gasolina <= 0:
        go.st()
        janela.update()
        turtle.done()

def iniciar():
    global gasolina
    global km
    pstart.ht()
    go.ht()
    #Comando para zerar a pontuação e voltar os ítens pra posição inicial
    gasolina = 50
    km = 0
    pontuacao.clear()
    bom.goto(random.randint(-100, 100), random.randint(310, 450))
    ruim.goto(random.randint(-100, 100), random.randint(310, 450))
    pers.goto(0,-150)
    turtle.ontimer(andar, 1000 // 60)#Definição do FPS junto com chamada da função inicial
janela.onkeypress(iniciar, 'space')

#Definição das teclas que serão utilizadas para a movimentaçao do personagem principal(nave)
janela.onkeypress(personagemEsquerda, "a")
janela.onkeypress(personagemDireita, "d")
janela.listen()
#Comando para a janela permanecer aberta
janela.mainloop()