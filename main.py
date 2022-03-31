import rcn_module
from time import sleep

for i in range(0, 10):
    rcn_module.textRGB("Break a leg")
    sleep(.3)

print(rcn_module.generate_password(10))