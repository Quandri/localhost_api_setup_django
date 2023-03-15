from urllib import request
"""If we use urllib and not requests, we should not install requests in the setup.py

The main logic:
    - IDEA: copy this func to (...)_helpers.py and import it into setup.py to set it instead of the model into install_requires; 
    - online_source variable attributed in the func is to give a link if localhost api is not working, so the server can 
      download the model from github;
    - if localhost api works (as it should), the model will be taken directly from the host server without any need
      to connect to internet
      
    - This api we can also modify and use for other installings in the setup.py if any similar issue comes up for other
      libraries or files
"""


def define_source(online_source="en-core-web-lg @ https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.4.1/en_core_web_lg-3.4.1-py3-none-any.whl") -> str:
    try:
        response = request.urlopen("http://localhost/en_spacy_model/?format=json")
        parsed_path = eval(response.read().decode())["path"]
        if isinstance(parsed_path, str):
            whole_path = "en-core-web-lg @ " + parsed_path
            return whole_path
        else:
            raise ValueError
    except Exception:
        return online_source


print(define_source())
