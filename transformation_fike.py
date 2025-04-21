
import string
import random

#have to repeat translation tho...
# Initialize EasyNMT for translation
from easynmt import EasyNMT

model_name = 'mbart50_m2m'
# Create the translator
translator = EasyNMT(model_name=model_name, language_detection = 'fasttext')

string22 = ("I was talking of ladies smiling in the eyes of gentlemen; and of late so many smiles have been shed into Mr. Rochester’s eyes that they overflow like two cups filled above the brim: have you never remarked that?")

string2 =" The flame flickers in the eye; the eye shines like dew; it looks soft\
and full of feeling; it smiles at my jargon: it is susceptible;\
impression follows impression through its clear sphere; where it ceases\
to smile, it is sad; an unconscious lassitude weighs on the lid: that\
signifies melancholy resulting from loneliness. It turns from me; it\
will not suffer further scrutiny; it seems to deny, by a mocking\
glance, the truth of the discoveries I have already made,—to disown the\
charge both of sensibility and chagrin: its pride and reserve only\
confirm me in my opinion. The eye is favourable."


def replace_word(string, term):
    word = random.choice(string.split(' '))
    string = string.replace(word, term)
    return string, word

def translate_word_to_en(word):
    translated_word= translator.translate(word, target_lang='en')
    return translated_word


def translate_word_to_it(word):
    translated_word = translator.translate(word, target_lang='it')
    return translated_word

print(replace_word(string22, 'chicken'))

en_term = random.choice(string22.split(' '))

term_in_it = translate_word_to_it(en_term)

term_in_en = translate_word_to_en(term_in_it)


print(replace_word(string22, term_in_en))








