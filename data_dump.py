import pymongo
import pandas as pd
import json
from dotenv import load_dotenv

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://DivyankR:Agra282001@cluster0.wfihpup.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"
DATAFILE_PATH = "/config/workspace/aps_failure_training_set1.csv"


if __name__ == "__main__":
    df = pd.read_csv(DATAFILE_PATH)
    print(f"Rows and Columns:{df.shape}")

    # convert the dataframe to json so that we can dump records in mongdb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # insert converted json records into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
