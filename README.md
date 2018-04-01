# NTUOSS Create Your Own Waifu Workshop
#### Create your context-aware smart waifu in 1 hour or less!

*by [Jarrett Yeo](https://github.com/jarrettyeo) and [Clarence Castillo](https://github.com/clarencecastillo) for NTU Open Source Society*

*Date last updated: 30 March 2018*

___

## **Overview**

This workshop will teach you how to create your own context-aware waifu using Python and visual novel creator Ren'Py. Do cool things with your digital waifu:

1. Your waifu will read jokes for you using ```urllib2```,

2. She'll talk about her day and she'll ask you about yours; your waifu will respond appropriately using ```TextBlob``` and ```nltk``` via sentiment analysis,

3. She'll update you on the weather using Open Weather's JSON API,

4. And best of all your waifu will magically albeit hackily sync your NTUlearn files (well, most of them) just like how Dropbox seamlessly does using ```Blackbox```.

## **Workshop Structure**

Here's what we'll be doing:

1. We'll go through together how Ren'Py roughly works using Ren'Py's default well-crafted tutorial (15 mins),

2. Talk briefly about some simple Pythonic concepts that we'll be using (10 mins),

3. And finally add the above features to our visual novel waifu (30 mins)!

## **Pre-Requisites**

Here's what we need:

1. A text editor like Sublime Text or Atom,

2. [Ren'Py 6.99.14.2](https://www.renpy.org/latest.html) downloaded and installed to your Desktop,

3. [Python 3.6](https://www.python.org/downloads/) with ```pip```,

4. The following dependencies installed using ```pip``` via your console:

Windows:

```
$ pip install selenium, nltk, textblob
```

Mac:

```
$ sudo pip3 install selenium, nltk, textblob 
```

5. And finally, some ```corpora``` lite pre-trained sentiment analysis data:

Windows:

```
$ python -m textblob.download_corpora lite
```

Mac:

```
$ python3 -m textblob.download_corpora lite
```

The above might take 5-10 mins to set up.
___

## Questions

If you have a question regarding any of the instructions here, feel free to raise your hand any time during the pre-workshop or email your questions to [me](mailto:shanwei96@gmail.com).

## Errors

For errors, typos or suggestions, please do not hesitate to [post an issue](https://github.com/jarrettyeo/Waifu-Creator/issues/new). Thank you!

## **Disclaimer**

Neither the author nor NTU OSS claims or owns the appended resources. We also do not accept any responsibility for things that happen to your machine or you because of this tutorial.

___

# **Step 0 - Introduction to Ren'Py**

## *What's the big deal?*

Ren'Py is an extremely simple-to-use visual novel creator that lets you to create professional-looking visual novels quickly. It pretty much takes care of everything for you - scene transitions, dialogues, persistent game variables such as HP or money and so on.

## *Is it Python?*

Even simpler. If you thought Python was easy, Ren'Py is easier.

The native Ren'Py language (.rpy) is not Python (.py) but is heavily influenced by Python. Its quirks to make visual novel development easy (such as ```jump``` or scene changes).

It allows external Python code to be embedded within Ren'Py itself. Just start the indented code of block with the header ```python:``` or your statement with ```$```.

We'll be implementing these later.

## *Limitations*

Ren'Py however does not support third-party Python libraries well.

Using them will usually entail a somewhat hacky way of executing Python scripts (.py) using your machine's shell, but it's good enough for us!

___

# **Step 1 - Ren'Py Tutorial**

## **Overview**

Let's quickly get started!

## **DIY 1 - Go through the basic tutorials (15 mins)**

Now that you have Ren'Py installed, double-click on the Ren'Py executable and then launch the tutorial.

Go through the first few tutorials. It should take you 15 minutes or less. You can go through it yourself, and if you're fast you can also explore the more advanced tutorials too while we wait for the rest.

Don't worry if you do not understand everything, we will be explaining as we go along implementing our waifu features.

___

# **STEP 2A - Basic Pythonic Concepts Used in Ren'Py**

## **Overview**

Now we'll go through a few basic concepts that will help you in learning both Ren'Py and Python.

Because these concepts are really simple to grasp, we'll just explain briefly:

## **Pythonic Code vs Ren'Py Code**

Every .rpy file contains both code written in native Ren'Py code and in Python.

Python code are distinguished using two ways:

1. One-liner using ```$```

Python one-liners can be denoted by using ```$``` at the start tof the sentence.

```
$ import requests
```

2. Code Blocks using ```python:``` as header

When you need to write multiple lines of Python code, you can use ```python:``` to signpost that the indented code that follows is meant to be run as Python code:

```
python:

# python code starts below

    import requests
    import datetime

    hour_now = datetime.datetime.now().hour

# Ren'Py code starts below

    define e = Character("Sylvie")
```

3. All other code is written in Ren'Py

As seen above, all other code written without ```$``` or not under a ```python:``` header will be executed as Ren'Py code.

## **Other Things to Note**

We'll be explaining the following briefly:

1. (chapter) label / jump (to chapter)

2. play (music)

3. (display) scene

4. show (character)

5. (display) menu
___

# **STEP 2B - Creating Our First Project in Ren'Py**

## **Overview**

Now that we know a bit more about Ren'Py, it's time to create our own project!

## **DIY 2A - Creating Your Project**

Open Ren'Py and click on "Create New Project". **When prompted, select your Desktop as the working directory.** This will make it easier for us to access our files later.

Click Continue, and for the project name, key in "Waifu-Creator" without the quotes. 

The default screen resolution of 1280 x 720 should already be selected for you. Click Continue.

Ren'Py will prompt you for the color scheme. You can select any, but we recommend the default easy-to-see blue scheme.

Ren'Py will take a while to create the project for you...

And we're done!

Ren'Py will now show you "Waifu-Creator" on the main menu. Let's select it, and click on Launch Project.

Once Rem'Py has spawned our new game, you should see a boring main menu. Let's click on Start. 

A spooky silhouette called Eileen will tell you that you've created your new game in Ren'Py! Yay!

## **DIY 2B - Downloading the Workshop Repository**

Let's download our workshop repo by right-clicking and saving the zip anywhere on your computer [here](https://github.com/jarrettyeo/Waifu-Creator/archive/master.zip). Next, open the zip folder and click into the ```Waifu-Creator-master``` folder. Extract all files and folders inside the ```Waifu-Creator-master``` folder into your ```Waifu-Creator``` folder on your Desktop. All files and folders from your original project can be safely replaced.

Your ```Waifu-Creator``` directory should look *something* like this:

```
/Desktop

    /Waifu-Creator

        /game
            /01example.rpy
            /blackbox.py
            /chromedriver(.exe)
            /examples.rpy
            /gui.rpy
            /illurock.opus
            /keywords.py
            /options.rpy
            /screens.rpy
            /script.rpy
            /sentiment.py

            /gui
                /frame.png
                /game_menu.png
                /main_menu.png
                /namebox.png
                /notify.png
                /nvl.png
                /skip.png
                /textbox.png
                /window_icon.png

                /bar
                    /Various images...

                /button
                    /Various images...

                /overlay
                    /Various images...

                /phone
                    /Various images...
                
                /scrollbar
                    /Various images...

                /slider
                    /Various images...  

            /images
                /bg club.jpg
                /bg lecturehall.jpg
                /bg meadow.jpg
                /bg uni.jpg
                /sylvie blue giggle.png
                /sylvie blue normal.png
                /sylvie blue smile.png
                /sylvie blue surprised.png
                /sylvie green giggle.png
                /sylvie green normal.png
                /sylvie green smile.png
                /sylvie green surprised.png
```

It doesn't really matter if there are other files in your directory. Just leave them.

## **DIY 2C - Install the Required Dependencies**

In case you have forgotten to download the required packages, remember to open your console and execute:

#### **Download 1 - pip packages**

Windows:

```
$ pip install selenium, nltk, textblob
```

Mac:

```
$ sudo pip3 install selenium, nltk, textblob 
```

#### **Download 2 - corpora lite pre-trained NLP data**

Additionally, download some ```corpora``` lite pre-trained sentiment analysis data as well:

Windows:

```
$ python -m textblob.download_corpora lite
```

Mac:

```
$ python3 -m textblob.download_corpora lite
```

___

# **STEP 3 - Our Waifu is Alive!**

## **Overview**

The most exciting part of this workshop so far - finally, we will be saying hi to our waifu!

## **DIY 3A - Launch Waifu!**

If you have the Waifu-Creator default game running, close it first.

From Ren'Py, relaunch our game. 

___

# **STEP 4 - The Rest of the Workshop**

## **Overview**

"Wait that's it? Where's the rest of the tutorial?""

We are trying out something different today! We will be explaining the rest of the workshop in your Ren'Py itself!

Your game will talk directly to our server and all of us will be able to enjoy an interactive tutorial. As we move along, our server will update your game to unlock new content for you. Pretty cool, ain't it!
___

# **The End!**

## **Closing Remarks**

That's all we have for this workshop. Go forth and create your waifu! What are other things that you can think of implementing?

Off the top of Sylvie's head, she's thinking about reading real news headlines to you. And maybe searching for Events to go on dates with you (we really did code that and then Cambridge Analytica happened and Facebook's Event API is temporarily frozen).

Maybe Sylvie will have more cool features developed for you in our Waifu-Creator V2.0 workshop next semester. Stay tuned!

## **More Resources**

If you need more information, it probably is in the Python and Ren'Py docs.

If you need tons and tons of cool visuals such as character sprites and backgrounds etc., the Internet is [your oyster](https://steamcommunity.com/app/345370/discussions/0/611701360822466443/).
___

## **Sources**

The resources which we have mainly relied on, other than the docs, are from Ren'Py's tutorial and the example game which were shipped with Ren'Py. 

## **Acknowledgements**

Explanations of how our code works is largely borrowed directly or indirectly from the docs or its authors.

Much of our code structure, visuals and audio is taken from the default tutorial and example game shipped with Ren'Py.

We claim no credit to any resources not belonging to us in our course of writing and conducting this free workshop.

## **Missing References?**

While we have made sure our acknowledgements is as comprehensive as possible, please forgive us if we left any out. We promise to update our references accordingly. Cheers!

___

## Test Info

This tutorial has been tested using a Windows 10 computer running Home 10.0.16299 and (coming soon- a MacBook Air running OS X Version 10.9.5. Both are run on Python 3.6.3). It is accurate as of 1 April 2018.

## Acknowledgements

Many thanks to [Chang Kai Lin, Ries](https://www.instagram.com/kailinchanggg/) for sacrificing her MacBook Air and loaning it to me indefinitely for testing, and the [NTU Open Source Society](https://github.com/ntuoss) committee for making this happen!