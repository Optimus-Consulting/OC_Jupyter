
# Utility program to find pron for a word...
from balautil import requestutil as R

def find_value_in_dict_recursively(d, cond_f, path=None, values=[]):
    #print(d,)
    if isinstance(d, dict):
        for k,v in d.items():
            if isinstance(v, str):
                if cond_f(v):
                    #print(v, path)
                    values.append(v)
            if isinstance(v, (list,dict)):
                find_value_in_dict_recursively(v, cond_f, path=str(path) +f'["{k}"]',values=values)

    if isinstance(d, list):
        for i, o in enumerate(d):
            find_value_in_dict_recursively(o, cond_f,  path=str(path)+f"[{i}]", values=values)

def get_pron_for_word(word):
    url = f"https://api.pearson.com/v2/dictionaries/entries?headword={word}"
    data = R.Get(url)
    list_of_urls = []
    
    f = lambda x: str(x).endswith(".mp3")
    find_value_in_dict_recursively(data ,  f, values=list_of_urls)
    list_of_urls = [ "https://api.pearson.com" + u for u in list_of_urls]
    return list_of_urls
