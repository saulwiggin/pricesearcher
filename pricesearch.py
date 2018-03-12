import falcon, csv, requests, json

class ImportCSV:
    def __init__(self):
        self.products = []
    def grep(file, id):
        with open('products.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                if (row[0] == id):
                    return row
                else:
                    return null
    def fetch():
        url = 'https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json'
        r = requests.get(url);
        products = r.json
        return products

class ProductResource():
   def on_put(self, req, resp, id):
       productImport = ImportCSV()
       product = productImport.grep(id)

       if (product is none):
        JSON = productImport.fetch()
        jsonObject = json.loads(jsonString)

        for id in jsonObject:
            value = jsonObject[id]
            if (value == id):
                product = value

        pass

       resp.media = product

router = MyRouter()
api = falcon.API()
api.add_route('/product/{id}', ProductResource())
