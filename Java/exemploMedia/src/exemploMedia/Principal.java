package exemploMedia;

import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        /*
         Desenvolva uma aplicacao que solicite o nome
          do usuario e tres notas (0 a 10) retornando
          ao final o resultado da media simples.
        */

        String nome;
        float n1, n2, n3, media;
        
        Scanner leitorTexto = new Scanner(System.in);
        Scanner leitorNumero = new Scanner(System.in);
        
        System.out.print("Informe o nome do aluno: ");
        nome = leitorTexto.nextLine();
        
        System.out.print("Informe a primeira nota: ");
        n1 = leitorNumero.nextFloat();
        
        System.out.print("Informe a segunda nota: ");
        n2 = leitorNumero.nextFloat();
        
        System.out.print("Informe a terceira nota: ");
        n3 = leitorNumero.nextFloat();
        
        media = (n1 + n2 + n3) / 3;
        
        System.out.println(nome + " sua media foi: " + media);
    }
}