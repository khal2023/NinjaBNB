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

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    property_name VARCHAR(255),
    street_address VARCHAR(255),
    city VARCHAR(255),
    property_description VARCHAR(255),
    price_per_night INT,
    person_owner_id INT,
    FOREIGN KEY (person_owner_id) REFERENCES people(id)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    property_id INT,
    person_booker_id INT,
    booking_start_date DATE,
    booking_end_date DATE,
    FOREIGN KEY (property_id) REFERENCES properties(id),
    FOREIGN KEY (person_booker_id) REFERENCES people(id)
);
