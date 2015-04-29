import RPi.GPIO as GPIO
import datetime
import time
import sqlite3



WindCount=0
mph=0
Wind_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(Wind_PIN, GPIO.IN)

sqlite_file = 'windlog.db'    # name of the sqlite database file
table_name = 'wind'  # name of the table to be created
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#############################################################################################

def main():

	global WindCount
     
	try:
		GPIO.add_event_detect(Wind_PIN, GPIO.RISING, callback=MOTION)
		time.sleep(1)
		timerec = time.ctime()
		mph = (WindCount * 2.5)
		text_file = open("mph.html", "w")
		text_file.write("%s" % mph)
		text_file.close()
		c.execute('''INSERT INTO windlog(date, mph)
                	VALUES(?,?)''', (timerec, mph))
		conn.commit()
		conn.close()
		GPIO.cleanup()

	except KeyboardInterrupt:
		print "Quit"
		GPIO.cleanup()

#############################################################################################
#############################################################################################

def MOTION(Rain_PIN):
    global WindCount
    WindCount = WindCount + 1

if __name__ == "__main__":
   main()