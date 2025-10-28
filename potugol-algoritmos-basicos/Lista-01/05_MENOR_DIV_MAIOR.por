programa
{
	inteiro  num1, num2
	funcao inicio()
	{
		escreva("####################################\n")
		escreva("#     05 - Menor divide Maior      #\n")
		escreva("####################################\n\n")

		escreva("Digite o primeiro número: ")
		leia(num1)
		
		escreva("Digite o segundo número: ")
		leia(num2)

		se ((num1 != 0) e (num2 != 0)){ 
			se (num1 > num2){		 
				se (num1 % num2 == 0){ 
					escreva("O numero ",num1, " é divisivel por ", num2," !\n\n") 
				}senao{
					escreva("O numero ",num1, " não é divisivel por ", num2," !\n\n")  
					 }		
			}senao{
				se (num2 % num1 == 0){ 
					escreva("O numero ",num2, " é divisivel por ", num1," !\n\n") 
				}senao{
					escreva("O numero ",num2, " não é divisivel por ", num1," !\n\n")  
				 }
			}
		}senao{ 
			escreva("Erro! Não é possivel realizar divisão por 0.\n\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 856; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */