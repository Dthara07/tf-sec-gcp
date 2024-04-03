import json

def json_process():
  kms_row_dict = {}
  with open('kms.json') as json_file:
    kms_data = json.load(json_file)
    asset_res_data = kms_data["asset"]["resource"]
    
    kms_row_dict["name"] = kms_data["asset"]["name"]
    kms_row_dict["assetType"] = kms_data["asset"]["name"]
    kms_row_dict["location"] = asset_res_data["location"]
    kms_row_dict["parent"] = asset_res_data["parent"]
    kms_row_dict["state"] = asset_res_data["data"]["primary"]["state"]
    kms_row_dict["createTime"] = asset_res_data["data"]["primary"]["createTime"]
    kms_row_dict["rotationPeriod"] = asset_res_data["data"]["rotationPeriod"]
    kms_row_dict["nextRotationTime"] = asset_res_data["data"]["nextRotationTime"]
    kms_row_dict["destroyScheduledDuration"] = asset_res_data["data"]["destroyScheduledDuration"]
    kms_row_dict["nextRotationTime"] =  asset_res_data["data"]["primary"]["protectionLevel"]
    kms_row_dict["nextRotationTime"] =  asset_res_data["data"]["primary"]["algorithm"]
    kms_row_dict["nextRotationTime"] =  asset_res_data["data"]["purpose"]
    kms_row_dict["version"] =  asset_res_data["data"]["primary"]["name"]
    
    print('kms_row_dict', kms_row_dict)



json_process()