programa
{
	cadeia nome[100], cond ="Sim"
	inteiro idade[100], c = 0, menor, maior
	funcao inicio()
	{
	enquanto (cond == "Sim") {
		limpa()
		escreva("####################################\n")
		escreva("#       08 - JOVEM e VELHO         #\n")
		escreva("####################################\n\n")

		escreva("Digite o nome: ")
		leia(nome[c])
		escreva("Digte a idade: ")
		leia(idade[c]) 

		se ( c > 0 ) { 
			se (idade[c] >= idade[c-1]) { 
				maior = c
			}senao{
				se (idade[c] <= idade[c-1]) { 
					menor = c
				}
			}
		}senao{
			maior = c 
			menor = c
		}

		c = c + 1
		escreva("\nDeseja inserir mais dados [Sim/Não]? ") 
		leia(cond)
			
					}
	    limpa()
	    escreva("####################################\n")
	    escreva("#       08 - JOVEM e VELHO         #\n")
	    escreva("####################################\n\n")
	    escreva("A pessoa mais velha é ",nome[maior]," com ",idade[maior]," anos!\n\n")
	    escreva("A pessoa mais nova é ",nome[menor]," com ",idade[menor]," anos!\n\n")
	    escreva("Quantidade de pessoas lidas: ",c)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1059; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */