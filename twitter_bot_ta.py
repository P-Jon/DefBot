from TwitterAPI import TwitterAPI
import time
import datetime

# These need to be filled with custom keys etc
consumer_key        = ""
consumer_secret     = ""
access_token_key    = ""
access_token_secret = ""

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

definitions_file = open("definitions.txt","r")

definitions = []
current_line = 1
fileline_count = 0

for line in definitions_file:
    definitions.append(line)
    fileline_count += 1

while(True):
    now = datetime.datetime.now()
    
    if current_line > fileline_count:
        break
    
    if now.hour == 11 and now.minute == 0:
        tweet = api.request('statuses/update',{'status':definitions[current_line - 1]})
        error_file = open("error_log.txt","w")
        error_file.write("Tweeted, status code: {0} Time: {1}:{2}".format(tweet.status_code,now.hour,now.minute))
        error_file.close()
        current_line += 1
        time.sleep(60)
    else:
        time.sleep(30)
definitions_file.close()

