from time import sleep
import schedule
from requests_oauthlib import OAuth1Session
CK = ""
CS = ""
AT = ""
AS = ""
update_url = "https://api.twitter.com/1.1/statuses/update.json"
def tweet():
  twitter = OAuth1Session(CK, CS, AT, AS)
  body = "tweet!"
  params = {"status" : body}
  res = twitter.post(update_url, params = params)
  if res.status_code == 200:
    print("Success")
  else:
    print("code : %d"% res.status_code)
if __name__ == "__main__":
  schedule.every().day.at("15:40").do(tweet)
  while True:
    schedule.run_pending()
    sleep(300)
