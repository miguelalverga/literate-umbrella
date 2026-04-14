public class Servico {

private int idServico;
private String nomeServico;
private double preco;

public Servico(int idServico, String nomeServico, double preco) {
this.idServico = idServico;
this.nomeServico = nomeServico;
this.preco = preco;
}

public int getIdServico() {
return idServico;
}

public String getNomeServico() {
return nomeServico;
}

public double getPreco() {
return preco;
}
}
