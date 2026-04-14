package dao;

import model.Servico;
import java.sql.*;

public class ServicoDAO {

    public void inserir(Servico s) {

        String sql =
        "INSERT INTO servicos (nome, preco) VALUES (?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, s.getNome());
            stmt.setDouble(2, s.getPreco());
            stmt.executeUpdate();

            System.out.println("Serviço cadastrado!");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}