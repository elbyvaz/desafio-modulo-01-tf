
# nao precisei usar no desafio
# de csv para parquet foi feito no jupyter lab

from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

#creating spark variable
spark = (
    SparkSession
    .builder
    .appName("igti-edc-modulo1-desafio")
    .getOrCreate()    
)

# reading rais 2020 data
rais = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .option("encoding", "latin1")
    .load("s3://desafio-modulo-01/raw/")
)

#transforming to parquet format
(
    rais
    .coalesce(50)
    .write.mode('overwrite')
    .partitionBy('uf')
    .format('parquet')
    .save('s3://desafio-modulo-01/staging/')
)