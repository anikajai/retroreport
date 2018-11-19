// // ES6 / TypeScript
// import { getSubtitles } from 'youtube-captions-scraper';
//
// getSubtitles({
//   videoID: 'd39c7STZal4', // youtube video id
//   lang: 'fr' // default: `en`
// }).then(captions => {
//   console.log(captions);
// });

// // ES5
var getSubtitles = require('youtube-captions-scraper').getSubtitles;
const express = require('express');
const cors = require('cors');

const app = express();
const port = 3000;
app.use(cors());
app.use(express.static('static'))

app.get('/captions/:videoID', (req, res) => {
    getSubtitles({
        videoID: req.params.videoID, // youtube video id
        lang: 'en' // default: `en`
    }).then(function(captions) {
        res.send(captions);
    }).catch(err =>{
        res.send(404)
        console.log(err)
    });
});

app.get('/:videoID', (req, res) => {
    videoId = req.params.videoID;
   res.send('<!DOCTYPE html>\n' +
       '<html>\n' +
       '<head>\n' +
       '<meta charset="UTF-8">\n' +
       '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n' +
       '<script src="youtube.js"></script>\n' +
       '<link rel="stylesheet" href="youtube.css">\n' +
       '<body>\n' +
       '<p><iframe id="'+videoId +'" src="https://www.youtube.com/embed/'+videoId +'?enablejsapi=1" width="560" height="315" allowfullscreen="allowfullscreen"></iframe></p>\n' +
       '<div id="videoTranscript'+videoId +'" class="mmocVideoTranscript" data-language="en" data-name=""></div>\n' +
       '</body>\n' +
       '</html>');
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
