
INSERT INTO Usuario(Correo, Nombre, ApellidoPaterno, ApellidoMaterno, FechaNacimiento, Passwrd, Capital) VALUES ("aers@gmail.com", "Ranlett", "Flint", "Charles", "1850-01-24", "IBM", 2000.5);

INSERT INTO Giro(ID_GIRO, Nombre) VALUES (NULL,"Software");
INSERT INTO Giro(ID_GIRO, Nombre) VALUES (NULL,"IT");

INSERT INTO Empresa(ID_EMPRESA, Nombre, FechaFundacion, ID_Giro) VALUES (NULL, "Microsoft", "1975-04-04", 01);
INSERT INTO Empresa(ID_EMPRESA, Nombre, FechaFundacion, ID_Giro) VALUES (NULL, "Apple", "1976-04-01", 02);
INSERT INTO Empresa(ID_EMPRESA, Nombre, FechaFundacion, ID_Giro) VALUES (NULL, "Alphabet", "2015-10-02", 02);
INSERT INTO Empresa(ID_EMPRESA, Nombre, FechaFundacion, ID_Giro) VALUES (NULL, "IBM", "1911-06-11", 02);

INSERT INTO ACCION(Fecha, ID_Empresa, PrecioApertura, PrecioClausura, Pico, Depresion, Volumen) VALUES ("2016-10-07", 02, 114.309998, 114.059998, 114.559998, 113.510002, 	24329900); 
INSERT INTO ACCION(Fecha, ID_Empresa, PrecioApertura, PrecioClausura, Pico, Depresion, Volumen) VALUES ("2016-10-06", 02, 113.699997, 113.889999, 114.339996, 113.129997, 28779300);
INSERT INTO ACCION(Fecha, ID_Empresa, PrecioApertura, PrecioClausura, Pico, Depresion, Volumen) VALUES ("2016-10-05", 02, 113.400002, 113.050003, 113.660004, 112.690002, 21453100);
INSERT INTO ACCION(Fecha, ID_Empresa, PrecioApertura, PrecioClausura, Pico, Depresion, Volumen) VALUES ("2016-10-04", 02, 113.059998, 113.00, 114.309998, 112.629997, 29736800);
INSERT INTO ACCION(Fecha, ID_Empresa, PrecioApertura, PrecioClausura, Pico, Depresion, Volumen) VALUES ("2016-10-03", 02, 112.709999, 112.519997, 	113.050003, 112.279999, 21701800);
INSERT INTO ACCION(Fecha, ID_Empresa, PrecioApertura, PrecioClausura, Pico, Depresion, Volumen) VALUES ("2016-10-02", 02, 112.459999, 113.050003, 113.370003, 111.800003, 36379100);
