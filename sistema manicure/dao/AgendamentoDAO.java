package dao;

import model.Agendamento;
import java.sql.*;

public class AgendamentoDAO {

    public void inserir(Agendamento a) {

        String sql =
        "INSERT INTO Agendamento (id_Agendamento, id_cliente, id_servico, id_manicure, data_hora,  status) VALUES (?, ?, ?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, a.getClienteId());
            stmt.setInt(2, a.getServicoId());
            stmt.setTimestamp(3,
                Timestamp.valueOf(a.getData()));

            stmt.executeUpdate();

            System.out.println("Agendamento realizado!");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}