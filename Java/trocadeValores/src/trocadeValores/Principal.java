package trocadeValores;

import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        /*
         Desenvolva uma aplicacao que solicite dois
         valores numericos inteiros e armazene nas
         variaveis [A] e [B].
         Apos receber os valores efetue a troca deles
         apresentando ao final o novo valor de [A] e [B].
         */
        
        int a;
        int b;
        //int aux;
        
        Scanner leitorInt = new Scanner(System.in);
        
        System.out.print("Informe o primeiro valor: [A]");
        a = leitorInt.nextInt(); // 4
        
        System.out.print("Informe o segundo valor: [B]");
        b = leitorInt.nextInt(); // 3
        
        //Processamento
        
        //aux = a;
        //a   = b;
        //b   = aux;
        
        a = a + b; // a = 4 + 3 --> 7
        b = a - b; // b = 7 - 3 --> 4
        a = a - b; // a = 7 - 4 --> 3
        
        System.out.println("Novo valor de A: " + a);
        System.out.println("Novo valor de B: " + b);
    }

}