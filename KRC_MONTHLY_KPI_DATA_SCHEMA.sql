CREATE TABLE TMWIN.KRC_MONTHLY_KPI_DATA (
  ID VARCHAR(7) NOT NULL UNIQUE,
  MONTH TIMESTAMP,
  MILES INTEGER,
  AVG_DRIVERS INTEGER
)@
GRANT SELECT ON TABLE TMWIN.KRC_MONTHLY_KPI_DATA TO PUBLIC@
GRANT ALL ON TABLE TMWIN.KRC_MONTHLY_KPI_DATA TO TMW_SCRIPTING@
