from HTTPClass import HTTPClass
from celery import Celery
from celery.task.schedules import crontab  
from celery.decorators import periodic_task 

celery = Celery('tasks', broker='amqp://guest@localhost//') 

class LoadEvent:	

    def __init__(self , xmlFileName = "configuration/config.xml"):
        self.myhttp = HTTPClass(xmlFileName) #create the HTTP  object


    def logEvents(self, filename = "logFolder/log.txt"):
        #save content of monitorObjList to a log file
        logfile = open(filename, 'a')      #append the file to prevent overwriting   
        for monObj in self.myhttp.getResponses( ):
            #write to file in the order of response object, duration, url,  current time, result code
            wordString = "{0} | {1} | {2} | {3} | {4}\n".format(monObj[0], monObj[1], monObj[2], monObj[3], monObj[4])
            logfile.write(wordString)
        logfile.close() 


    def getCheckingPeriod(self):
        return self.myhttp.getCheckingPeriod( )


event = LoadEvent() 
n_hour, n_minute, n_day_of_week = event.getCheckingPeriod( )

@periodic_task(run_every=crontab(hour=n_hour, minute=n_minute, day_of_week=n_day_of_week))  
def PerformCheck():
    event = LoadEvent()
    event.logEvents()

    
