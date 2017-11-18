import sys
def info_rede(addr, smask, pref):
    print("endereço sub-rede:"+ addr)
    bin_addr=bin_change_addr(addr)
    print("endereço sub-rede binario:"+bin_addr)
    if smask==' ':
        smask=calc_smask(pref)
    print ("mascara de subrede: "+smask)

#add um em binario
def bin_change_addr(num):
    part=[]
    div=num.split('.')
    for i in range(0,4):
        mid='{0:08b}'.format(int(div[i]))
        part.append(str(mid))

    resp="s%.s%.s%.s%"%(part[0],part[1],part[2],part[3])
    return resp
def calc_smask(pref):
    resp=""
    for j in  range(0,4):
        for i in range(0,8):
            if pref>1:
                resp= resp+"1"
                pref=pref-1
            else:
                resp=resp+"0"
        resp="."
    return resp


tipo =sys.argv[1]
addr=sys.argv[2]
submask=' '
pref=' '
if '.' in sys.argv[3]:
    submask=sys.argv[3]
else:
    pref=sys.argv[3]
if tipo == "1":
    info_rede(addr, submask, pref)
elif tipo == "2":
    fixed_mode(addr, submask, pref, adicional)
elif tipo == "3":
    varied_mode()
