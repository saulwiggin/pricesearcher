import falcon, csv, requests, json

class MyRouter(object):
    def add_route(self, uri_template, method_map, resource):
        """Adds a route between URI path template and resource.

        Args:
            uri_template (str): The URI template to add.
            method_map (dict): A method map obtained by calling
                falcon.routing.create_http_method_map.
            resource (object): Instance of the resource class that
                will handle requests for the given URI.
        """

    def find(self, uri, req=None):
        """Search for a route that matches the given partial URI.

        Args:
            uri(str): The requested path to route.

        Keyword Args:
             req(Request): The Request object that will be passed to
                the routed responder. The router may use `req` to
                further differentiate the requested route. For
                example, a header may be used to determine the
                desired API version and route the request
                accordingly.

                Note:
                    The `req` keyword argument was added in version
                    1.2. To ensure backwards-compatibility, routers
                    that do not implement this argument are still
                    supported.

        Returns:
            tuple: A 4-member tuple composed of (resource, method_map,
                params, uri_template), or ``None`` if no route matches
                the requested path.

        """
        
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
       print id
       #deliver product from csv
       # productImport = ImportCSV()
       #product = productImport.grep(id)

       # if (product is none):
       #  #JSON = productImport.fetch()
       #  jsonObject = json.loads(jsonString)
       #
       #  for id in jsonObject:
       #      value = jsonObject[id]
       #      if (value == id):
       #          product = value
       #
       #  pass
       #
       # resp.media = product
       # deliver product from api

router = MyRouter()
api = falcon.API(router=router)
api.add_route('/product/{id}', ProductResource())
