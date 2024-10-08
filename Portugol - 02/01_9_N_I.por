programa
{
	inteiro numeros[9], divisor=0,c=0

	funcao cabecalho(){
		escreva("++++++++++++++++++++++++++++++++++++\n")
		escreva("+     01 - 9 Números Inteiros     +\n")
		escreva("++++++++++++++++++++++++++++++++++++\n\n")

		}
	
	funcao inicio()
	{
		cabecalho()
		para (inteiro a=0; a<9; a++) {
			escreva("Digite um número: ")
			leia(numeros[a]) 
		}
		limpa()
		cabecalho()
		escreva("Os números primos digitados foram:\n")
		para (inteiro a=0; a<9; a++) {
			para (inteiro i=1; i<=numeros[a]; i++){
				se (numeros[a] % i == 0) {
					divisor++  
				}
			}
			se (divisor == 2) { 
				escreva(numeros[a]," na posição [",a+1,"] do vetor\n")
			}senao{
				c++
			}
			divisor = 0
		}
		se (c == 9) {
			limpa()
			cabecalho()
			escreva("Nenhum número digitado é Primo!")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 738; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */