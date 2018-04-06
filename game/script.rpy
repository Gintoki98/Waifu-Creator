# "example" method is not shipped with standard Ren'Py
# It is provided for by 01example.rpy, 01example.rpyc, keywords.py, examples.rpy, examples.rpyc

define e = Character("Sylvie")

init python:
    
    import os
    import subprocess
    import time
    import platform
    import sys
    from urllib2 import urlopen, Request
    import json, ssl
    ssl._create_default_https_context = ssl._create_unverified_context

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

    show text "Getting progress..."

    pause 0

    python:

        import datetime

        hour_now = datetime.datetime.now().hour

        if 0 <= hour_now < 12:

            time_of_day = "morning"

        elif 12 <= hour_now < 18:

            time_of_day = "afternoon"

        else:

            time_of_day = "evening"

        try:

            url = 'https://dl.dropboxusercontent.com/s/fe5njz6bl8djh8u/README.js?dl=0'

            request = Request(url, headers={
                "Accept": "text/plain",
                "User-Agent": "Renpy"
            })

            progress = int(urlopen(request, timeout=5).read())

            progress_available = True

        except:

            progress_available = False

    hide text

    if progress_available:

        menu:

            e "What should we do this [time_of_day], [persistent.player_name]? Once we are done with every checkpoint of this workshop, click on 'Refresh Progress' to move on!"

            "You're boring, get yourself a change of clothes!" if progress == 1:

                jump change_clothes

            "How's the weather out there?" if progress == 2:

                jump get_weather

            "Tell me a joke!" if progress == 3:

                jump get_joke

            "Let's share about our day." if progress == 4:

                jump lets_talk

            "Sync my NTUlearn files!" if progress == 5:

                jump launch_blackbox

            "How does the code for changing clothes work?" if progress == 1:

                jump code_change_clothes

            "How does the weather code work?" if progress == 2:

                jump code_get_weather

            "How does the joke code work?" if progress == 3:

                jump code_get_joke

            "How does the talking code work?" if progress == 4:

                jump code_lets_talk

            "How does the Blackbox code work?" if progress == 5:

                jump code_launch_blackbox                                                          

            "How do these menu options work?" if progress == 0:

                jump code_introduction

            "Refresh Progress.":

                jump ask_menu  

            "Reset Game & Name.":

                jump reset_game

            "Leave Game.":

                jump end_game                                              

    else: # if workshop progress can't be fetched
    
        menu:

            e "Either the workshop is over, or that I can't access the internet. But it's alright. What should we do this [time_of_day], [persistent.player_name]?"

            "You're boring, get yourself a change of clothes!":

                jump change_clothes

            "How's the weather out there?":

                jump get_weather

            "Tell me a joke!":

                jump get_joke            

            "Let's share about our day.":

                jump lets_talk

            "Sync my NTUlearn files!":

                jump launch_blackbox

            "Reset Game & Name.":

                jump reset_game

            "Leave game.":

                jump end_game

