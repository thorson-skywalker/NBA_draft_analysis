-- Joining 2017-18_MBB_SeasonStats and 2018_Draft_Results tables
SELECT ssn."Player",
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
	dft."Player"
FROM "2017-18_MBB_SeasonStats" as ssn
LEFT JOIN "2018_Draft_Results" as dft
ON ssn."Player" = dft."Player"
ORDER BY dft."Pk"