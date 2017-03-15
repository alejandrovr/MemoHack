
from lyrics import songs

import unicodedata
import re

def remove_accents(input_str):
     nfkd_form = unicodedata.normalize('NFKD', input_str)
     only_ascii = nfkd_form.encode('ASCII', 'ignore')
     return only_ascii

def syllable(songwords,syllables):
    '''syllables is a list of the syllables defined by the user, 'ta-ble'-> ['ta','ble'].'''
    syllables=syllables.split('-')
    #first try an initials like approach.
    window_len=len(syllables)
    counter=0
    results=[]
    while len(songwords)>counter+window_len: #iterate over the words in the song
        window_words=[]
        for i in range(window_len):
            window_words.append(songwords[counter+i])
            
        flag=0
        for j in range(window_len):
            if not window_words[j].startswith(syllables[j]): #'abc'[::-1].startswith('cba') endswith
                flag=1
                
        if flag==0 and window_words not in results:
            results.append(window_words)
        counter+=1
        
    return results
        
def initials(songwords,user_input):
    all_results=[]
    counter=0
    memo=[]
    window=len(user_input)
    while len(songwords)>counter+window:
        windowstr=''
        result=[]
        for i in range(window):
            result.append(songwords[counter+i])
            windowstr+=songwords[counter+i][0] #first letter of all words inside the window

        if windowstr==user_input:
            print(result,windowstr)
            if result not in all_results:
                all_results.append(result)
        counter+=1
    return all_results

def regexsearch(songwords, syllables):
    syllables=syllables.split('-')
    regez=''
    for syl in syllables:
        regez=regez+'('+syl+'.*?)' #? avoids greedy behaviour
    songwords=' '.join(songwords)
    matches=re.search(regez, songwords)
    result=''
    if matches:
        for i in range(len(syllables)):
            result=result+'<br>'+syllables[i]+'</br>'+matches.group(i+1)[len(syllables)-1:]
    return result
    


def main(songs):
    user_input=str(input('What word you wanna learn?')).lower()
    syllables=str(input('Split in syllables the word:')).lower()
    initials_results=[]
    syllable_results=[]
    regex_results=[]
    for song in songs:
        song=song.lower()
        song=song.replace('.',' ')
        song=song.replace('!','')
        song=song.replace('?','')
        song=song.replace('¡','')
        song=song.replace('¿','')  
        song=song.replace('\n',' ')
        song=song.replace(',',' ')
        songwords=song.split(' ')
        songwords=[remove_accents(word).decode("utf-8") for word in songwords if word!='']
        
        #save result if any.
        inires=initials(songwords,user_input)
        if inires:
            initials_results.append(inires)
            
        syres=syllable(songwords,syllables)
        print('syres is' ,syres)
        if syres:
            syllable_results.append(syres)
            
        reres=regexsearch(songwords, syllables)            
        if reres:
            regex_results.append(reres)
    
    if len(initials_results)==0 and len(syllable_results)==0 and len(regex_results)==0:
        return 'No results found. Sorry, we are also dissapointed with ourselves. We payed a lot for our masters. Damm it.'
        
    return (initials_results,syllable_results, regex_results)
    

print(main(songs))
