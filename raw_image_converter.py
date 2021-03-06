import numpy as np 
import os
import rawpy
import imageio
count = 0;
for i,f,h in os.walk("."):
    for a in h :
        ext = os.path.splitext(a)[1]
        name = os.path.splitext(a)[0]
        if ext == ".raw" or ext == ".ARW":
            try: 
                print("Starting {} of {}".format(name,count))
                name = str(name)+".jpg"
                img = np.fromfile(a, dtype=np.uint32)
                raw = rawpy.imread(a);
                rgb = raw.postprocess()
                imageio.imsave(name, rgb)
                count +=1
            except Exception as e:
                print(e)

  