label code_introduction:

    show sylvie green smile at center with ease

    e "Let's take a look at how the code works! Jarrett and Clarence will go through how this works briefly."

    example:
    
        # e "First of all, let's take a look at the menu structure."

        menu:

            "Refresh progress.":

                hide example

                # jump ask_menu 

            "Reset Game & Name.":

                hide example

                # jump reset_game

            "Leave game.":

                hide example

                # jump end_game    

            "When you're ready, click here to continue.":

                hide example

    e "Next, did you notice that Sylvie knows the time of your day? She also remembers your name even after you quit the game. We'll show you how she does it."

    example:

        e "This is the code for getting your time and remembering your name!"

        python:

            import datetime

            hour_now = datetime.datetime.now().hour

            if 0 <= hour_now < 12:

                time_of_day = "morning"

            elif 12 <= hour_now < 18:

                time_of_day = "afternoon"

            else:

                time_of_day = "evening"

        if not persistent.player_name:

            e "Hey there, nice to meet you! I'm Sylvie."

            python:

                player_name = renpy.input("What's your name?")

                player_name = player_name.strip() or "Stranger"

                persistent.player_name = player_name

            e "[player_name]. That's a nice name!"            

    hide example

    e "And that's how Sylvie asks: What should we do this [time_of_day], [persistent.player_name]?"

    example:

        e "What about refreshing the progress?"

        show text "Getting progress..."

        pause 0

        python:

            try:

                url = 'https://dl.dropboxusercontent.com/s/fe5njz6bl8djh8u/README.js?dl=0'

                request = Request(url, headers={
                    "Accept": "text/plain",
                    "User-Agent": "Renpy"
                })

                progress = int(urlopen(request, timeout=5).read())

                progress_available = True

            except:

                progress_available = False

        hide text

    hide example

    e "Your current progress is at Checkpoint [progress]. Sylvie actually uses Dropbox as our Checkpoint server lel."

    e "What about resetting the game? It's actually really simple."

    example:

        $ persistent.player_name = None

        e "Done! Let's restart! Your player name has been resetted. Click on the 'Reset Game & Name' button later to set your name again! Your name will temporarily default to 'Stranger'."

    hide example

    $ persistent.player_name = "Stranger"

    e "Finally, how does the quit to the main menu button work?"

    example:

        e "Oh man, you've got to leave so quickly?"

        show sylvie green smile at center with dissolve

        e "Goodbye! I'll miss you, [persistent.player_name]."

        hide example # not in actual code

        return

    hide example

    jump ask_menu

label get_weather:

    show sylvie green surprised at center with ease

    show text "Offering tribute to the weather gods..."

    pause 0

    python:

        try:

            key = '688abb832887b89786cc6167ec1427ac'

            url = 'http://api.openweathermap.org/data/2.5/weather?q=Singapore&APPID='

            weather = json.load(urlopen(url + key, timeout=5))['weather'][0]['description']

            weather_available = True

        except:

            weather_available = False

    hide text

    if weather_available:

        show sylvie green smile with ease

        e "The weather now in Singapore is [weather]! It's nice isn't it?"

    else:

        e "Something isn't right. The weather gods must be asleep at the moment."

    jump ask_menu

label code_get_weather:

    show sylvie green smile at center with ease

    e "Let's take a look at how the code works!"

    example:

        show sylvie green surprised at center with ease

        show text "Offering tribute to the weather gods..."

        pause 0

        python:

            try:

                key = '688abb832887b89786cc6167ec1427ac'

                url = 'http://api.openweathermap.org/data/2.5/weather?q=Singapore&APPID='

                weather = json.load(urlopen(url + key, timeout=5))['weather'][0]['description']

                weather_available = True

            except:

                weather_available = False

        hide text

        if weather_available:

            show sylvie green smile with ease

            e "The weather now in Singapore is [weather]! It's nice isn't it?"

        else:

            e "Something isn't right. The weather gods must be asleep at the moment."

    e "Jarrett and Clarence will go through how this works briefly."

    hide example

    e "That's it! Hope this explains the code, [persistent.player_name]."

    jump ask_menu

label get_joke:

    show sylvie at center with ease
    
    show text "Formulating joke..."

    pause 0

    python:

        try:

            url = 'https://icanhazdadjoke.com/'

            request = Request(url, headers={
                "Accept": "text/plain",
                "User-Agent": "Renpy"
            })

            joke = urlopen(request, timeout=5).read()

            joke_available = True

        except:

            joke_available = False

    hide text

    if joke_available:

        show sylvie green giggle with ease

        e "[joke]"

        e "Hahaha it's funny isn't it? Hehe!"

    else:

        show sylvie green surprised with ease

        e "Why did the chicken cros-"

        e " Uhmmm... Sorry, I kinda forgot how the story goes. Try again later?"

    jump ask_menu

label code_get_joke:

    show sylvie green smile at center with ease

    e "Let's take a look at how the code works!"

    example:

        show sylvie at center with ease
        
        show text "Formulating joke..."

        pause 0

        python:

            try:

                url = 'https://icanhazdadjoke.com/'

                request = Request(url, headers={
                    "Accept": "text/plain",
                    "User-Agent": "Renpy"
                })

                joke = urlopen(request, timeout=5).read()

                joke_available = True

            except:

                joke_available = False

        hide text

        if joke_available:

            show sylvie green giggle with ease

            e "[joke]"

            e "Hahaha it's funny isn't it? Hehe!"

        else:

            show sylvie green surprised with ease

            e "Why did the chicken cros-"

            e " Uhmmm... Sorry, I kinda forgot how the story goes. Try again later?"

    e "Jarrett and Clarence will go through how this works briefly."

    hide example

    e "That's it! Hope this explains the code, [persistent.player_name]."

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

            "Dude you should probably empty your digital thrash."]

        import random

        banter_message = banter_list[random.randint(0, len(banter_list) - 1)]

    e "[banter_message]"

    e "But other than that, same old. I'm excited to hear about yours too! Hahaha my attention span is probably limited to 255 characters though."

    python:
    
        player_message = renpy.input("Quick, tell me about your day!")

        player_message = player_message.strip()

    show text "Flipping the dictionary..."

    pause 0

    python:

        sentiment_script_path = os.path.abspath(os.path.join(config.basedir, "game", "sentiment.py"))

        if sys.platform == "win32":

            try:

                import pickle

                pickle.dump(player_message, open( "message.p", "wb" ), protocol=2 )

                os.startfile(sentiment_script_path)

                time.sleep(3)

                player_sentiment = pickle.load( open( "sentiment.p", "rb" ) )

            except:

                player_sentiment = "error"

        else:

            cmd = ["/usr/local/bin/python3", sentiment_script_path, player_message]

            try:

                output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)

            except subprocess.CalledProcessError as exc:

                player_sentiment = "error"

            else:

                player_sentiment = output.strip()

    hide text

    if player_sentiment == "bad":

        show sylvie green surprised at center with ease

        e "Oh no, I'm sorry your day didn't go as well as I expected... It's alright! I always believe that things will get better! You know I'm always here for you."

    elif player_sentiment == "okay":

        show sylvie green normal at center with ease

        e "I see I see! Glad your day was still manageable!"

    elif player_sentiment == "good":

        show sylvie green giggle at center with ease

        e "Awesome! Haha I always enjoy hearing about your day! I wish that every day will be like this for you!"

    else:

        show sylvie green surprised at center with ease

        e "Oops.. Something went wrong!"


    jump ask_menu


label code_lets_talk:

    show sylvie green smile at center with ease

    e "Let's take a look at how the code works!"

    example:

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

                "Dude you should probably empty your digital thrash."]

            import random

            banter_message = banter_list[random.randint(0, len(banter_list) - 1)]

        e "[banter_message]"

        e "But other than that, same old. I'm excited to hear about yours too! Hahaha my attention span is probably limited to 255 characters though."

        python:
        
            player_message = renpy.input("Quick, tell me about your day!")

            player_message = player_message.strip()

        show text "Flipping the dictionary..."

        pause 0

        python:

            sentiment_script_path = os.path.abspath(os.path.join(config.basedir, "game", "sentiment.py"))

            if sys.platform == "win32":

                try:

                    import pickle

                    os.startfile(sentiment_script_path)

                    time.sleep(3)

                    player_sentiment = pickle.load( open( "sentiment.p", "rb" ) )

                except:

                    player_sentiment = "error"

            else:

                cmd = ["/usr/local/bin/python3", sentiment_script_path, player_message]

                try:

                    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)

                except subprocess.CalledProcessError as exc:

                    player_sentiment = "error"

                else:
                    
                    player_sentiment = output.strip()

        hide text

        if player_sentiment == "bad":

            show sylvie green surprised at center with ease

            e "Oh no, I'm sorry your day didn't go as well as I expected... It's alright! I always believe that things will get better! You know I'm always here for you."

        elif player_sentiment == "okay":

            show sylvie green normal at center with ease

            e "I see I see! Glad your day was still manageable!"

        elif player_sentiment == "good":

            show sylvie green giggle at center with ease

            e "Awesome! Haha I always enjoy hearing about your day! I wish that every day will be like this for you!"

        else:

            show sylvie green surprised at center with ease

            e "Oops.. Something went wrong!"

    e "Jarrett and Clarence will go through how this works briefly."

    hide example

    e "That's it! Hope this explains the code, [persistent.player_name]."

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

