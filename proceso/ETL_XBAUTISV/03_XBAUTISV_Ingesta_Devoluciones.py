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

ruta = f"abfss://{container}@{storageName}.dfs.core.windows.net/devoluciones.csv"

# COMMAND ----------

df_devoluciones = spark.read.option('header', True)\
                        .option('inferSchema', True)\
                        .option('delimiter', ';')\
                        .option('encoding', 'ISO-8859-1')\
                        .csv(ruta)


# COMMAND ----------

devoluciones_schema = StructType(fields=[StructField("id_pedido", StringType(), False),
                                     StructField("devuelto", StringType(), True)
])

# COMMAND ----------

# DBTITLE 1,Use user specified schema to load df with correct types
df_devoluciones_final = spark.read\
.option('header', True)\
.option('delimiter', ';')\
.option('encoding', 'ISO-8859-1')\
.schema(devoluciones_schema)\
.csv(ruta)

# COMMAND ----------

# DBTITLE 1,select only specific cols
devoluciones_selected_df = df_devoluciones_final.select(col("id_pedido"), 
                                                col("devuelto"))

# COMMAND ----------

devoluciones_renamed_df = devoluciones_selected_df.withColumnRenamed("id_pedido", "id_pedido") \
                                            .withColumnRenamed("devuelto", "pedido_devuelto")

# COMMAND ----------

# DBTITLE 1,Add col with current timestamp 
devoluciones_final_df = devoluciones_renamed_df.withColumn("fecha_carga",current_timestamp())

# COMMAND ----------

spark.sql(f"DROP TABLE IF EXISTS {catalogo}.{esquema}.devoluciones")

# COMMAND ----------

devoluciones_final_df.write.mode("overwrite").saveAsTable(f"{catalogo}.{esquema}.devoluciones")
