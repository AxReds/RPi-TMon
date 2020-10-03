#!/usr/bin/env python3
#to make the script executable added the above line (a shebang: a # + a !)
#read the readme file for details

#Raspberry-Pi Temperature Monitoring (RPi-TMon) - v2.0.
#Copyright (C) 2020 Alessio Rossini <alessior@live.com>
#Original source code available at https://github.com/AxReds/RPi-TMon

#
#This program is free software; you can redistribute it and/or modify it under
#the terms of the GNU General Public License as published by the Free Software Foundation;
#either version 2 of the License, or any later version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#See the GNU General Public License for more details
#https://opensource.org/
#
#You should have received a copy of the GNU General Public License along with this program; 
#if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
#
#This improved version starts from the idea of Alexander Bilz https://gist.github.com/lxndrblz
#His original source code is at https://gist.github.com/lxndrblz/27e6ca08363bbc8be994a2f7b1a9d523
#
#Include libraries
import os
import smtplib
from email.mime.text import MIMEText
import sys

#include gpiozero library function to simplify the code
from gpiozero import CPUTemperature


#
# initialize constants
critical = False
high_Temp = 55 #no higher than 70
too_high_Temp = 80 #The Raspberry Pi Foundation recommends that the temperature of your Raspberry Pi device should be below 85 degrees Celsius for it to work properly. That is the maximum limit.
SMTP_ServerName = "smtp.live.com" # if your using Hotmail
SMTP_port = 587
SMTP_account = "donald.trump@whitehouse.gov"
SMTP_password = "BlackLivesMatter"
SMTP_from = "donald.trump@whitehouse.gov"
SMTP_to = "joe.biden@am_the_next_president.com"
no_console_output = "-noconsole"
show_help = "-help"
version = "v2.0"
welcomeMessage = "\nRaspberry-Pi Temperature Monitoring (RPi-TMon) - " + version + ".\n"\
    "Copyright (C) 2020 Alessio Rossini <alessior@live.com>\n\n" \
    "\t|This software is free and comes with ABSOLUTELY NO WARRANTY.\n" \
    "\t|You are welcome to redistribute it under the terms of the\n"\
    "\t|GNU General Public License as published by the Free Software Foundation\n"\
    "\t|either version 2 of the License or any later version.\n"

#
#Define a function that returns current CPU temperature in float
def CPUTempF():
    #Read the temperature from Raspberry PI internal sensor
    cpuTemp = CPUTemperature()
    return(float(cpuTemp.temperature))

#
#Define a function that send emails
def sendMail (sender, recipient, subject, body):
        #
        #Establish an smtp connection
        server = smtplib.SMTP(SMTP_ServerName, SMTP_port) 
        server.ehlo()
        server.starttls()
    
        #
        #Login
        server.login(SMTP_account, SMTP_password)
    
        #
        #Compose the message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        #
        #Send the e-mail
        server.sendmail(SMTP_from, SMTP_to, msg.as_string())
        server.quit()
        return

#
#Read the current temperature
temp = CPUTempF()

#  
#Process command line arguments
#If you schedule the running with Cron use the swtich "-noconsole"
if len(sys.argv) == 1:
    os.system('clear')
    #
    #Interactive Mode
    # Check if the temperature is above high_Temp (you can change this value, but it shouldn't be above 70)
    if temp < high_Temp :
        #a messagge will be displayed to the user but no email will be sent
        print (welcomeMessage + "\n\nEverything is working fine!\n"\
       "Current CPU temperature is: %s'C\n\n" %temp)
    elif temp >= high_Temp and temp <= too_high_Temp:
        print (welcomeMessage + "\n\nWarning!\n"\
        "The actual CPU temperature is: %s\n\n" %temp)
    elif temp >= too_high_Temp:
        print (welcomeMessage + "\n\nCritical Warning!\n"  \
            "The actual CPU temperature is: %s\n\n"
            "Please shut down Raspberry Pi!\n\n" %temp)
else:
    if str(sys.argv[1]) == show_help:
      print (welcomeMessage \
            + "\n\nSyntax: %s [commandline_arguments]:\n"\
            "\n\t-noconsole for silent mode & Cron use\n"\
            "\t-help to show this help\n" %str(sys.argv[0]))
    elif str(sys.argv[1]) == no_console_output: 
      #
      #Non-interactive Mode
      #no console interaction. Email will be sent to the user
        #
        # Check if the temperature is above high_Temp (you can change this value, but it shouldn't be above 70)
        if temp >= high_Temp and temp <= too_high_Temp:
                sendMail (SMTP_from, SMTP_to, \
                "Warning! The CPU temperature is: {} ".format(temp), \
                "Warning! The actual CPU temperature is: {} ".format(temp))
        elif temp >= too_high_Temp:
         #       critical = True
                sendMail (SMTP_from, SMTP_to, \
                    "Critical warning! The CPU temperature is: {} shutting down!!".format(temp), \
                    "Critical warning! The actual CPU temperature is: {} \n\n Shutting down the pi!".format(temp))
                #os.popen('sudo halt')
                print ("sudo halt")
    else:
        print (welcomeMessage \
            + "\n\nType %s -help to show help." %str(sys.argv[0]))