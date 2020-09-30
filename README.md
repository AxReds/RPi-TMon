

# RPi-TMon
## Raspberry-Pi Temperature Monitoring (RPi-TMon)

### Copyright (C) 2020 - Alessio Rossini <alessior@live.com> 
--- 
The script will display the current GPU temperature of your Raspberry-Pi and if above thresholds it will send and alert email and/or display a message. 

The script can be executed as a ***bash*** console command or scheduled in ***cron***.

To run it as a ***bash*** console command, ensure to add execute attribute to the file in your directory by running the following command:

```sh
    $ chmod +x ./RPi-TMon.py  
```

then simply run the command `$ ./RPi-TMon.py`
To schedule in ***cron*** do the following:

 1. `sudo crontab -e`  <*if it is the first time you run it, choose your editor*>
 2. go to the last line of the file or the first empty one
 3. add the following two lines to ***crontab*** to run the script every 10 mins everyday
 
 ```sh
 	#Schedule RPi-TMon
 	*/10 * * * * python /home/pi/RPi-TMon.py -noconsole > /home/pi/log_RPi-TMon.txt
 ```
  

The "**-noconsole**" switch will prevent to display the console messages and will presever Cron from failing launching the command

> ***REMINDER**: remember to modify the SMTP parameters otherwise you won't get any email, unless you're Donald Trump*



<!--stackedit_data:
eyJoaXN0b3J5IjpbMTczMjk4NTk0NiwtMTE4MDc5NzMzOCwxMD
E2NjIzNTE0LDEwNzAzNzI3OV19
-->
