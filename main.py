import json
import random
from win10toast import ToastNotifier
from winotify import Notification
from translate import Translator

toast = ToastNotifier()

with open('./phrases.json', 'r') as f:

     data=f.read()
dataParsed=json.loads(data)
length = len(dataParsed['commonWords'])

randomIndex = random.randint(0, length)
word = dataParsed['commonWords'][randomIndex]
translator = Translator(to_lang = 'ar')
translation = translator.translate(word)

toast = Notification(app_id="Learn Arabic",
                     title=word,
                     msg=translation,
                     icon=r"C:\\Users\\DELL\\Desktop\\pythonPrograms\\learnArabic\\icon.ico")

toast.show()