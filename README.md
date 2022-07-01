# particles
Based on 'https://fnky.github.io/particle-life/'
Two different versions of the same idea implemented in C# within Unity, and in Python

The version I made of this within Unity is much older and I am no graphic designer by any means, but I was curious if I could make this idea myself.

The actual idea behind this is akin to conways game of life or boids where simple rules lead to some cool emergent behavior. In this case it is a set of particles, whose number and number of types are customizable. Each particle type is set a random attraction or repulsion to every other type of particle, which again is dependent on the particles type. From this, not always, but sometimes structures that seem similar to molcules or even chains of molecules can occur which is pretty cool.

The Unity version is a run-at-your-own-risk because it is an EXE as I lost the source code itself because I didn't back up things in high school (bad data practice I know). For that version specifically you can restart and re-randomize everything by pressing the 'r' key. It is a much more efficient version than the python version which I wrote more recently but also much quicker.

The python version I did not worry about optimizing, I just wanted to learn some Python which I have a long ways to go still. It works but there are much more advanced Python features I could have used.
As well as this there are a lot of ways I could have improved the efficiency by using something akin to vector fields per particle type. I could also use octree methods to try and improve collision recognition but I honestly just wanted to do this for some fun. 
