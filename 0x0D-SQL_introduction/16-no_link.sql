-- Lists descending `score`s their `name`s in `second_table`, unless no `name`.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
