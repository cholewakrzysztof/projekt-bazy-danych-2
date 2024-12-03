-- Tworzenie użytkownika administratora
DROP USER 'admin_user'@'%';
DROP USER 'worker_user'@'%';
DROP USER 'client_user'@'%';


CREATE USER 'admin_user'@'%' IDENTIFIED BY 'secure_password_admin';
-- Tworzenie użytkownika pracownika
CREATE USER 'worker_user'@'%' IDENTIFIED BY 'secure_password_worker';

-- Tworzenie użytkownika klienta
CREATE USER 'client_user'@'%' IDENTIFIED BY 'secure_password_client';

GRANT ALL PRIVILEGES ON db_schema.* TO 'admin_user'@'%';
-- Uprawnienia SELECT dla wszystkich tabel w db_schema
GRANT SELECT ON db_schema.* TO 'worker_user'@'%';

-- Uprawnienia INSERT, UPDATE na tabeli Bilety
GRANT INSERT, UPDATE ON db_schema.tickets TO 'worker_user'@'%';


GRANT SELECT ON db_schema.tickets TO 'client_user'@'%';
GRANT SELECT ON db_schema.concerts TO 'client_user'@'%';
GRANT SELECT ON db_schema.event_series TO 'client_user'@'%';
GRANT SELECT ON db_schema.performers TO 'client_user'@'%';
GRANT SELECT ON db_schema.bands TO 'client_user'@'%';
GRANT SELECT ON db_schema.memberships TO 'client_user'@'%';
