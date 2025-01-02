from AnieXMusic.core.bot import FIXX
from AnieXMusic.core.dir import dirr
from AnieXMusic.core.git import git
from AnieXMusic.core.userbot import Userbot
from AnieXMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = FIXX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
