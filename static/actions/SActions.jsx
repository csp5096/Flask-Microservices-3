import AppDispatcher from '../dispatcher';
import ActionTypes from '../constants';

export default{
	receivedTweets(rawTweets){
		//console.log(3, "Received Tweets");
		AppDispatcher.dispatch({
			actionType: ActionTypes.RECEIVED_TWEETS,
			rawTweets
		})
	},
	receivedTweet(rawTweet){
		AppDispatcher.dispatch({
			actionType: ActionTypes.RECEIVED_TWEET,
			rawTweet
		})
	}
}