from dashboard import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Coords(db.Model):
  tablename = 'coords'

  coords_ID = db.Column(db.Integer, primary_key = True, nullable=False)
  coord_1 = db.Column(db.Numeric, nullable=False)
  coord_2 = db.Column(db.Numeric, nullable=False)
  coord_3 = db.Column(db.Numeric, nullable=False)
  coord_4 = db.Column(db.Numeric, nullable=False)
  coord_5 = db.Column(db.Numeric, nullable=False)
  coord_6 = db.Column(db.Numeric, nullable=False)
  coord_7 = db.Column(db.Numeric, nullable=False)
  coord_8 = db.Column(db.Numeric, nullable=False)
  coord_9 = db.Column(db.Numeric, nullable=False)
  coord_10 = db.Column(db.Numeric, nullable=False)
  coord_11 = db.Column(db.Numeric, nullable=False)
  coord_12 = db.Column(db.Numeric, nullable=False)
  coord_13 = db.Column(db.Numeric, nullable=False)
  coord_14 = db.Column(db.Numeric, nullable=False)
  coord_15 = db.Column(db.Numeric, nullable=False)
  coord_16 = db.Column(db.Numeric, nullable=False)
  coord_17 = db.Column(db.Numeric, nullable=False)
  coord_18 = db.Column(db.Numeric, nullable=False)
  coord_19 = db.Column(db.Numeric, nullable=False)
  coord_20 = db.Column(db.Numeric, nullable=False)
  coord_21 = db.Column(db.Numeric, nullable=False)
  coord_22 = db.Column(db.Numeric, nullable=False)
  coord_23 = db.Column(db.Numeric, nullable=False)
  coord_24 = db.Column(db.Numeric, nullable=False)
  coord_25 = db.Column(db.Numeric, nullable=False)
  coord_26 = db.Column(db.Numeric, nullable=False)
  coord_27 = db.Column(db.Numeric, nullable=False)
  coord_28 = db.Column(db.Numeric, nullable=False)
  coord_29 = db.Column(db.Numeric, nullable=False)
  coord_30 = db.Column(db.Numeric, nullable=False)
  coord_31 = db.Column(db.Numeric, nullable=False)
  coord_32 = db.Column(db.Numeric, nullable=False)
  coord_33 = db.Column(db.Numeric, nullable=False)
  coord_34 = db.Column(db.Numeric, nullable=False)
  coord_35 = db.Column(db.Numeric, nullable=False)
  coord_36 = db.Column(db.Numeric, nullable=False)
  coord_37 = db.Column(db.Numeric, nullable=False)
  coord_38 = db.Column(db.Numeric, nullable=False)
  coord_39 = db.Column(db.Numeric, nullable=False)
  coord_40 = db.Column(db.Numeric, nullable=False)
  coord_41 = db.Column(db.Numeric, nullable=False)
  coord_42 = db.Column(db.Numeric, nullable=False)
  coord_43 = db.Column(db.Numeric, nullable=False)
  coord_44 = db.Column(db.Numeric, nullable=False)
  coord_45 = db.Column(db.Numeric, nullable=False)
  coord_46 = db.Column(db.Numeric, nullable=False)
  coord_47 = db.Column(db.Numeric, nullable=False)
  coord_48 = db.Column(db.Numeric, nullable=False)
  coord_49 = db.Column(db.Numeric, nullable=False)
  coord_50 = db.Column(db.Numeric, nullable=False)
  coord_51 = db.Column(db.Numeric, nullable=False)
  coord_52 = db.Column(db.Numeric, nullable=False)
  coord_53 = db.Column(db.Numeric, nullable=False)
  coord_54 = db.Column(db.Numeric, nullable=False)
  coord_55 = db.Column(db.Numeric, nullable=False)
  coord_56 = db.Column(db.Numeric, nullable=False)
  coord_57 = db.Column(db.Numeric, nullable=False)
  coord_58 = db.Column(db.Numeric, nullable=False)
  coord_59 = db.Column(db.Numeric, nullable=False)
  coord_60 = db.Column(db.Numeric, nullable=False)
  coord_61 = db.Column(db.Numeric, nullable=False)
  coord_62 = db.Column(db.Numeric, nullable=False)
  coord_63 = db.Column(db.Numeric, nullable=False)
  coord_64 = db.Column(db.Numeric, nullable=False)
  coord_65 = db.Column(db.Numeric, nullable=False)
  coord_66 = db.Column(db.Numeric, nullable=False)
  coord_67 = db.Column(db.Numeric, nullable=False)
  coord_68 = db.Column(db.Numeric, nullable=False)
  coord_69 = db.Column(db.Numeric, nullable=False)
  coord_70 = db.Column(db.Numeric, nullable=False)
  coord_71 = db.Column(db.Numeric, nullable=False)
  coord_72 = db.Column(db.Numeric, nullable=False)
  coord_73 = db.Column(db.Numeric, nullable=False)
  coord_74 = db.Column(db.Numeric, nullable=False)
  coord_75 = db.Column(db.Numeric, nullable=False)
  coord_76 = db.Column(db.Numeric, nullable=False)
  coord_77 = db.Column(db.Numeric, nullable=False)
  coord_78 = db.Column(db.Numeric, nullable=False)
  coord_79 = db.Column(db.Numeric, nullable=False)
  coord_80 = db.Column(db.Numeric, nullable=False)

  def __repr__(self):
    return f"Hashtags({self.coords_ID},{self.coord_1},{self.coord_2},{self.coord_3},{self.coord_4},{self.coord_5},{self.coord_6},{self.coord_7},{self.coord_8},{self.coord_9},{self.coord_10},{self.coord_11},{self.coord_12},{self.coord_13},{self.coord_14},{self.coord_15},{self.coord_16},{self.coord_17},{self.coord_18},{self.coord_19},{self.coord_20},{self.coord_21},{self.coord_22},{self.coord_23},{self.coord_24},{self.coord_25},{self.coord_26},{self.coord_27},{self.coord_28},{self.coord_29},{self.coord_30},{self.coord_31},{self.coord_32},{self.coord_33},{self.coord_34},{self.coord_35},{self.coord_36},{self.coord_37},{self.coord_38},{self.coord_39},{self.coord_40},{self.coord_41},{self.coord_42},{self.coord_43},{self.coord_44},{self.coord_45},{self.coord_46},{self.coord_47},{self.coord_48},{self.coord_49},{self.coord_50},{self.coord_51},{self.coord_52},{self.coord_53},{self.coord_54},{self.coord_55},{self.coord_56},{self.coord_57},{self.coord_58},{self.coord_59},{self.coord_60},{self.coord_61},{self.coord_62},{self.coord_63},{self.coord_64},{self.coord_65},{self.coord_66},{self.coord_67},{self.coord_68},{self.coord_69},{self.coord_70},{self.coord_71},{self.coord_72},{self.coord_73},{self.coord_74},{self.coord_75},{self.coord_76},{self.coord_77},{self.coord_78},{self.coord_79},{self.coord_80})"

