# twitter_heatmap
#### Using Twitter API and @sethoscope heatmap generator for Python 3.6.

This project aims to generate a file containing a list of tweets within a given region and a file containing all of their locations. We can then use the latter to generate a heatmap with @sethoscope utility (https://github.com/sethoscope/heatmap).

The idea for a future update is to generate a positive/negative heatmap based on the TextBlob result of each tweet.

Python dependencies:
* pip install tweepy





### Example in Comunidad de Madrid (Spain)

First, you will need to replace the following lines:
> ckey = 'CONSUMER_KEY'
> csecret = 'CONSUMER_SECRET'
> atoken = 'ACCESS_TOKEN'
> asecret = 'ACCESS_SECRET'

With the ones provided by your Twitter API. You can create your own [here](https://apps.twitter.com/)

Then you will need to replace the following with your region coordinates:
> region = [-4.650673, 39.859128, -2.943299, 41.226270]

The first pair indicates the longitude and latitude of the southwest corner of your region, and the second one indicates the coordinates of the northeast corner.

Once we have done this, we will start capturing tweets in this location with the following cmd command:
python twitter_heatmap.py

In this example, I waited 30 minutes before closing the process, resulting on 538 tweets in my 'tweets_coordinates.txt' file.

We will then call the heatmap program to start drawing our map. In this case, we will indicate the following arguments, which you can adjust at your needs:

> python heatmap.py -o output.png --osm -W 2000 -v -e 39.8591,-4.6506,41.2262,-2.9432 -d 0.6 -r 60 http://b.tile.stamen.com/toner tweets_coordinates.txt

This generated the following map:

![Image](/madrid_example/madrid_050720181302_050720181332.png)
