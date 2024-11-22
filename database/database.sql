CREATE TABLE IF NOT EXISTS municipios
(
    id smallint PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS estabelecimentos
(
    cnpj bigint NOT NULL,
    situacaocadastral smallint,
    nomefantasia text COLLATE pg_catalog."default",
    endereco text COLLATE pg_catalog."default",
    complemento text COLLATE pg_catalog."default",
    bairro text COLLATE pg_catalog."default",
    cidade smallint,
    cep integer,
    uf character varying(2) COLLATE pg_catalog."default",
    email text COLLATE pg_catalog."default",
    CONSTRAINT estabelecimentos_pkey PRIMARY KEY (cnpj),
    CONSTRAINT fk_cidade FOREIGN KEY (cidade)
        REFERENCES public.municipios (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

DROP TABLE zapEnviados;
DROP TABLE emailEnviados;
DROP TABLE devedores;
DROP TABLE titulos;
DROP TABLE cartorios;
DROP TABLE contatos;
CREATE TABLE cartorios (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    webSite VARCHAR(100)
);

CREATE TABLE titulos (
    id SERIAL PRIMARY KEY,
    cartorio_id INT,
    protocolo VARCHAR(255) NOT NULL,
    credor VARCHAR(255) NOT NULL,
    valorprotestado NUMERIC(10, 2) NOT NULL,
    numerotitulo VARCHAR(255) NOT NULL,
    dataprotesto DATE NOT NULL,
    mesano INT NOT NULL CHECK (mesAno >= 202001 AND mesAno <= 210001),
    valorboleto NUMERIC(10, 2) NOT NULL,
    datainsert TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (cartorio_id) REFERENCES cartorios(id)
);
insert into cartorios values (1,'1o Ofício de Notas e Protesto','https://1cartoriodefortaleza.com.br/');
insert into cartorios values (5,'Cartório Ossian Araripe','https://www.cartorioossianararipe.com.br/');
insert into cartorios values (8,'Cartório Aguiar','https://www.cartorioaguiar.com.br/');
CREATE TABLE devedores (
    titulo_id INT, 
    documento NUMERIC(14,0) NOT NULL,
	nome VARCHAR(255) NOT NULL,
    FOREIGN KEY (titulo_id) REFERENCES titulos(id)
);


CREATE TABLE emailEnviados (
    messageId VARCHAR(100)NULL,
    titulo_id INT, 
    accepted VARCHAR(255) NULL,
    rejected VARCHAR(255) NULL,
    response VARCHAR(255) NULL,
    error VARCHAR(255) NULL,
    dataInsert TIMESTAMP without time zone default now(),
    FOREIGN KEY (titulo_id) REFERENCES titulos(id)
);

CREATE TABLE contatos (
    documento NUMERIC(14,0) NOT NULL,
    telefone VARCHAR(13) NULL,
    email VARCHAR(100)NULL,
    PRIMARY KEY (documento, telefone)
);


CREATE TABLE zapenviado (
    messageId VARCHAR(100) NULL,
    titulo_id INT, 
    whatsapp VARCHAR(13) NULL,
    wa_id VARCHAR(13) NULL,
    message_status VARCHAR(50) NULL,
    accepted VARCHAR(255) NULL,
    rejected VARCHAR(255) NULL,
    response VARCHAR(255) NULL,
    error VARCHAR(255) NULL,
    dataInsert TIMESTAMP without time zone default now(),
    FOREIGN KEY (titulo_id) REFERENCES titulos(id)
);
