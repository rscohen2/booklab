
""" Lost in translation
 The goal of this project is to take text, transform it using roundtrip translation on a random word within the string, and return the transformed string."""

import string
import random
import nltk

nltk.download('punkt_tab')

#have to repeat translation tho...
# Initialize EasyNMT for translation
from easynmt import EasyNMT

model_name = 'mbart50_m2m'
# model_name = 'opus-mt'
model = EasyNMT(model_name)



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
    translated_word= model.translate(word, target_lang='en')
    return translated_word


def translate_word_to_it(word):
    translated_word = model.translate(word,source_lang='en', target_lang='it')
    return translated_word



def roundtrip_translation(string):
    # orig_word = random.choice(string.split(' '))
    # print(orig_word)
    string = translate_word_to_it(string)
    # print(word)
    string = translate_word_to_en(string)
    # print(word)
    # string = string.replace(string, word)
    # print(string)
    return string

# def iterate_50_translations(string2):
#     string_result = string2
#     for _ in range(50):
#         string_result = roundtrip_translation(string_result)
#     return string_result

print(roundtrip_translation(string22))
