-- Tabela persons
INSERT INTO persons (person_id, first_name, last_name, sex, age) VALUES 
(1, 'John', 'Doe', 1, 30),
(2, 'Jane', 'Smith', 0, 25),
(3, 'Emily', 'Johnson', 0, 35);

-- Tabela contact_info
INSERT INTO contact_info (contact_info_id, email, phone_number) VALUES 
(1, 'john.doe@example.com', '1234567890'),
(2, 'jane.smith@example.com', '0987654321'),
(3, 'emily.johnson@example.com', '1122334455');

-- Tabela employees
INSERT INTO employees (employee_id, person_id) VALUES 
(1, 1),
(2, 2);

-- Tabela roles
INSERT INTO roles (role_id, name) VALUES 
(1, 'Manager'),
(2, 'Technician');

-- Tabela works
INSERT INTO works (work_id, concert_id, role_id, employee_id, salary, work_hours) VALUES 
(1, 1, 1, 1, 5000, 40),
(2, 2, 2, 2, 3000, 35);

-- Tabela artists
INSERT INTO artists (artist_id, person_id, pseudonym) VALUES 
(1, 3, 'EmilyJ');

-- Tabela bands
INSERT INTO bands (band_id, band_name, address_id) VALUES 
(1, 'The Rockers', NULL),
(2, 'Jazz Quartet', NULL);

-- Tabela memberships
INSERT INTO memberships (membership_id, artist_id, band_id, start_date, end_date, position) VALUES 
(1, 1, 1, '2020-01-01', NULL, 'Lead Singer');

-- Tabela styles
INSERT INTO styles (style_id, name) VALUES 
(1, 'Rock'),
(2, 'Jazz');

-- Tabela event_series
INSERT INTO event_series (series_id, name, start_date, end_date) VALUES 
(1, 'Winter Fest', '2024-01-01', '2024-02-01');

-- Tabela address
INSERT INTO address (address_id, country, province, post_code, city, street, street_number, apartment_number) VALUES 
(1, 'USA', 'CA', '90210', 'Los Angeles', 'Sunset Blvd', '101', NULL);

-- Tabela localizations
INSERT INTO localizations (localization_id, name, address_id, capacity, price, comment) VALUES 
(1, 'Stadium LA', 1, 50000, 1000, 'Large venue');

-- Tabela concerts
INSERT INTO concerts (concert_id, localization_id, event_series_id, name, date, duration) VALUES 
(1, 1, 1, 'Rock Night', '2024-01-15', '02:00:00'),
(2, 1, 1, 'Jazz Evening', '2024-01-20', '01:30:00');

-- Tabela performers
INSERT INTO performers (perform_id, concert_id, band_id, style_id, price, place_in_concert) VALUES 
(1, 1, 1, 1, 1000, 1),
(2, 2, 2, 2, 800, 2);

-- Tabela participants
INSERT INTO participants (participant_id, person_id) VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Tabela ticket_types
INSERT INTO ticket_types (type_id, name) VALUES 
(1, 'Standard'),
(2, 'VIP');

-- Tabela tickets
INSERT INTO tickets (ticket_id, concert_id, price, type_id, participant_id, place, used) VALUES 
(1, 1, 100.00, 1, 1, 'A1', 0),
(2, 2, 200.00, 2, 2, 'B1', 1);

-- Tabela contribution_types
INSERT INTO contribution_types (contribution_type_id, name) VALUES 
(1, 'Sponsorship'),
(2, 'Donation');

-- Tabela partners
INSERT INTO partners (partner_id, name, tin) VALUES 
(1, 'Company X', '12345678901'),
(2, 'Company Y', '09876543210');

-- Tabela contributions
INSERT INTO contributions (contribution_id, partner_id, series_id, contribution_type_id, price) VALUES 
(1, 1, 1, 1, 50000),
(2, 2, 1, 2, 30000);