class Emotions(db.Model):
  __tablename__ = 'emotions'

  emotion_ID = db.Column(db.Integer, primary_key = True, nullable=False)
  emotion_VPOS = db.Column(db.Numeric(10,4), nullable=False)
  emotion_POS = db.Column(db.Numeric(10,4), nullable=False)
  emotion_NEU = db.Column(db.Numeric(10,4), nullable=False)
  emotion_NEG = db.Column(db.Numeric(10,4), nullable=False)
  emotion_VNEG = db.Column(db.Numeric(10,4), nullable=False)

  #emotionsR = db.relationship('Trends', remote_side = emotion_ID, foreign_keys='Trends.emotion_ID')

  def __repr__(self):
    return f"Emotions({self.emotion_ID}, {self.emotion_VPOS}, {self.emotion_POS}, {self.emotion_NEU}, {self.emotion_NEG}, {self.emotion_VNEG})"

class Hashtags(db.Model):
  __tablename__ = 'hashtags'

  hashtag_ID = db.Column(db.Integer, primary_key = True, nullable=False)
  hashtag_1 = db.Column(db.String(255), nullable=False)
  hashtag_2 = db.Column(db.String(255), nullable=False)
  hashtag_3 = db.Column(db.String(255), nullable=False)
  hashtag_4 = db.Column(db.String(255), nullable=False)
  hashtag_5 = db.Column(db.String(255), nullable=False)
  hashtag_6 = db.Column(db.String(255), nullable=False)
  hashtag_7 = db.Column(db.String(255), nullable=False)
  hashtag_8 = db.Column(db.String(255), nullable=False)
  hashtag_9 = db.Column(db.String(255), nullable=False)
  hashtag_10 = db.Column(db.String(255), nullable=False)
  hashtag_11 = db.Column(db.String(255), nullable=False)
  hashtag_12 = db.Column(db.String(255), nullable=False)

  #hashtagsR = db.relationship('Trends', remote_side = hashtag_ID, foreign_keys='Trends.hashtag_ID')

  def __repr__(self):
    return f"Hashtags({self.hashtag_ID}, {self.hashtag_1}, {self.hashtag_2}, {self.hashtag_3}, {self.hashtag_4}, {self.hashtag_5}, {self.hashtag_6}, {self.hashtag_7}, {self.hashtag_8}, {self.hashtag_9}, {self.hashtag_10}, {self.hashtag_11}, {self.hashtag_12})"


