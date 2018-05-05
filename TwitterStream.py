from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

#consumer key, consumer secret, access token, access secret
ckey='tmD5cQJGlGrMvTgWse3B9f7jO'
csecret='hx9n52Jz60YVmVDvbhsghw00Q9gEoxvhpes5odlhLKmZPbjIgd'
atoken='977816386859757568-LndHX3GmrCgjilPfcv818CYlP7lQvSj'
asecret='e31Gwi8TIleLtNtMtbgPIc8P76MWv10S93ux6KQmT2Nve'

class listener(StreamListener):
    def on_data(self, data):
        try:
            #print(data)
#To split on basis of text in tweet
            tweet =data.split(',"text":"')[1].split('","source')[0]
            print(tweet)
            saveThis = str(time.time())+'::'+tweet
        #To save data in file
            saveFile = open('twitDB.csv','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return(True)
         except BaseException :
            print('Failed on Data,',str(e))
            time.sleep(5)
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream=Stream(auth, listener())
twitterStream.filter(track=["Car"])
