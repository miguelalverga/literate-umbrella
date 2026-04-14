public class Encomenda {
    private int codigo;
    private String destinatario;
    private String endereco;
    private String status;

    // Construtor
    public Encomenda(int codigo, String destinatario, String endereco, String status) {
        this.codigo = codigo;
        this.destinatario = destinatario;
        this.endereco = endereco;
        this.status = status;
    }

    // Métodos
    public void exibirInfo() {
        System.out.println("Código: " + codigo);
        System.out.println("Destinatário: " + destinatario);
        System.out.println("Endereço: " + endereco);
        System.out.println("Status: " + status);
        System.out.println("-----------------------------");
    }

    public void atualizarStatus(String novoStatus) {
        this.status = novoStatus;
    }

    public int getCodigo() {
        return codigo;
    }
}
