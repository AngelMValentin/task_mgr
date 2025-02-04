
-- How to drop tables:
-- DROP TABLE task;

-- Create out table:
CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64),
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

INSERT INTO task (
    name, 
    summary,
    description 
) VALUES
(
    "Walk the dog",
    "Take Fido out for a stroll",
    "Make sure you go three laps around the park"
),
(
    "Wash dishes",
    "All the dishes must be washed before 10pm",
    "Make sure to use the fancy new dish soap"
),
(
    "Buy groceries",
    "Go to the supermarket and buy groceries",
    "We need: eggs, bacon and tomatoes"
)