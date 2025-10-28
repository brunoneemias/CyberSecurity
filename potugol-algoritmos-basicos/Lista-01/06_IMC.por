programa
{
	real altura, peso, imc 	
	funcao inicio()
	{
		escreva("####################################\n")
		escreva("#            06 - IMC              #\n")
		escreva("####################################\n\n")

		escreva("Informe a altura(m): ")
		leia(altura) 
		escreva("informe o peso(kg): ")
		leia(peso)

		imc = peso / (altura*altura)

		se (imc < 18.5) {
			escreva("MAGRO!")
		}senao{
			se((imc >= 18.5) e (imc <25)){
				escreva("NORMAL!")	
			}senao{
				se ((imc >= 25) e (imc <30)){ 
					escreva("OBESO!")
				}senao{ 
					se (imc >= 30){
						escreva("OBESO MORBIDO!")
					}
				}
			}
		}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 402; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */