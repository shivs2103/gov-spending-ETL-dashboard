from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("GovtStreamingDemo") \
    .getOrCreate()

# Simulated streaming source
stream_df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 1) \
    .load()

query = stream_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()