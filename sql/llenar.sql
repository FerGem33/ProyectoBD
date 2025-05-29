-- Generos
INSERT INTO Genero (descripcion) VALUES ('Accion');
INSERT INTO Genero (descripcion) VALUES ('Comedia');
INSERT INTO Genero (descripcion) VALUES ('Drama');
INSERT INTO Genero (descripcion) VALUES ('Ciencia Ficcion');
INSERT INTO Genero (descripcion) VALUES ('Misterio');
INSERT INTO Genero (descripcion) VALUES ('Terror');
INSERT INTO Genero (descripcion) VALUES ('Fantasia');
INSERT INTO Genero (descripcion) VALUES ('Documental');

-- Actores
INSERT INTO Actor (nombre) VALUES ('Tom Hanks');
INSERT INTO Actor (nombre) VALUES ('Natalie Portman');
INSERT INTO Actor (nombre) VALUES ('Emma Stone');
INSERT INTO Actor (nombre) VALUES ('Robert Downey Jr.');
INSERT INTO Actor (nombre) VALUES ('Jennifer Lawrence');
INSERT INTO Actor (nombre) VALUES ('Brad Pitt');
INSERT INTO Actor (nombre) VALUES ('Morgan Freeman');
INSERT INTO Actor (nombre) VALUES ('Johnny Depp');
INSERT INTO Actor (nombre) VALUES ('Anne Hathaway');
INSERT INTO Actor (nombre) VALUES ('Hugh Jackman');
INSERT INTO Actor (nombre) VALUES ('Gal Gadot');
INSERT INTO Actor (nombre) VALUES ('Zendaya');
INSERT INTO Actor (nombre) VALUES ('Keanu Reeves');
INSERT INTO Actor (nombre) VALUES ('Chris Hemsworth');

-- Directores
INSERT INTO Director (nombre) VALUES ('Steven Spielberg');
INSERT INTO Director (nombre) VALUES ('Christopher Nolan');
INSERT INTO Director (nombre) VALUES ('Quentin Tarantino');
INSERT INTO Director (nombre) VALUES ('Greta Gerwig');
INSERT INTO Director (nombre) VALUES ('Guillermo del Toro');

-- Generos_2
INSERT INTO Genero_2 (descripcion) VALUES ('Masculino');
INSERT INTO Genero_2 (descripcion) VALUES ('Femenino');
INSERT INTO Genero_2 (descripcion) VALUES ('Otro');

-- Sala
INSERT INTO Sala (Butaca) VALUES (50);
INSERT INTO Sala (Butaca) VALUES (75);
INSERT INTO Sala (Butaca) VALUES (100);

-- Pelicula
-- Inception (Origen)
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (5, 4, 2, 'Inception', 'B', 148);

-- La La Land
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (3, 3, 4, 'La La Land', 'B', 128);

-- Avengers: Endgame
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (1, 14, 2, 'Avengers: Endgame', 'B', 181);

-- Titanic
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (3, 6, 1, 'Titanic', 'B', 195);

-- Harry Potter y la piedra filosofal
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (7, 5, 5, 'Harry Potter y la piedra filosofal', 'A', 152);

-- El señor de los anillos: La comunidad del anillo
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (7, 7, 5, 'El señor de los anillos: La comunidad del anillo', 'B', 178);

-- Joker
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (3, 15, 2, 'Joker', 'C', 122);

-- Matrix
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (4, 13, 2, 'The Matrix', 'B', 136);

-- Wonder Woman
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (1, 11, 4, 'Wonder Woman', 'B', 141);

-- Interstellar
INSERT INTO Pelicula (idGenero, idActor, idDirector, nombre, clasificacion, Duracion)
VALUES (4, 10, 2, 'Interstellar', 'B', 169);