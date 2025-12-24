import sys
import logging
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

if __name__ == "__main__":
    print("Starting Glue Code")
    try:
        main()
        print("Ending Glue Code")
    except Exception as e:
        raise