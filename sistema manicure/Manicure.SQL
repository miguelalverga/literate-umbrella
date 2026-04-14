CREATE DATABASE manicure_db;

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE servicos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2)
);

CREATE TABLE agendamentos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    servico_id INT REFERENCES servicos(id),
    data_agendamento TIMESTAMP
);