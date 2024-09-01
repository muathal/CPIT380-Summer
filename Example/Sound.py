from jes4py import *
def normalize(sound):
  largest = 0
  for s in getSamples(sound):
    if getSampleValue(s) > largest:
      largest = getSampleValue(s)
  amplification = 32767.0 / largest
  print ("Largest sample value in original sound was", largest)
  print ("Amplification factor is", amplification)
  for s in getSamples(sound):
    louder =  amplification * getSampleValue(s)
    setSampleValue(s, louder)

def merge():
  muath = makeSound(getMediaPath("../sound/muath.wav"))
  mute = makeSound(getMediaPath("../sound/mute.wav"))
  section = makeSound(getMediaPath("../sound/section.wav"))
  index = 0
  for source in range(0, getLength(muath)):
    value = getSampleValueAt(muath, source)
    setSampleValueAt(mute, index, value)
    index = index + 1
  for source in range(0, int(0.1*getSamplingRate(mute))):
    setSampleValueAt(mute, index, 0)
    index = index + 1
  for source in range(0, getLength(section)):
    value = getSampleValueAt(section, source)
    setSampleValueAt(mute, index, value)
    index = index + 1
  normalize(mute)
  print(getSamplingRate(mute))
  muathit = makeEmptySound(325109,44100)
  for source in range (0,getLength(muathit)):
    value = getSampleValueAt(mute,source)
    setSampleValueAt(muathit,source,value)
  writeSoundTo(muathit,"../sound/muathIT.wav")
merge()