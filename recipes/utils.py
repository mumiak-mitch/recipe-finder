import requests

def fetch_recipes(query):
    app_id = ''  
    app_key = '' 
    url = f'https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')  
        
    return {}

# Testing
if __name__ == "__main__":
    query = "tea"
    recipes = fetch_recipes(query)
    print(recipes)
