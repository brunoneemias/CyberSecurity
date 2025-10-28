programa
{
	inteiro numero 	
	funcao inicio()
	{
		escreva("***********************************\n")
		escreva("    02 - DIVISIVEL POR 2 E 3       \n")
		escreva("***********************************\n\n")

		escreva("Digite um número: ")
		leia(numero)
		limpa()
		
		 se ((numero % 2 == 0) e (numero % 3 == 0)) {
		 	escreva("O número ",numero," é divisivel por 2 e 3.\n\n")
		 }senao{ 
		 	 se (numero % 2 == 0) {
		 	 	escreva("O número ",numero," é divisivel por 2. \n\n")
		 	 }senao{ 
		 	 	 se (numero % 3 == 0) {
		 	 	escreva("O número ",numero," é divisivel por 3. \n\n")
		 	 }senao{ 
		 	 	escreva("O número ",numero," não é divisivel por 2 e 3. \n\n")
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
 * @POSICAO-CURSOR = 678; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */