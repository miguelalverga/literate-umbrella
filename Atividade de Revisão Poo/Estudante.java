public class Estudante {
    private int id;
    private String nome;
    private int idade;

    public Estudante(int id, String nome, int idade) {
        this.id = id;
        this.nome = nome;
        this.idade = idade;
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public void exibirDados() {
        System.out.println("ID: " + id + " | Nome: " + nome + " | Idade: " + idade);
    }
}