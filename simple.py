<<<<<<< HEAD
# # from translate import Translator
# from gettext import translation
import pyttsx3

# translator= Translator(from_lang="english", to_lang="german")
# translation = translator.translate("Good Morning")
# print(translation)

# engine = pyttsx3.init()
# engine.say(translation)
# engine.runAndWait()

# from googletrans import Translator
# import googletrans
# str="Hello World"

# translator = Translator()
# translations = translator.translate(str,dest="he")
# speak_engine.say(translation.text)
# speak_engine.runAndWait()
# print(googletrans.LANGUAGES)

# from googletrans import Translator

# translator = Translator()

# translated = translator.translate(str, src='en', dest='mr')

# print(translated.text)

engine = pyttsx3.init()

# engine.runAndWait()

from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()

# Assuming 'str' is the text you want to translate
text_to_translate = 'Hello Mumbai'  # Replace 'str' with the actual text you want to translate

translated = translator.translate(text_to_translate, src='en', dest='mr')
translated_text = translated.text

# Speak the translated text
tts = gTTS(text=translated_text, lang='mr')  # 'mr' is the language code for Marathi, change it to the desired language code
# engine.say(translated_text)
print(translated_text)
tts.save("translated.mp3")

os.system("mpg321 translated.mp3")  # or any other audio player you have installed
=======
# # from translate import Translator
# from gettext import translation
import pyttsx3

# translator= Translator(from_lang="english", to_lang="german")
# translation = translator.translate("Good Morning")
# print(translation)

# engine = pyttsx3.init()
# engine.say(translation)
# engine.runAndWait()

# from googletrans import Translator
# import googletrans
# str="Hello World"

# translator = Translator()
# translations = translator.translate(str,dest="he")
# speak_engine.say(translation.text)
# speak_engine.runAndWait()
# print(googletrans.LANGUAGES)

# from googletrans import Translator

# translator = Translator()

# translated = translator.translate(str, src='en', dest='mr')

# print(translated.text)

engine = pyttsx3.init()

# engine.runAndWait()

from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()

# Assuming 'str' is the text you want to translate
text_to_translate = 'Hello Mumbai'  # Replace 'str' with the actual text you want to translate

translated = translator.translate(text_to_translate, src='en', dest='mr')
translated_text = translated.text

# Speak the translated text
tts = gTTS(text=translated_text, lang='mr')  # 'mr' is the language code for Marathi, change it to the desired language code
# engine.say(translated_text)
print(translated_text)
tts.save("translated.mp3")

os.system("mpg321 translated.mp3")  # or any other audio player you have installed
>>>>>>> f6ad058038ff994e68179139f8be41e5415178a5
