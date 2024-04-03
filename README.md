bq --location=europe-west2 mk -d \
 --default_table_expiration 3600 \
 --description "This is my dataset." \
 spc_sec_asset_dataset

-- KMS table with schema
bq mk \
 --table \
 --schema kms_schema.json \
 spc_sec_asset_dataset.kms_data_table

bq mk \
 --table \
 --schema sm_schema.json \
 spc_sec_asset_dataset.secret_manager_data_table

gcloud functions deploy process-asset-data \
 --runtime python312 \
 --trigger-topic asset-feed-spc-psb \
 --region europe-west2 \
 --entry-point process_asset_data

[
{ "name": "data", "type": "STRING" },
{ "name": "attributes", "type": "STRING" },
{ "name": "message_id", "type": "STRING" },
{ "name": "subscription_name", "type": "STRING" },
{ "name": "publish_time", "type": "TIMESTAMP" },
{ "name": "asset", "type": "JSON" },
{ "name": "window", "type": "JSON" },
{ "name": "priorAssetState", "type": "STRING" }
]

1. Pass the list to search_json and get the entire dict at once
2. Move the static contents to config.json
3. Secret - map with in a map to capture the replicas
