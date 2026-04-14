import dao.*;
import model.*;

import java.time.LocalDateTime;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        ClienteDAO ClienteDAO = new ClienteDAO();
        ServicoDAO servicoDAO = new ServicoDAO();
        AgendamentoDAO AgendamentoDAO = new AgendamentoDAO();

        int opcao;

        do {
            System.out.println("\n=== SISTEMA MANICURE ===");
            System.out.println("1 - Cadastrar Cliente");
            System.out.println("2 - Listar Cliente");
            System.out.println("3 - Cadastrar Serviço");
            System.out.println("4 - Agendar Serviço");
            System.out.println("0 - Sair");
            opcao = sc.nextInt();
            sc.nextLine();

            switch (opcao) {

                case 1:
                    System.out.print("Nome: ");
                    String nome = sc.nextLine();
                    System.out.print("Telefone: ");
                    String tel = sc.nextLine();
                    System.out.print("Email: ");
                    String email = sc.nextLine();

                    ClienteDAO.inserir(new Cliente(nome, tel, email));
                    break;

                case 2:
                    ClienteDAO.listar()
                        .forEach(c ->
                            System.out.println(
                                c.getId() + " - " + c.getNome()));
                    break;

                case 3:
                    System.out.print("Nome do serviço: ");
                    String servNome = sc.nextLine();
                    System.out.print("Preço: ");
                    double preco = sc.nextDouble();

                    servicoDAO.inserir(
                        new Servico(servNome, preco));
                    break;

                case 4:
                    System.out.print("ID Cliente: ");
                    int clienteId = sc.nextInt();
                    System.out.print("ID Serviço: ");
                    int servicoId = sc.nextInt();

                    AgendamentoDAO.inserir(
                        new Agendamento(
                            clienteId,  
                            servicoId,
                            LocalDateTime.now()));
                    break;
            }

        } while (opcao != 0);

        sc.close();
    }
}