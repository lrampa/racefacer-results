-- racefacer.dbo.racefacer_runs definition

-- Drop table

-- DROP TABLE racefacer.dbo.racefacer_runs;

CREATE TABLE racefacer.dbo.racefacer_runs (
	ID int IDENTITY(1,1) NOT NULL,
	team varchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	last_passing varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	pits int NULL,
	laps int NULL,
	current_line_width decimal(38,17) NULL,
	total_line_duration int NULL,
	CONSTRAINT racefacer_results_pk PRIMARY KEY (ID)
);

