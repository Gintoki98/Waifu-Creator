# For quicker debugging and developing, hit Shift + R just once to automatically reload your game whenever this script is updated.

define e = Character("Sylvie")

init python:
    
    import os
    import subprocess
    import time
    import platform
    import sys

label start:

    play music "illurock.opus"

    scene bg lecturehall with fade

    show sylvie green smile with dissolve


    if not persistent.player_name:

        e "Hey there, nice to meet you! I'm Sylvie."

        python:

            player_name = renpy.input("What's your name?")

            player_name = player_name.strip() or "Stranger"

            persistent.player_name = player_name

        e "[player_name]. That's a nice name!"

label ask_menu:

    show sylvie green smile at right with ease

    python:
        import datetime

        hour_now = datetime.datetime.now().hour

        if 0 <= hour_now < 12:

            time_of_day = "morning"

        elif 12 <= hour_now < 18:

            time_of_day = "afternoon"

        else:

            time_of_day = "evening"

    menu:

        e "What should we do this [time_of_day], [persistent.player_name]?"

        "Update my weather.":

            jump get_weather

        "Let's share about our day.":

            jump lets_talk

        "Tell me a joke!":

            jump get_joke            

        "Let's go on a date!":

            jump lets_date

        "Sync my NTUlearn files!":

            jump launch_blackbox

        "I want to check out your wardrobe!":

            jump change_clothes

        "Reset game.":

            jump reset_game

        "Leave game.":

            jump end_game

label get_weather:

    # Clarence

    jump ask_menu

label get_joke:

    # Clarence

    jump ask_menu

label lets_talk:

    e "Sure let's! I'll go first!"

    python:

        banter_list = [
            "Nothing much happened today for me! Just looked around the pictures in your computer. You look cute!",
            "I went to shop at the Dark Web for something for you. Hehe!",
            "I was looking at the workshops NTU OSS will be having next year. The ones by Clarence and Jarrett sound pretty interesting! You should join them!",
            "Haha my friend from another computer called me using websockets and we were gossiping about you.",
            "Remember I told you that I was writing a paper on the hype on machine learing? I think I'm almost there!",
            "Had a talk with Alexa! Or was it Siri? I'm not too sure.",
            "I looked through your internet history... I have seen things...",
            "Dude you should probably empty your digital thrash."
        ]

        import random

        banter_message = banter_list[random.randint(0, len(banter_list) - 1)]

    e "[banter_message]"

    e "But other than that, same old. I'm excited to hear about yours too! Hahaha my attention span is probably limited to 255 characters though."

    python:
    
        player_message = renpy.input("Quick, tell me about your day!")

        player_message = player_message.strip()

    show text "Loading..."

    python:

        import pickle

        pickle.dump(player_message, open( "message.p", "wb" ), protocol=2 )

        # http://textblob.readthedocs.io/en/dev/install.html
        # pip install nltk, textblob
        # python -m textblob.download_corpora lite

        sentiment_path = os.path.abspath(os.path.join(config.basedir, "game", "sentiment.py"))

        if sys.platform == "win32":

            os.startfile(sentiment_path)

        elif platform.mac_ver()[0]:

            subprocess.Popen([ "open", sentiment_path ])

        else:

            subprocess.Popen([ "xdg-open", sentiment_path ])

    pause 3
    hide text

    $ player_sentiment = pickle.load( open( "sentiment.p", "rb" ) )

    if player_sentiment == "bad":

        show sylvie green surprised at center with ease        

        e "Oh no, I'm sorry your day didn't go as well as I expected... It's alright! I always believe that things will get better! You know I'm always here for you."

    elif player_sentiment == "okay":

        show sylvie green normal at center with ease                

        e "I see I see! Glad your day was still manageable!"

    elif player_sentiment == "good":

        show sylvie green giggle at center with ease  

        e "Awesome! Haha I always enjoy hearing about your day! I wish that every day will be like this for you!"
    
    jump ask_menu

label change_clothes:

    show sylvie at center with ease

    e "Haha sure!"

    hide sylvie with fade

    show sylvie blue smile at center

    e "How does this look!"

    show sylvie blue giggle with dissolve

    e "Hehe that's enough for today!"

    hide sylvie with fade

    jump ask_menu

label launch_blackbox:

    show sylvie green normal at right
    with ease

    e "I've learnt some programming hacks from OSS from joining their workshops every Friday and I've made Blackbox just for you! It's still patchy but I'm learning and I'll make it better soon!"

    show sylvie green giggle at center
    with dissolve

    e "It syncs your NTUlearn files into your machine, just like Dropbox. Get it? {i}Black-box{/i}?"

    show sylvie green normal
    with ease

    e "Let me put them to test for you, [persistent.player_name]! To show you the magic I've made, I will be downloading the files using Chrome and you can check it live!"

    $ blackbox_path = os.path.abspath(os.path.join(config.basedir, "game", "Blackbox"))

    $ game_path = os.path.abspath(os.path.join(config.basedir, "game"))

    e "Before that, remember to download {b}chromedriver{/b} and {b}blackbox.py{/b} in the following directory for Blackbox to work: [game_path]. When you are ready, let me know!"

    show text "Initialising..."
    pause 0

    python:        

        blackbox_path = os.path.abspath(os.path.join(config.basedir, "game", "blackbox.py"))

        if sys.platform == "win32":

            os.startfile(blackbox_path)

        elif platform.mac_ver()[0]:

            subprocess.Popen([ "open", blackbox_path ])

        else:

            subprocess.Popen([ "xdg-open", blackbox_path ])

    hide text

    e "Blackbox launched! Check out the Chrome doing its magic! Your NTUlearn files will be synced to the Blackbox folder in [blackbox_path]."

    jump ask_menu

label reset_game:

    show sylvie green normal at center
    with ease

    $ persistent.player_name = None

    e "Done! Let's restart!"

    jump start


label end_game:

    show sylvie green surprised at center
    with ease

    e "Oh man, you've got to leave so quickly?"

    show sylvie green smile at center
    with dissolve

    e "Goodbye! I'll miss you."

    return
