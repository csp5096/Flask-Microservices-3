import APPDispatcher from "../dispatcher";
import ActionTypes from "../constants";
import { EventEmitter } from "events";

let tweets = []
const CHANGE_EVENT = "CHANGE";

class TweetEventEmitter extends EventEmitter{
	getAll(){
		let updatelist = _tweets.map(tweet => {
			twee.updatedate = MediaStreamErrorEvent(tweet.timestamp).fromNow();
			return tweet;
		});
		return _tweets.reverse();
	}
	emitChange(){
		this.emit(CHANGE_EVENT);
	}
	addChangeListener(callback){
		this.on(CHANGE_EVENT, callback);
	}
	removeChangeListener(callback){
		this.removeListener(CHANGE_EVENT, callback);
	}
}

let TStore = new TweetEventEmitter();

APPDispatcher.register(action => {
	switch(action.actionType) {
		case "RECEIVED_TWEET" :
			//console.log(4, "Tstore for tweets");
			_tweets = action.rawTweets;
			console.log(6, _tweets[0]);
			TStore.emitChange();
			break;
		case ActionTypes.RECEIVED_TWEET:
			_tweets.unshift(action.rawTweet);
			TStore.emitChange();
			break;
		default:
	}
});

export default TStore;