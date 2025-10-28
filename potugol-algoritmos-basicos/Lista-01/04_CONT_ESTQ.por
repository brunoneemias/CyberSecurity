programa
{
	inteiro  qtd_atual, qtd_max, qtd_min, qtd_med
	funcao inicio()
	{
		escreva("####################################\n")
		escreva("#     04 - Controle de estoque     #\n")
		escreva("####################################\n\n")

		escreva("Digite a quantidade atual no estoque do produto: ")
		leia(qtd_atual)
		escreva("Digite a quantidade max no estoque do produto: ")
		leia(qtd_max)
		escreva("Digite a quantidade min no estoque do produto: ")
		leia(qtd_min)

		qtd_med = (qtd_atual + qtd_max + qtd_min) / 3 

		limpa()
		escreva("A quantide média do produto é de ",qtd_med," unidades.\n")

		se (qtd_atual >= qtd_med) {
			escreva("Não efetuar a compra! \n\n")
		}senao{
			escreva("Efetue a compra! \n\n")
		}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 247; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */