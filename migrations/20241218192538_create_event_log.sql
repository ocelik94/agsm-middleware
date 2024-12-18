-- Add migration script here
CREATE TABLE IF NOT EXISTS events
(
    id         SERIAL PRIMARY KEY,
    event      VARCHAR   NOT NULL,
    event_type VARCHAR          DEFAULT 'generic',
    time       TIMESTAMP NOT NULL DEFAULT NOW()
);