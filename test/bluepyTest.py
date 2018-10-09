from bluepy import btle

print ("Connecting...");
#dev = btle.Peripheral("F4:5E:AB:B1:0C:4A")
dev = btle.Peripheral("F4:5E:AB:B0:8B:70");

print ("Services...");
for svc in dev.services:
    print (str(svc));

print ("Characteristics...");
for ch in dev.getCharacteristics():
    print ("  0x"+ format(ch.getHandle(),'02X')  +"   "+str(ch.uuid) +" " + ch.propertiesToString());

ch = dev.getCharacteristics(uuid='0000dfb1-0000-1000-8000-00805f9b34fb')[0];
ch.write("1".encode('utf-8'))
