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
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-raw`
# MAGIC URL 'abfss://raw@adlsxbautisv.dfs.core.windows.net/'
# MAGIC WITH (STORAGE CREDENTIAL credentialxbautisv)
# MAGIC COMMENT 'Ubicación externa para los archivos del raw del Data Lake';
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-bronze`
# MAGIC URL 'abfss://bronze@adlsxbautisv.dfs.core.windows.net/'
# MAGIC WITH (STORAGE CREDENTIAL credentialxbautisv)
# MAGIC COMMENT 'Ubicación externa para los archivos del raw del Data Lake';
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-silver`
# MAGIC URL 'abfss://silver@adlsxbautisv.dfs.core.windows.net/'
# MAGIC WITH (STORAGE CREDENTIAL credentialxbautisv)
# MAGIC COMMENT 'Ubicación externa para los archivos del raw del Data Lake';
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-golden`
# MAGIC URL 'abfss://golden@adlsxbautisv.dfs.core.windows.net/'
# MAGIC WITH (STORAGE CREDENTIAL credentialxbautisv)
# MAGIC COMMENT 'Ubicación externa para los archivos del raw del Data Lake';
