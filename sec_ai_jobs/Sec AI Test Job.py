import sys
import logging
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from func_one import func_one
from func_two import func_two


def main():
    print("========== GLUE GITHUB TEST START ==========")

    func_one()
    func_two()

    print("========== GLUE GITHUB TEST END ==========")

if __name__ == "__main__":
    print("Starting Glue Code")
    try:
        main()
        print("Ending Glue Code")
    except Exception as e:
        raise