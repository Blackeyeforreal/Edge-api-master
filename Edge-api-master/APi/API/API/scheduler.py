from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

def your_function():
    # Perform your desired task
    print("Function executed at the desired time.")
    return "your life"

# Create a scheduler
scheduler1 = BackgroundScheduler()

# Schedule your function to run at a specific time
scheduler1.add_job(your_function, 'date', run_date=datetime.now() + timedelta(seconds= 3))

# Start the scheduler
scheduler1.start()
