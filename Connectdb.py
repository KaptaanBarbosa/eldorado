__author__ = 'shrivas'
import time
import re
import urllib3

from http.cookiejar import CookieJar
import datetime
import sqlite3




conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()


def createDB():
    c.execute("CREATE TABLE knowledgeBase (unix REAL, datestamp TEXT, namedEntity TEXT, relatedWord TEXT)")
    c.commit()




def main():
    try:
        page = 'http://feeds.huffingtonpost.com/huffingtonpost/raw_feed'
        req = Request(page)
        res = urllib3.urlopen(req)        #print sourceCode

        try:
            titles = re.findall(r'<title>(.*?)</title>',res)
            links = re.findall(r'<link.*?href=\"(.*?)\"',res)
            #for title in titles:
                #print title
            for link in links:
                if '.rdf' in link:
                    pass
                else:
                    print('let\'s visit:', link);
                    print(' _____________________________________');
                    linkSource = opener.open(link).read()
                    linesOfInterest = re.findall(r'<p>(.*?)</p>',str(linkSource))
                    print('Content:');
                    for eachLine in linesOfInterest:
                        if '<img width' in eachLine:
                            pass
                        elif '<a href=' in eachLine:
                            pass
                        else:
                            print(eachLine)

                    time.sleep(1)


        except Exception as e:
            print(e.__str__());

    except Exception as e:
        print(e.__str__());
        pass

createDB()