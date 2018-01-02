def word_parser(filename):
    return open(filename).read().splitlines()

import twitter
api = twitter.Api(consumer_key='uAUti19JVqrz7BD32dfdrCU3F',
 					consumer_secret='RMeM8EJpINfDPxUhLJK55XGKigRVUqhvs2Dh2fUoGxMrQyStvA',
                    access_token_key='939532563135324162-dH5GnmdBsHbwktT44gfoVJpiADQUOY9',
                    access_token_secret='mRPfNlcka7FQFuLakjwuEx8SD5jYT5BmsZn40qAu0hWYE')



statuses = api.GetUserTimeline(screen_name="usertest1235")
tweet = statuses[0].text

neg_words = word_parser("negative-words.txt")
pos_words = word_parser("positive-words.txt")

neg_counter = 0
pos_counter = 0
#couts how much bad and postive words there are in the tweet.
for word in tweet.split():
	if word in neg_words:
		neg_counter = neg_counter + 1
	if word in pos_words:
		pos_counter = pos_counter + 1

print neg_counter
print pos_counter



#if it has more negatives words then postive
if neg_counter > pos_counter:
	api.PostDirectMessage(user_id='939577673176748033',text=
'''
I saw you might of been down. Just wanted to send you a favorite poem of mine:



Peter Robert Hamilton. Aug 2015

Heartwarming

Sweetness on the inside and outside
Is a rare combination 
You can't buy that in Cash
Go ahead, call me a liar.
I know it when i see and feel it.
Astonishingly heartwarming 
I don't know about the world's Global Warming
But you triggered mine, but with positive effects.


'''


		)
	stat_id_here = statuses[0].id
	print(stat_id_here)
	api.PostMedia(status='yo look at this bro @usertest1235',media='/Users/monkeyman/Downloads/giphy_2.gif')
#if it has more postive words then negitive words
else:
	api.PostDirectMessage(user_id='939577673176748033',text=


		'''
yoyoyo
		'''

			)
	stat_id_here = statuses[0].id
	print(stat_id_here)
	api.PostMedia(status='yo look at this bro @usertest1235',media='/Users/monkeyman/Downloads/giphy_1.gif')#,possibly_sensitive=True,in_reply_to_status_id =stat_id_here)



#RIP

#status = api.PostUpdate('I love python-twitter!')
