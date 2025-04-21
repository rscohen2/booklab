
import string
import random

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
    length = len(string.split(' '))
    word = random.choice(string.split(' '))
    string = string.replace(word, term)
    return string, word

def translate_word(word):
    pass

print(replace_word(string22, 'chicken'))



