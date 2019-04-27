
#### * @param string fileName The path to the log file.
#### * @return array The list of URL with the ratio of success.


def analyzeAccessLog(fileName):

    fileObj = open(fileName, "r") 
    listofFileContent =  fileObj.readlines()

    SUCCESS = 200

    totalCnt = 0

    result = {}

    failedrequests = {} 

    for line in listofFileContent:

        responseStr, duration, url,  currentTime, resCode = line.split("|")

        if url in result:  
            result[url] = result[url] + 1

            if ( resCode != SUCCESS ):
                failedrequests[url] = failedrequests[url] + 1

        else:
            result[url] = 1;

            failedrequests[url] = 0;
            if ( resCode != SUCCESS ):
                failedrequests[url] = 1;

            totalCnt = totalCnt + 1;

  

    for key in result:
        result[key] = failedrequests[key] / result[key]



    return result

