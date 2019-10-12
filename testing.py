import os,subprocess
x=subprocess.check_output(["iwlist","wlan0","scan"])
#y=x[x.find("ESSID:")+7:x.find("ESSID:")+15]

z = [i for i in range(len(x)) if x.startswith('ESSID',i)]

log_file = open ("iwlist_wlan0_scan log file.txt","w")
log_file.write(x)
log_file.close()

output_file = open ("iwlist_wlan0_scan output file.txt","w")
#output_file.write("Number of Networks Found: "+str(len(z))+"\n")
#output_file.write("#1) SSID: "+x[z[0]+7:x.find("Bit")-3])
output_file.write("#1) SSID: "+x[z[0]+7:z[0]+x.find("\n")-1]+"\n")
output_file.write("#2) SSID: "+x[z[1]+7:z[1]+x.find("\n")-1]+"\n")
output_file.close()

