This code was tested using 
Target OS:      Ubuntu 16.04
Python version: python 2.7 

The OS can be anything as not system specific code in use.

Third party libraries
----------------------


Python 2.7  :This is the version of python used in this project.

pip     : for installing
requests: for handling HTTP

lxml: for parsing XML



How to set up the system
--------------------------
use pip


* Install lxml for parsing HTML
sudo apt-get install python-lxml



How the application works
---------------------------

* 1. Reads a list of web pages (HTTP URLs) from a configuration file.
The urls and there contents are saved in an XML file named config.xml. This makes it very easy to modify and make changes. 
    <Configuration>

        <Website>
            <Url>http://www.ewtn.com</Url>
        </Website>
        <Website>
            <Url>http://localhost:12345/</Url>
        </Website>
        <Time>
            <Hour>*/5</Hour>
            <Minute>15</Minute>
            <Day_Of_Week>*</Day_Of_Week>
        </Time>


    </Configuration>

Configuration.py
------------------
The configuation.py has a Configuration class whose contructor accepts the filename. The filename is made a default argument to makle the class more versatile. This can has a method the returns of tuple of list of urls. It also have methods for checking the number of websites. It has the checking period. However, since checking period can set the value of the celery method for running the periodic event. 

* 2. Periodically makes an HTTP request to each page.
HTTPClass.py
The HTTPClass class has method that makes the request to the webpage and store the result of request in a convenient structure.  The getresponse method of the class contains a list of lists of all the request objects and attributes. We also save some logging detail with the request object.


* 3. Measures the time it took for the web server to complete the whole request.
The time is also measured for each request and saved to a suitable structure in the HTTPClass.py file. This done in the getResponses method. We get the time before the request was made and subtract from the time after the request was made.

* 4. Writes a log file that shows the progress of the periodic checks.
The log file is writing when the periodic event is called in the tasks.py file using celery instead of the conventional crontab job. The log file can be done with the logging module in python standard library. However, due to time constraint, it is faster writing to a file. 



crawler
    /logFolder
        log.txt   #log file

    Configuration.py

    /Configuration
        config.xml         

    HTTPClass.py      

    __init__.py 
         
    tasks.py   
 
    loganalysis.py

The logFolder contains the log file.

The template folder houses all the HTML templates required to run the one paged application.

The TestMonitor folder contain the unittest class. Unit test should be seperate from the application as it may fail.

Configuration.py contains the Configuration class. It has a number of methods of which the most important is the list of URLs.
  
config.xml file contains the weblinks and pooling intervals.

loganalysis.py contain code to analyzing the log.

HTTPClass.py  contains a method the get all the required attributes of the response from the result in a computer friendly structure. It also wraps some functions from Configuration.py

   

tasks.py contains all the periodic task. Navigate to the folder and run to start task
$ celery -A tasks worker --loglevel=info

The source codes can be found in a compressed file named crawler.tar.gz

Issues
No unit testing for sake of time.
Open files were not closed. It can be fixed with a with context manager.
requirement.txt file is huge as I was not on virtualenv. It is that of my huge supercomputer.

