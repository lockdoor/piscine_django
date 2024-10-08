import requests
import dewiki
import json
import sys


def myfunc():
    if len(sys.argv) != 2:
        print ("Error: Require only 1 argument")
        return
    
    key_word = sys.argv[1]

    search_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={key_word}&limit=1&namespace=0&format=json"
    req = requests.get(search_url).json()
    # print (req)
    # try get title
    if not req[1]:
        print (f'{key_word} not found')
        return

    parse_url = f"https://en.wikipedia.org/w/api.php?action=parse&page={key_word}&prop=wikitext&format=json"
    parse_response = requests.get(parse_url).json()
    if "parse" in parse_response:
        # open file to save wikitext
        # wiki_file = open(f'{key_word}.wiki', 'w')
        with open(f'{key_word}.wiki', 'w') as wiki_file:
            wiki_file.write(parse_response["parse"]["wikitext"]["*"])
    else:
        print("Wikitext not found for the page.")

if __name__ == "__main__":
    myfunc()

'''
python3 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirement.txt
'''
