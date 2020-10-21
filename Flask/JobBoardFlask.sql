-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : lun. 05 oct. 2020 à 09:50
-- Version du serveur :  10.4.14-MariaDB
-- Version de PHP : 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `JobBoardFlask`
--

DELIMITER $$
--
-- Procédures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteCategory` (IN `paramId` INT)  NO SQL
BEGIN
DELETE FROM Category where Category.Id=paramId;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteCompany` (IN `paramId` INT)  NO SQL
BEGIN
DELETE FROM Company where Company.Id=paramId;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteJob` (IN `paramId` INT)  NO SQL
BEGIN
DELETE FROM Job where Job.Id=paramId;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteUser` (IN `paramId` INT)  NO SQL
BEGIN
DELETE FROM `User` where `User`.`Id`=paramId;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertAdvertisement` (IN `paramIdUser` INT(11), IN `paramIdJob` INT(11))  NO SQL
BEGIN
	if(SELECT EXISTS (SELECT 1 from Advertisements where Advertisements.Id_User = paramIdUser COLLATE utf8mb4_unicode_ci AND Advertisements.Id_Job=paramIdJob COLLATE utf8mb4_unicode_ci)) THEN
    	Select 'Advertisement already exists';
    ELSE
    	INSERT INTO Advertisements(Advertisements.Id_User, Advertisements.Id_Job) VALUES(paramIdUser, paramIdJob);
    End If;
 


END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertCategory` (IN `paramTitle` VARCHAR(255))  NO SQL
BEGIN
	if(SELECT EXISTS (SELECT 1 from Category where Category.Title = paramTitle COLLATE utf8mb4_unicode_ci)) THEN
    	Select 'Category exists !!';
    
    ELSE
    	INSERT into Category(Category.Title) VALUES(paramTitle);
    END IF;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertCompany` (IN `paramName` VARCHAR(255) CHARSET utf8mb4, IN `paramSiret` BIGINT(14))  NO SQL
BEGIN
	if(SELECT EXISTS (SELECT 1 from Company where Company.Name = paramName COLLATE utf8mb4_unicode_ci)) THEN
    	Select 'Company exists !!';
    
    ELSE
   		insert into Company
        (
            Company.Name,
            Company.SIRET
        )VALUES
        (paramName,
        paramSiret);
    END IF;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertJob` (IN `paramTitle` VARCHAR(255), IN `paramContent` TEXT, IN `paramIdComp` INT(11), IN `paramIdCateg` INT(11))  NO SQL
BEGIN
	if(SELECT EXISTS (SELECT 1 from Job where Job.Title = paramTitle COLLATE utf8mb4_unicode_ci)) THEN
    	Select 'Job exists !!';
	ELSE 
    	INSERT INTO Job(Job.Title, Job.DateAdded, Job.Content, Job.Id_Company, Job.Id_Category) VALUES (paramTitle, curdate(), paramContent, paramIdComp, paramIdCateg);
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertMail` (IN `paramContent` TEXT, IN `paramIdAd` INT(11))  NO SQL
BEGIN
	INSERT INTO Mail(Mail.Content, Mail.Id_Advertissements) VALUES (paramContent, paramIdAd);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertUser` (IN `paramEmail` VARCHAR(255), IN `paramName` VARCHAR(255), IN `paramLastname` VARCHAR(255), IN `paramAge` INT(11), IN `paramPassword` VARCHAR(255), IN `paramCategory` TINYINT(1))  NO SQL
BEGIN
	    if ( select exists (select 1 from `User` where `User`.`Email` = paramEmail COLLATE utf8mb4_unicode_ci) ) THEN
        select 'Username Exists !!';
        
        ELSE
           insert into `User`
        (
            Name,
            Lastname,
            Age,
            Email,
            `Password`,
            Category
            
        )
        values
        (
           	paramName,
            paramLastname,
            paramAge,
            paramEmail,
            paramPassword,
            paramCategory
        );
     
    END IF;
        
     



END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updateCategory` (IN `paramId` INT(11), IN `paramTitle` VARCHAR(255))  NO SQL
BEGIN
UPDATE Category SET Title=paramTitle WHERE Id=paramId;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updateCompany` (IN `paramId` INT(11), IN `paramName` VARCHAR(255), IN `paramSiret` BIGINT(14))  NO SQL
BEGIN
UPDATE Company SET Name=paramName, SIRET=paramSiret WHERE Id=paramId;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updateJob` (IN `paramId` INT, IN `paramTitle` VARCHAR(255), IN `paramContent` TEXT, IN `paramIdComp` INT(11), IN `paramIdCat` INT(11))  NO SQL
BEGIN
UPDATE Job SET Title=paramTitle, Content=paramContent,
Id_Company=paramIdComp,
Id_Category=paramIdCat
WHERE Id=paramId;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updateUser` (IN `paramId` INT(11), IN `paramName` VARCHAR(255), IN `paramLastname` VARCHAR(255), IN `paramAge` INT(11), IN `paramEmail` VARCHAR(255), IN `paramPassword` VARCHAR(255), IN `paramCateg` TINYINT(1))  NO SQL
BEGIN
update `User` SET Name=paramName, Lastname=paramLastname,
Age=paramAge,
Email=paramEmail,
`Password`=paramPassword,
Category=paramCateg
WHERE Id=paramId;


