import json
from difflib import get_close_matches

dataset = json.load(open("thesaurus_raw_data.json"))

def translate(w):
    if w in dataset:
         return dataset[w]
    elif w.title() in dataset:
         return dataset[w.title()]
    elif w.upper() in dataset:
         return dataset[w.upper()]
    elif len(get_close_matches(w, dataset.keys()))>0 :
         yn = input('Did you mean %s instead ? Y/N : '%get_close_matches(w,dataset.keys())[0]).upper()
         if yn == 'Y':
               return dataset[get_close_matches(w, dataset.keys())[0]]
         elif yn == 'N':
               return 'The word does not exist. Please check it.'
         else :
               return 'We did not understand your entry.'
                  
    else:
        return ('The word does not exist. Please check it.')

resp = 'Y'
while resp == 'Y':
    word = input('\nEnter word : ')
    out = translate(word)

    if type(out) == list:
        for item in out:
               print(item)
    else :
        print(out)

    resp = input('\nDo you wish to search again ? Y/N : ').upper()
    if resp != 'Y':
        break
        
        