label code_change_clothes:

    show sylvie green smile at center with ease

    e "Let's take a look at how the code works!"

    example:

        show sylvie at center with ease

        e "Haha sure!"

        hide sylvie with fade

        show sylvie blue smile at center

        e "How does this look!"

        show sylvie blue giggle with dissolve

        e "Hehe that's enough for today!"

        hide sylvie with fade

    e "Jarrett and Clarence will go through how this works briefly."

    hide example

    e "That's it! Hope this explains the code, [persistent.player_name]."

    jump ask_menu

label launch_blackbox:

    show sylvie green normal at right with ease

    e "Before we continue, locate your blackbox.py file in your game folder and edit the following: BLACKBOARD_USERNAME, BLACKBOARD_PASSWORD and CHROMEDRIVER_PATH."

    e "I've learnt some programming hacks from OSS from joining their workshops every Friday and I've made Blackbox just for you! It's still patchy but I'm learning and I'll make it better soon!"

    show sylvie green giggle at center with dissolve

    e "It syncs your NTUlearn files into your machine, just like Dropbox. Get it? {i}Black-box{/i}?"

    show sylvie green normal with ease

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

            subprocess.Popen([ "/usr/local/bin/python3", blackbox_path ])

        else:

            subprocess.Popen([ "xdg-open", blackbox_path ])

    hide text

    $ blackbox_path = os.path.abspath(os.path.join(config.basedir, "game", "Blackbox"))

    e "Blackbox launched! Check out the Chrome doing its magic! Your NTUlearn files will be synced to the Blackbox folder in [blackbox_path]. Remember, try not to peep into the Downloads folder!"

    jump ask_menu


label code_launch_blackbox:

    show sylvie green smile at center with ease

    e "Let's take a look at how the code works!"

    example:

        show sylvie green normal at right with ease

        e "I've learnt some programming hacks from OSS from joining their workshops every Friday and I've made Blackbox just for you! It's still patchy but I'm learning and I'll make it better soon!"

        show sylvie green giggle at center with dissolve

        e "It syncs your NTUlearn files into your machine, just like Dropbox. Get it? {i}Black-box{/i}?"

        show sylvie green normal with ease

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

                subprocess.Popen([ "/usr/local/bin/python3", blackbox_path ])

            else:

                subprocess.Popen([ "xdg-open", blackbox_path ])

        hide text

        e "Blackbox launched! Check out the Chrome doing its magic! Your NTUlearn files will be synced to the Blackbox folder in [blackbox_path]. Remember, try not to peep into the Downloads folder!"

    e "Jarrett and Clarence will go through how this works briefly."

    hide example

    e "That's it! Hope this explains the code, [persistent.player_name]."

    jump ask_menu

label reset_game:

    show sylvie green normal at center with ease

    $ persistent.player_name = None

    e "Done! Let's restart!"

    jump start

label end_game:

    e "Oh man, you've got to leave so quickly?"

    show sylvie green smile at center with dissolve

    e "Goodbye! I'll miss you, [persistent.player_name]."

    return
