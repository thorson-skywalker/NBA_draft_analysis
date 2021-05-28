-- Joining MBB_Season_Stats and NBA_Draft_Results tables
SELECT ssn."#",
	ssn."Player",
	ssn."Team",
	ssn."GP",
	ssn."MPG",
	ssn."FGM",
	ssn."FGA",
	ssn."FG%",
	ssn."3PM",
	ssn."3PA",
	ssn."3P%",
	ssn."FTM",
	ssn."FTA",
	ssn."FT%",
	ssn."TOV",
	ssn."PF",
	ssn."ORB",
	ssn."DRB",
	ssn."RPG",
	ssn."APG",
	ssn."SPG",
	ssn."BPG",
	ssn."PPG",
	dft."Pk",
	dft."Player1"
INTO "MBB_StatsAndDraft"
FROM "MBB_Season_Stats" as ssn
LEFT JOIN "NBA_Draft_Results" as dft
ON ssn."Player" = dft."Player1"
ORDER BY dft."Pk"

SELECT * FROM "MBB_StatsAndDraft";