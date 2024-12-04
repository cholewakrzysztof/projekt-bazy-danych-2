CREATE TABLE persons (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    sex BIT NULL,
    age INT NULL
);

CREATE TABLE contact_info (
    contact_info_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50) NULL,
    phone_number VARCHAR(12) NULL
);

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT,
    FOREIGN KEY (person_id) REFERENCES persons(person_id)
);

CREATE TABLE roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60)
);

CREATE TABLE works (
    work_id INT AUTO_INCREMENT PRIMARY KEY,
    concert_id INT,
    role_id INT,
    employee_id INT,
    salary INT NULL,
    work_hours INT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(role_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT,
    pseudonym VARCHAR(60) NULL,
    FOREIGN KEY (person_id) REFERENCES persons(person_id)
);

CREATE TABLE bands (
    band_id INT AUTO_INCREMENT PRIMARY KEY,
    band_name VARCHAR(60) NULL,
    address_id INT
);

CREATE TABLE memberships (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_id INT,
    band_id INT,
    start_date DATE,
    end_date DATE NULL,
    position VARCHAR(60) NULL,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
    FOREIGN KEY (band_id) REFERENCES bands(band_id)
);

CREATE TABLE styles (
    style_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60)
);

CREATE TABLE event_series (
    series_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60),
    start_date DATE,
    end_date DATE NULL
);

CREATE TABLE localizations (
    localization_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60) NULL,
    address_id INT,
    capacity INT NULL,
    price INT NULL,
    comment TEXT
);

CREATE TABLE address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(40),
    province VARCHAR(40) NULL,
    post_code VARCHAR(40),
    city VARCHAR(40),
    street VARCHAR(40) NULL,
    street_number VARCHAR(4),
    apartment_number VARCHAR(4) NULL
);

CREATE TABLE concerts (
    concert_id INT AUTO_INCREMENT PRIMARY KEY,
    localization_id INT,
    event_series_id INT,
    name VARCHAR(60) NULL,
    date DATE,
    duration TIME(7) NULL,
    FOREIGN KEY (localization_id) REFERENCES localizations(localization_id),
    FOREIGN KEY (event_series_id) REFERENCES event_series(series_id)
);

CREATE TABLE performers (
    perform_id INT AUTO_INCREMENT PRIMARY KEY,
    concert_id INT,
    band_id INT,
    style_id INT,
    price INT NULL,
    place_in_concert INT NULL,
    FOREIGN KEY (concert_id) REFERENCES concerts(concert_id),
    FOREIGN KEY (band_id) REFERENCES bands(band_id),
    FOREIGN KEY (style_id) REFERENCES styles(style_id)
);

CREATE TABLE participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT,
    FOREIGN KEY (person_id) REFERENCES persons(person_id)
);

CREATE TABLE ticket_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60)
);

CREATE TABLE tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    concert_id INT,
    price INT NOT NULL,
    type_id INT,
    participant_id INT,
    place VARCHAR(60) NULL,
    used BOOLEAN NULL,
    FOREIGN KEY (concert_id) REFERENCES concerts(concert_id),
    FOREIGN KEY (type_id) REFERENCES ticket_types(type_id),
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id)
);

CREATE TABLE contribution_types (
    contribution_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60)
);

CREATE TABLE partners (
    partner_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60),
    tin VARCHAR(11)
);

CREATE TABLE contributions (
    contribution_id INT AUTO_INCREMENT PRIMARY KEY,
    partner_id INT,
    series_id INT,
    contribution_type_id INT,
    price INT,
    FOREIGN KEY (partner_id) REFERENCES partners(partner_id),
    FOREIGN KEY (series_id) REFERENCES event_series(series_id),
    FOREIGN KEY (contribution_type_id) REFERENCES contribution_types(contribution_type_id)
);