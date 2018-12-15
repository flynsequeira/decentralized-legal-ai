import json
import urllib.request as urllib



class SearchElastic:

    # Constructor for the class
    def __init__(self, host):
        self.hosturl = host

    def search(self, searchType, searchText):
        result = ""
        url = self.hosturl + "/case" + "_search"
        print('url',  url)
        query_args = self.queryMaker(searchType, searchText)
        print('query',  query_args)
        request = urllib.Request(url, query_args.encode())
        result = urllib.urlopen(request)
        print('result', result)
        parsedresult = json.loads(result.read())
        return parsedresult

    def queryMaker(self, searchType, searchText):
        params = '{}'
        if searchType == 'searchall':
            params = '{"from": 0,"size" : 61,"query":{"query_string":{"query":"' + searchText + '"}}}'
        return params