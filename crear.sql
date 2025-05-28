CREATE TABLE Actor ( 
  idActor NUMBER NOT NULL,
  Nombre VARCHAR2(100),
  Apellido VARCHAR2(100),
  Edad NUMBER,
  PRIMARY KEY(idActor)
);

CREATE TABLE Director (
  idDirector NUMBER NOT NULL,
  Nombre VARCHAR2(100),
  Apellido VARCHAR2(100),
  PRIMARY KEY(idDirector)
);

CREATE TABLE Funcion (
  idFuncion NUMBER NOT NULL,
  idPelicula NUMBER NOT NULL,
  idSala NUMBER NOT NULL,
  Horario DATE, 
  Fecha DATE,
  PRIMARY KEY(idFuncion)
);

CREATE TABLE Cliente (
  idCliente NUMBER NOT NULL,
  idGenero_2 NUMBER NOT NULL,
  idMembresia NUMBER NOT NULL,
  nombre VARCHAR2(100),
  paterno VARCHAR2(100),
  materno VARCHAR2(100),
  edad NUMBER,
  telefono VARCHAR2(20),
  correo VARCHAR2(100),
  PRIMARY KEY(idCliente)
);

CREATE TABLE Funcion_has_Cliente (
  idCliente NUMBER NOT NULL,
  idFuncion NUMBER NOT NULL,
  PRIMARY KEY(idCliente, idFuncion)
);

CREATE TABLE Genero (
  idGenero NUMBER NOT NULL,
  Descripcion VARCHAR2(100),
  PRIMARY KEY(idGenero)
);

CREATE TABLE Genero_2 (
  idGenero_2 NUMBER NOT NULL,
  Descripcion VARCHAR2(100),
  PRIMARY KEY(idGenero_2)
);

CREATE TABLE membresia (
  idMembresia NUMBER NOT NULL,
  Tipo VARCHAR2(100),
  PRIMARY KEY(idMembresia)
);

CREATE TABLE Pelicula (
  idPelicula NUMBER NOT NULL,
  idGenero NUMBER NOT NULL,
  idActor NUMBER NOT NULL,
  idDirector NUMBER NOT NULL,
  nombre VARCHAR2(100),
  clasificacion VARCHAR2(10),
  Duracion NUMBER,
  PRIMARY KEY(idPelicula)
);

CREATE TABLE Sala (
  idSala NUMBER NOT NULL,
  Butaca NUMBER,
  PRIMARY KEY(idSala)
);