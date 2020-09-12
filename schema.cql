CREATE TABLE certificates_by_email (
   email text,
   url text,
   first_name text,
   last_name text,
   PRIMARY KEY (email, url)
);

CREATE TABLE users_by_first_name (
    first_name_lowercase text,
    last_name text,
    url text,
    first_name text,
    PRIMARY KEY (first_name_lowercase, last_name, url)
);

CREATE TABLE users_by_last_name (
    last_name_lowercase text,
    first_name text,
    url text,
    last_name text,
    PRIMARY KEY (last_name_lowercase, first_name, url)
);
