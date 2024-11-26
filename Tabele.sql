CREATE TABLE persons (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    sex ENUM('M', 'F', 'Other'),
    age INT,
    email VARCHAR(100),
    phone_number VARCHAR(15)
);

CREATE TABLE contact_info (
    contact_info_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    phone_number VARCHAR(15)
);

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT,
    FOREIGN KEY (person_id) REFERENCES persons(person_id)
);

CREATE TABLE roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE works (
    work_id INT AUTO_INCREMENT PRIMARY KEY,
    concert_id INT,
    role_id INT,
    employee_id INT,
    salary DECIMAL(10, 2),
    work_hours INT,
    FOREIGN KEY (role_id) REFERENCES roles(role_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT,
    pseudonym VARCHAR(50),
    FOREIGN KEY (person_id) REFERENCES persons(person_id)
);

CREATE TABLE bands (
    band_id INT AUTO_INCREMENT PRIMARY KEY,
    band_name VARCHAR(100),
    address_id INT
);

CREATE TABLE memberships (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_id INT,
    band_id INT,
    start_date DATE,
    end_date DATE,
    position VARCHAR(50),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
    FOREIGN KEY (band_id) REFERENCES bands(band_id)
);

CREATE TABLE styles (
    style_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE event_series (
    series_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    start_date DATE,
    end_date DATE
);

CREATE TABLE localizations (
    localization_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address_id INT,
    capacity INT,
    price DECIMAL(10, 2),
    comment TEXT
);

CREATE TABLE address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(50),
    city VARCHAR(50),
    post_code VARCHAR(20),
    street VARCHAR(100),
    street_number VARCHAR(10),
    apartment_number VARCHAR(10)
);

CREATE TABLE concerts (
    concert_id INT AUTO_INCREMENT PRIMARY KEY,
    localization_id INT,
    event_series_id INT,
    name VARCHAR(100),
    date DATE,
    duration TIME,
    FOREIGN KEY (localization_id) REFERENCES localizations(localization_id),
    FOREIGN KEY (event_series_id) REFERENCES event_series(series_id)
);

CREATE TABLE performers (
    perform_id INT AUTO_INCREMENT PRIMARY KEY,
    concert_id INT,
    band_id INT,
    style_id INT,
    price DECIMAL(10, 2),
    place_in_concert INT,
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
    name VARCHAR(50)
);

CREATE TABLE tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    concert_id INT,
    type_id INT,
    participant_id INT,
    price DECIMAL(10,2),
    place VARCHAR(50),
    used BOOLEAN,
    FOREIGN KEY (concert_id) REFERENCES concerts(concert_id),
    FOREIGN KEY (type_id) REFERENCES ticket_types(type_id),
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id)
);

CREATE TABLE contribution_types (
    contribution_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE partners (
    partner_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    tin VARCHAR(20)
);

CREATE TABLE contributions (
    contribution_id INT AUTO_INCREMENT PRIMARY KEY,
    partner_id INT,
    series_id INT,
    contribution_type_id INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (partner_id) REFERENCES partners(partner_id),
    FOREIGN KEY (series_id) REFERENCES event_series(series_id),
    FOREIGN KEY (contribution_type_id) REFERENCES contribution_types(contribution_type_id)
);