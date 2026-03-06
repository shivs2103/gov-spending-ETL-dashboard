-- Clustering

ALTER TABLE fact_spending
CLUSTER BY (state_id, time_id);


-- Time Travel Example

SELECT *
FROM fact_spending
AT (TIMESTAMP => '2026-02-20 10:00:00');


-- Semi-Structured Data (JSON)

SELECT data:scheme_name::string
FROM raw_json_table;


-- Role Based Access Control

CREATE ROLE analyst;
GRANT SELECT ON TABLE fact_spending TO ROLE analyst;


-- Data Masking

CREATE MASKING POLICY mask_amount
AS (val NUMBER) RETURNS NUMBER ->
CASE
    WHEN CURRENT_ROLE() IN ('admin')
    THEN val
    ELSE NULL
END;