scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def major_scale(note):

    for i in range(len(scale)):
        if ascii(note) == ascii(scale[i]):
            true_note = i
            break
        else:
            continue

    if true_note + 12 > len(scale):
        for j in range(-1, -13, -1):
            if ascii(scale[j]) == ascii(scale[true_note]):
                negindex = j
                return scale[negindex], scale[negindex + 2], scale[negindex + 4], scale[negindex + 5], scale[negindex + 7], scale[negindex + 9], scale[negindex + 11]
                break
            else:
                continue
    else:
        return scale[true_note], scale[true_note + 2], scale[true_note + 4], scale[true_note + 5], scale[true_note + 7], scale[true_note + 9], scale[true_note + 11]
        
x = input('Enter root note: ')

print(major_scale(x))

    
