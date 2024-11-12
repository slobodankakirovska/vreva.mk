import time
from main import main
import schedule

def job():
    print("Running scheduled job...")
    main()

# Schedule the job every 5 seconds
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
