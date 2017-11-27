import sys
import math
def info_rede(addr, smask, pref):
    bin_addr=bin_change_addr(addr)
    bin_sub_addr=bin_change_addr(addr)
    sub_addr=bin_to_dec(bin_addr)


    print("endereço sub-rede:"+ sub_addr)
    print("endereço sub-rede binario:"+bin_sub_addr)#calculo do endereço de subrede

    print ("mascara de sub-rede binario: "+smask)
    smask_dec = bin_to_dec(smask)
    print ("mascara de subrede : "+smask_dec)#calculo da mascara de subrede

    broad_bin=calc_broadcast(bin_addr,pref)
    print("endereço de broadcast binario: "+broad_bin)#calculo do endereço de broadcast
    broad=bin_to_dec(broad_bin)
    print("endereço de broadcast: "+broad)

    print("tamanho do prefixo:"+pref)#bota o tamanho do prefixo na tela

    bottom_addr=min_addr(bin_sub_addr)
    print('primeiro endereço disponivel binario: '+bottom_addr)#primeiro endereço possivel de uso na subrede
    dec_bottom=bin_to_dec(bottom_addr)
    print('primeiro endereço disponivel: '+dec_bottom)

    top_addr=max_addr(broad_bin)#ultimo endereço possivel de uso
    print("ultimo endereço disponivel binario: "+top_addr)
    dec_top=bin_to_dec(top_addr)
    print('ultimo endereço disponivel: '+dec_top)

    num_addrs=str(int(math.pow(2,32-int(pref)))-2)
    print("numero de endereços disponiveis: "+ num_addrs)

#addr em binario
def bin_change_addr(num):
    part=[]
    div=num.split('.')
    for i in range(0,4):
        mid='{0:08b}'.format(int(div[i]))
        part.append(str(mid))
    resp=('{}.{}.{}.{}'.format(part[0],part[1],part[2],part[3]))
    return resp

def calc_smask(pref):
    resp=""
    test=int(pref)
    for j in  range(0,4):
        for i in range(0,8):
            if test>0:
                resp= resp+"1"
                test=test-1
            else:
                resp=resp+"0"
        if j!=3:
            resp=resp+"."
    return resp

def calc_broadcast(bin_addr,pref):
    substitute=''
    val=int(pref)//8
    print (val)
    num=0
    for i in range(0,35):
        if bin_addr[i]=='.':
            substitute=substitute+'.'
        elif num<int(pref):
            substitute=substitute+bin_addr[i]
            num=num+1
        else:
            substitute=substitute+'1'
    return substitute

def calc_subaddr(bin_addr,pref):
    substitute=''
    #val=int(pref)//8
    #print (val)
    num=0
    for i in range(0,35):
        if bin_addr[i]=='.':
            substitute=substitute+'.'
        elif num<int(pref):
            substitute=substitute+bin_addr[i]
            num=num+1
        else:
            substitute=substitute+'0'
        print (substitute)
    return substitute

def bin_to_dec(bin_addr):
    div=bin_addr.split('.')
    #print(div[0])
    new=[]

    for i in range(0,4):
        mid=str(int(div[i],2))
        new.append(mid)
    resp=('{}.{}.{}.{}'.format(new[0],new[1],new[2],new[3]))
    return resp

def min_addr(bin_sub_addr):
    div=bin_sub_addr.split('.')
    new_num=int(div[3],2)+1
    div[3]='{0:08b}'.format(new_num)
    resp=('{}.{}.{}.{}'.format(div[0],div[1],div[2],div[3]))
    return resp

def max_addr(bin_broad_addr):
    div=bin_broad_addr.split('.')
    new_num=int(div[3],2)-1
    div[3]='{0:08b}'.format(new_num)
    resp=('{}.{}.{}.{}'.format(div[0],div[1],div[2],div[3]))
    return resp


def fixed_mode(addr,submask,pref,adicional):
    info_rede(addr,submask,pref)
    endereco=vetor_addr(addr)
    #divisor()


def vetor_addr(addr):
    div=bin_broad_addr.split('.')
    resp=[]
    for j in  range(0,4):
        for i in range(0,8):
            resp.append(div[j][i])
    return resp


tipo =sys.argv[1]
addr=sys.argv[2]
submask=' '
pref=' '
if '.' in sys.argv[3]:
    submask=sys.argv[3]
    pref=addr.count('1')
else:
    pref=sys.argv[3]
    submask=calc_smask(pref)

if tipo == "1":
    info_rede(addr, submask, pref)
elif tipo == "2":
    if '.' in sys.argv[4]:
        extra_subm=sys.argv[4]
        extra_pref=extra_subm.count('1')
    else:
        extra_pref=sys.argv[4]
        extra_subm=calc_smask(extra_pref)
    fixed_mode(addr, submask, pref, x_subm,x_pref)
elif tipo == "3":
    varied_mode()
