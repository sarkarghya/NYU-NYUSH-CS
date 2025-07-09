--
--
-- Create model ContentType
--
CREATE TABLE IF NOT EXISTS `django_content_type` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(100) NOT NULL, `app_label` varchar(100) NOT NULL, `model` varchar(100) NOT NULL);
--
-- Alter unique_together for contenttype (1 constraint(s))
--
ALTER TABLE `django_content_type` ADD CONSTRAINT `django_content_type_app_label_model_76bd3d3b_uniq` UNIQUE (`app_label`, `model`);
--
-- Change Meta options on contenttype
--
--
-- Alter field name on contenttype
--
ALTER TABLE `django_content_type` MODIFY `name` varchar(100) NULL;
--
-- MIGRATION NOW PERFORMS OPERATION THAT CANNOT BE WRITTEN AS SQL:
-- Raw Python operation
--
--
-- Remove field name from contenttype
--
ALTER TABLE `django_content_type` DROP COLUMN `name`;
--
-- Create model Permission
--
CREATE TABLE IF NOT EXISTS `auth_permission` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(50) NOT NULL, `content_type_id` integer NOT NULL, `codename` varchar(100) NOT NULL);
--
-- Create model Group
--
CREATE TABLE IF NOT EXISTS `auth_group` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(80) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `group_id` integer NOT NULL, `permission_id` integer NOT NULL);
--
-- Create model User
--
CREATE TABLE IF NOT EXISTS `auth_user` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `password` varchar(128) NOT NULL, `last_login` datetime(6) NOT NULL, `is_superuser` bool NOT NULL, `username` varchar(30) NOT NULL UNIQUE, `first_name` varchar(30) NOT NULL, `last_name` varchar(30) NOT NULL, `email` varchar(75) NOT NULL, `is_staff` bool NOT NULL, `is_active` bool NOT NULL, `date_joined` datetime(6) NOT NULL);
CREATE TABLE IF NOT EXISTS `auth_user_groups` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `user_id` integer NOT NULL, `group_id` integer NOT NULL);
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `user_id` integer NOT NULL, `permission_id` integer NOT NULL);
ALTER TABLE `auth_permission` ADD CONSTRAINT `auth_permission_content_type_id_codename_01ab375a_uniq` UNIQUE (`content_type_id`, `codename`);
ALTER TABLE `auth_permission` ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` UNIQUE (`group_id`, `permission_id`);
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_user_id_group_id_94350c0c_uniq` UNIQUE (`user_id`, `group_id`);
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` UNIQUE (`user_id`, `permission_id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
--
-- Alter field name on permission
--
ALTER TABLE `auth_permission` MODIFY `name` varchar(255) NOT NULL;
--
-- Alter field email on user
--
ALTER TABLE `auth_user` MODIFY `email` varchar(254) NOT NULL;
--
-- Alter field username on user
--
--
-- Alter field last_login on user
--
ALTER TABLE `auth_user` MODIFY `last_login` datetime(6) NULL;
--
-- Alter field username on user
--
--
-- Alter field username on user
--
ALTER TABLE `auth_user` MODIFY `username` varchar(150) NOT NULL;
--
-- Alter field last_name on user
--
ALTER TABLE `auth_user` MODIFY `last_name` varchar(150) NOT NULL;
--
-- Alter field name on group
--
ALTER TABLE `auth_group` MODIFY `name` varchar(150) NOT NULL;
--
-- MIGRATION NOW PERFORMS OPERATION THAT CANNOT BE WRITTEN AS SQL:
-- Raw Python operation
--
--
-- Alter field first_name on user
--
ALTER TABLE `auth_user` MODIFY `first_name` varchar(150) NOT NULL;
--
-- Create model Session
--
CREATE TABLE IF NOT EXISTS `django_session` (`session_key` varchar(40) NOT NULL PRIMARY KEY, `session_data` longtext NOT NULL, `expire_date` datetime(6) NOT NULL);
CREATE INDEX `django_session_expire_date_a5c62663` ON `django_session` (`expire_date`);

-- Create model Product
--
CREATE TABLE IF NOT EXISTS `LegacySite_product` (`product_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `product_name` varchar(50) NOT NULL UNIQUE, `product_image_path` varchar(100) NOT NULL UNIQUE, `recommended_price` integer NOT NULL, `description` varchar(250) NOT NULL);
--
-- Create model User
--
CREATE TABLE IF NOT EXISTS `LegacySite_user` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `last_login` datetime(6) NULL, `username` varchar(30) NOT NULL UNIQUE, `password` varchar(97) NOT NULL);
--
-- Create model Card
--
CREATE TABLE IF NOT EXISTS `LegacySite_card` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `data` longblob NOT NULL, `amount` integer NOT NULL, `fp` varchar(100) NOT NULL UNIQUE, `used` bool NOT NULL, `product_id` integer NOT NULL, `user_id` integer NOT NULL);
ALTER TABLE `LegacySite_card` ADD CONSTRAINT `LegacySite_card_product_id_a477f64b_fk_LegacySit` FOREIGN KEY (`product_id`) REFERENCES `LegacySite_product` (`product_id`);
ALTER TABLE `LegacySite_card` ADD CONSTRAINT `LegacySite_card_user_id_c0621db6_fk_LegacySite_user_id` FOREIGN KEY (`user_id`) REFERENCES `LegacySite_user` (`id`);
--
-- Create model LogEntry
--
CREATE TABLE IF NOT EXISTS `django_admin_log` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `action_time` datetime(6) NOT NULL, `object_id` longtext NULL, `object_repr` varchar(200) NOT NULL, `action_flag` smallint UNSIGNED NOT NULL CHECK (`action_flag` >= 0), `change_message` longtext NOT NULL, `content_type_id` integer NULL, `user_id` integer NOT NULL);
ALTER TABLE `django_admin_log` ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
ALTER TABLE `django_admin_log` ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
--
-- Alter field action_time on logentry
--
--
-- Alter field action_flag on logentry
--
--
-- Put products into table.
--
LOAD DATA INFILE '/products.csv' INTO TABLE LegacySite_product FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\r\n';
--
-- Put user into table.
--
LOAD DATA INFILE '/users.csv' INTO TABLE LegacySite_user FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\r\n';
