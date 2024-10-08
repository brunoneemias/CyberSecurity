programa
{
	funcao cabecalho(){
		escreva("++++++++++++++++++++++++++++++++++++\n")
		escreva("+     03 - Vetor crescente        +\n")
		escreva("++++++++++++++++++++++++++++++++++++\n\n")

	}
	
	inteiro numeros[8],c=0, aux=0
	funcao inicio()
	{
		cabecalho()
		para (inteiro i=0; i<8; i++){ 
		escreva("Digite o ",i+1,"° número:")
		leia(numeros[i])

		se (c > 0) { 
			para (inteiro a=0; a<=c; a++){
				para(inteiro b=0; b<=c; b++) { 
					se(numeros[a] < numeros[b]){
						aux = numeros[b]
						numeros[b] = numeros[a] 
						numeros[a] = aux
					}
				}
			}
		
		}
	c++
		}
	
	escreva("Numeros inseridos em forma crescente: \n")
	para (inteiro i=0; i<8; i++){
		escreva("[",numeros[i],"]\n")
	}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 643; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */