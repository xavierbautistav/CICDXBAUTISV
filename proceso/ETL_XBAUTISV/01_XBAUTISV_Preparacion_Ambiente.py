# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %sql
# MAGIC DROP CATALOG IF EXISTS xbautisv_prd CASCADE;
# MAGIC
# MAGIC CREATE CATALOG IF NOT EXISTS xbautisv_prd;
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS xbautisv_prd.raw;
# MAGIC CREATE SCHEMA IF NOT EXISTS xbautisv_prd.bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS xbautisv_prd.silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS xbautisv_prd.golden;
# MAGIC CREATE SCHEMA IF NOT EXISTS xbautisv_prd.exploratory;
# MAGIC
# MAGIC CREATE VOLUME IF NOT EXISTS xbautisv_prd.raw.datasets;
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
