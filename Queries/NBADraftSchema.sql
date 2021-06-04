-- Joining 07-19_MBB_Season_Stats and 07-19_NBA_Draft_Results tables
SELECT ssn."#",
	ssn."player",
	ssn."team",
	ssn."gp",
	ssn."mpg",
	ssn."fgm",
	ssn."fga",
	ssn."FG%",
	ssn."3PM",
	ssn."3PA",
	ssn."3P%",
	ssn."ftm",
	ssn."fta",
	ssn."FT%",
	ssn."tov",
	ssn."pf",
	ssn."orb",
	ssn."drb",
	ssn."rpg",
	ssn."apg",
	ssn."spg",
	ssn."bpg",
	ssn."ppg",
	ssn."season_year",
	dft."pk",
	dft."player1",
	dft."draft_year"
INTO "07-19_MBB_StatsAndDraft"
FROM "07-19_MBB_Season_Stats" as ssn
LEFT JOIN "07-19_NBA_Draft_Results" as dft
ON ssn."player" = dft."player1"
ORDER BY dft."pk"

SELECT * FROM "07-19_MBB_StatsAndDraft";


-- Joining 07-20_MBB_Season_Stats and 07-20_NBA_Draft_Results tables
SELECT ssn."#",
	ssn."player",
	ssn."team",
	ssn."gp",
	ssn."mpg",
	ssn."fgm",
	ssn."fga",
	ssn."FG%",
	ssn."3PM",
	ssn."3PA",
	ssn."3P%",
	ssn."ftm",
	ssn."fta",
	ssn."FT%",
	ssn."tov",
	ssn."pf",
	ssn."orb",
	ssn."drb",
	ssn."rpg",
	ssn."apg",
	ssn."spg",
	ssn."bpg",
	ssn."ppg",
	ssn."season_year",
	dft."pk",
	dft."player1",
	dft."draft_year"
INTO "07-20_MBB_StatsAndDraft"
FROM "07-20_MBB_Season_Stats" as ssn
LEFT JOIN "07-20_NBA_Draft_Results" as dft
ON ssn."player" = dft."player1"
ORDER BY dft."pk"

SELECT * FROM "07-20_MBB_StatsAndDraft";