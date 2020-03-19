from time import sleep
import schedule
def minute():
  print("毎分10秒タスク実行")
def hourA():
  print("毎時00分タスク実行")
def hourB():
  print("毎時15分タスク実行")
def hourC():
  print("毎時30分タスク実行")
def hourD():
  print("毎時45分タスク実行")
def day():
  print("毎日13時15分タスク実行")
def sunday():
  print("毎週日曜日08時30分タスク実行")
if __name__ == "__main__":
  schedule.every().minute.at(":10").do(minute)
  schedule.every().hour.at(":00").do(hourA)
  schedule.every().hour.at(":15").do(hourB)
  schedule.every().hour.at(":30").do(hourC)
  schedule.every().hour.at(":45").do(hourD)
  schedule.every().day.at("13:15").do(day)
  schedule.every().sunday.at("08:30").do(sunday)
  print("開始")
  while True:
    sleep(1)
    schedule.run_pending()
  print("終了")
