package comandosEntrada;

import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        /*
         Tipos de Dados Primitivos:
         int             --> Valores numericos inteiros
         float ou double --> Valores Numericos Fracionados
         String          --> Cadeia de Caracteres (texto)
         boolean         --> Dados Logicos (true/false)
         
         Sintaxe de declaracao de variavel:
         tipoDeDado nomeDaVariavel;
         */
        String nomeUsuario;
        int idade;
        
        Scanner leitor = new Scanner(System.in);
        Scanner leitorNumeros = new Scanner(System.in);
        
        System.out.print("Informe seu nome: ");
        // A variavel nomeUsuario RECEBE os dados lidos pelo Scanner
        nomeUsuario = leitor.nextLine(); //nextLine() para receber texto
        
        System.out.print("Informe sua idade: ");
        idade = leitorNumeros.nextInt();
        
        System.out.println("Ola " + nomeUsuario);
        System.out.println("Idade informada: " + idade);
    }

}