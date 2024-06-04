import json
import pandas as pd


def load_json_data(file):
    with open(file, 'r', encoding="utf8") as f:
        data = json.load(f)
    return data


def dump_json_data(file, data):
    with open(file, "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, default=list)


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def write_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")
        return None


def process_json_query(query_results, df):
    print("Got " + str(len(query_results["results"]["bindings"])) + " results.")
    data = {}
    for item in query_results["results"]["bindings"]:
        for key in item:
            if key not in data:
                data[key] = []
            data[key].append(item[key]["value"])
    df_temp = pd.DataFrame.from_dict(data)
    df = pd.concat([df, df_temp], ignore_index=True)
    return df
