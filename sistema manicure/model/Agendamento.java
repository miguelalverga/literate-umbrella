package model;

import java.time.LocalDateTime;

public class Agendamento {

    private int ClienteId;
    private int servicoId;
    private LocalDateTime data;

    public Agendamento(int clienteId, int servicoId, LocalDateTime data) {
        this.ClienteId = clienteId;
        this.servicoId = servicoId;
        this.data = data;
    }

    public int getClienteId() { return ClienteId; }
    public int getServicoId() { return servicoId; }
    public LocalDateTime getData() { return data; }
}