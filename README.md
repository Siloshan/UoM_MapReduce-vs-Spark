# MapReduce vs. Spark
## Hadoop MapReduce and Apache Spark are two widely recognized big data architectures.They provide a robust platform for processing large amounts of data and integrating machine learning applications. So, this repository refers the time comparison of the both architechtrues on how those react on queries.

#### For analysing we have used hive which uses hiveQL statement which runs over MapReduce and spark which uses Spark-SQL which runs over spark framework. 

## Data set:
### To compare each processes, below data set was used which is available in the kaggle. 
### https://www.kaggle.com/code/adveros/flight-delay-eda-exploratory-data-analysis/data
##### The airlines market has been faced losses due to the flight delay and there are many reasons for delaying a flight. In this Analysis, you need to analyse the various delay happens in airlines per year and run the queries as follows.  Data set has 1000 rows.

#### Below queries were exacuted in the both setups and all experiment result were listed belows.


 
###### 1. Year wise carrier delay from 2003-2010
###### 2. Year wise NAS delay from 2003-2010
###### 3. Year wise Weather delay from 2003-2010
###### 4. Year wise late aircraft delay from 2003-2010
###### 5. Year wise security delay from 2003-2010

### Hadoop map reduced and Apache Spark resluts for each queries:
###### 1. Year wise carrier delay from 2003-2010

![This is an image](./MapReduce/images/image1.png| width=100)
