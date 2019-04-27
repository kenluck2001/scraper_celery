from Configuration import Configuration
import time
import requests
from datetime import datetime
import requests  #library for HTTP
import lxml.html  #library for parsing HTML


class HTTPClass:

    def __init__(self, xmlFileName = "configuration/config.xml"):
        """ Initializes the Cofiguration class """
        self.conf = Configuration(xmlFileName) #create the configuration object

    def __getCurrentTime(self): #make method private
        return str(datetime.now())

    def __getResponseStatus(self, res):
        """ This gets the status """
        status = None 
        if res.status_code == requests.codes.ok:
            status = "Success"

        if res.status_code == 404:
            #Not Found
            status = "Not Found"

        if res.status_code == 408:
            #Request Timeout
            status = "Request Timeout"

        if res.status_code == 410:
            #Gone no longer in server
            status = "Not ON Server"

        if res.status_code == 503:
            #Website is temporary unavailable for maintenance
            status = "Temporary Unavailable"

        if res.status_code == 505:
            #HTTP version not supported
            status = "HTTP version not supported"

        return status, res.status_code


    def getResponses(self):
        """ get all the response object attributes in a suitable structure """
        propertyList = []
        url_content = self.conf.MapUrlToContent()

        for url in url_content:
            start_time = time.time()
            #create a Response object //remove all the required attributes to be logged

            try:
                res = requests.get(url)     #make a get request to know status code
                final_time = time.time()
                real_time = final_time - start_time #duration of request
                #get Http response status
                resStatus, rescode = self.__getResponseStatus(res)
                output = resStatus,real_time, url , self.__getCurrentTime(), rescode #response object, duration, url,  current time, result code
                propertyList.append(output)
            except ValueError:
                print "This Url is not valid: ", url
            except ConnectionError: 
                print "DNS failure, refused connection"
            except HTTPError:
                print "Invalid HTTP response"  
            except TooManyRedirects:
                print "Exceeds the configured number of maximum redirections"

        return propertyList


    def getCheckingPeriod(self):
        return self.conf.getCheckingPeriod()

    def numberOfWebSites(self):
        return self.conf.numberOfWebSites()



if __name__ == '__main__' :
    xmlFileName = "config.xml"
    myhttp = HTTPClass()
    print myhttp.getResponses( )
    print myhttp.getCheckingPeriod( )
    print myhttp.numberOfWebSites( )
        

