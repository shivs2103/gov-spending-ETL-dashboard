-- Dimension Tables

CREATE TABLE dim_state (
    state_id INT PRIMARY KEY,
    state_name VARCHAR(100)
);

CREATE TABLE dim_department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE dim_scheme (
    scheme_id INT PRIMARY KEY,
    scheme_name VARCHAR(100)
);

CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    year INT
);

-- Fact Table

CREATE TABLE fact_spending (
    state_id INT,
    department_id INT,
    scheme_id INT,
    time_id INT,
    amount_spent FLOAT,
    beneficiaries INT,
    FOREIGN KEY (state_id) REFERENCES dim_state(state_id),
    FOREIGN KEY (department_id) REFERENCES dim_department(department_id),
    FOREIGN KEY (scheme_id) REFERENCES dim_scheme(scheme_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);