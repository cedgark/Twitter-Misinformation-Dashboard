from flask import render_template, url_for, request, redirect, flash, session
from dashboard import app, db
from dashboard.models import Emotions, Hashtags, Locations, Mentions, Trends, Tweetids, Wordcloud, Coords, States
from dashboard.form import hashtagForm, searchBar

from dashboard.graphics.graphics import createMood, createCloud, createLocBar, createMentionBar, createStateBar
from dashboard.graphics.Map import coordSort


@app.route("/")
@app.route("/home")
def home():
    trending = Trends.query.order_by(Trends.occurrences.desc()).limit(20).all()
    return render_template('home.html', trending=trending)


def query(htmlpage, start_date, end_date, trend_filter, hashtag_search):
    if hashtag_search != '':
        search = "%{}%".format(hashtag_search)
        if trend_filter == 'low-to-high':

            trending = Trends.query.filter(Trends.keyword.like(search)).filter(Trends.date.between(start_date, end_date)).order_by(Trends.occurrences.asc()).all()
            if not bool(trending):
                trending = Trends.query.filter(Trends.keyword.like(search)).filter(Trends.date.between(end_date, start_date)).order_by(Trends.occurrences.asc()).all()

            return render_template(htmlpage, trending=trending, startdate=start_date, enddate = end_date)

        elif trend_filter == 'newest':

            trending = Trends.query.filter(Trends.keyword.like(search)).filter(Trends.date.between(start_date, end_date)).order_by(Trends.date.desc()).all()
            if not bool(trending):
                trending = Trends.query.filter(Trends.keyword.like(search)).filter(Trends.date.between(end_date, start_date)).order_by(Trends.date.desc()).all()

            return render_template(htmlpage, trending=trending, startdate=start_date, enddate = end_date)

        else:

            trending = Trends.query.filter(Trends.keyword.like(search)).filter(Trends.date.between(start_date, end_date)).order_by(Trends.occurrences.desc()).all()
            if not bool(trending):
                trending = Trends.query.filter(Trends.keyword.like(search)).filter(Trends.date.between(end_date, start_date)).order_by(Trends.occurrences.desc()).all()

            return render_template(htmlpage, trending=trending, startdate=start_date, enddate = end_date)

    else:
        #need same commands as above
        if trend_filter == 'low-to-high':
            trending = Trends.query.filter(Trends.date.between(start_date, end_date)).order_by(Trends.occurrences.asc()).all()
            if not bool(trending):
                trending = Trends.query.filter(Trends.date.between(end_date, start_date)).order_by(Trends.occurrences.asc()).all()
            return render_template(htmlpage, trending=trending, startdate=start_date, enddate = end_date)

        elif trend_filter == 'newest':
            trending = Trends.query.filter(Trends.date.between(start_date, end_date)).order_by(Trends.date.desc()).all()
            if not bool(trending):
                trending = Trends.query.filter(Trends.date.between(end_date, start_date)).order_by(Trends.date.desc()).all()
            return render_template(htmlpage, trending=trending, startdate=start_date, enddate = end_date)

        else:
            trending = Trends.query.filter(Trends.date.between(start_date, end_date)).order_by(Trends.occurrences.desc()).all()
            if not bool(trending):
                trending = Trends.query.filter(Trends.date.between(end_date, start_date)).order_by(Trends.occurrences.desc()).all()
            return render_template(htmlpage, trending=trending, startdate=start_date, enddate = end_date)

@app.route("/top_hashtags", methods=['GET', 'POST'])
def top_hashtags():

    session['start_date'] = request.args.get('startdate', default='2020-03-01')
    session['end_date'] = request.args.get('enddate', default='2020-03-01')
    session['trend_filter'] = request.args.get('sort_by', default='')
    session['hashtag_search'] = request.args.get('hashtag_search', default='')

    return query('top_hashtags.html', session['start_date'], session['end_date'], session['trend_filter'], session['hashtag_search'])


@app.route("/top_mentions", methods=['GET', 'POST'])
def top_mentions():
    return render_template('top_mentions.html')

@app.route("/top_topics", methods=['GET', 'POST'])
def top_topics():

    session['start_date'] = request.args.get('startdate', default='2020-03-01')
    session['end_date'] = request.args.get('enddate', default='2020-03-01')
    session['trend_filter'] = request.args.get('sort_by', default='')
    session['hashtag_search'] = request.args.get('hashtag_search', default='')

    return query('top_topics.html', session['start_date'], session['end_date'], session['trend_filter'], session['hashtag_search'])

@app.route("/topic/<int:id>", methods=["GET", "POST"])
def topic(id):

    #Retrieving the topics data from each of the tables
    topic = Trends.query.filter_by(entryindx = id).first()
    coords = Coords.query.filter_by(coords_ID = int(topic.coords_ID)).first()
    hashtag = Hashtags.query.filter_by(hashtag_ID = int(topic.hashtags_ID)).first()
    emotion = Emotions.query.filter_by(emotion_ID = int(topic.emotions_ID)).first()
    location = Locations.query.filter_by(location_ID = int(topic.locations_ID)).first()
    mention = Mentions.query.filter_by(mention_ID = int(topic.mentions_ID)).first()
    tweetids = Tweetids.query.filter_by(tweetid_ID = int(topic.tweetids_ID)).first()
    state = States.query.filter_by(states_ID = int(topic.states_ID)).first()
    wordcloud = Wordcloud.query.filter_by(wordcloud_ID = int(topic.wordcloud_ID)).first()

    createMood(emotion)
    createCloud(hashtag)
    createLocBar(location)
    createStateBar(state)
    createMentionBar(mention)
    coordSort(coords)

    tweet_ids_to_show = []
    for i in range (1,13):
        tweet_ids_to_show.append(getattr(tweetids, ('tweet_' + str(i))))


    return render_template('topic.html', topic=topic, hashtag=hashtag, emotion=emotion, location=location, mention=mention, idstoshow=tweet_ids_to_show, wordcloud=wordcloud)

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response