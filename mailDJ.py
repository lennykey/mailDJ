#!/home/mars/python27/bin/python
# _*_ coding: utf-8 _*_

import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main(): 
    logging.basicConfig(level = logging.INFO)
    log = logging.getLogger("mailDJ")
    
    dataFile = open('addressees.csv')
    dataFileLines = dataFile.readlines() 
    dataFile.close()
    
    htmlFile = open('mail.html')
    myMail = htmlFile.read()
    htmlFile.close()
    
    s = smtplib.SMTP('mail.yourDomaim.com')
    s.login('user@yourDomain.com', 'password')
    
    for line in dataFileLines:
        
        msg = MIMEMultipart('alternative')
        
        test = line.split(',')
        log.debug(myMail)
        #print myMail
        myMail2 = myMail.replace('##forename##', test[0])
        myMail2 = myMail2.replace('##surname##', test[1])
       
        part1 = MIMEText(myMail2, 'html')
        msg.attach(part1)
        #print myMail2
        log.info(myMail2)
        #print test
        log.debug(test)
        s.sendmail('sender@yourDomain.com', test[2], 'From: Blah\r\nTo:Foo\r\nSubject:Your Subject Here\r\n' + msg.as_string())

    s.quit()

if __name__=="__main__":
    main() 
