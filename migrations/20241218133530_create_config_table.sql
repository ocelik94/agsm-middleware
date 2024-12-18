-- Add migration script here
CREATE TABLE IF NOT EXISTS configs
(
    key        VARCHAR PRIMARY KEY,
    value      VARCHAR,
    valid_to   TIMESTAMP,
    valid_from TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);