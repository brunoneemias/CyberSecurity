programa
{
	funcao cabecalho(){
		escreva("++++++++++++++++++++++++++++++++++++\n")
		escreva("+     04 - Aritmética de vetor     +\n")
		escreva("++++++++++++++++++++++++++++++++++++\n\n")

	}
	inteiro x[20], y[20],z[20]
	funcao inicio()
	{
		cabecalho()
		para (inteiro i=0; i<20; i++){ 
		escreva("Digite o ",i+1,"° número:")
		leia(x[i])

		y[i] =(x[i]*100)
		}

		para (inteiro a=0; a<20; a++){
			z[a] =(y[a]/x[a])
		}
		limpa()
		cabecalho()
		escreva("Vetor X -> ") 
		para (inteiro i=0; i<20; i++){
			escreva(x[i]," ")
		}

		escreva("\nVetor Y -> ") 
		para (inteiro i=0; i<20; i++){
			escreva(y[i]," ")
		}

		escreva("\nVetor Z -> ") 
		para (inteiro i=0; i<20; i++){
			escreva(z[i]," ")
		}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 718; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */