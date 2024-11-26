DELIMITER //
CREATE PROCEDURE MarkUsedTicketsForPastConcerts()
BEGIN
    UPDATE tickets 
    SET used = 1
    WHERE concert_id IN (
        SELECT concert_id 
        FROM concerts 
        WHERE date < CURDATE()
    );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateSalariesByWorkRoleAndConcert
(
    IN p_concert_id INT,  
    IN p_work_role_id INT,  
    IN p_multiplier DECIMAL(10, 2)
)
BEGIN
    UPDATE works 
    SET salary = salary * p_multiplier  
    WHERE role_id = p_work_role_id  
    AND concert_id = p_concert_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteBandPerformancesAndAdjustPlaces
(
    IN p_band_id INT,  
    IN p_concert_id INT
)
BEGIN
    DECLARE deleted_count INT;
    -- Obliczenie liczby występów do usunięcia
    SELECT COUNT(*) INTO deleted_count 
    FROM performers  
    WHERE band_id = p_band_id AND concert_id = p_concert_id;
    -- Usunięcie występów zespołu z koncertu
    DELETE FROM performers  
    WHERE band_id = p_band_id AND concert_id = p_concert_id;
    -- Aktualizacja miejsc dla pozostałych występów
    UPDATE performers 
    SET place_in_concert = place_in_concert - deleted_count  
    WHERE concert_id = p_concert_id  
    AND place_in_concert > (
        SELECT COALESCE(MAX(place_in_concert), 0) 
        FROM performers  
        WHERE band_id = p_band_id  
        AND concert_id = p_concert_id
    );
END //
DELIMITER ;

