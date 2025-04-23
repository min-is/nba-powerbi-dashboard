CREATE TABLE dim_player (
    player_key BIGINT PRIMARY KEY,
    player_id INT NOT NULL,
    full_name VARCHAR(255),
    position VARCHAR(3),
    height_cm DECIMAL(5,2),
    weight_kg DECIMAL(5,2),
    draft_year SMALLINT,
    birth_date DATE,
    scd_start DATE NOT NULL,
    scd_end DATE,
    current_record BOOLEAN,
    CONSTRAINT unique_player_rec UNIQUE (player_id, scd_start)
);


CREATE TABLE dim_contract_history (
    contract_key BIGINT PRIMARY KEY,
    player_key BIGINT REFERENCES dim_player,
    team_key BIGINT REFERENCES dim_team,
    salary_amount DECIMAL(12,2),
    contract_start DATE,
    contract_end DATE,
    incentives JSONB
);