class Locations(db.Model):
  __tablename__ = 'locations'

  location_ID = db.Column(db.Integer, primary_key = True, nullable=False)
  location_1 = db.Column(db.String(255), nullable=False)
  location_2 = db.Column(db.String(255), nullable=False)
  location_3 = db.Column(db.String(255), nullable=False)
  location_4 = db.Column(db.String(255), nullable=False)
  location_5 = db.Column(db.String(255), nullable=False)
  location_6 = db.Column(db.String(255), nullable=False)
  location_7 = db.Column(db.String(255), nullable=False)
  location_8 = db.Column(db.String(255), nullable=False)
  location_9 = db.Column(db.String(255), nullable=False)
  location_10 = db.Column(db.String(255), nullable=False)
  location_11 = db.Column(db.String(255), nullable=False)
  location_12 = db.Column(db.String(255), nullable=False)
  location_13 = db.Column(db.String(255), nullable=False)
  location_14 = db.Column(db.String(255), nullable=False)
  location_15 = db.Column(db.String(255), nullable=False)
  location_16 = db.Column(db.String(255), nullable=False)
  location_17 = db.Column(db.String(255), nullable=False)
  location_18 = db.Column(db.String(255), nullable=False)
  location_19 = db.Column(db.String(255), nullable=False)
  location_20 = db.Column(db.String(255), nullable=False)
  location_21 = db.Column(db.String(255), nullable=False)
  location_22 = db.Column(db.String(255), nullable=False)
  location_23 = db.Column(db.String(255), nullable=False)
  location_24 = db.Column(db.String(255), nullable=False)
  location_25 = db.Column(db.String(255), nullable=False)


  def __repr__(self):
    return f"Hashtags({self.location_ID}, {self.location_1}, {self.location_2}, {self.location_3}, {self.location_4}, {self.location_5}, {self.location_6},  {self.location_7}, {self.location_8}, {self.location_9}, {self.location_10}, {self.location_11}, {self.location_12}, {self.location_13}, {self.location_14}, {self.location_15}, {self.location_16},  {self.location_17}, {self.location_18}, {self.location_19}, {self.location_20}, {self.location_21}, {self.location_22}, {self.location_23}, {self.location_24}, {self.location_25})"

class Mentions(db.Model):
  __tablename__ = 'mentions'

  mention_ID = db.Column(db.Integer, primary_key = True, nullable=False)
  mention_1 = db.Column(db.String(255), nullable=False)
  mention_2 = db.Column(db.String(255), nullable=False)
  mention_3 = db.Column(db.String(255), nullable=False)
  mention_4 = db.Column(db.String(255), nullable=False)
  mention_5 = db.Column(db.String(255), nullable=False)
  mention_6 = db.Column(db.String(255), nullable=False)
  mention_7 = db.Column(db.String(255), nullable=False)
  mention_8 = db.Column(db.String(255), nullable=False)
  mention_9 = db.Column(db.String(255), nullable=False)
  mention_10 = db.Column(db.String(255), nullable=False)
  mention_11 = db.Column(db.String(255), nullable=False)
  mention_12 = db.Column(db.String(255), nullable=False)

  #mentionR = db.relationship('Trends', remote_side = mention_ID, foreign_keys='Trends.mention_ID')

  def __repr__(self):
    return f"Hashtags({self.mention_ID}, {self.mention_1}, {self.mention_2}, {self.mention_3}, {self.mention_4}, {self.mention_5}, {self.mention_6}, {self.mention_7}, {self.mention_8}, {self.mention_9}, {self.mention_10}, {self.mention_11}, {self.mention_12})"

