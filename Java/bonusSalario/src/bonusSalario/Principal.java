package bonusSalario;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		/*
		 Desenvolva uma aplicacao que receba o
		 valor do salario de um funcionario e 
		 adicione 10% de bonus.
		 Ao final exibir o Salario Base, Valor do 
		 Bonus e o Salario final (base + bonus)
		 */

		float salarioBase;
		final float bonus = 0.1f;
		float valorBonus;
		float salarioFinal;
		
		Scanner leitorDouble = new Scanner(System.in);
		
		System.out.print("Informe o salario: R$");
		salarioBase = leitorDouble.nextFloat();
		
		valorBonus   = salarioBase * bonus;
		salarioFinal = salarioBase + valorBonus;
		
		System.out.println("Salario Base: R$"   + salarioBase );
		System.out.println("Valor do Bonus: R$" + valorBonus  );
		System.out.println("Salario Final: R$"  + salarioFinal);
	}

}