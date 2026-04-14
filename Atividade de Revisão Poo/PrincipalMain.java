import java.util.ArrayList;
import java.util.Scanner;

public class PrincipalMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Disciplina> disciplinas = new ArrayList<>();
        ArrayList<Estudante> estudantes = new ArrayList<>();

        int opcao;

        do {
            System.out.println("\n===== MENU_ESCOLA =====");
            System.out.println("1 - Cadastrar Disciplina");
            System.out.println("2 - Cadastrar Estudante");
            System.out.println("3 - Inserir Aluno na disciplina");
            System.out.println("4 - Listar ALunos e disciplinas");
            System.out.println("5 - Encerrar programa");
            System.out.print("Escolha: ");
            opcao = sc.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("ID da disciplina: ");
                    int idDisc = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Nome da disciplina: ");
                    String nomeDisc = sc.nextLine();

                    disciplinas.add(new Disciplina(idDisc, nomeDisc));
                    System.out.println("Disciplina cadastrada com sucesso!");
                    break;

                case 2:
                    System.out.print("ID do estudante: ");
                    int idEst = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Nome do estudante: ");
                    String nomeEst = sc.nextLine();

                    System.out.print("Idade: ");
                    int idade = sc.nextInt();

                    estudantes.add(new Estudante(idEst, nomeEst, idade));
                    System.out.println("Estudante cadastrado com sucesso!");
                    break;

                case 3:
                    System.out.print("Digite o ID do estudante: ");
                    int idAluno = sc.nextInt();

                    System.out.print("Digite o ID da disciplina: ");
                    int idMateria = sc.nextInt();

                    Estudante estudanteEncontrado = null;
                    Disciplina disciplinaEncontrada = null;

                    for (Estudante e : estudantes) {
                        if (e.getId() == idAluno) {
                            estudanteEncontrado = e;
                            break;
                        }
                    }

                    for (Disciplina d : disciplinas) {
                        if (d.getId() == idMateria) {
                            disciplinaEncontrada = d;
                            break;
                        }
                    }

                    if (estudanteEncontrado != null && disciplinaEncontrada != null) {
                        disciplinaEncontrada.adicionarEstudante(estudanteEncontrado);
                        System.out.println("Estudante inserido na disciplina!");
                    } else {
                        System.out.println("Estudante ou disciplina não encontrado.");
                    }
                    break;

                case 4:
                    System.out.println("\n=== DISCIPLINAS ===");
                    for (Disciplina d : disciplinas) {
                        d.listarEstudantes();
                        System.out.println();
                    }

                    System.out.println("=== ESTUDANTES CADASTRADOS ===");
                    for (Estudante e : estudantes) {
                        e.exibirDados();
                    }
                    break;

                case 5:
                    System.out.println("Programa encerrado.");
                    break;

                default:
                    System.out.println("Opção inválida.");
            }

        } while (opcao != 5);

        sc.close();
    }
}