import random

a = 'It is clear to everyone that astronomy at all events compels the soul to look upwards, and draws it from the things of this world to the other - Plato'

c = 'Do there exist many worlds, or is there but a single world... This is one of the most noble and exalted questions in the study of Nature - Albertus Magnus'
d = 'The history of astronomy is a history of receding horizons - Edwin P. Hubble'
e = 'The boundary condition of the universe is that is has no boundary - Stephen Hawking'
f = 'This dead of midnight is the noon of thought, And Wisdom mounts her zenith with the stars - Anna Barbauld'
g = 'Two things fill the mind with ever new and increasing wonder and awe the starry heavens above me and the moral law within me - Immanuel Kant'
h = 'No one regards what is before his feet; we all gaze at the stars - Quintus Ennius'
i = 'Astronomy, as nothing else can do, teaches men humility - Arthur C. Clarke'
j = 'Astronomy taught us our insignificance in Nature - Ralph Waldo Emerson'
k = 'Astronomy is the science of the harmony of infinite expanse - Lord john Russel'



def generate():
    quote = random.choice([a, c, d, e, f, g, h, i, j, k])
    return quote

