import sys
import auxiliar as aux
from SPARQLWrapper import SPARQLWrapper, CSV, JSON
import pandas as pd

endpoint_url = "https://query.wikidata.org/sparql"  # Endpoint

count_query = aux.read_file("./queries/count")

offset_query = aux.read_file("./queries/offset")  # Offset MUST be coded as {{w}}
offset = 25000  # According to query


def get_results(endpoint_url, query, format):
    user_agent = "Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(format)
    return sparql.query().convert()

def query():
    df = pd.DataFrame()
    count_results = get_results(endpoint_url, count_query, JSON)


    count = count_results["results"]["bindings"][0]['subsetting_size']['value']
    print(count)

    for i in range(0, int(count) + offset, offset):
        print("Query with offset " + str(i))
        offseted_query = offset_query.replace("{{w}}", str(i))
        query_results = get_results(endpoint_url, offseted_query, JSON)
        df = aux.process_json_query(query_results, df)

    df.to_csv("./results.csv")


if __name__ == "__main__":
    query()
