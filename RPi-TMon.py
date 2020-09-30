#!/usr/bin/env python2
#to make the script executable added the above line (a shebang: a # + a !)
#read the readme file for details

#Raspberry-Pi Temperature Monitoring (RPi-TMon) - v1.0.
##Copyright (C) 2020 Alessio Rossini <alessior@live.com>
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
#Original source code at https://gist.github.com/lxndrblz/27e6ca08363bbc8be994a2f7b1a9d523
 

#Include libraries
import os
import smtplib
from email.mime.text import MIMEText
import sys

#
# initialize constants
critical = False
high_Temp = 60 #no higher than 70
too_high_Temp = 80
SMTP_ServerName = "smtp.live.com" # if your using Hotmail
SMTP_port = 587
SMTP_account = "donald.trump@whitehouse.gov"
SMTP_password = "BlackLivesMatter"
SMTP_from = "donald.trump@whitehouse.gov"
SMTP_to = "Joe.Biden@amthenewpresident.com"
no_console_output = "-noconsole"
show_help = "help"


#
#Define a function that returns the current CPU-Temperature with this defined function
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

#
#Convert temperature value into a float number
temp = float(getCPUtemperature())


#  
# If you schedule the running with Cron use the swtich "-noconsole"
# otherwise Cron will endlessy send you an email for any command that returns "any" output 
#if str(sys.argv[1]) != no_console_output:
if len(sys.argv) == 1:
    os.system('clear')
    print (\
    "\nRaspberry-Pi Temperature Monitoring (RPi-TMon) - v1.0.\n"\
    "Copyright (C) 2020 Alessio Rossini <alessior@live.com>\n\n" \
    "\t|This software is free and comes with ABSOLUTELY NO WARRANTY.\n" \
    "\t|You are welcome to redistribute it under the terms of the\n"\
    "\t|GNU General Public License as published by the Free Software Foundation\n"\
    "\t|either version 2 of the License or any later version.\n"\
    "\n\nEverything is working fine!\n"\
    "Current GPU temperature is: %s\n\n" %getCPUtemperature())
else:
    if str(sys.argv[1]) == no_console_output: 
      #do nothing
      no_console_output
    elif str(sys.argv[1]) == show_help:
      print ("\nRaspberry-Pi Temperature Monitoring (RPi-TMon) - v1.0.\n"\
            "Copyright (C) 2020 Alessio Rossini <alessior@live.com>\n\n"\
            "Use RPi-TMon.py with commandline argument -noconsole for silent mode & Cron use.\n\n")
   


#
# Check if the temperature is above high_Temp (you can change this value, but it shouldn't be above 70)
if (temp > high_Temp):
    if temp > too_high_Temp:
        critical = True
        subject = "Critical warning! The temperature is: {} shutting down!!".format(temp)
        body = "Critical warning! The actual temperature is: {} \n\n Shutting down the pi!".format(temp)
    else:
        subject = "Warning! The temperature is: {} ".format(temp)
        body = "Warning! The actual temperature is: {} ".format(temp)
 

    # Enter your smtp Server-Connection
    server = smtplib.SMTP(SMTP_ServerName, SMTP_port) 
    server.ehlo()
    server.starttls()
    
    # Login
    server.login(SMTP_account, SMTP_password)
    
    #Compose the message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_from
    msg['To'] = SMTP_to

    #Send the e-mail
    server.sendmail(SMTP_from, SMTP_to, msg.as_string())
    server.quit()
    
    #If critical, shut down the pi
    if critical:
        #print("Warning! The actual temperature is: %f" %(temp))
        os.popen('sudo halt')
