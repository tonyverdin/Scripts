# import urllib library 
from urllib.request import urlopen 
  
# import json 
import json 

def get_json_response(url):
    try:
        response = urlopen(url)
        return json.loads(response.read())
    except Exception as e:
      raise()