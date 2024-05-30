import os
import yaml

secrets_path = "secrets.yaml"
ENV = bool(os.environ.get('ENV', False))
if ENV:

    apiID = os.environ.get('apiID', "24056535")
    apiHASH = os.environ.get('apiHASH', "449a14964e8a15e70f8c0919266832b1")
    botTOKEN = os.environ.get('botTOKEN', "7453978767:AAHxoTc4XT--FBQq7UCfmLKQjTvHyhWMdwY")

    MongoDB_URI = os.environ.get("MongoDB_URI", "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")
    database = os.environ.get("database", None)
    collection = os.environ.get('userCollection', "users")
    encryption_key = os.environ.get("key", "")

elif os.path.isfile(secrets_path):
    yaml_file = open(secrets_path, 'r')
    yaml_content = yaml.load(yaml_file, Loader=yaml.FullLoader)
    apiID = yaml_content['telegram'][0]['apiID']
    apiHASH = yaml_content['telegram'][1]['apiHASH']
    botTOKEN = yaml_content['telegram'][2]['botTOKEN']

    MongoDB_URI = yaml_content['MongoDB'][0]['URI']
    database = yaml_content['MongoDB'][1]["database"]
    collection = yaml_content['MongoDB'][2]["collection"]

    encryption_key = yaml_content['Encryption'][0]["key"]

else:
    print(
        'This app is not configured correctly. Check README or contact support team.'
    )
    quit(1)
