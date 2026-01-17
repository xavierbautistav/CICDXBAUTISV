-- Databricks notebook source
-- MAGIC %python
-- MAGIC dbutils.widgets.removeAll()

-- COMMAND ----------

create widget text storageName default "adlsxbautisv";

-- COMMAND ----------

DROP CATALOG IF EXISTS catalog_xbautisv CASCADE;

-- COMMAND ----------

CREATE CATALOG IF NOT EXISTS catalog_xbautisv;

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.raw;
CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.bronze;
CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.silver;
CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.golden;
CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.exploratory;

CREATE VOLUME IF NOT EXISTS catalog_xbautisv.raw.datasets;

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-raw`
URL 'abfss://raw@${storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credentialxbautisv)
COMMENT 'Ubicación externa para los archivos del raw del Data Lake';

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-bronze`
URL 'abfss://bronze@${storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credentialxbautisv)
COMMENT 'Ubicación externa para los archivos del raw del Data Lake';

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-silver`
URL 'abfss://silver@${storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credentialxbautisv)
COMMENT 'Ubicación externa para los archivos del raw del Data Lake';

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-golden`
URL 'abfss://golden@${storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credentialxbautisv)
COMMENT 'Ubicación externa para los archivos del raw del Data Lake';
