from supabase_utils.client import supabase_client
import json

def upload_data_to_supabase_bucket(data, supabase_file_path, bucket_name):
    json_data = json.dumps(
        data,
        indent=4,
        ensure_ascii=False
    )

    supabase_client.storage.from_(bucket_name).update(
        supabase_file_path,
        json_data.encode("utf-8"),
        {"content-type": "application/json"}
    )

def download_data_from_supabase_bucket(bucket_file_name, bucket_name):
    '''return a python object of the json in supabase'''
    try:

        response = supabase_client.storage.from_(bucket_name).download(
        bucket_file_name
        )

        training_data = json.loads(response)

        return training_data
    
    except Exception as e:
        print(f"Download failed: {e}")

    

