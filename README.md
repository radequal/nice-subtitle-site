# Nice Subtitle Site - User Guide
A subtitle workflow used for live streams.

## Introduction
The Nice Subtitle Site is a simple web UI that allows anyone on the web to create subtitle sessions. These sessions are split into two use cases
* __Write__ subtitles
* __Read__ subtitles

Whatever gets written in the “write” tab, gets saved in a temporary database, ready for viewing by anyone who has the “view” tab. The “write” tab has very few options, including adding text to the session. This is done simply by writing in the input box and hitting enter. There are also options for switching the text direction to LTR or RTL, and wiping the history clean.

The “view” tab has several options on how to display the content that was inputted in the “write” tab, including:
* The refresh cycle
  How often the “view” tab asks the database for new messages. Default = 1000 ms
* Background colour
  The colour of the background of where the content is displayed
* Font colour / Font size
  The colour and size of the subtitles
* Box height
  The height of the box where the content gets displayed
* Padding
  The padding of the box where the content gets displayed
* Text direction
  Direction of the subtitles, this is useful for RTL languages, e.g. Farsi and Arabic

There’s also a button to wipe the session data. This removes the content that was previously added to the database.

## Where’s the code?
The code is hosted on App Engine. A copy of the code has been uploaded to:
https://github.com/radequal/nice-subtitle-site

If you’d like to host a Nice Subtitle Site yourself, this is a good guide:
https://developer.mozilla.org/en-US/docs/Learn/Common_questions/How_do_you_host_your_website_on_Google_App_Engine

## How to use the site
Simple, follow the following steps, split out by user role.

__If you DON’T already have a session__
* Go to https://nss-app.appspot.com
* Start a new session by clicking the button “New session”
* Pick a suitable name, and a unique link will be created for you
* You can share this link with all parties that will be viewing or writing subtitles

__Writer__
* Open the session link
* Click on “Write subtitles”
* Whatever you write in the input box will be visible to the “viewer”

__Viewer__
* Open the session link
* Click on “View subtitles”
* Whatever the writer enters will appear in the box at the bottom of the screen
* You have options to customise the look and feel of the output, and how often to check back for new messages
