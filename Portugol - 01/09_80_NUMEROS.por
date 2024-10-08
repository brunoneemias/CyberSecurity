programa
{
	inteiro c=0
	real numeros[80], numeros1[80]
	funcao inicio()
	{
		escreva("####################################\n")
		escreva("#       09 - 80 Números            #\n")
		escreva("####################################\n\n")

		para (inteiro i=0; i<80; i++) {
			escreva("Insira o ",i+1,"° numero: ")
			leia(numeros[i])

			se ((numeros[i] >= 10) e (numeros[i] <=150)){
				numeros1[c] = numeros[i]
				c=c+1 
			}
		}
		limpa()
		escreva("####################################\n")
		escreva("#       09 - 80 Números            #\n")
		escreva("####################################\n\n")
		se(c>0) {
		escreva(c, " números estão entre 10(inclusive) e 150(inclusive) e são eles:\n")
		para (inteiro i=0; i<c; i++){
			escreva(i+1,"° ",numeros1[i],"\n")
			}
		}senao{
			escreva("Os números inseridos não estão entre o intervalo de 10 e 150!\n\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 26; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */