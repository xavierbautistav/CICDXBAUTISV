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

ruta = f"abfss://{container}@{storageName}.dfs.core.windows.net/compras.csv"

# COMMAND ----------

df_compras = spark.read.option('header', True)\
                        .option('inferSchema', True)\
                        .option('delimiter', ';')\
                        .option('encoding', 'ISO-8859-1')\
                        .csv(ruta)


# COMMAND ----------

compras_schema = StructType(fields=[StructField("id_fila", IntegerType(), False),
                                    StructField("id_pedido", StringType(), False),
                                    StructField("fecha_pedido", DateType(), False),
                                    StructField("fecha_envio", DateType(), False),
                                    StructField("metodo_envio", StringType(), False),
                                    StructField("id_cliente", StringType(), False),
                                    StructField("ciudad", StringType(), False),
                                    StructField("provincia_estado_departamento", StringType(), False),
                                    StructField("pais_region", StringType(), False),
                                    StructField("region", StringType(), False),
                                    StructField("id_producto", StringType(), False),
                                    StructField("ventas", DecimalType(10,2), False),
                                    StructField("cantidad", StringType(), False),
                                    StructField("descuento",  DecimalType(10,2), False)
                                   ])

# COMMAND ----------

# DBTITLE 1,Use user specified schema to load df with correct types
df_compras_final = spark.read\
.option('header', True)\
.option('delimiter', ';')\
.option('encoding', 'ISO-8859-1')\
.schema(compras_schema)\
.csv(ruta)

# COMMAND ----------

# DBTITLE 1,select only specific cols
compras_selected_df = df_compras_final.select(col("id_fila"),
                                                col("id_pedido"),
                                                col("fecha_pedido"),
                                                col("fecha_envio"),
                                                col("metodo_envio"),
                                                col("id_cliente"),
                                                col("ciudad"),
                                                col("provincia_estado_departamento"),
                                                col("pais_region"),
                                                col("region"),
                                                col("id_producto"),
                                                col("ventas"),
                                                col("cantidad"),
                                                col("descuento")
)

# COMMAND ----------

compras_renamed_df = compras_selected_df.withColumnRenamed("id_fila", "id_fila") \
                                            .withColumnRenamed("id_pedido", "id_pedido") \
                                            .withColumnRenamed("fecha_pedido", "fecha_pedido") \
                                            .withColumnRenamed("fecha_envio", "fecha_envio") \
                                            .withColumnRenamed("metodo_envio", "metodo_envio") \
                                            .withColumnRenamed("id_cliente", "id_cliente") \
                                            .withColumnRenamed("ciudad", "ciudad") \
                                            .withColumnRenamed("provincia_estado_departamento", "provincia") \
                                            .withColumnRenamed("pais_region", "pais") \
                                            .withColumnRenamed("region", "region") \
                                            .withColumnRenamed("id_producto", "id_producto") \
                                            .withColumnRenamed("ventas", "monto_ventas") \
                                            .withColumnRenamed("cantidad", "monto_cantidad") \
                                            .withColumnRenamed("descuento", "monto_descuento")
                                            

# COMMAND ----------

# DBTITLE 1,Add col with current timestamp 
compras_final_df = compras_renamed_df.withColumn("fecha_carga",current_timestamp())

# COMMAND ----------

spark.sql(f"DROP TABLE IF EXISTS {catalogo}.{esquema}.compras")

# COMMAND ----------

compras_final_df.write.mode("overwrite").saveAsTable(f"{catalogo}.{esquema}.compras")
