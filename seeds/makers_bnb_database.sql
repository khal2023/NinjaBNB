DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS bookings;

CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255),
    username VARCHAR(255),
    user_password VARCHAR(255)
);

INSERT INTO properties (first_name, surname, username, user_password) VALUES ('Khalid', 'Ham', 'KHam', 'Python24');
INSERT INTO properties (first_name, surname, username, user_password) VALUES ('Bakar', 'Shariffali', 'BShariffali', 'CSharp60');
INSERT INTO properties (first_name, surname, username, user_password) VALUES ('Lou', 'Paine', 'LPaine', 'Fortran90');
INSERT INTO properties (first_name, surname, username, user_password) VALUES ('Alberto', 'Tobarra', 'ATobarra', 'Java54');
INSERT INTO properties (first_name, surname, username, user_password) VALUES ('John', 'O Neill', 'JONeill', 'HTML30');


CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    property_name VARCHAR(255),
    street_address VARCHAR(255),
    city VARCHAR(255),
    property_description TEXT,
    price_per_night INT,
    person_owner_id INT,
    FOREIGN KEY (person_owner_id) REFERENCES people(id)
);

INSERT INTO properties (property_name, street_address, city, property_description, price_per_night, person_owner_id) VALUES ('The Ferns', '123 Wembley Downs', 'London', 'Haunted', 50, 1);
INSERT INTO properties (property_name, street_address, city, property_description, price_per_night, person_owner_id) VALUES ('The Laurels', '56 Secret Bay', 'Reykjavik', 'Cold', 30, 2);
INSERT INTO properties (property_name, street_address, city, property_description, price_per_night, person_owner_id) VALUES ('The Roses', '34 Sphinx Lane', 'Cairo', 'Warm', 60, 3);
INSERT INTO properties (property_name, street_address, city, property_description, price_per_night, person_owner_id) VALUES ('The Bananas', '1730 Clark St', 'Chicago', 'Windy', 65, 4);
INSERT INTO properties (property_name, street_address, city, property_description, price_per_night, person_owner_id) VALUES ('The Pines', '435 Melbourne Ave', 'Adelaide', 'Very Warm', 110, 5);


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    property_id INT,
    person_booker_id INT,
    booking_start_date DATE,
    booking_end_date DATE,
    FOREIGN KEY (property_id) REFERENCES properties(id),
    FOREIGN KEY (person_booker_id) REFERENCES people(id)
);

