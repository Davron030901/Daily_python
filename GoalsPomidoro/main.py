import time

def pomodoro_timer(work_time, break_time):
  """
  This function implements the Pomodoro Technique.

  Args:
    work_time: The duration of the work interval in minutes.
    break_time: The duration of the break interval in minutes.
  """

  while True:
    print("Work time!")
    time.sleep(work_time * 60)
    print("Break time!")
    time.sleep(break_time * 60)


def main():
  """
  Gets user input for work and break times, then starts the Pomodoro timer.
  """
  try:
    work_time = int(input("Enter work time (in minutes): "))
    break_time = int(input("Enter break time (in minutes): "))
    pomodoro_timer(work_time, break_time)
  except ValueError:
    print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
  main()
