# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %sql
# MAGIC DROP CATALOG IF EXISTS catalog_xbautisv CASCADE;
# MAGIC
# MAGIC CREATE CATALOG IF NOT EXISTS catalog_xbautisv;
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.raw;
# MAGIC CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.golden;
# MAGIC CREATE SCHEMA IF NOT EXISTS catalog_xbautisv.exploratory;
# MAGIC
# MAGIC CREATE VOLUME IF NOT EXISTS catalog_xbautisv.raw.datasets;
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-raw-prd`
# MAGIC URL 'abfss://raw@adlxbautisvprd.dfs.core.windows.net/'
# MAGIC WITH (STORAGE CREDENTIAL credentialxbautisvprd)
# MAGIC COMMENT 'Ubicación externa para los archivos del raw del Data Lake';
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-bronze-prd`
# MAGIC URL 'abfss://bronze@adlxbautisvprd.dfs.core.windows.net/'
# MAGIC WITH (STORAGE CREDENTIAL credentialxbautisvprd)
# MAGIC COMMENT 'Ubicación externa para los archivos del raw del Data Lake';
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-silver-prd`
# MAGIC URL 'abfss://silver@adlxbautisvprd.dfs.core.windows.net/'
# MAGIC WITH (STORAGE CREDENTIAL credentialxbautisvprd)
# MAGIC COMMENT 'Ubicación externa para los archivos del raw del Data Lake';
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-golden-prd`
# MAGIC URL 'abfss://golden@adlxbautisvprd.dfs.core.windows.net/'
# MAGIC WITH (STORAGE CREDENTIAL credentialxbautisvprd)
# MAGIC COMMENT 'Ubicación externa para los archivos del raw del Data Lake';
