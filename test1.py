from test import Asr



if __name__=="__main__":
    asr = Asr()
    result = asr.predcit("audio.mp3")
    print(result)