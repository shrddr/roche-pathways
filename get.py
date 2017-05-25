#import requests
import httpproxy
from PIL import Image
from io import BytesIO

URL = 'http://mapserver1.biochemical-pathways.com/map1/{l}/{z}/{x}/{y}.png?v=4'
layers = ['background', 'substrates', 'regulatoryEffects', 'unicellularOrganisms', 'higherPlants', 'enzymes']
zoom = 5
xcount = 3#27
ycount = 3#19
xsize = 1024
ysize = 1024
           
def make_tile(x, y):
    
    print('reading ({} {})'.format(x, y))
    tile = Image.new('RGB', (xsize,ysize), (255,255,255,255))
    
    for l in layers:
        try:
            #r = requests.get(URL.format(l=l,z=zoom,x=x,y=y)).content
            r = httpproxy.get(URL.format(l=l,z=zoom,x=x,y=y))
            i = Image.open(BytesIO(r))
            if i.size == (xsize,ysize):
                i = i.convert('RGBA')
                tile.paste(i, (0,0), i)
            
        except Exception as e:
            print('error: {}'.format(e))
            
    return tile
           
canvas = Image.new('RGB', (xcount*xsize,ycount*ysize))

for x in range(0, xcount):
    for y in range(0, ycount):
        tile = make_tile(x, y)
        canvas.paste(tile, (x*xsize,y*ysize))           
  
canvas.save('out.png', 'PNG')

