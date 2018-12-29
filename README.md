# retroreport
RetroReport's technical website enhancements


## 1)Install youtube-captions-scraper

* `> npm install -S youtube-captions-scraper` OR
* `> yarn add youtube-captions-scraper`

## 2) Download Youtube 
*    Run node usage.js on command line.
*    Edit angular-retro.html http://192.168.1.138:3000/ value to the system running node usage.js's IP address and port as 3000.
*    Run angular-retro.html on a browser.
*      Cureently search match works on abstract and title of the video, due to limitations of memory size of keeping synonym list.

##3) familyOfWords.py 
*     This file is used to generate the synonyms, hypernyms, meronyms and most simlar words from google word list for the words in for-synonyms.txt. The output file is in synonyms-extended.txt.

##4) algolia-index.py
 *   Copy content of for-synonyms.txt contents in this file. This is the file that can be used to upload these extended words to the algolia synonym list. Kindly upload at max 70 such pairs at a call.
 
 ##5) The features impacted by this minimum viable product is:
  *  search is smarter as it is not only searching on exact text in tarnscript but on similar words too. Like weather can match rainfall too!
  *  search results should be ordered in the descending order of pulication date.
  *  the results count should be displayed.
  *  Both the transcript and the video link should be presented.
  *  The videos should be manually/technically tagged with special search keywords that may not be in the transcript text.
  *  The user when selects the link of the result they can go to the window where the video will be dragged to begin on the click of the selected text.
   
     