class States(db.Model):
  tablename = "states"

  states_ID = db.Column(db.Integer, primary_key = True, nullable=False)

  state_1 = db.Column(db.Numeric, nullable=False)
  state_2 = db.Column(db.Numeric, nullable=False)
  state_3 = db.Column(db.Numeric, nullable=False)
  state_4 = db.Column(db.Numeric, nullable=False)
  state_5 = db.Column(db.Numeric, nullable=False)
  state_6 = db.Column(db.Numeric, nullable=False)
  state_7 = db.Column(db.Numeric, nullable=False)
  state_8 = db.Column(db.Numeric, nullable=False)
  state_9 = db.Column(db.Numeric, nullable=False)
  state_10 = db.Column(db.Numeric, nullable=False)
  state_11 = db.Column(db.Numeric, nullable=False)
  state_12 = db.Column(db.Numeric, nullable=False)
  state_13 = db.Column(db.Numeric, nullable=False)
  state_14 = db.Column(db.Numeric, nullable=False)
  state_15 = db.Column(db.Numeric, nullable=False)
  state_16 = db.Column(db.Numeric, nullable=False)
  state_17 = db.Column(db.Numeric, nullable=False)
  state_18 = db.Column(db.Numeric, nullable=False)
  state_19 = db.Column(db.Numeric, nullable=False)
  state_20 = db.Column(db.Numeric, nullable=False)
  state_21 = db.Column(db.Numeric, nullable=False)
  state_22 = db.Column(db.Numeric, nullable=False)
  state_23 = db.Column(db.Numeric, nullable=False)
  state_24 = db.Column(db.Numeric, nullable=False)
  state_25 = db.Column(db.Numeric, nullable=False)
  state_26 = db.Column(db.Numeric, nullable=False)
  state_27 = db.Column(db.Numeric, nullable=False)
  state_28 = db.Column(db.Numeric, nullable=False)
  state_29 = db.Column(db.Numeric, nullable=False)
  state_30 = db.Column(db.Numeric, nullable=False)
  state_31 = db.Column(db.Numeric, nullable=False)
  state_32 = db.Column(db.Numeric, nullable=False)
  state_33 = db.Column(db.Numeric, nullable=False)
  state_34 = db.Column(db.Numeric, nullable=False)
  state_35 = db.Column(db.Numeric, nullable=False)
  state_36 = db.Column(db.Numeric, nullable=False)
  state_37 = db.Column(db.Numeric, nullable=False)
  state_38 = db.Column(db.Numeric, nullable=False)
  state_39 = db.Column(db.Numeric, nullable=False)
  state_40 = db.Column(db.Numeric, nullable=False)

  def __repr__(self):
    return f"Hashtags({self.state_ID},{self.state_1},{self.state_2},{self.state_3},{self.state_4},{self.state_5},{self.state_6},{self.state_7},{self.state_8},{self.state_9},{self.state_10},{self.state_11},{self.state_12},{self.state_13},{self.state_14},{self.state_15},{self.state_16},{self.state_17},{self.state_18},{self.state_19},{self.state_20},{self.state_21},{self.state_22},{self.state_23},{self.state_24},{self.state_25},{self.state_26},{self.state_27},{self.state_28},{self.state_29},{self.state_30},{self.state_31},{self.state_32},{self.state_33},{self.state_34},{self.state_35},{self.state_36},{self.state_37},{self.state_38},{self.state_39},{self.state_40})"

class Trends(db.Model):
  tablename = "trends"

  entryindx = db.Column(db.Integer, primary_key=True, nullable=False)
  keyword = db.Column(db.String(255), nullable=False)
  date = db.Column(db.String(255), nullable=False)
  hashtags_ID = db.Column(db.Integer, nullable=False)
  locations_ID = db.Column(db.Integer, nullable=False)
  mentions_ID = db.Column(db.Integer, nullable=False)
  emotions_ID = db.Column(db.Integer,  nullable=False)
  tweetids_ID = db.Column(db.Integer, nullable=False)
  wordcloud_ID = db.Column(db.Integer, nullable=False)
  occurrences = db.Column(db.Integer, nullable=False)
  coords_ID = db.Column(db.Integer, nullable=False)
  states_ID = db.Column(db.Integer, nullable=False)

  def repr(self):
    return f"Trends('{self.keyword}', '{self.date}', '{self.hashtags_ID}, {self.locations_ID}', '{self.mentions_ID}', '{self.emotions_ID}, {self.tweetids_ID}', '{self.wordcloud_ID}', '{self.occurrences}', '{self.coords_ID}', '{self.states_ID}')"


