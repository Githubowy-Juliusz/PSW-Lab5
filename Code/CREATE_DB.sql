DROP SCHEMA IF EXISTS `pswdb`;
CREATE SCHEMA IF NOT EXISTS `pswdb` DEFAULT CHARACTER SET utf8;
USE `pswdb`;
DROP TABLE IF EXISTS `pswdb`.`user`;

CREATE TABLE IF NOT EXISTS `pswdb`.`user`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(100) NOT NULL,
	`last_name` VARCHAR(100) NOT NULL,
	`login` VARCHAR(100) NOT NULL,
	`password` VARCHAR(1000) NOT NULL,
	`email` VARCHAR(255) NOT NULL,
	`permission` VARCHAR(10) NOT NULL,
	`registration_date` DATE NOT NULL,
	PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `pswdb`.`event`;

CREATE TABLE IF NOT EXISTS `pswdb`.`event`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(100) NOT NULL,
	`agenda` VARCHAR(100) NOT NULL,
	`date` DATE NOT NULL,
	PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `pswdb`.`event_signup`;

CREATE TABLE IF NOT EXISTS `pswdb`.`event_signup`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`id_user` INT NOT NULL,
	`id_event` INT NOT NULL,
	`type` VARCHAR(50) NOT NULL,
	`catering` VARCHAR(50) NOT NULL,
	`accepted` BOOLEAN NOT NULL,
	PRIMARY KEY (`id`),
	INDEX `fk_event_signup_1_idx` (`id_user` ASC),
	INDEX `fk_event_signup_2_idx` (`id_event` ASC),
	CONSTRAINT `fk_event_signup_1`
		FOREIGN KEY (`id_user`)
		REFERENCES `pswdb`.`user` (`id`)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	CONSTRAINT `fk_event_signup_2`
		FOREIGN KEY (`id_event`)
		REFERENCES `pswdb`.`event` (`id`)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

INSERT INTO pswdb.user VALUES(0, 'Juliusz', 'Słowacki', 'root', 'localhost', 'root@localhost', 'admin', CURDATE());
INSERT INTO pswdb.event VALUES(0, 'Hello World!', 'Goodbye world', CURDATE());
INSERT INTO pswdb.event_signup VALUES(0, 1, 1, 'Organizer', 'No preference', FALSE);
