import requests
import pprint


class Query:

    def __init__(self, setQuery:str,sort:str,order:str,perPage:int,page:int) ->None:
        self.url ="https://api.github.com/search/repositories"
        self.headers = {"Authorization" : open("githubAPI\githubkey").readline()}
        self.params= {
            "q" : setQuery,
            "per_page" : perPage,
            "page" : page
        }
        self.contains = set()

    def loadSet(self)->None:
        with open('githubAPI\githubLink.txt','r') as file:
            self.contains = {link.strip() for link in file.readlines()}

    
    def request(self)->requests.Response:
        return requests.get(self.url,headers=self.headers,params=self.params)
    
    def writeToFile(self) -> None:
        response=self.request()
        if response.status_code == 200:
            data = response.json()
            with open("githubAPI\githubLink.txt",'a+') as file: 
                for user in data['items']:
                    if not (user['html_url'] in self.contains):
                        file.write(user['html_url'] + '\n')
                        self.contains.add(user['html_url'])
                    
        else:
            print(f"Error: {response.status_code}, {response.text}")


def main()->None:
    query = Query("leetcode in:name stars:<10 forks:<10","stars","asc",5,4)
    query.loadSet()
    query.writeToFile()
    
    

if __name__=='__main__':
    main()
        