END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Structure de la table `Advertisements`
--

CREATE TABLE `Advertisements` (
  `Id` int(11) NOT NULL,
  `Id_User` int(11) NOT NULL,
  `Id_Job` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `Advertisements`
--

INSERT INTO `Advertisements` (`Id`, `Id_User`, `Id_Job`) VALUES
(1, 3, 3),
(2, 2, 3),
(3, 2, 1),
(4, 3, 3),
(5, 4, 4),
(6, 2, 4);

-- --------------------------------------------------------

--
-- Structure de la table `Category`
--

CREATE TABLE `Category` (
  `Id` int(11) NOT NULL,
  `Title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `Category`
--

INSERT INTO `Category` (`Id`, `Title`) VALUES
(1, 'Alimentation'),
(2, 'Development'),
(3, 'Store\r\n');

-- --------------------------------------------------------

--
-- Structure de la table `Company`
--

CREATE TABLE `Company` (
  `Id` int(11) NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `SIRET` bigint(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `Company`
--

INSERT INTO `Company` (`Id`, `Name`, `SIRET`) VALUES
(1, 'EvilCorp', 12345678912345),
(2, 'Google', 98765432198765),
(3, 'Vittel', 49347568456189),
(4, 'IKEA', 45967538427928);

-- --------------------------------------------------------

--
-- Structure de la table `Job`
--

CREATE TABLE `Job` (
  `Id` int(11) NOT NULL,
  `Title` varchar(255) NOT NULL,
  `DateAdded` timestamp NULL DEFAULT NULL,
  `Content` text NOT NULL,
  `Id_Company` int(11) NOT NULL,
  `Id_Category` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `Job`
--

INSERT INTO `Job` (`Id`, `Title`, `DateAdded`, `Content`, `Id_Company`, `Id_Category`) VALUES
(1, 'Seller at IKEA', NULL, 'Searching M/W', 4, 3),
(2, 'Developer C for Google', NULL, 'Developer C M/W', 2, 2),
(3, 'Developer Front for Vittel', NULL, 'Developer M/W', 3, 2),
(4, 'Developer FullStack for EvilCorp', NULL, 'Developer M/W', 1, 2);

-- --------------------------------------------------------

--
-- Structure de la table `JobSeekers`
--

CREATE TABLE `JobSeekers` (
  `Id_User` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `JobSeekers`
--

INSERT INTO `JobSeekers` (`Id_User`) VALUES
(2),
(3),
(4),
(6),
(79);

-- --------------------------------------------------------

--
-- Structure de la table `Mail`
--

CREATE TABLE `Mail` (
  `Id` int(11) NOT NULL,
  `Content` text NOT NULL,
  `Id_Advertissements` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `Mail`
--

INSERT INTO `Mail` (`Id`, `Content`, `Id_Advertissements`) VALUES
(1, 'Mail 1 from Ad1', 1),
(2, 'Mail 2 from Ad1', 1),
(3, 'Mail 1 from ad 4', 4),
(4, 'Mail 2 from ad4', 4),
(5, 'Mail 1 from Ad5 ', 5),
(6, 'Mail 2 from ad5', 5),
(7, 'Mail 3 from ad5', 5);

-- --------------------------------------------------------

--
-- Structure de la table `RH`
--

CREATE TABLE `RH` (
  `Id_User` int(11) NOT NULL,
  `Id_Company` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `RH`
--

INSERT INTO `RH` (`Id_User`, `Id_Company`) VALUES
(1, NULL),
(5, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `User`
--

CREATE TABLE `User` (
  `Id` int(11) NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Lastname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Age` int(11) NOT NULL,
  `Email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Category` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `User`
--

INSERT INTO `User` (`Id`, `Name`, `Lastname`, `Age`, `Email`, `Password`, `Category`) VALUES
(1, 'Jean', 'VALJEAN', 35, 'jean.valjean@gmail.com', '12345', 1),
(2, 'Pierre', 'DUPOND', 51, 'pierre.dupond@gmail.com', '12345', 0),
(3, 'Charles', 'DUPONT', 52, 'charles.dupont@gmail.com', '12345', 0),
(4, 'Julie', 'JACQUEMUS', 24, 'julie.jacquemus@gmail.com', '12345', 0),
(5, 'Hugo', 'PACKARD', 30, 'hugo.packard@gmail.com', '12345', 1),
(6, 'Lucie', 'SIMONS', 42, 'lucie.simons@gmail.com', '12345', 0),
(79, 'aze', 'aze@gmail', 45, 'a', 'azeaze', 0);

--
-- Déclencheurs `User`
--
DELIMITER $$
CREATE TRIGGER `RHonInsert` AFTER INSERT ON `User` FOR EACH ROW IF (NEW.Category = 1) THEN
INSERT INTO RH VALUES(NEW.Id, null);
ELSE
INSERT INTO JobSeekers VALUES(NEW.Id);
END IF
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `RHonupdate` BEFORE UPDATE ON `User` FOR EACH ROW IF (NEW.Category = 1) THEN
DELETE FROM JobSeekers where Id_User=new.id;
INSERT INTO RH VALUES(NEW.Id, null);
ELSE
DELETE FROM RH where Id_User=new.id;
INSERT INTO JobSeekers VALUES(NEW.Id);
END IF
$$
DELIMITER ;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Advertisements`
--
ALTER TABLE `Advertisements`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Id_User` (`Id_User`),
  ADD KEY `Id_Job` (`Id_Job`);

--
-- Index pour la table `Category`
--
ALTER TABLE `Category`
  ADD PRIMARY KEY (`Id`);

--
-- Index pour la table `Company`
--
ALTER TABLE `Company`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `SIRET` (`SIRET`);

--
-- Index pour la table `Job`
--
ALTER TABLE `Job`
  ADD PRIMARY KEY (`Id`) USING BTREE,
  ADD KEY `Id_Category` (`Id_Category`),
  ADD KEY `fkcomp` (`Id_Company`);

--
-- Index pour la table `JobSeekers`
--
ALTER TABLE `JobSeekers`
  ADD KEY `Id_User` (`Id_User`);

--
-- Index pour la table `Mail`
--
ALTER TABLE `Mail`
  ADD PRIMARY KEY (`Id`) USING BTREE,
  ADD KEY `Id_Advertissements` (`Id_Advertissements`);

--
-- Index pour la table `RH`
--
ALTER TABLE `RH`
  ADD KEY `fk_userId` (`Id_User`),
  ADD KEY `fk_company` (`Id_Company`);

--
-- Index pour la table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`Id`) USING BTREE,
  ADD KEY `Email` (`Email`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Advertisements`
--
ALTER TABLE `Advertisements`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `Category`
--
ALTER TABLE `Category`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `Company`
--
ALTER TABLE `Company`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `Job`
--
ALTER TABLE `Job`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `Mail`
--
ALTER TABLE `Mail`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `User`
--
ALTER TABLE `User`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=80;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Advertisements`
--
ALTER TABLE `Advertisements`
  ADD CONSTRAINT `advertisements_ibfk_2` FOREIGN KEY (`Id_User`) REFERENCES `JobSeekers` (`Id_User`) ON DELETE CASCADE,
  ADD CONSTRAINT `advertisements_ibfk_3` FOREIGN KEY (`Id_Job`) REFERENCES `Job` (`Id`) ON DELETE CASCADE;

--
-- Contraintes pour la table `Job`
--
ALTER TABLE `Job`
  ADD CONSTRAINT `fkcomp` FOREIGN KEY (`Id_Company`) REFERENCES `Company` (`Id`),
  ADD CONSTRAINT `job_ibfk_1` FOREIGN KEY (`Id_Category`) REFERENCES `Category` (`Id`);

--
-- Contraintes pour la table `JobSeekers`
--
ALTER TABLE `JobSeekers`
  ADD CONSTRAINT `JobSeekers_ibfk_1` FOREIGN KEY (`Id_User`) REFERENCES `User` (`Id`) ON DELETE CASCADE;

--
-- Contraintes pour la table `Mail`
--
ALTER TABLE `Mail`
  ADD CONSTRAINT `mail_ibfk_1` FOREIGN KEY (`Id_Advertissements`) REFERENCES `Advertisements` (`Id`);

--
-- Contraintes pour la table `RH`
--
ALTER TABLE `RH`
  ADD CONSTRAINT `fk_company` FOREIGN KEY (`Id_Company`) REFERENCES `Company` (`Id`),
  ADD CONSTRAINT `fk_userId` FOREIGN KEY (`Id_User`) REFERENCES `User` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
