-- Creating Conference_Draft_Data table

CREATE TABLE "Conference_Draft_Data" (
	Pk INT NOT NULL,
   Tm VARCHAR NOT NULL,
	Player1 VARCHAR NOT NULL,
	College VARCHAR NOT NULL
);
SELECT * FROM "Conference_Draft_Data";



-- Creating Conference_NCAATeam_Data table

CREATE TABLE "Conference_NCAATeam_Data" (
	TEAM VARCHAR NOT NULL,
   CONF VARCHAR NOT NULL
);
SELECT * FROM "Conference_NCAATeam_Data";



-- Joining Conference_Draft_Data and Conference_NCAATeam_Data tables

SELECT dft.Pk,
	dft.Tm,
	dft.Player1,
	dft.College,
	team.CONF
INTO "Conference_Data_Final"
FROM "Conference_Draft_Data" as dft
LEFT JOIN "Conference_NCAATeam_Data" as team
ON dft.College = team.TEAM
ORDER BY team.CONF

SELECT * FROM "Conference_Data_Final";