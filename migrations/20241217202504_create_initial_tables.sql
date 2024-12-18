-- Add migration script here
CREATE TABLE IF NOT EXISTS categories
(
    name       VARCHAR PRIMARY KEY,
    valid_to   TIMESTAMP,
    valid_from TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS games
(
    name       VARCHAR PRIMARY KEY,
    image      VARCHAR   NOT NULL,
    tag        VARCHAR   NOT NULL,
    category   VARCHAR   NOT NULL REFERENCES categories (name),
    valid_to   TIMESTAMP,
    valid_from TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS servers
(
    id                 SERIAL PRIMARY KEY,
    game               VARCHAR   NOT NULL REFERENCES games (name),
    discord_channel_id BIGINT    NOT NULL,
    valid_to           TIMESTAMP,
    valid_from         TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at         TIMESTAMP NOT NULL DEFAULT NOW()
);

