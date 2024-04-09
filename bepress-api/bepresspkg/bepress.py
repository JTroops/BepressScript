import requests
import csv
import json

def bepress(type, pubYear):
    limit = "1000"

    url = 'https://content-out.bepress.com/v2/epublications.marquette.edu/query?document_type="' + type + '"&publication_year=' + pubYear + '&limit=' + limit

    headers = {
        'Access-Control-Allow-Origin':'*',
        'Authorization': 'EOFeFwNE1ZtlGZXMHETLNqBIu2jrXYSTlaq8jXmem3M='
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    cleanData = []
    with open('cleanData.json', 'w') as json_file:
      for i in data["results"]:
        documentTypes = data["results"][data["results"].index(i)]["document_type"]
        for j in documentTypes:
          if type == "thesis":
            if j == "thesis" or j == "Thesis" or j == "Theses" or j == "Thesis - Restricted" or j == "Theses - Restricted":
              cleanData.append(i)
              break
          elif type == "dissertation":
            if j == "dissertation" or j == "Dissertation" or j == "Dissertations" or j == "Dissertation - Restricted":
              cleanData.append(i)
              break

      return json.dump(cleanData, json_file)

    #with open('dirtydata.json', 'w') as json_file:
      #json.dump(data, json_file)
