from googletrans import Translator
translator=Translator()
text=input('Enlish text enter:')
obj=translator.translate(text=text,dest='uz',src='en')
print(obj.text)

