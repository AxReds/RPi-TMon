

# RPi-TMon
## Raspberry-Pi Temperature Monitoring (RPi-TMon)

### Copyright (C) 2020 Alessio Rossini <alessior@live.com> 
--- 
The script will display the currente GPU temperature and if above thresholds will send and alert email and display a message. 

To schedule in ***cron*** do the following:

 1. `sudo crontab -e`  <*if it is the first time you run it, choose your editor*>
 2. go to the last line of the file or the first empty one
 3. add the following lines to run the script every 10 mins everyday
		`#Schedule RPi-TMon`


The "**-noconsole**" switch will prevent to display the console messages and will presever Cron from failing launching the command*

> REMINDER: remember to modify the SMTP parameters otherwise you won't > get any email, unless you're Donald Trump



<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA5MDU4NTE2OV19
-->