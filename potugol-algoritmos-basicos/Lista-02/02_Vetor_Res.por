programa
{
	inteiro numeros[8], res_positivo[8], res_negativo[8],c1=0,c2=0
	funcao cabecalho(){
		escreva("++++++++++++++++++++++++++++++++++++\n")
		escreva("+     02 - Vetor Resultante        +\n")
		escreva("++++++++++++++++++++++++++++++++++++\n\n")

		}
	funcao inicio()
	{
		cabecalho()
		para (inteiro i=0; i<8; i++){
			escreva("Digite o ",i+1,"° número:")
			leia(numeros[i])
	
			se(numeros[i] < 0){ 
				res_negativo[c1] = numeros[i]
				c1=c1+1
			}senao{ 
				se(numeros[i] > 0) {
					res_positivo[c2] = numeros[i]
				c2=c2+1
				}
			}
		}
		limpa()
		cabecalho()
		escreva("Numeros positivos: \n")
		para (inteiro i=0; i<c2; i++) {
			escreva(" [",res_positivo[i],"]\n")
		}
		
		escreva("Numeros negativos: \n")
		para(inteiro i=0; i<c1; i++){
			escreva("[",res_negativo[i] ,"]\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 815; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {c2, 3, 60, 2};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */