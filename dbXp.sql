CREATE TABLE `hist_diario` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`Date` TIMESTAMP(6) NOT NULL,
	`Open` FLOAT(10) NOT NULL,
	`High` FLOAT(10) NOT NULL,
	`Low` FLOAT(10) NOT NULL,
	`Close` FLOAT(10) NOT NULL,
	`Volume` INT(20) NOT NULL,
	`Dividends` FLOAT(10) NOT NULL,
	`Stock_Splits` FLOAT(10) NOT NULL,
	`Daily_Change` FLOAT(10) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `hist_semanal` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`Date` TIMESTAMP(6) NOT NULL,
	`Open` FLOAT(10) NOT NULL,
	`High` FLOAT(10) NOT NULL,
	`Low` FLOAT(10) NOT NULL,
	`Close` FLOAT(10) NOT NULL,
	`Volume` INT(20) NOT NULL,
	`Dividends` FLOAT(10) NOT NULL,
	`Stock_Splits` FLOAT(10) NOT NULL,
	`Weekly_Change` FLOAT(10) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `hist_mensal` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`Date` TIMESTAMP(6) NOT NULL,
	`Open` FLOAT(10) NOT NULL,
	`High` FLOAT(10) NOT NULL,
	`Low` FLOAT(10) NOT NULL,
	`Close` FLOAT(10) NOT NULL,
	`Volume` INT(20) NOT NULL,
	`Dividends` FLOAT(10) NOT NULL,
	`Stock_Splits` FLOAT(10) NOT NULL,
	`Monthly_Change` FLOAT(10) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `hist_anual` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`Date` TIMESTAMP(6) NOT NULL,
	`Open` FLOAT(10) NOT NULL,
	`High` FLOAT(10) NOT NULL,
	`Low` FLOAT(10) NOT NULL,
	`Close` FLOAT(10) NOT NULL,
	`Volume` INT(20) NOT NULL,
	`Dividends` FLOAT(10) NOT NULL,
	`Stock_Splits` FLOAT(10) NOT NULL,
	`Annual_Change` FLOAT(10) NOT NULL,
	PRIMARY KEY (`ID`)
);


create database dbXp;
use dbXp;
select * from daily_analysis;