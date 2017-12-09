import pygame as py

py.init()

#When ball cracks a multi-hit brick
crackSound = py.mixer.Sound('bad_disk_x.wav')
crackSound.play()

#When ball hits walls/paddles/etc.
boingSound = py.mixer.Sound('boing2.wav')
boingSound.play()

#When ball shatters a multi-hit brick
shatterSound = py.mixer.Sound('glass_shatter_c.wav')
shatterSound.play()

#when ball hits an unbreakable brick
steelSound = py.mixer.Sound('hammer_anvil3.wav')
steelSound.play()
