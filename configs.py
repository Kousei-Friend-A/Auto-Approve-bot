from os import path, getenv

class Config:
    API_ID = 17945796
    API_HASH = "4a05481a5da2d66f801acffc4ca5ee4b"
    BOT_TOKEN = "5700920410:AAEk8j5NZb6wiIVuu3-NS6AL243bl57EpvU"
    FSUB = getenv("FSUB", "SDBotz")
    CHID = -1001874063925
    SUDO = 5152809878
    MONGO_URI = "mongodb+srv://manu911:manu911@cluster0.frtlbqt.mongodb.net/?retryWrites=true&w=majority"
        
cfg = Config()
