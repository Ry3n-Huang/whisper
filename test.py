'''
# https://blog.csdn.net/m0_52156129/article/details/129263703?spm=1001.2014.3001.5502
'''


import whisper
# model = whisper.load_model("base")
# result = model.transcribe("Path")
# print(result["text"])

class Asr():
    def __init__(self):
        self.model = whisper.load_model("base")

    def predcit(self, wavpath):
        result = self.model.transcribe(wavpath)
        return result["text"]

 
# if __name__=="__main__":
#     asr = Asr()
#     result = asr.predcit("audio.mp3")
#     print(result)






