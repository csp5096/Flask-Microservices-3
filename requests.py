# Importing modules

from flask import Flask, render_template, request, jsonify, redirect, session
from flask import abort
from flask_cors import CORS, cross_origin
from flask import make_response, url_for
from pymongo import MongoClient
from time import gmtime, strftime

import json
import random

# Connection to MongoDB Database
connection = MongoClient("mongodb://localhost:27017/")

class Requests:
    def add_user(new_user):
        """Adding a new user to the database (Create/POST - User)"""
        api_list=[]
        print (new_user)
        db = connection.app.users
        user = db.find(
            {'$or':[{"username":new_user['username']} ,
            {"email":new_user['email']}]}
        )
        for i in user:
            print (str(i))
            api_list.append(str(i))
        if api_list == []:
            # print(new_user)
            db.insert(new_user)
            return "Success"
        else :
           abort(409)

    def list_users():
        """List users from the database (Read/GET - Users)"""
        api_list=[]
        db = connection.app.users
        for row in db.find():
            api_list.append(str(row))
        # print(api_list)
        return jsonify({'user_list': api_list})

    def list_user(user_id):
        """List a specific user from the database (Read/GET - User)"""
        api_list=[]
        db = connection.app.users
        for i in db.find({'id':user_id}):
            api_list.append(str(i))
        if api_list == []:
            abort(404)
        # print(user_id)
        return jsonify({'user_details':api_list})

    def upd_user(user):
        """Update the User's information in the database (Update/PUT - User)"""
        api_list=[]
        db_user = connection.app.users
        users = db_user.find_one(
            {"id":user['id']}
        )
        for i in users:
            api_list.append(str(i))
        if api_list == []:
           abort(409)
        else:
            db_user.update(
                {'id':user['id']},
                {'$set': user}, 
                upsert=False 
            )
            # print(user)
            return "Success"

    def del_user(del_user):
        """Delete the User from the database (DELETE/DELETE - User"""
        db = connection.app.users
        api_list=[]
        for i in db.find({'username':del_user}):
            api_list.append(str(i))
        if api_list == []:
            abort(404)
        else:
           db.remove({"username":del_user})
           # print(del_user)
           return "Success"

    def add_tweet(new_tweet):
        """Adding a new tweet per user to the database (Create/POST - Tweet)"""
        api_list=[]
        db_user = connection.app.users
        db_tweet = connection.app.tweets
        user = db_user.find(
            {"username":new_tweet['tweetedby']}
        )
        for i in user:
            api_list.append(str(i))
        if api_list == []:
           abort(404)
        else:
            db_tweet.insert(new_tweet)
            # print(new_tweet)
            return "Success"

    def list_tweets():
        """List tweets per user from the database (Read/GET - Tweets)"""
        api_list=[]
        dict = {}
        db = connection.app.tweets
        for row in db.find():
            print (row)
            dict = {}
            dict['id'] = row['id']
            dict['timestamp'] = row['timestamp']
            dict['tweetedby'] = row['tweetedby']
            dict['body'] = row['body']
            api_list.append(dict)
        # print(api_list)
        return json.dumps(api_list)

    def list_tweet(user_id):
        """List a specific tweet per suer from the database (Read/GET - Tweet)"""
        api_list=[]
        db = connection.app.tweets
        tweet = db.find({'tweetedby':user_id})
        for i in tweet:
            api_list.append(str(i))
        if api_list == []:
            abort(404)
        # print(user_id)
        return jsonify({'tweet': api_list})

    
