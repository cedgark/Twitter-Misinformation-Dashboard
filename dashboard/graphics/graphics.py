from PIL import Image
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def createCloud(hashtag):

    string = '#' + hashtag.hashtag_1 + '\n'
    for i in range(2,13):
        s = getattr(hashtag, 'hashtag_'+str(i))
        string = string + '#'+ s + '\n'

    wc = WordCloud(max_words=20, background_color="#F5F5F5" ,margin=10, random_state=1).generate(string)

    wc.to_file("dashboard\static\images\cloud.png")

    return

def createMood(emotion):

    y = [emotion.emotion_VPOS, emotion.emotion_POS,emotion.emotion_NEU,emotion.emotion_NEG,emotion.emotion_VNEG]
    mylabels = ["Very Positive", "Positive", "Neutral", "Negative", "Very Negative"]
    mycolors = ["green", "limegreen", "lightgrey", "red", (0.75,0,0,1)]

    plt.clf()
    fig = plt.pie(y, labels=mylabels, colors=mycolors, autopct='%1.0f%%', startangle = 90, wedgeprops = {"edgecolor" : "black",'linewidth': 1,'antialiased': True})
    plt.title("Emotional Score", bbox={'facecolor':'0.9'})


    plt.savefig("dashboard\static\images\emotion.png")

    im = Image.open(r"dashboard\static\images\emotion.png")
    width, height = im.size
    left = 80
    top = 20
    right = 560
    bottom = 400
    im1 = im.crop((left, top, right, bottom))
    im1.save("dashboard\static\images\emotion.png")
    plt.close('all')

def createLocBar(location):
    x = []
    for i in range(1,18):
        loc = getattr(location, 'location_'+str(i))
        if loc != 'none':
            x.append(loc)
    y = []
    n = 10
    i=0
    while i < len(x):
        y.append(n)
        n = n/2
        i += 1


    fig, ax = plt.subplots(frameon=False)

    right_side = ax.spines["right"]
    right_side.set_visible(False)
    left_side = ax.spines["left"]
    left_side.set_visible(False)
    top_side = ax.spines["top"]
    top_side.set_visible(False)

    bars = plt.bar(x,y)
    for b in bars[::2]:
        b.set_color((0.592, 0.329, 1))
    for b in bars[1::2]:
        b.set_color((0.737, 0.392, 1))

    plt.yticks([])
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    ax.set_facecolor((0.96, 0.96, 0.96))
    fig.savefig("dashboard\static\images\locBar.png", bbox_inches='tight')


    im = Image.open(r"dashboard\static\images\locBar.png")
    width, height = im.size
    left = 0
    top = 20
    right = 560
    bottom = 480
    im1 = im.crop((left, top, right, bottom))
    im1.save("dashboard\static\images\locBar.png")
    plt.close('all')
    return

def createStateBar(location):
    x = []
    for i in range(1,18):
        loc = getattr(location, 'state_'+str(i))
        if loc != 'none':
            x.append(loc)
    y = []
    n = 10
    i=0
    while i < len(x):
        y.append(n)
        n = n/2
        i += 1


    fig, ax = plt.subplots(frameon=False)

    right_side = ax.spines["right"]
    right_side.set_visible(False)
    left_side = ax.spines["left"]
    left_side.set_visible(False)
    top_side = ax.spines["top"]
    top_side.set_visible(False)

    bars = plt.bar(x,y)
    for b in bars[::2]:
        b.set_color((0.592, 0.329, 1))
    for b in bars[1::2]:
        b.set_color((0.737, 0.392, 1))

    plt.yticks([])
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    ax.set_facecolor((0.96, 0.96, 0.96))
    fig.savefig("dashboard\static\images\stateBar.png", bbox_inches='tight')


    im = Image.open(r"dashboard\static\images\stateBar.png")
    width, height = im.size
    left = 0
    top = 20
    right = 560
    bottom = 480
    im1 = im.crop((left, top, right, bottom))
    im1.save("dashboard\static\images\stateBar.png")
    plt.close('all')
    return

def createMentionBar(mention):

    x = []
    for i in range(1,13):
        ment = getattr(mention, 'mention_'+str(i))
        x.append('@' + ment)

    y = []
    n = len(x)

    while n > 0:
        y.append(n)
        n -= 1

    fig, ax = plt.subplots(frameon=False)

    right_side = ax.spines["right"]
    right_side.set_visible(False)
    left_side = ax.spines["left"]
    left_side.set_visible(False)
    top_side = ax.spines["top"]
    top_side.set_visible(False)

    bars = plt.bar(x,y)
    for b in bars[::2]:
        b.set_color((0.38, 0.918, 1))
    for b in bars[1::2]:
        b.set_color((0.533, 0.941, 1))

    plt.yticks([])
    plt.setp(ax.get_xticklabels(), rotation=40, horizontalalignment='right')
    ax.set_facecolor((0.96, 0.96, 0.96))
    fig.savefig("dashboard\static\images\menBar.png",bbox_inches='tight')

    im = Image.open(r"dashboard\static\images\menBar.png")
    width, height = im.size
    left = 0
    top = 20
    right = 560
    bottom = 480
    im1 = im.crop((left, top, right, bottom))
    im1.save("dashboard\static\images\menBar.png")
    plt.close('all')
    return
