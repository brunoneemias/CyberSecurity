programa
{
	inclua biblioteca Tipos --> t
	real numeros[50], soma=0.0, maior, menor
	inteiro c=0, impar =0
	funcao inicio()
	{
		escreva("####################################\n")
		escreva("#       10 - 50 Números            #\n")
		escreva("####################################\n\n")

		para (inteiro i=0; i<50; i++) {
			escreva("Insira o ",i+1,"° numero: ")
			leia(numeros[i])
			soma = soma + numeros[i] 
		
			se ( c > 0 ) { 
				se (numeros[i] >= numeros[i-1]) { 
					maior = numeros[i]
				}senao{
					se (numeros[i] <= numeros[i-1]) { 
						menor = numeros[i]
						}
					}
			}senao{
			maior = numeros[i] 
			menor = numeros[i]
			}
			
			se ((t.real_para_inteiro(numeros[i]) % 2 != 0)) { 
				impar = impar + 1
			}
		c = c+1 
			}
			limpa()
		escreva("####################################\n")
		escreva("#       10 - 50 Números            #\n")
		escreva("####################################\n\n")	
		escreva("\n\nSoma dos números: ",soma)
		escreva("\nMédia dos números: ",soma/c)
		escreva("\nO menor número: ",menor)
		escreva("\nO maior número: ",maior)
		
		escreva("\n\nDobro: \n")
	para (inteiro a=0; a<50; a++) {
		escreva(numeros[a], " -> ",numeros[a]*2,"\n")
		}
		
		escreva("\n\nCubo: \n")
	para (inteiro b=0; b<50; b++) { 
		escreva(numeros[b], " -> ",numeros[b]*numeros[b]*numeros[b],"\n")
		}
		
		escreva("\n\nA porcentagem de números ímpares foi de: ",(impar*100)/c,"%\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 316; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */