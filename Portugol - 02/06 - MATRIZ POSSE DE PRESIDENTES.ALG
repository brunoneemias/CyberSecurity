Algoritmo "semnome"

Var
Presidentes:vetor[1..7, 1..2] de caractere

ano_atual, i:inteiro
presidente: caractere
ano_posse,tempo_P,c  : inteiro

Inicio
Presidentes[1,1]<- ("|        Nome Presidente          |")
Presidentes[1,2]<- ("    Ano Posse     |")
Presidentes[2,1]<-("         Itamar Franco")
Presidentes[2,2]<-("                 1992")
Presidentes[3,1]<- ("         Fernando Henrique Cardoso")
Presidentes[3,2]<- ("     1995")
Presidentes[4,1]<- ("         Lula")
Presidentes[4,2]<- ("                          2003")
Presidentes[5,1]<- ("         Dilma Rouseef")
Presidentes[5,2]<- ("                 2011")
Presidentes[6,1]<- ("         Michel Temer")
Presidentes[6,2]<-("                  2016")
Presidentes[7,1]<-("         Jair Bolsonaro")
Presidentes[7,2]<- ("                2019")

para i de 1 ate 7 faca
     para c de 1 ate 2 faca
     escreva(Presidentes[i,c])
     fimpara
     escreval()
fimpara
escreval()
escreva("Digite o Ano Atual: ")
leia(ano_atual)

para i de 2 ate 7 faca
     presidente <- Presidentes[i,1]
     ano_posse <- caracpnum(presidentes[i,2])
     tempo_P <- ano_atual - ano_posse
     escreval(presidente, " foi presidente em ",ano_posse," e já fazem ",tempo_P," anos da sua posse")
     escreval()
fimpara

Fimalgoritmo