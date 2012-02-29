from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

class TestRunner:
    
    def __init__(self):
        test = Test(1, "GETing some webpage")
        self.request = test.wrap(HTTPRequest())
    
    def __call__(self):
        response = self.request.GET("http://espenhh.com/grinder/rocksolid.php")
        print str(response.statusCode) + " " + response.text
