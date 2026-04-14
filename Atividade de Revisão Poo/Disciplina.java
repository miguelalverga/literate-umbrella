import java.util.ArrayList;

public class Disciplina {
    private int id;
    private String nome;
    private ArrayList<Estudante> estudantes;

    public Disciplina(int id, String nome) {
        this.id = id;
        this.nome = nome;
        this.estudantes = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public void adicionarEstudante(Estudante estudante) {
        estudantes.add(estudante);
    }

    public void listarEstudantes() {
        System.out.println("Disciplina: " + nome);
        if (estudantes.isEmpty()) {
            System.out.println("Nenhum estudante cadastrado.");
        } else {
            for (Estudante e : estudantes) {
                e.exibirDados();
            }
        }
    }
}