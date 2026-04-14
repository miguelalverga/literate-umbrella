package dao;

import model.Cliente;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ClienteDAO {

    public void inserir(Cliente c) {

        String sql =
        "INSERT INTO Cliente (nome, telefone, email) VALUES (?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, c.getNome());
            stmt.setString(2, c.getTelefone());
            stmt.setString(3, c.getEmail());
            stmt.executeUpdate();

            System.out.println("Cliente cadastrado!");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Cliente> listar() {

        List<Cliente> lista = new ArrayList<>();
        String sql = "SELECT * FROM Cliente";

        try (Connection conn = Conexao.conectar();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                lista.add(new Cliente(
                        rs.getInt("id"),
                        rs.getString("nome"),
                        rs.getString("telefone"),
                        rs.getString("email")));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }

        return lista;
    }

    public void deletar(int id) {

        String sql = "DELETE FROM Cliente WHERE id = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            stmt.executeUpdate();

            System.out.println("Cliente removido!");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}