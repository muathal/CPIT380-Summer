from jes4py import *
def IncDecSound(s):
    sampleArray = getSamples(s)
    for sample in sampleArray:
        value = getSampleValue(sample)
        if value > 0:
            setSampleValue(sample,int(value*.5))
        else:
            setSampleValue(sample,int(value*2))
fileName= pickAFile()
sound = makeSound(fileName)
IncDecSound(sound)
play(sound)

def speedSound(s):
    sampleRate = getSamplingRate(s)
    sampleArray = getSamples(s)
    sound = makeEmptySound(len(sampleArray),sampleRate *2)
    i = 0
    for sample in sampleArray:
        value = getSampleValue(sample)
        setSampleValueAt(sound,i,value)
        i += 1
    return sound
fileName= pickAFile()
sound = makeSound(fileName)
nsound =speedSound(sound)
play(nsound)
def slowSound(s):
    sampleRate = getSamplingRate(s)
    sampleArray = getSamples(s)
    sound = makeEmptySound(len(sampleArray),int(sampleRate/2))
    i = 0
    for sample in sampleArray:
        value = getSampleValue(sample)
        setSampleValueAt(sound,i,value)
        i += 1
    return sound
fileName= pickAFile()
sound = makeSound(fileName)
nsound =slowSound(sound)
play(nsound)
