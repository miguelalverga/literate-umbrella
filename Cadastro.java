import java.util.Scanner;

public class Cadastro {

    private Scanner sc = new Scanner(System.in);

    public clientes cadastrarClientes() {

        System.out.println("=== Cadastro de Cliente ===");

        System.out.print("ID: ");
        int id = sc.nextInt();
        sc.nextLine(); // limpar buffer

        System.out.print("Nome: ");
        String nome = sc.nextLine();

        System.out.print("Telefone: ");
        String telefone = sc.nextLine();

        System.out.print("Email: ");
        String email = sc.nextLine();

        clientes clientes = new clientes(id, nome, telefone, email);

        System.out.println("Cliente cadastrado com sucesso!");

        return clientes;
    }
}