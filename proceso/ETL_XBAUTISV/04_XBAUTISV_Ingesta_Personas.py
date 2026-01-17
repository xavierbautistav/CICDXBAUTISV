# Databricks notebook source
dbutils.widgets.removeAll()

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

dbutils.widgets.text("container", "raw")
dbutils.widgets.text("catalogo", "catalog_xbautisv")
dbutils.widgets.text("esquema", "bronze")
dbutils.widgets.text("storageName", "adlsxbautisv")

# COMMAND ----------

container = dbutils.widgets.get("container")
catalogo = dbutils.widgets.get("catalogo")
esquema = dbutils.widgets.get("esquema")
storageName = dbutils.widgets.get("storageName")

ruta = f"abfss://{container}@{storageName}.dfs.core.windows.net/personas.csv"

# COMMAND ----------

df_personas = spark.read.option('header', True)\
                        .option('inferSchema', True)\
                        .option('delimiter', ';')\
                        .option('encoding', 'ISO-8859-1')\
                        .csv(ruta)


# COMMAND ----------

personas_schema = StructType(fields=[StructField("region", StringType(), False),
                                     StructField("gerente_regional", StringType(), True)
])

# COMMAND ----------

# DBTITLE 1,Use user specified schema to load df with correct types
df_personas_final = spark.read\
.option('header', True)\
.option('delimiter', ';')\
.option('encoding', 'ISO-8859-1')\
.schema(personas_schema)\
.csv(ruta)

# COMMAND ----------

# DBTITLE 1,select only specific cols
personas_selected_df = df_personas_final.select(col("region"), 
                                                col("gerente_regional"))

# COMMAND ----------

personas_renamed_df = personas_selected_df.withColumnRenamed("region", "region") \
                                            .withColumnRenamed("gerente_regional", "gerente_regional")

# COMMAND ----------

# DBTITLE 1,Add col with current timestamp 
personas_final_df = personas_renamed_df.withColumn("fecha_carga",current_timestamp())

# COMMAND ----------

spark.sql(f"DROP TABLE IF EXISTS {catalogo}.{esquema}.personas")

# COMMAND ----------

personas_final_df.write.mode("overwrite").saveAsTable(f"{catalogo}.{esquema}.personas")
