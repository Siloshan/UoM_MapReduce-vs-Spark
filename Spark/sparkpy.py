import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import SQLContext
from pyspark import SparkContext as sc


S3_DATA_S0URCE_PATH = 's3://aws-logs-359303467698-us-east-1/elasticmapreduce/input/DelayedFlights-updated.csv'
#S3_DATA_0UTPUT_PATH =  's3://mybucketsilo/emr_hive/output/'

conf = pyspark.SparkConf()

def main():
    spark = SparkSession.builder.appName('UOM_spark_app').getOrCreate()
    
    
    #all_data = spark.read.csv(S3_DATA_S0URCE_PATH, header=True)
    all_data = spark.read.format("csv").option("header", "true").load("s3://aws-logs-359303467698-us-east-1/elasticmapreduce/input/DelayedFlights-updated.csv")
    all_data.createOrReplaceTempView("delay_flights")   
    
    
    sc = pyspark.SparkContext.getOrCreate(conf=conf)
    sqlcontext = SQLContext(sc)
    
    
    #df2 = sqlcontext.sql("SELECT 'DayofMonth' from delay_flights").show()
    df = sqlcontext.sql("SELECT Year, avg((CarrierDelay /ArrDelay)*100) from delay_flights GROUP BY Year").show()
    df.show()
    
    #df2.write.format(".csv").save("filtered.csv")
    #df2.write.mode('overwrite').save(S3_DATA_0UTPUT_PATH)
    
    #df2.show()
    print("Script exacuted Successfully")
    

if __name__=='__main__':
    main()