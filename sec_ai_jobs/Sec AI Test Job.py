

if __name__ == "__main__":
    print("Starting Glue Code")
    try:
        main()
        job.commit()
        
        print("Ending Glue Code")
    except Exception as e:
        logger.exception("Glue job failed")
        raise