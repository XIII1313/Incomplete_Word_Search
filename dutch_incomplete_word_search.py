import urllib.request


req = urllib.request.Request("https://raw.githubusercontent.com/titoBouzout/Dictionaries/master/Dutch.dic")
resp = urllib.request.urlopen(req)
data = resp.read().decode("utf8")
dirty_data_split = data.split("\n")
dutch_word_list = [word.split("/")[0] for word in dirty_data_split]
dutch_word_list_fixed = [word.replace("ĳ", "ij") for word in dutch_word_list]
hit_list = []


def find_word(target_word: str) -> None:
    target_word_length = len(target_word)
    for suspect_word in dutch_word_list_fixed:
        if target_word_length != len(suspect_word):
            continue
        else:
            counter = 0
            while counter < target_word_length:
                target_letter = target_word[counter]
                if target_letter != "*":
                    if target_letter != suspect_word[counter]:
                        break
                if counter == target_word_length-1:
                    hit_list.append([suspect_word, len(suspect_word)])
                counter += 1


find_word("v**en")


print(hit_list)
