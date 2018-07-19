import requests, id

def get_html_body() :
    r = requests.get(id.url)
    r_decoded = r.content.decode('utf-8')
    return r_decoded
