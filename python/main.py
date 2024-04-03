from google.cloud import bigquery
import base64
import json


def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def search_json(json_obj, target_list, results):

    def _search_json(obj, target_list):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key in target_list:
                    results[key] = value
                    target_list.remove(key)
                else:
                    _search_json(value, target_list)
        elif isinstance(obj, list):
            for item in obj:
                _search_json(item, target_list)

    _search_json(json_obj, target_list)
    return results


def process_asset_data(event, context):
    client = bigquery.Client()
    dataset_id = "spc_sec_asset_dataset"

    # Get the Pub/Sub message data
    pubsub_message = base64.b64decode(event["data"]).decode("utf-8")
    asset_data = json.loads(pubsub_message)
    print("asset_data", asset_data)
    insert_data_statement = {}

    config = load_json("config.json")
    results = {}

    if asset_data["asset"]["assetType"] == "cloudkms.googleapis.com/CryptoKey":
        insert_data_statement = search_json(asset_data, config["kms_schema"], results)
        table_id = "kms_data_table"
    else:
        insert_data_statement = search_json(asset_data, config["sm_schema"], results)
        table_id = "secret_manager_data_table"

    print("insert_data_statement :::", insert_data_statement)

    # Get the dataset reference
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    table = client.get_table(table_ref)

    # Insert row into BigQuery table
    errors = client.insert_rows(table, [insert_data_statement])

    if errors:
        print(f"Errors: {errors}")
    else:
        print("Data successfully inserted into BigQuery.")
