-- MySQL Script generated by MySQL Workbench
-- 10/10/16 01:25:10
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema PortafolioInversiones
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema PortafolioInversiones
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `PortafolioInversiones` DEFAULT CHARACTER SET utf8 ;
USE `PortafolioInversiones` ;

-- -----------------------------------------------------
-- Table `PortafolioInversiones`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PortafolioInversiones`.`Usuario` (
  `Correo` VARCHAR(255) NOT NULL,
  `Nombre` VARCHAR(50) NULL,
  `Apellido Paterno` VARCHAR(50) NULL,
  `Apellido Materno` VARCHAR(50) NULL,
  `FechaNacimiento` DATE NULL,
  `Password` VARCHAR(50) NOT NULL,
  `Capital` DECIMAL(65) NOT NULL,
  PRIMARY KEY (`Correo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PortafolioInversiones`.`Giro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PortafolioInversiones`.`Giro` (
  `ID_Giro` INT(50) NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`ID_Giro`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PortafolioInversiones`.`Empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PortafolioInversiones`.`Empresa` (
  `ID_Empresa` INT(50) NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(50) NOT NULL,
  `FechaFundacion` DATE NULL,
  `ID_Giro` INT(50) NOT NULL,
  PRIMARY KEY (`ID_Empresa`),
  CONSTRAINT `fk_Empresa_Giro`
    FOREIGN KEY (`ID_Giro`)
    REFERENCES `PortafolioInversiones`.`Giro` (`ID_Giro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PortafolioInversiones`.`PreferenciaEmpresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PortafolioInversiones`.`PreferenciaEmpresa` (
  `Correo` VARCHAR(250) NOT NULL,
  `ID_Empresa` INT(50) NOT NULL,
  PRIMARY KEY (`Correo`, `ID_Empresa`),
  CONSTRAINT `fk_Usuario_Empresa`
    FOREIGN KEY (`Correo`)
    REFERENCES `PortafolioInversiones`.`Usuario` (`Correo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Empresa_Usuario`
    FOREIGN KEY (`ID_Empresa`)
    REFERENCES `PortafolioInversiones`.`Empresa` (`ID_Empresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PortafolioInversiones`.`PreferenciaGiro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PortafolioInversiones`.`PreferenciaGiro` (
  `Correo` VARCHAR(250) NOT NULL,
  `ID_Giro` INT(50) NOT NULL,
  PRIMARY KEY (`Correo`, `ID_Giro`),
  CONSTRAINT `fk_Usuario_Giro`
    FOREIGN KEY (`Correo`)
    REFERENCES `PortafolioInversiones`.`Usuario` (`Correo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Giro_Usuario`
    FOREIGN KEY (`ID_Giro`)
    REFERENCES `PortafolioInversiones`.`Giro` (`ID_Giro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PortafolioInversiones`.`Accion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PortafolioInversiones`.`Accion` (
  `Fecha` DATE NOT NULL,
  `ID_Empresa` INT(50) NOT NULL,
  `PrecioApertura` DECIMAL(65) NULL,
  `PrecioClausura` DECIMAL(65) NULL,
  `Pico` DECIMAL(65) NULL,
  `Depresión` DECIMAL(65) NULL,
  `Volumen` INT(50) NULL,
  PRIMARY KEY (`Fecha`, `ID_Empresa`),
  CONSTRAINT `fk_Accion_Empresa`
    FOREIGN KEY (`ID_Empresa`)
    REFERENCES `PortafolioInversiones`.`Empresa` (`ID_Empresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PortafolioInversiones`.`Inversion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PortafolioInversiones`.`Inversion` (
  `ID_Inversion` INT(150) NOT NULL,
  `Correo` VARCHAR(255) NOT NULL,
  `Fecha` DATE NULL,
  `ID_Empresa` INT(50) NOT NULL,
  `CapitalInvertido` DECIMAL(65) NOT NULL,
  PRIMARY KEY (`ID_Inversion`),
  CONSTRAINT `fk_Empresa_Inversion`
    FOREIGN KEY (`ID_Empresa`)
    REFERENCES `PortafolioInversiones`.`Empresa` (`ID_Empresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Inversion`
    FOREIGN KEY (`Correo`)
    REFERENCES `PortafolioInversiones`.`Usuario` (`Correo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;