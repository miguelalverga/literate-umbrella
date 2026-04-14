public class Manicure {

private int idManicure;
private String nome;
private String especialidade;

public Manicure(int idManicure, String nome, String especialidade) {
this.idManicure = idManicure;
this.nome = nome;
this.especialidade = especialidade;
}

public int getIdManicure() {
return idManicure;
}

public void setIdManicure(int idManicure) {
this.idManicure = idManicure;
}

public String getNome() {
return nome;
}

public String getEspecialidade() {
return especialidade;
}
}