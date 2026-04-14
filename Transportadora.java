public class Transportadora {
    private Encomenda[] encomendas;
    private int quantidade;

    public Transportadora() {
        this.encomendas = new Encomenda[10]; // até 10 encomendas
        this.quantidade = 0;
    }

    public void adicionarEncomenda(Encomenda encomenda) {
        if (quantidade < encomendas.length) {
            encomendas[quantidade] = encomenda;
            quantidade++;
        } else {
            System.out.println("Não é possível adicionar mais encomendas!");
        }
    }

    public void listarEncomendas() {
        if (quantidade == 0) {
            System.out.println("Nenhuma encomenda cadastrada.");
        } else {
            for (int i = 0; i < quantidade; i++) {
                encomendas[i].exibirInfo();
            }
        }
    }

    public Encomenda buscarPorCodigo(int codigo) {
        for (int i = 0; i < quantidade; i++) {
            if (encomendas[i].getCodigo() == codigo) {
                return encomendas[i];
            }
        }
        return null; // não encontrada
    }
}
