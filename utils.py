import json

def save_json_file(data, path, file_name):
    json_object = json.dumps(data)
    with open(path + file_name + ".json", "w") as outfile:
        outfile.write(json_object)
