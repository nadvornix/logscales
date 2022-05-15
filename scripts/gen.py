import sys, random


print("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   id="svg1419"
   version="1.1"
   viewBox="0 0 210 297"
   height="297mm"
   width="210mm">
  <defs
     id="defs1413" />
  <metadata
     id="metadata1416">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     id="layer1">""")
for i, line in enumerate(sys.stdin.readlines()):
   # _, num, power, lg, desc = line.split("\t")
   desc, num, power, lg = line.split("\t")
   lg = 20*float(lg)
   print("""    <path
       id="path{i}"
       d="M 1.8708867,{lg} H 20.312484"
       style="fill:none;stroke:#000000;stroke-width:0.26458332px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <text
       id="text{i}"
       y="{lg}"
       x="35"
       style="font-style:normal;font-weight:normal;font-size:0.65;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.26458332"
       xml:space="preserve"><tspan
         id="tspan{i}"
         style="stroke-width:0.26458332"
         y="{lg}"
         x="43.030396">{num} 10 ^ {power}</tspan></text>

     <text
       id="text{i}b"
       y="{lg}"
       x="50"
       style="font-style:normal;font-weight:normal;font-size:0.65;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.26458332"
       xml:space="preserve"><tspan
         id="tspan{i}b"
         style="stroke-width:0.26458332"
         y="{lg}"
         x="50">{desc}</tspan></text>
		""".format(power=power, desc=desc, lg=lg, i=i, num=num))

print ("""    </g>
</svg>

""")