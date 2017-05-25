There's a map-like large image posted online, the task is to download and stitch it into a single image suitable for printing.

http://mapserver2.biochemical-pathways.com/map1/background/4/2/0.png?v=4
http://mapserver1.biochemical-pathways.com/map1/grid/4/1/0.png?v=4


http://mapserver{n}.biochemical-pathways.com/map1/{layer}/{z}/{x}/{y}.png?v=4

n = { 1 2 }

layer = 
grid - don't want
background - formulas and arrows
substrates - black
regulatoryEffects - orange arrows
unicellularOrganisms - red arrows
higherPlants - green arrows
enzymes - blue text

z = 
4 small
5 ok        [x = 0..27, y = 0..17]
6 pixelated


response good: http://mapserver0.biochemical-pathways.com/map1/background/5/25/17.png?v=4

Content-Length:11918
Content-Type:image/png

1024x1024

response bad: http://mapserver2.biochemical-pathways.com/map1/background/5/27/17.png?v=4

Content-Length:43
Content-Type:image/gif