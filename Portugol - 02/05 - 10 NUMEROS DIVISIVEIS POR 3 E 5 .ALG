Algoritmo "05 - 10 numeros divisiveis por 3 e 5 "
procedimento cabecalho()
inicio
   escreval("++++++++++++++++++++++++++++++++++++")
   escreval("+ 10 numeros divisiveis por 3 e 5  +")
   escreval("++++++++++++++++++++++++++++++++++++")
   escreval()
fimprocedimento
Var
   k,l,m: vetor[1..10] de inteiro
   i,valor: inteiro
Inicio
   cabecalho()
   Para i de 1 ate 10 faca
      Escreva("Digite o ", i, "º número inteiro divisivel por 3: ")
      Leia(valor)
      enquanto (valor % 3 <> 0) faca
         escreva("Numero invalido! Digite outro valor: ")
         leia(valor)
      fimenquanto
      k[i] <- valor
   fimpara
   limpatela()
   cabecalho()
   Para i de 1 ate 10 faca
      Escreva("Digite o ", i, "º número inteiro divisivel por 5: ")
      Leia(valor)
      enquanto (valor % 5 <> 0) faca
         escreva("Numero invalido! Digite outro valor: ")
         leia(valor)
      fimenquanto
      l[i] <- valor
   fimpara
   limpatela()
   cabecalho()
   Para i de 1 ate 10 faca
      se (k[i] > l[i]) ou (k[i] = l[i]) entao
         m[i] <- (k[i] - l[i])
      senao
         m[i] <- (l[i] - k[i])
      fimse
   fimpara
   escreval()
   escreva("Valores divisiveis por 3 -> ")
   para i de 1 ate 10 faca
      escreva("[",k[i],"]")
   fimpara

   escreval()
   escreva("Valores divisiveis por 5 -> ")
   para i de 1 ate 10 faca
      escreva("[",l[i],"]")
   fimpara

   escreval()
   escreva("Resultado da substração ->  ")
   para i de 1 ate 10 faca
      escreva("[",m[i],"]")
   fimpara
Fimalgoritmo