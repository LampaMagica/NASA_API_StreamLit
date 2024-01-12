import function as fk

with open('secret/api_secret.txt') as api_file:
    api = api_file.read()

data = fk.get_nasa_content(api)

fk.web_page(data.get('title'),data.get('hdurl'),data.get('explanation'))
