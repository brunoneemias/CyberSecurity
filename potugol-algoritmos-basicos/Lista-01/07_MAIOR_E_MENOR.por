programa
{
	real n1,n2,n3,n4,maior,menor
	funcao inicio()
	{
		escreva("####################################\n")
		escreva("#       07 - MAIOR E MENOR         #\n")
		escreva("####################################\n\n")

		escreva("Digite o número 1: ")
		leia(n1)
		escreva("Digite o número 2: ")
		leia(n2)
		escreva("Digite o número 3: ")
		leia(n3)
		escreva("Digite o número 4: ")
		leia(n4)
		limpa()
		se ((n1 == n2) e (n2 == n3) e (n3 == n4)){ 
			escreva("Os números informados são iguais!")
		}senao{ 
			se ((n1 > n2) e (n1 > n3) e (n1 > n4)) {
				maior = n1
			}senao{ 
				se ((n2 > n1) e (n2 > n3) e (n2 > n4)) {
					maior = n2
				}senao{ 
					se ((n3 > n1) e (n3 > n2) e (n3 > n4)) {
						maior = n3
					}senao{
						maior = n4
						}
					}
				}
			se ((n1 < n2) e (n1 < n3) e (n1 < n4)) {
				menor= n1
			}senao{ 
				se ((n2 < n1) e (n2 < n3) e (n2 < n4)) {
					menor = n2
				}senao{ 
					se ((n3 < n1) e (n3 < n2) e (n3 < n4)) {
						menor = n3
					}senao{
						menor = n4
						 }
					}
				}
		escreva("O maior numero foi: ",maior,"\n\nO menor número foi: ",menor,"\n")
		
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1125; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */