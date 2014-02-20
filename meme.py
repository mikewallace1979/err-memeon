from errbot import BotPlugin
from random import choice, randint


class MemeOn(BotPlugin):

    memes = {
        "oh my": [
            "http://925rebellion.com/wp-content/uploads/2013/09/3q7rym.jpg",
            "http://media1.giphy.com/media/FoUHKTJhoQU6I/200_s.gif",
            "http://ruadouche.com/wp-content/uploads/2013/05/George-Takei-oh-my.jpg",
            "http://newnownext.mtvnimages.com/2013/11/george-takei-oh-my.png",
        ],
        "savalas": [
            "http://upload.wikimedia.org/wikipedia/commons/9/90/Telly_Savalas_Kojak_1973.JPG",
            "http://images3.makefive.com/images/entertainment/movies/best-james-bond-bad-guys/ernst-stavro-blofeld-as-played-by-telly-savalas-7.jpg",
            "http://www.biography.com/imported/images/Biography/Images/Profiles/S/Telly-Savalas-9542523-1-402.jpg",
            "http://image1.findagrave.com/photos/2010/323/1832_129030321490.jpg",
            "http://img.kimdir.com/kimdir/t/e/5b16633ed7c0fb9a2fa50607696dfdd9e0eeaecb.jpg",
            "http://www.recordsale.de/cdpix/t/telly_savalas-sweet_surprise(1).jpg"
        ]
    }

    def callback_message(self, conn, mess):
        body = mess.getBody().lower()
        for meme in self.memes:
            if body.find(meme) != -1 and randint(1, 10) == 1:
                self.send(
                    mess.getFrom(),
                    choice(self.memes[meme]),
                    message_type='groupchat'
                )
