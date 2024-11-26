DELIMITER //
CREATE TRIGGER CheckTicketCapacity
BEFORE INSERT ON tickets
FOR EACH ROW
BEGIN
    DECLARE loc_capacity INT;
    -- Pobranie pojemności lokalizacji na podstawie koncertu
    SELECT l.capacity INTO loc_capacity
    FROM concerts c
    JOIN localizations l ON c.localization_id = l.localization_id
    WHERE c.concert_id = NEW.concert_id;
    -- Sprawdzenie, czy liczba biletów przekracza pojemność
    IF (SELECT COUNT(*) FROM tickets WHERE concert_id = NEW.concert_id) >= loc_capacity THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert new ticket: capacity exceeded for the given localization.';
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER CheckConcertDate
BEFORE INSERT ON concerts
FOR EACH ROW
BEGIN
    DECLARE start_date DATE;
    DECLARE end_date DATE;
    -- Pobranie daty rozpoczęcia i zakończenia serii wydarzeń
    SELECT es.start_date, es.end_date 
    INTO start_date, end_date
    FROM event_series es
    WHERE es.series_id = NEW.event_series_id;
    -- Sprawdzenie, czy data koncertu mieści się w zakresie serii
    IF NEW.date < start_date THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Concert date must be after the start date of the event series.';
    END IF;
    IF end_date IS NOT NULL THEN
        IF NEW.date > end_date THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Concert date must be before the end date of the event series.';
        END IF;
    END IF;
END //
DELIMITER ;
