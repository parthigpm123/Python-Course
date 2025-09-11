import pyscreenshot as sc 

import time

time.sleep(3)

k = sc.grab()

k.save("Sample-Screenshot.png")

k.show()