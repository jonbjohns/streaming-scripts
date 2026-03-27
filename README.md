# streaming-scripts
A set of scripts I've created for use while streaming on twitch

Since these are mostly one off scripts, I'm not creating a separate repo for each one.

getWTF
This is based on WTFEngine https://github.com/soulwire/WTFEngine. However instead of 
using javascript, this is based on python for just personal preference. I currently
embed this within mixitup as a twitch point incentive. However, I'm not documenting
that flow I use at the moment. For a short summary, if you want to use WTFEngine as
a terminal output or to send to some other api, this is a good starting point to
remix.

Contents
getWTF.py
The main script. Expected to run by 
python getWTF.py option
option - a value in the match/case section in the code

sample.json
Same format from WTFEngine. 
