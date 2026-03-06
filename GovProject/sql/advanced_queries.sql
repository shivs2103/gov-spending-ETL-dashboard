-- CTE Example

WITH state_total AS (
    SELECT state_id, SUM(amount_spent) AS total_spent
    FROM fact_spending
    GROUP BY state_id
)
SELECT *
FROM state_total
ORDER BY total_spent DESC;


-- Window Function Example

SELECT 
    state_id,
    scheme_id,
    amount_spent,
    RANK() OVER (PARTITION BY state_id ORDER BY amount_spent DESC) AS rank_in_state
FROM fact_spending;


-- Indexing

CREATE INDEX idx_state ON fact_spending(state_id);
CREATE INDEX idx_time ON fact_spending(time_id);


-- Partitioning (Conceptual)

-- Example for large datasets
-- PARTITION BY RANGE (year);