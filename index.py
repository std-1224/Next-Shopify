
import subprocess
import random
from datetime import datetime, timedelta

# Define start and end dates
start_date = datetime(2017, 6, 12)
end_date = datetime(2017, 7, 29)

# Define holidays (in the format "MM-DD")
holidays = {"01-01", "01-02", "01-03", "01-04", "01-05", "12-25", "12-26", "12-27", "12-28", "12-29", "12-30", "12-31", "02-23", "09-20"}  # Add more holidays as needed

# Define possible commit messages
commit_messages = [
    "Fix minor bug",
    "Update documentation",
    "Refactor code",
    "Improve performance",
    "Add new feature",
    "Update dependencies",
    "Refactor module structure",
    "Fix typo in code",
    "Add test cases",
    "Code cleanup",
    "Fix compatibility issues",
    "Optimize function",
    "Refactor redundant code",
    "Update README",
]

# Define intense work months
intense_work_months = {3, 4, 6, 7, 9, 10, 11, 12}

# Helper function to check if a day is a workday
def is_workday(date):
    return date.weekday() < 5  # Monday-Friday

# Helper function to check if a date is a holiday
def is_holiday(date):
    return date.strftime("%m-%d") in holidays

# Function to simulate an empty commit on a given date
def make_empty_commit(commit_date, commit_count, work_start, work_end):
    for i in range(commit_count):
        # Select a random commit message
        commit_message = random.choice(commit_messages)
        
        # Select a random time within working hours
        commit_time = commit_date.replace(
            hour=random.randint(work_start, work_end), 
            minute=random.randint(0, 59), 
            second=random.randint(0, 59)
        )
        
        # Log commit details for debugging
        print(f"Committing on {commit_time} with message: '{commit_message}'")
        
        # Create an empty commit with the specified commit time
        try:
            subprocess.check_call([
                "git", "commit", "--allow-empty", "-m", commit_message,
                "--date", commit_time.strftime("%Y-%m-%d %H:%M:%S")
            ])
        except subprocess.CalledProcessError as e:
            print(f"Error creating commit on {commit_time}: {e}")
            break  # Stop if there is an error

# Loop through each day in the date range
current_date = start_date
while current_date <= end_date:
    # Skip if it's a holiday
    if is_holiday(current_date):
        print(f"Skipping holiday on {current_date.strftime('%Y-%m-%d')}")
        current_date += timedelta(days=1)
        continue
    
    # Determine if work is done based on weekday/weekend probability
    if is_workday(current_date):
        work_today = random.random() < 0.9 if current_date.month in intense_work_months else random.random() < 0.6
        if work_today:
            # Workday hours and commit count distribution
            work_start, work_end = 9, 19  # 9 AM to 7 PM
            chance = random.random()
            if chance < 0.6:
                commit_count = random.randint(6, 10)
            elif chance < 0.9:
                commit_count = random.randint(11, 20)
            else:
                commit_count = random.randint(20, 25)
    else:
        work_today = random.random() < 0.1  # 10% chance to work on weekends
        if work_today:
            # Weekend hours and commit count distribution
            work_start, work_end = 10, 17  # 10 AM to 5 PM
            chance = random.random()
            if chance < 0.7:
                commit_count = random.randint(6, 10)
            else:
                commit_count = random.randint(11, 15)

    # Make the empty commits for the current date if work is done
    if work_today:
        print(f"Working on {current_date.strftime('%Y-%m-%d')}: {commit_count} commits")
        make_empty_commit(current_date, commit_count, work_start, work_end)
    else:
        print(f"Not working on {current_date.strftime('%Y-%m-%d')}")

    # Move to the next day
    current_date += timedelta(days=1)