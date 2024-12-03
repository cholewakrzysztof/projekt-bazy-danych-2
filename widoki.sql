CREATE VIEW Concert_details_view AS
SELECT c.concert_id,c.name AS concert_name,c.date,c.duration,es.name AS series_name,a.country,a.city, a.street,a.street_number
FROM concerts c
JOIN event_series es ON c.event_series_id = es.series_id
JOIN localizations l ON c.localization_id = l.localization_id
JOIN address a ON l.address_id = a.address_id;


CREATE VIEW Employee_work_details AS
SELECT p.first_name, p.last_name, ci.email, c.concert_id, c.name AS concert_name, c.date, w.work_hours, r.name AS role_name, w.salary
FROM works w
JOIN employees e ON w.employee_id = e.employee_id
JOIN persons p ON e.person_id = p.person_id
JOIN roles r ON w.role_id = r.role_id
JOIN concerts c ON w.concert_id = c.concert_id
JOIN contact_info ci ON p.person_id = ci.person_id;


CREATE VIEW Ticket_sales_summary AS
SELECT es.series_id, es.name AS series_name, c.concert_id, c.name AS concert_name,COUNT(t.ticket_id) AS sum_sold_tickets,
COUNT(DISTINCT t.participant_id) AS number_of_participants
FROM tickets t
JOIN concerts c ON t.concert_id = c.concert_id
JOIN event_series es ON c.event_series_id = es.series_id
JOIN participants pt ON t.participant_id = pt.participant_id
GROUP BY es.series_id, es.name, c.concert_id, c.name;
