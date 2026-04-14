import java.util.Scanner;

public class Números {
    public static void main(String[] args) {
        Scanner teclado = new Scanner (System.in);
        int[] numeros = new int[15];
        for(int i = 0; i < numeros.length; i++) {
            System.out .println ("Digite um número:");
            numeros[i] = teclado .nextInt(); 
        }
    
    
        for(int i = 0; i < numeros.length; i++) {
            System.out.println("Número " + (numeros[i]));
        }
        teclado.close();
    }
        }

