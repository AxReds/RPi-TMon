# RPi-TMon
Raspberry-Pi Temperature Monitoring (RPi-TMon)
Copyright (C) 2020 Alessio Rossini <alessior@live.com>

The script will display the currente GPU temperature and if above thresholds will send and alert email and display a message.


To schedule in Cron do the following
  sudo crontab -e
  <if it is the first time you run it, choose your editor>
  go to the last line of the file or the first empty one
  add the following lines to run the script every 10 mins everyday
  #Schedule RPi-TMon
  */10 * * * * python /home/pi/RPi-TMon.py -noconsole > /home/pi/log_RPi-TMon.txt


The "-noconsole" switch will prevent to display the console messages and will presever Cron from failing launching the command

REMINDER: remember to modify the SMTP parameters otherwise you won't get any email, unless you're Donald Trump

