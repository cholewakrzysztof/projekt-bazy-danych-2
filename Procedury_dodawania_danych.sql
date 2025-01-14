DELIMITER $$
-- Tabela persons
CREATE PROCEDURE AddPersons(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO persons (first_name, last_name, sex, age)
        VALUES (CONCAT('PersonFirst', i), CONCAT('PersonLast', i), 1, 25);
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela contact_info
CREATE PROCEDURE AddContactInfo(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO contact_info (email, phone_number, person_id)
        VALUES (CONCAT('email', i, '@example.com'), CONCAT('12345678', i), i);
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela employees
CREATE PROCEDURE AddEmployees(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        IF NOT EXISTS (SELECT 1 FROM persons WHERE person_id = i) THEN
            INSERT INTO persons (first_name, last_name, sex, age)
            VALUES (CONCAT('EmployeeFirst', i), CONCAT('EmployeeLast', i), 1, 30);
        END IF;
        INSERT INTO employees (person_id)
        VALUES (i);
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela roles
CREATE PROCEDURE AddRoles(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO roles (name)
        VALUES (CONCAT('RoleName', i));
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela works
CREATE PROCEDURE AddWorks(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        IF NOT EXISTS (SELECT 1 FROM concerts WHERE concert_id = 1) THEN
            INSERT INTO concerts (localization_id, event_series_id, name, date, duration)
            VALUES (1, 1, 'Default Concert', '2024-01-01', '02:00:00');
        END IF;
        IF NOT EXISTS (SELECT 1 FROM roles WHERE role_id = 1) THEN
            INSERT INTO roles (name) VALUES ('Default Role');
        END IF;
        IF NOT EXISTS (SELECT 1 FROM employees WHERE person_id = i) THEN
			INSERT INTO persons (first_name, last_name, sex, age)
			VALUES (CONCAT('EmployeeFirst', i), CONCAT('EmployeeLast', i), 1, 30);
			INSERT INTO employees (person_id) VALUES (i);
		END IF;
        INSERT INTO works (concert_id, role_id, employee_id, salary, work_hours)
        VALUES (1, 1, i, 3000, 8);
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela artists
CREATE PROCEDURE AddArtists(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        IF NOT EXISTS (SELECT 1 FROM persons WHERE person_id = i) THEN
            INSERT INTO persons (first_name, last_name, sex, age)
            VALUES (CONCAT('ArtistFirst', i), CONCAT('ArtistLast', i), 1, 28);
        END IF;
        INSERT INTO artists (person_id, pseudonym)
        VALUES (i, CONCAT('ArtistPseudonym', i));
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela bands
CREATE PROCEDURE AddBands(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO bands (band_name, address_id)
        VALUES (CONCAT('BandName', i), i);
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela memberships
CREATE PROCEDURE AddMemberships(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        IF NOT EXISTS (SELECT 1 FROM artists WHERE artist_id = i) THEN
            CALL AddArtists(i);
        END IF;
        IF NOT EXISTS (SELECT 1 FROM bands WHERE band_id = i) THEN
            INSERT INTO bands (band_name, address_id) VALUES (CONCAT('Band', i), 1);
        END IF;
        INSERT INTO memberships (artist_id, band_id, start_date, end_date, position)
        VALUES (i, i, '2024-01-01', NULL, CONCAT('Position', i));
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela styles
CREATE PROCEDURE AddStyles(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO styles (name)
        VALUES (CONCAT('StyleName', i));
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela event_series
CREATE PROCEDURE AddEventSeries(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO event_series (name, start_date, end_date)
        VALUES (CONCAT('SeriesName', i), '2024-01-01', NULL);
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela localizations
CREATE PROCEDURE AddLocalizations(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO localizations (name, address_id, capacity, price, comment)
        VALUES (CONCAT('Localization', i), i, 500, 1000, 'Example comment');
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela address
CREATE PROCEDURE AddAddress(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO address (country, province, post_code, city, street, street_number, apartment_number)
        VALUES ('Country', 'Province', CONCAT('00-', i), 'City', 'Street', CONCAT(i), NULL);
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela concerts
CREATE PROCEDURE AddConcerts(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        IF NOT EXISTS (SELECT 1 FROM localizations WHERE localization_id = 1) THEN
            INSERT INTO localizations (name, address_id, capacity, price, comment)
            VALUES ('Default Localization', 1, 500, 1000, 'Example comment');
        END IF;
        IF NOT EXISTS (SELECT 1 FROM event_series WHERE series_id = 1) THEN
            INSERT INTO event_series (name, start_date, end_date)
            VALUES ('Default Series', '2024-01-01', NULL);
        END IF;
        INSERT INTO concerts (localization_id, event_series_id, name, date, duration)
        VALUES (1, 1, CONCAT('Concert', i), '2024-01-01', '02:00:00');
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela performers
CREATE PROCEDURE AddPerformers(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        IF NOT EXISTS (SELECT 1 FROM concerts WHERE concert_id = 1) THEN
            CALL AddConcerts(1);
        END IF;
        IF NOT EXISTS (SELECT 1 FROM bands WHERE band_id = 1) THEN
            INSERT INTO bands (band_name, address_id) VALUES ('Default Band', 1);
        END IF;
        IF NOT EXISTS (SELECT 1 FROM styles WHERE style_id = 1) THEN
            INSERT INTO styles (name) VALUES ('Default Style');
        END IF;
        INSERT INTO performers (concert_id, band_id, style_id, price, place_in_concert)
        VALUES (1, 1, 1, 1000, i);
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela participants
CREATE PROCEDURE AddParticipants(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        IF NOT EXISTS (SELECT 1 FROM persons WHERE person_id = i) THEN
            INSERT INTO persons (first_name, last_name, sex, age)
            VALUES (CONCAT('ParticipantFirst', i), CONCAT('ParticipantLast', i), 1, 20);
        END IF;
        INSERT INTO participants (person_id)
        VALUES (i);
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela ticket_types
CREATE PROCEDURE AddTicketTypes(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO ticket_types (name)
        VALUES (CONCAT('TicketType', i));
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela tickets
CREATE PROCEDURE AddTickets(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        IF NOT EXISTS (SELECT 1 FROM concerts WHERE concert_id = 1) THEN
            CALL AddConcerts(1);
        END IF;
        IF NOT EXISTS (SELECT 1 FROM ticket_types WHERE type_id = 1) THEN
            INSERT INTO ticket_types (name) VALUES ('Default Type');
        END IF;
        IF NOT EXISTS (SELECT 1 FROM participants WHERE participant_id = i) THEN
			INSERT INTO participants (person_id) VALUES (i);
		END IF;
        INSERT INTO tickets (concert_id, price, type_id, participant_id, place, used)
        VALUES (1, 100, 1, i, CONCAT('Place', i), NULL);
        SET i = i + 1;
    END WHILE;
END$$


-- Tabela contribution_types
CREATE PROCEDURE AddContributionTypes(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO contribution_types (name)
        VALUES (CONCAT('ContributionType', i));
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela partners
CREATE PROCEDURE AddPartners(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO partners (name, tin)
        VALUES (CONCAT('Partner', i), LPAD(i, 11, '0'));
        SET i = i + 1;
    END WHILE;
END$$

-- Tabela contributions
CREATE PROCEDURE AddContributions(IN num_records INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= num_records DO
        INSERT INTO contributions (partner_id, series_id, contribution_type_id, price)
        VALUES (1, 1, 1, 1000 + i);
        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;