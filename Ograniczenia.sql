ALTER TABLE works
ADD CONSTRAINT check_salary_non_negative 
CHECK (salary >= 0);

ALTER TABLE performers
ADD CONSTRAINT fk_band 
FOREIGN KEY (band_id) REFERENCES bands(band_id);

ALTER TABLE concerts
ADD CONSTRAINT unique_concert_date_per_localization 
UNIQUE (localization_id, date);
-- **********************************(nowe - nie dodane jeszcze)
ALTER TABLE concerts
ADD CONSTRAINT unique_concert_date_per_localization 
UNIQUE (localization_id, date);

ALTER TABLE localizations
ADD CONSTRAINT check_capacity_positive 
CHECK (capacity > 0);

ALTER TABLE tickets
ADD CONSTRAINT check_ticket_price_positive 
CHECK (price >= 0);

ALTER TABLE persons
ADD CONSTRAINT check_valid_sex 
CHECK (sex IN ('M', 'F', 'Other'));

ALTER TABLE event_series
ADD CONSTRAINT check_event_series_date_range 
CHECK (start_date <= end_date OR end_date IS NULL);

ALTER TABLE works
ADD CONSTRAINT check_work_hours_positive 
CHECK (work_hours > 0);

ALTER TABLE address
ADD CONSTRAINT check_post_code_length 
CHECK (LENGTH(post_code) >= 5);

ALTER TABLE artists
ADD CONSTRAINT check_pseudonym_not_empty 
CHECK (pseudonym IS NOT NULL AND LENGTH(pseudonym) > 0);

