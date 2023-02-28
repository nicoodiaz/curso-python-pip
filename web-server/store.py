import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    
    # Obtener informacion, estado HTTP
    print(r.status_code)
    
    # Saber cual es el retornoy que info nos da la API
    print(r.text)
    print(type(r.text))
    
    # Para transformarlo en una lista directamente y poder iterar
    categories = r.json()
    for category in categories:
        print(category['name'])
    print(type(categories))