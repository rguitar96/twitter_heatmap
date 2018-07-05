#   ***************************MY_API_INFO***********************************************
#   rguitar96_sentiment_analyzer
#   Consumer Key (API Key)	HS38Z8lPuAiaOcogMVybFBtzR (manage keys and access tokens)
#   Callback URL	None
#   Sign in with Twitter	Yes
#   App-only authentication	https://api.twitter.com/oauth2/token
#   Request token URL	https://api.twitter.com/oauth/request_token
#   Authorize URL	https://api.twitter.com/oauth/authorize
#   Access token URL	https://api.twitter.com/oauth/access_token

#   Consumer Key (API Key)	HS38Z8lPuAiaOcogMVybFBtzR
#   Consumer Secret (API Secret)	fqNEDpXxoIoWUY4e7vDf3F3SYhm8qFNmqZiZOL5W77enWBcc1v
#   Access Level	Read and write (modify app permissions)
#   Owner	RGuitar96
#   Owner ID	540079107

#   Access Token	540079107-a6HSC1Ipm9LhagMSTiQyDpoEQjuq8ZG420dOUMC5
#   Access Token Secret	zd1T13XKQ7DhVuEqBx540Y1SGnbkfu0NHdiWC1L16NOHY
#   Access Level	Read and write
#   Owner	RGuitar96
#   Owner ID	540079107
#   ***************************MY_API_INFO***********************************************

#   Dependencies:
#   pip install tweepy
#   pip install textblob

import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'HS38Z8lPuAiaOcogMVybFBtzR'
csecret = 'fqNEDpXxoIoWUY4e7vDf3F3SYhm8qFNmqZiZOL5W77enWBcc1v'
atoken = '540079107-a6HSC1Ipm9LhagMSTiQyDpoEQjuq8ZG420dOUMC5'
asecret = 'zd1T13XKQ7DhVuEqBx540Y1SGnbkfu0NHdiWC1L16NOHY'

# First pair (longitude, latitude) indicates the lower left or southwest corner
# Second pair indicates the upper right or northeast corner
# alcalá de henares
# region = [-3.406054, 40.462477, -3.335267, 40.521660] 
# comunidad de madrid
region = [-4.650673, 39.859128, -2.943299, 41.226270]


class listener(StreamListener):

    def on_data(self, data):
        # Data returned in JSON
        try:
            decoded = json.loads(data)
        except Exception as e:
            print(e)
            return True

        file =  open('tweets.txt', 'a')
        file_coordinates =  open('tweets_coordinates.txt', 'a')
        location = decoded['place']['bounding_box']['coordinates']
        
        if (location) is not None:
            lat = 0
            lon = 0
            for x in range(0, len(location[0])):
                lon = lon + location[0][x][0]
                lat = lat + location[0][x][1]
            lon = lon/len(location[0])
            lat = lat/len(location[0])
            location = [lat,lon]
            coord = '%s %s\n' % (lat,lon)
        else:
            location = '[,]'

        if (lat>region[1] and lat<region[3] and lon>region[0] and lon<region[2]):
            text = decoded['text'].replace('\n',' ').encode('utf-8')
            user = '@' + decoded.get('user').get('screen_name')
            created = decoded.get('created_at')
            tweet = '%s|%s|%s|%s\n' % (user,location,created,text)

            file.write(tweet)
            file.close()
            file_coordinates.write(coord)
            file_coordinates.close()
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    print('Stream has began...')

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(locations=region)

#   When you are done capturing tweets, you can generate a heatmap
#   as shown below. You can adjust the parameters as you prefer.
#   
#   python heatmap.py -o output.png --osm -W 2000 
#                     -v -e 39.8591,-4.6506,41.2262,-2.9432 
#                     -d 0.6 -r 60 http://b.tile.stamen.com/toner tweets_coordinates.txt