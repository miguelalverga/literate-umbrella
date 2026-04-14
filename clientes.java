public class clientes {

private int idCliente;
private String nome;
private String telefone;
private String email;

public clientes(int i, String string, String string2, String string3) {
    //TODO Auto-generated constructor stub
}

public void Clientes(int idClientes, String nome, String telefone, String email) {
this.idCliente = idClientes;
this.nome = nome;
this.telefone = telefone;
this.email = email;
}

public int getIdCliente() {
return idCliente;
}

public void setIdCliente(int idCliente) {
this.idCliente = idCliente;
}

public String getNome() {
return nome;
}

public void setNome(String nome) {
this.nome = nome;
}

public String getTelefone() {
return telefone;
}

public void setTelefone(String telefone) {
this.telefone = telefone;
}

public String getEmail() {
return email;
}

public void setEmail(String email) {
this.email = email;
}
}