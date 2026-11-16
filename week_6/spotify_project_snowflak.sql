CREATE DATABASE IF NOT EXISTS spotify_db;

CREATE SCHEMA IF NOT EXISTS spotify_db.music;

CREATE WAREHOUSE IF NOT EXISTS spotify_wh
WAREHOUSE_SIZE = 'XSMALL'
AUTO_SUSPEND = 60
AUTO_RESUME = TRUE;

USE WAREHOUSE spotify_wh;

USE SCHEMA spotify_db.music;

USE DATABASE spotify_db;

CREATE OR REPLACE FILE FORMAT spotify_csv_ff
    TYPE = CSV
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    NULL_IF = ('');

    CREATE OR REPLACE TABLE spotify_songs (

    acousticness FLOAT,
    danceability FLOAT,
    duration_ms INT,
    energy FLOAT,
    instrumentalness FLOAT,
    key INT,
    liveness FLOAT,
    loudness FLOAT,
    mode INT,
    speechiness FLOAT,
    tempo FLOAT,
    time_signature INT,
    valence FLOAT,
    target INT,
    song_title STRING,
    artist STRING

);

CREATE OR REPLACE STAGE spotify_stage
FILE_FORMAT = spotify_csv_ff;

DESC TABLE spotify_songs;

SELECT
    CURRENT_DATABASE(),
    CURRENT_SCHEMA(),
    CURRENT_WAREHOUSE(),
    CURRENT_ROLE();

COPY INTO spotify_db.music.spotify_songs
FROM @spotify_db.music.spotify_stage/spotify_data.csv
FILE_FORMAT = (
    FORMAT_NAME = 'spotify_db.music.spotify_csv_ff'
)
ON_ERROR = 'ABORT_STATEMENT';

SELECT *
FROM spotify_db.music.spotify_songs
LIMIT 10;


SELECT COUNT(*)
FROM spotify_db.music.spotify_songs;

-- 1. Which is the longest song released yet? 
-- I converted the duration from milliseconds to minutes(1s = 1000ms:1m = 6000ms)

SELECT
    song_title,
    artist,
    duration_ms,
    ROUND(duration_ms / 60000.0, 2) AS duration_minutes
FROM spotify_songs
ORDER BY duration_ms DESC
LIMIT 1;

-- 2. How many songs has Drake sung? 
SELECT COUNT(*) AS drake_song_count
FROM spotify_songs
WHERE artist = 'Drake';

--  3 List those songs with letter ‘Love’ in them.
-- ILIKE searches without case sensitivity
SELECT
    song_title,
    artist
FROM spotify_songs
WHERE song_title ILIKE '%Love%';

-- 4. Select songs which have a number in them.
-- REGEXP '[0-9]' — finds titles containing a digit from 1 to 9.
SELECT
    song_title,
    artist
FROM spotify_songs
WHERE REGEXP_LIKE(song_title, '.*[1-9][0-9]+.*');

-- 5. You have a bachelorette weekend, which songs would you play the most?

SELECT
    song_title,
    artist,
    danceability,
    energy,
    tempo
FROM spotify_songs
WHERE danceability >= 0.8
  AND energy >= 0.8
ORDER BY danceability DESC, energy DESC
LIMIT 20;

-- 6. In a dance battle, which 3 songs would you choose for a dance off ?
SELECT
    song_title,
    artist,
    danceability,
    energy,
    tempo
FROM spotify_songs
ORDER BY
    (danceability + energy) DESC
LIMIT 3;

-- Which artist has the max songs released?
SELECT
    artist,
    COUNT(*) AS total_songs
FROM spotify_songs
GROUP BY artist
ORDER BY total_songs DESC
LIMIT 1;

-- 8. Make a ‘break-up’ song list >..< 

SELECT
    song_title,
    artist,
    valence,
    energy,
    acousticness
FROM spotify_songs
WHERE valence <= 0.3
ORDER BY valence ASC
LIMIT 20;
