import schedule
import time
import os

def job():
    os.system("python vasTest.py")

try:
	print("\nI'm working in every " + "3" + " minutes...\n")
	schedule.every(3).minutes.do(job)
	job()
except (IOError, TypeError) as error:
	print 'Error: ' + str(error)


while True:
    schedule.run_pending()
    time.sleep(1)