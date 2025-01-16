-- Set SQL mode if necessary
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

-- Create patients table
CREATE TABLE `patients` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `first_name` varchar(55) NOT NULL,
    `last_name` varchar(55) NOT NULL,
    `email` varchar(55) NOT NULL,
    `phone` varchar(15) NOT NULL, -- Changed to VARCHAR to better suit phone numbers
    `address` varchar(255) NOT NULL, -- Increased length for address
    `gender` varchar(55) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `phone` (`phone`) --nb i added the entity age to this table
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Create medicines table
CREATE TABLE `medicines` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(55) NOT NULL,
    `quantity_left` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Create treatment table
CREATE TABLE `treatment` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `medicines_id` int(11) NOT NULL,
    `quantity` int(11) NOT NULL,
    `dosage` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fk_treatment_medicines_id` (`medicines_id`),
    CONSTRAINT `fk_treatment_medicines_id` FOREIGN KEY (`medicines_id`) REFERENCES `medicines` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Create nurses table
CREATE TABLE `nurses` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `first_name` varchar(55) NOT NULL,
    `last_name` varchar(55) NOT NULL,
    `email` varchar(55) NOT NULL,
    `gender` varchar(55) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Create users table
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(55) NOT NULL,
    `display_name` varchar(55) NOT NULL,
    `rank` varchar(55) NOT NULL,
    `password` varchar(55) NOT NULL,
    `profile_picture` varchar(55) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Create patient_treatment_information table
CREATE TABLE `patient_treatment_information` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `patient_id` int(11) NOT NULL,
    `nurses_id` int(11) NOT NULL,
    `day_of_treatment` date NOT NULL, -- Changed to DATE to better represent a date
    `treatment_id` int(11) NOT NULL,
    `symptoms` varchar(255) NOT NULL, -- Changed to VARCHAR for textual description of symptoms
    PRIMARY KEY (`id`),
    KEY `fk_patient_treatment_information_patient_id` (`patient_id`),
    KEY `fk_patient_treatment_information_treatment_id` (`treatment_id`),
    KEY `fk_patient_treatment_information_nurses_id` (`nurses_id`),
    CONSTRAINT `fk_patient_treatment_information_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`id`),
    CONSTRAINT `fk_patient_treatment_information_treatment_id` FOREIGN KEY (`treatment_id`) REFERENCES `treatment` (`id`),
    CONSTRAINT `fk_patient_treatment_information_nurses_id` FOREIGN KEY (`nurses_id`) REFERENCES `nurses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE users ADD COLUMN age INT;

COMMIT;
