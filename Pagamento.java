public class Pagamento {

private int idPagamento;
private String formaPagamento;
private double valor;
private String status;
private Agendamento agendamento;

public Pagamento(int idPagamento, String formaPagamento,
double valor, String status, Agendamento agendamento) {
this.idPagamento = idPagamento;
this.formaPagamento = formaPagamento;
this.valor = valor;
this.status = status;
this.agendamento = agendamento;
}

public String getFormaPagamento() {
return formaPagamento;
}

public double getValor() {
return valor;
}

public String getStatus() {
return status;
}

public Agendamento getAgendamento() {
return agendamento;
}
}
