from collections import OrderedDict
import matplotlib.pyplot as plt
import json

def load_vmf():
    '''
    Loads a VMF file into memory.
    '''
    with open('../bwv108.6.vmf') as data_file:
        data = json.load(data_file)

    return data

def get_label(pitch_class, octave):
    '''
    Determines the appropriate label for this pitch
    '''
    if pitch_class is 0:
        return 'C' + str(octave)
    elif pitch_class is 1:
        return 'C#' + str(octave)
    elif pitch_class is 2:
        return 'D' + str(octave)
    elif pitch_class is 3:
        return 'D#' + str(octave)
    elif pitch_class is 4:
        return 'E' + str(octave)
    elif pitch_class is 5:
        return 'F' + str(octave)
    elif pitch_class is 6:
        return 'F#' + str(octave)
    elif pitch_class is 7:
        return 'G' + str(octave)
    elif pitch_class is 8:
        return 'G#' + str(octave)
    elif pitch_class is 9:
        return 'A' + str(octave)
    elif pitch_class is 10:
        return 'A#' + str(octave)
    elif pitch_class is 11:
        return 'B' + str(octave)

vectorMusic = load_vmf()
body = vectorMusic['body']

LABELS = [
    'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1',
    'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2',
    'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',
    'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4',
    'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5',
    'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6',
    'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7',
]

# Initialize data structure
pitches = OrderedDict()

for label in LABELS:
    pitches[label] = []

fig, ax = plt.subplots()
fig.set_size_inches(20, 20)

currentNote = None
currentLabel = None
currentTick = 1

for tick in body:
    # Deal with one part for now.
    part = tick[0]

    if part[0] is 1:
        if currentNote is not None:
            pitches[currentLabel].append(currentNote)

        currentLabel = get_label(part[3], part[4])
        currentNote = (currentTick, 1)
    elif part[0] is 2:
        currentNote = (currentNote[0], currentNote[1] + 1)
    else:
        if currentNote is not None:
            pitches[currentLabel].append(currentNote)

    currentTick += 1

height = 10

for label, data in pitches.items():
    ax.broken_barh(data, (height, 10), facecolors='green')
    height += 10

ax.set_xlabel('seconds since start')
ax.set_yticks([x for x in range(10, 860, 10)])

ax.set_yticklabels(LABELS)

plt.savefig('out.png')