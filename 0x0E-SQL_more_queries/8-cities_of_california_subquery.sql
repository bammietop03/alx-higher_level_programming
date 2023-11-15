-- lists all the cities of California that can be found in the hbtn_0d_usa
SELECT cities.id, cities.names FROM cities, state
WHERE cities.state_id = states.iD AND states.name = 'California'
ORDER BY cities.id ASC;
