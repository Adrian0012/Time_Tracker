from datetime import datetime
from pathlib import Path

timesheet_path = Path('/home/adrian__/Python/Time_Tracker/timesheets')

print("""
 ----------------------------------
      Welcome to Time Tracker
 ----------------------------------
""")

def start_tracker():
  while True:
    print("""
     Press [1] Start Time Tracking
     Press [2] Stop Time Tracking
     Press [3] Display Timesheets
     Press [Q] Quit Application 
    """)

    cmd = input('Select Option: \n')

    if cmd == '1':
      timesheet = input('Select or Create a Timesheet? \n')
      timesheet_name = timesheet_path.joinpath(timesheet)
      start_time = datetime.now()
      print('[Time Tracker ONLINE!]')

    elif cmd == '2':
      time_spent = datetime.now() - start_time
      seconds = time_spent.total_seconds()
      hours = seconds // 3600
      minutes = (seconds % 3600) // 60
      seconds = seconds % 60
      date = start_time.strftime('%d/%m/%Y')
      with open(timesheet_name, 'a+') as file:
        file.write("Hours => {} Minutes => {} Date => {}\n".format(hours, minutes, date))
      print('[Time Tracker OFFLINE!]')

    elif cmd =='3':
      for timesheet_name in timesheet_path.iterdir():
        print(timesheet_name.stem)

    else:
      print('!!Closing Application...')
      exit()

start_tracker()

