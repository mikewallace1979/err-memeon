from errbot import BotPlugin, botcmd
from random import choice, randint


class MemeOn(BotPlugin):

    memes = {
        "oh my": [
            "http://925rebellion.com/wp-content/uploads/2013/09/3q7rym.jpg",
            "http://media1.giphy.com/media/FoUHKTJhoQU6I/200_s.gif",
            "http://ruadouche.com/wp-content/uploads/2013/05/George-Takei-oh-my.jpg",
            "http://newnownext.mtvnimages.com/2013/11/george-takei-oh-my.png",
        ],
        "excellent": [
            "http://4.bp.blogspot.com/-w2dZIP16sew/TpE1L7g8IbI/AAAAAAAAAKA/kshUsHepP00/s1600/free-MrBurnsExcellent.gif",
            "http://www.scancrit.com/wp-content/uploads/2011/11/excellent-4689_preview.png",
            "http://static.rcgroups.net/forums/attachments/1/6/9/8/4/9/a2213358-88-mister-burns-excellent.jpg"
        ],
        "my kind of": [
            "http://www.biography.com/imported/images/Biography/Images/Profiles/S/Telly-Savalas-9542523-1-402.jpg"
        ],
        "yay": [
            "http://31.media.tumblr.com/0e9d3c5353afe255aab03101db5bc24c/tumblr_mjzn9l8cQ31r6ph6uo1_500.gif",
            "http://25.media.tumblr.com/tumblr_mdm2kdZZVz1rxdkjwo1_500.gif",
            "http://www.reactiongifs.com/wp-content/gallery/dance-party/willsmith.gif",
            "http://www.reactiongifs.com/wp-content/uploads/2013/11/stoked.gif"
        ],
        "savalas": [
            "http://upload.wikimedia.org/wikipedia/commons/9/90/Telly_Savalas_Kojak_1973.JPG",
            "http://images3.makefive.com/images/entertainment/movies/best-james-bond-bad-guys/ernst-stavro-blofeld-as-played-by-telly-savalas-7.jpg",
            "http://www.biography.com/imported/images/Biography/Images/Profiles/S/Telly-Savalas-9542523-1-402.jpg",
            "http://image1.findagrave.com/photos/2010/323/1832_129030321490.jpg",
            "http://img.kimdir.com/kimdir/t/e/5b16633ed7c0fb9a2fa50607696dfdd9e0eeaecb.jpg",
            "http://www.recordsale.de/cdpix/t/telly_savalas-sweet_surprise(1).jpg"
        ],
        "sad": [
            "http://www.mykindarain.com/wp-content/uploads/2011/10/no-one-likes-sad-panda-no-one-likes-sad-panda.jpg",
            "http://mashable.com/wp-content/uploads/2013/07/Dr.-Who.gif",
            "http://lookrobot.co.uk/files/2013/06/SadCat.jpg",
            "http://tearsoftime.com/wp-content/uploads/2012/07/katy-perry-crying.jpg",
        ],
        "dreams": [
            "http://cdn.shopify.com/s/files/1/0210/4540/products/urban_graphic_cards040_1024x1024.png"
        ],
        "lazy": [
            "http://cdn.shopify.com/s/files/1/0210/4540/products/urban_graphic_cards037_1024x1024.png"
        ],
        "kitten":[
            "http://cdn.sheknows.com/articles/2014/02/Mike/SheKnows_US/1029471/GIF5.gif",
            "http://www.cutecatgifs.com/wp-content/uploads/2014/02/soon.gif",
        ],
        "like a boss": [
            "http://upload.wikimedia.org/wikipedia/commons/4/4d/Bruce_Springsteen_1988.jpg",
            "http://i.imgur.com/aEG1ENr.jpg",
            "http://i.telegraph.co.uk/multimedia/archive/02604/Bruce_Springsteen_2604860k.jpg",
            "http://i.imgur.com/eHGYCrv.jpg",
            "http://audiophileparadise.files.wordpress.com/2012/07/bruce-springsteen-002.jpg",
            "http://www.peterguy.merseyblogs.co.uk/bruce-springsteen.jpg",
            "http://www.legacyrecordings.com/media/cache/86/26/86268187fb270d1f4af374b3ef28d53b.jpg",
            "http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2009/5/25/1243248389162/Bruce-Springsteen-And-The-003.jpg",
            "http://the-flack.com/wp-content/uploads/2014/02/Bruce-Springsteen-1.jpg",
            "http://static.tvtropes.org/pmwiki/pub/images/bruce-springsteen.jpg",
            "http://imgur.com/93k3zBe",
            "http://marshallmatlock.com/wp-content/uploads/2011/05/bruce-springsteen-banner.jpg",
        ],
        "heard": [
            "http://imgur.com/WNf5vJj.jpg",
            "http://www.eabf.org.uk/upload/news/dame-thora-hird.jpg",
            "http://bonfirehealth.com/wp-content/uploads/2011/09/herd.1.gif",
            "http://upload.wikimedia.org/wikipedia/commons/5/5a/Wilderbeest.jpg",
            "http://upload.wikimedia.org/wikipedia/commons/a/a9/Herd_Of_Goats.jpg"
        ],
        "love": [
            "https://www.youtube.com/watch?v=xhrBDcQq2DM",
            "http://www.grammy.com/files/styles/news_photos/public/news/haddaway3.jpg",
            "http://www.becomethesinger.com/wp-content/uploads/2012/11/Haddaway-what-is-love-lyrics-300x197.jpg",
            "http://pixhost.me/avaxhome/2007-06-04/BitmapI79.jpg",
            "http://cdn.7static.com/static/img/sleeveart/00/031/227/0003122749_500.jpg"
        ]
    }

    def callback_message(self, conn, mess):
        body = mess.getBody().lower()

        for meme in self.memes:
            if body.startswith(meme.replace(' ', '')):
                self.send(
                    mess.getFrom(),
                    choice(self.memes[meme]),
                    message_type='groupchat'
                )
                break
            if body.find(meme) != -1 and randint(1, 10) <= len(self.memes[meme]):
                self.send(
                    mess.getFrom(),
                    choice(self.memes[meme]),
                    message_type='groupchat'
                )

    @botcmd
    def sealion(self, mess, args):
        return "http://i.imgur.com/bmfwvDl.gif"

    @botcmd
    def polarpalm(self, mess, args):
        return "http://www.reactionface.info/sites/default/files/images/1310561236052.jpg"
