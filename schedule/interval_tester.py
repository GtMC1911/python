from time import sleep
import schedule
interval_t = 7
pendhing_t = 5
term = 5
def job():
  print("job実行")
if __name__ == "__main__":
  schedule.every(interval_t).seconds.do(job)
  print("開始")
  for i in range(term):
    for j in range(pendhing_t):
      sleep(1)
      print( str(i*5+j +1) + "秒経過")
    print("pending実行")
    schedule.run_pending()
  print("終了")
