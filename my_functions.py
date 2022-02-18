keys = {
    'C': 1,
    'B#': 1,
    'Db': 2,
    'C#': 2,
    'D': 3,
    'Eb': 4,
    'D#': 4,
    'E': 5,
    'F': 6,
    'E#': 6,
    'F#': 7,
    'Gb': 7,
    'G': 8,
    'Ab': 9,
    'G#': 9,
    'A': 10,
    'Bb': 11,
    'A#': 11,
    'B': 12
}

def get_key(val, my_dict): #get they key from value of a dictionary
    for key, value in my_dict.items():
         if val == value:
             return key

def transpose_key(key, point=0): #transpose the key by [point] levels
    level = keys[key]
    level += point
    
    if level < 1:
        level = 12 + level
    
    if level > 12:
        level -= 12
    
    return get_key(level, keys)

def transpose_song(song, point=0): #transpose the whole song, which is a string by [point] levels
    res = [i + 1 for i in range(len(song)) if song.startswith('[', i)]
    for i in range(len(song)):
        if song.startswith('[', i):
            i += 1
            index = -1
            for j in range(i, len(song)):
                if song.startswith(']', j):
                    index = j
                    break
            
            buffer = 0
            
            key = song[i:j+1].replace(" ", "")
            if key[1] == 'b' or key[1] == '#':
                key = key[:2]
                buffer = 2
            else:
                buffer = 1
                key = key[0]
            
            song = song[:i] + song[i:j].replace(' ', '') + song[j:]
            song = song[:i] + transpose_key(key, point) + song[i+buffer:]
    return song
        
