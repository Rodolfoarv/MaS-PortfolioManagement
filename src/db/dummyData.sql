use PortafolioInversiones;
INSERT INTO Usuario(Correo, Nombre, ApellidoPaterno, ApellidoMaterno, FechaNacimiento, Passwrd, Capital) VALUES ("aers@gmail.com", "Ranlett", "Flint", "Charles", "1850-01-24", "IBM", 2000.5);
INSERT INTO Usuario(Correo, Nombre, ApellidoPaterno, ApellidoMaterno, FechaNacimiento, Passwrd, Capital) VALUES ("bc@gmail.com", "Benedict", "Cumberbatch", "Carlton", "1976-07-19", "Dr.Strange", 4000.5);

INSERT INTO Giro(ID_GIRO, Nombre) VALUES (NULL,"Software");
INSERT INTO Giro(ID_GIRO, Nombre) VALUES (NULL,"IT");

INSERT INTO Empresa(ID_EMPRESA, Nombre, FechaFundacion, ID_Giro) VALUES (01, "Microsoft", "1975-04-04", 01);
INSERT INTO Empresa(ID_EMPRESA, Nombre, FechaFundacion, ID_Giro) VALUES (02, "Apple", "1976-04-01", 02);
INSERT INTO Empresa(ID_EMPRESA, Nombre, FechaFundacion, ID_Giro) VALUES (03, "Alphabet", "2015-10-02", 02);
INSERT INTO Empresa(ID_EMPRESA, Nombre, FechaFundacion, ID_Giro) VALUES (04, "IBM", "1911-06-11", 02);

INSERT INTO Accion(Fecha, ID_Empresa, PrecioApertura, PrecioClausura,ValorActual, Volumen, Volatilidad) VALUES ("2016-10-10", 02, 114.309998, 114.059998, 114.559998, 	24329900, 11);
INSERT INTO Accion(Fecha, ID_Empresa, PrecioApertura, PrecioClausura,ValorActual, Volumen, Volatilidad) VALUES ("2016-10-10", 01, 113.699997, 113.889999, 114.339996, 28779300, 20);
INSERT INTO Accion(Fecha, ID_Empresa, PrecioApertura, PrecioClausura,ValorActual, Volumen, Volatilidad) VALUES ("2016-10-10", 03, 113.400002, 113.050003, 113.660004, 21453100, 30);
INSERT INTO Accion(Fecha, ID_Empresa, PrecioApertura, PrecioClausura,ValorActual, Volumen, Volatilidad) VALUES ("2016-10-09", 02, 113.059998, 113.00, 114.309998, 29736800, 25);
INSERT INTO Accion(Fecha, ID_Empresa, PrecioApertura, PrecioClausura,ValorActual, Volumen, Volatilidad) VALUES ("2016-10-09", 01, 112.709999, 112.519997, 	113.050003, 21701800, 35);
INSERT INTO Accion(Fecha, ID_Empresa, PrecioApertura, PrecioClausura,ValorActual, Volumen, Volatilidad) VALUES ("2016-10-09", 03, 112.459999, 113.050003, 113.370003, 36379100, 40);
INSERT INTO Accion(Fecha, ID_Empresa, PrecioApertura, PrecioClausura,ValorActual, Volumen, Volatilidad) VALUES ("2016-11-27", 01, 112.709999, 112.519997, 	113.050003, 21701800, 10);
INSERT INTO Accion(Fecha, ID_Empresa, PrecioApertura, PrecioClausura,ValorActual, Volumen, Volatilidad) VALUES ("2016-11-27", 03, 112.459999, 113.050003, 113.370003, 36379100, 20);
INSERT INTO Accion(Fecha, ID_Empresa, PrecioApertura, PrecioClausura,ValorActual, Volumen, Volatilidad) VALUES ("2016-11-27", 02, 114.309998, 114.059998, 114.559998, 	24329900, 25);

INSERT INTO PreferenciaEmpresa(Correo, ID_Empresa) VALUES ("aers@gmail.com", 01);
INSERT INTO PreferenciaEmpresa(Correo, ID_Empresa) VALUES ("aers@gmail.com", 02);
INSERT INTO PreferenciaEmpresa(Correo, ID_Empresa) VALUES ("bc@gmail.com", 03);

INSERT INTO PreferenciaGiro(Correo, ID_Giro) VALUES ("bc@gmail.com", 01);
INSERT INTO PreferenciaGiro(Correo, ID_Giro) VALUES ("aers@gmail.com", 02);

INSERT INTO Inversion(ID_Inversion, Correo, Fecha, ID_Empresa, CapitalInvertido, ToleranciaRiesgo, EstrategiaInversion) VALUES (01, "aers@gmail.com", "2016-10-27", 02, 3000, 15, 2);
INSERT INTO Inversion(ID_Inversion, Correo, Fecha, ID_Empresa, CapitalInvertido, ToleranciaRiesgo, EstrategiaInversion) VALUES (02, "aers@gmail.com", "2016-10-27", 03, 2000, 10, 1);
INSERT INTO Inversion(ID_Inversion, Correo, Fecha, ID_Empresa, CapitalInvertido, ToleranciaRiesgo, EstrategiaInversion) VALUES (03, "aers@gmail.com", "2016-10-27", 01, 1500, 20, 3);
INSERT INTO Inversion(ID_Inversion, Correo, Fecha, ID_Empresa, CapitalInvertido, ToleranciaRiesgo, EstrategiaInversion) VALUES (04, "bc@gmail.com", "2016-10-27", 01, 2500, 15, 4);
INSERT INTO Inversion(ID_Inversion, Correo, Fecha, ID_Empresa, CapitalInvertido, ToleranciaRiesgo, EstrategiaInversion) VALUES (05, "bc@gmail.com", "2016-10-27", 02, 800, 8, 2);
INSERT INTO Inversion(ID_Inversion, Correo, Fecha, ID_Empresa, CapitalInvertido, ToleranciaRiesgo, EstrategiaInversion) VALUES (06, "bc@gmail.com", "2016-10-27", 04, 1000, 10, 1);