class Tweetids(db.Model):
  __tablename__ = 'tweetids'

  tweetid_ID = db.Column(db.Integer, primary_key = True, nullable=False)
  tweet_1 = db.Column(db.String(255), nullable=False)
  tweet_2 = db.Column(db.String(255), nullable=False)
  tweet_3 = db.Column(db.String(255), nullable=False)
  tweet_4 = db.Column(db.String(255), nullable=False)
  tweet_5 = db.Column(db.String(255), nullable=False)
  tweet_6 = db.Column(db.String(255), nullable=False)
  tweet_7 = db.Column(db.String(255), nullable=False)
  tweet_8 = db.Column(db.String(255), nullable=False)
  tweet_9 = db.Column(db.String(255), nullable=False)
  tweet_10 = db.Column(db.String(255), nullable=False)
  tweet_11 = db.Column(db.String(255), nullable=False)
  tweet_12 = db.Column(db.String(255), nullable=False)

  #tweetidsR = db.relationship('Trends', remote_side = tweetid_ID, foreign_keys='Trends.tweetids_ID')

  def __repr__(self):
    return f"Hashtags({self.tweetid_ID}, {self.tweet_1}, {self.tweet_2}, {self.tweet_3}, {self.tweet_4}, {self.tweet_5}, {self.tweet_6},  {self.tweet_7}, {self.tweet_8}, {self.tweet_9}, {self.tweet_10}, {self.tweet_11}, {self.tweet_12})"


class Wordcloud(db.Model):
  __tablename__ = 'wordcloud'

  wordcloud_ID = db.Column(db.Integer, primary_key = True, nullable=False)

  word_1 = db.Column(db.String(255), nullable=False)
  word_1_count = db.Column(db.Integer, nullable=False)
  word_2 = db.Column(db.String(255), nullable=False)
  word_2_count = db.Column(db.Integer, nullable=False)
  word_3 = db.Column(db.String(255), nullable=False)
  word_3_count = db.Column(db.Integer, nullable=False)
  word_4 = db.Column(db.String(255), nullable=False)
  word_4_count = db.Column(db.Integer, nullable=False)
  word_5 = db.Column(db.String(255), nullable=False)
  word_5_count = db.Column(db.Integer, nullable=False)
  word_6 = db.Column(db.String(255), nullable=False)
  word_6_count = db.Column(db.Integer, nullable=False)
  word_7 = db.Column(db.String(255), nullable=False)
  word_7_count = db.Column(db.Integer, nullable=False)
  word_8 = db.Column(db.String(255), nullable=False)
  word_8_count = db.Column(db.Integer, nullable=False)
  word_9 = db.Column(db.String(255), nullable=False)
  word_9_count = db.Column(db.Integer, nullable=False)
  word_10 = db.Column(db.String(255), nullable=False)
  word_10_count = db.Column(db.Integer, nullable=False)
  word_11 = db.Column(db.String(255), nullable=False)
  word_11_count = db.Column(db.Integer, nullable=False)
  word_12 = db.Column(db.String(255), nullable=False)
  word_12_count = db.Column(db.Integer, nullable=False)

  #wordcloudR = db.relationship('Trends', remote_side = wordcloud_ID, foreign_keys='Trends.wordcloud_ID')

  def __repr__(self):
    return f"Hashtags({self.wordcloud_ID}, {self.word_1}, {self.word_1_count}, {self.word_2}, {self.word_2_count}, {self.word_3}, {self.word_3_count}, {self.word_4}, {self.word_4_count}, {self.word_5}, {self.word_5_count}, {self.word_6}, {self.word_6_count},  {self.word_7}, {self.word_7_count}, {self.word_8}, {self.word_8_count}, {self.word_9}, {self.word_9_count}, {self.word_10}, {self.word_10_count},  {self.word_11}, {self.word_11_count},  {self.word_12}, {self.word_12_count} )"
