-- Add migration script here
INSERT INTO categories (name) VALUES ('game') ON CONFLICT DO NOTHING;
INSERT INTO categories (name) VALUES ('voice') ON CONFLICT DO NOTHING;
INSERT INTO categories (name) VALUES ('website') ON CONFLICT DO NOTHING;

INSERT INTO games (name, image, tag, category) VALUES ('minecraft', 'placeholder', 'placeholder', 'game') ON CONFLICT DO NOTHING;
INSERT INTO games (name, image, tag, category) VALUES ('ark survival ascended', 'placeholder', 'placeholder', 'game') ON CONFLICT DO NOTHING;
