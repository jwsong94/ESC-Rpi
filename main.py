from bluepy import btle

# BLUNO MAC TABLE
# ESC_HR : F4:5E:AB:B1:0C:06
# ESC_SY : F4:5E:AB:B0:8B:70
# ESC_JW : F4:5E:AB:B0:8C:A3
# ESC_MH : F4:5E:AB:B1:0C:4A

ble_list = ['f4:5e:ab:b1:0c:06', 'f4:5e:ab:b0:8b:70', 'f4:5e:ab:b0:8c:a3', 'f4:5e:ab:b1:0c:4a'];

dev_list = [];
conn_list = [];

cont_uuid = '0000dfb1-0000-1000-8000-00805f9b34fb';

scan = btle.Scanner();
print("Scanning for 5 seconds");
devs = scan.scan(5);

for dev in devs:
    dev_list.append(dev.addr);

for dev in dev_list:
    print(dev);

for ble_mac in ble_list:
    try:
        print("Try To connect : " + ble_mac);
        if ble_mac in dev_list:
            conn = btle.Peripheral(ble_mac);
            conn_list.append(conn);
        else:
            conn_list.append(None);
    except btle.BTLEException as ex:
        conn_list.append(None);

    '''
    if ble_mac is None:
        conn_list.append(0);
    else:
        conn_list.append(1);
    '''

for conn_val in conn_list:
    if conn_val != None:
        ch = conn_val.getCharacteristics(uuid=cont_uuid)[0];
        ch.write("1".encode('utf-8'));

'''
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
'''