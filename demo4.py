import requests
import fire

def scrape(url, timeout):
    response = requests.get(url, timeout=timeout)
    print(response.text)
    
    
if __name__ == '__main__':
    fire.Fire(scrape)