import java.time.LocalDate;
import java.time.LocalTime;

public class Agendamento<Clientes> {

private int idAgendamento;
private LocalDate data;
private LocalTime hora;
private Clientes clientes;
private Manicure manicure;
private Servico servico;

public Agendamento(int idAgendamento, LocalDate data, LocalTime hora,
Clientes clientes, Manicure manicure, Servico servico) {
this.idAgendamento = idAgendamento;
this.data = data;
this.hora = hora;
this.clientes = clientes;
this.manicure = manicure;
this.servico = servico;
}

public Clientes getCliente() {
return clientes;
}

public Manicure getManicure() {
return manicure;
}

public Servico getServico() {
return servico;
}
}