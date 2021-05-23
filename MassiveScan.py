import os 
import sys
import time
import socket
import threading

# чистка данных с ранее использованными ip 

drk_1 = os.path.abspath(os.curdir)
filename_1 = '/result_ips.txt'

if os.path.exists(drk_1 + filename_1) == True:
  os.remove(drk_1 + filename_1)


# удаление output_ips.txt

drk_2 = os.path.abspath(os.curdir)
filename_2 = '/output_ips.txt'

if os.path.exists(drk_2 + filename_2) == True:
  os.remove(drk_2 + filename_2)


# проверка файла ips.txt

check_file = os.path.exists('ips.txt')
if check_file == True:
    if os.path.getsize('ips.txt') == 0:
        print('')
        print('Error.')
        print('File ips.txt is empty.') 
        print('')
        sys.exit()
else:
    print('')
    print('Error.')
    print('Not found file ips.txt.')
    print('')
    sys.exit()


# проверка файла ips.txt на пустые строки 

with open('ips.txt') as infile, open('output_ips.txt', 'w') as outfile:
    for line in infile:
        if not line.strip():
            continue
        outfile.write(line) 


# запрос данных

print('')

ports = []

try:
    print('How many ports do you want to scan?')
    number_port = input('')

    for port in range(0,int(number_port)):
        one_port = input('port: ')
        ports.append(one_port)

except ValueError:
    print('')
    print('Error.')
    print('You did not specify ports to scan.')
    print('')
    sys.exit()


print('')
print('-------- You entered: --------')
print('')

try:
    for i in ports:
        print('port: ' + i)
        if i.isdigit() == False:
            print('')
            print('Error.')
            print('You have not entered one or more port(s).') 
            print('')
            sys.exit()

except ValueError:
    print('')
    print('Error.')
    print('You did not specify ports to scan.')
    print('')
    sys.exit()


# Вывод по  строчке ip/mask из текстового файла  

file = open('output_ips.txt', 'r')
for ip in file:
    res1_new = []
    res1 = ip.split('/')
    for i in res1:
        i = i.strip()

        if i == '0':
            error_info()
        if i == '1':
            error_info()
        if i == '2':
            error_info()
        if i == '3':
            error_info()
        if i == '4':
            error_info()
        if i == '5':
            error_info() 
        if i == '6':
            error_info() 
        if i == '7':
            error_info() 
        if i == '8':
            error_info() 
        if i == '9':
            error_info()

        res1_new.append(i)
        res2_new = []
        res2 = res1_new[0].split('.')
        for i in res2:
            i = i.strip()
            res2_new.append(i) 

    try:
        oktet_1_for_ip = (bin(int(res2_new[0]))[2:].zfill(8))
        oktet_2_for_ip = (bin(int(res2_new[1]))[2:].zfill(8))
        oktet_3_for_ip = (bin(int(res2_new[2]))[2:].zfill(8))
        oktet_4_for_ip = (bin(int(res2_new[3]))[2:].zfill(8))
        ip_2th_for_ip = oktet_1_for_ip + '.' + oktet_2_for_ip + '.' + oktet_3_for_ip + '.' + oktet_4_for_ip
    except ValueError:
        print('Error.')
        print('Invalid port.')
        os.remove('result_ips.txt')
        sys.exit()
    except IndexError:
        print('Error.')
        print('You did not correctly indicate the number of ports.')
        os.remove('result_ips.txt')
        sys.exit()

    oktet_1_for_ip = (bin(int(res2_new[0]))[2:].zfill(8))
    oktet_2_for_ip = (bin(int(res2_new[1]))[2:].zfill(8))
    oktet_3_for_ip = (bin(int(res2_new[2]))[2:].zfill(8))
    oktet_4_for_ip = (bin(int(res2_new[3]))[2:].zfill(8))
    ip_2th_for_ip = oktet_1_for_ip + '.' + oktet_2_for_ip + '.' + oktet_3_for_ip + '.' + oktet_4_for_ip


    mask_const = {
              0:'0.0.0.0',
              1:'128.0.0.0',
              2:'192.0.0.0',
              3:'224.0.0.0',
              4:'240.0.0.0',
              5:'248.0.0.0',
              6:'252.0.0.0',
              7:'254.0.0.0',
              8:'255.0.0.0',
              9:'255.128.0.0',
              10:'255.192.0.0', 
              11:'255.224.0.0', 
              12:'255.240.0.0', 
              13:'255.248.0.0', 
              14:'255.252.0.0', 
              15:'255.254.0.0', 
              16:'255.255.0.0', 
              17:'255.255.128.0', 
              18:'255.255.192.0', 
              19:'255.255.224.0', 
              20:'255.255.240.0', 
              21:'255.255.248.0', 
              22:'255.255.252.0', 
              23:'255.255.254.0', 
              24:'255.255.255.0', 
              25:'255.255.255.128', 
              26:'255.255.255.192', 
              27:'255.255.255.224', 
              28:'255.255.255.240', 
              29:'255.255.255.248', 
              30:'255.255.255.252',
              31:'255.255.255.254',
              32:'255.255.255.255',
              }

    for key, value in mask_const.items():
        if str(res1_new[1]) in str(key):
            res3 = value.split('.') 

            oktet_1_for_mask = (bin(int(res3[0]))[2:].zfill(8))
            oktet_2_for_mask = (bin(int(res3[1]))[2:].zfill(8))
            oktet_3_for_mask = (bin(int(res3[2]))[2:].zfill(8))
            oktet_4_for_mask = (bin(int(res3[3]))[2:].zfill(8))
            ip_2th_for_mask = oktet_1_for_mask + '.' + oktet_2_for_mask + '.' + oktet_3_for_mask + '.' + oktet_4_for_mask


# разбор октетов

# разбор первого откета ip в двоичном виде в список 

    oktet_1_for_ip_bit = []
    oktet_1_for_ip_bit.append(oktet_1_for_ip)

    oktet_1_for_ip_bit_new = []
    oktet_1_for_ip_bit = oktet_1_for_ip_bit[0]
    for i in oktet_1_for_ip_bit:
        oktet_1_for_ip_bit_new.append(i)


# разбор первого откета mask ip в двоичном виде в список 

    oktet_1_for_mask_bit = []
    oktet_1_for_mask_bit.append(oktet_1_for_mask)

    oktet_1_for_mask_bit_new = []
    oktet_1_for_mask_bit = oktet_1_for_mask_bit[0]
    for i in oktet_1_for_mask_bit:
        oktet_1_for_mask_bit_new.append(i)


# разбор 2 откета ip в двоичном виде в список 

    oktet_2_for_ip_bit = []
    oktet_2_for_ip_bit.append(oktet_2_for_ip)

    oktet_2_for_ip_bit_new = []
    oktet_2_for_ip_bit = oktet_2_for_ip_bit[0]
    for i in oktet_2_for_ip_bit:
        oktet_2_for_ip_bit_new.append(i)


# разбор 2 откета mask ip в двоичном виде в список 

    oktet_2_for_mask_bit = []
    oktet_2_for_mask_bit.append(oktet_2_for_mask)

    oktet_2_for_mask_bit_new = []
    oktet_2_for_mask_bit = oktet_2_for_mask_bit[0]
    for i in oktet_2_for_mask_bit:
        oktet_2_for_mask_bit_new.append(i)


# разбор 3 откета ip в двоичном виде в список 

    oktet_3_for_ip_bit = []
    oktet_3_for_ip_bit.append(oktet_3_for_ip)

    oktet_3_for_ip_bit_new = []
    oktet_3_for_ip_bit = oktet_3_for_ip_bit[0]
    for i in oktet_3_for_ip_bit:
        oktet_3_for_ip_bit_new.append(i)


# разбор 3 откета mask ip в двоичном виде в список 

    oktet_3_for_mask_bit = []
    oktet_3_for_mask_bit.append(oktet_3_for_mask)

    oktet_3_for_mask_bit_new = []
    oktet_3_for_mask_bit = oktet_3_for_mask_bit[0]
    for i in oktet_3_for_mask_bit:
        oktet_3_for_mask_bit_new.append(i)


# разбор 4 откета ip в двоичном виде в список 

    oktet_4_for_ip_bit = []
    oktet_4_for_ip_bit.append(oktet_4_for_ip)

    oktet_4_for_ip_bit_new = []
    oktet_4_for_ip_bit = oktet_4_for_ip_bit[0]
    for i in oktet_4_for_ip_bit:
        oktet_4_for_ip_bit_new.append(i)


# разбор 4 откета mask ip в двоичном виде в список 

    oktet_4_for_mask_bit = []
    oktet_4_for_mask_bit.append(oktet_4_for_mask)

    oktet_4_for_mask_bit_new = []
    oktet_4_for_mask_bit = oktet_4_for_mask_bit[0]
    for i in oktet_4_for_mask_bit:
        oktet_4_for_mask_bit_new.append(i)


# возведение в степень 

    wildcard_1_oktet = []
    wildcard_2_oktet = []
    wildcard_3_oktet = []
    wildcard_4_oktet = []

    def wildcardmasc(x, y, z):
        for i in range(8): 
            if x[i] < y[i]: 
                z.append("0") 
            elif x[i] > y[i]: 
                z.append("1") 
            else:
                if x[i] == "1":
                    z.append("0")
                else:
                    z.append("1")

    wildcardmasc(oktet_1_for_ip_bit_new, oktet_1_for_mask_bit_new, wildcard_1_oktet)
    wildcardmasc(oktet_2_for_ip_bit_new, oktet_2_for_mask_bit_new, wildcard_2_oktet)
    wildcardmasc(oktet_3_for_ip_bit_new, oktet_3_for_mask_bit_new, wildcard_3_oktet)
    wildcardmasc(oktet_4_for_ip_bit_new, oktet_4_for_mask_bit_new, wildcard_4_oktet)

    wildcard_1_oktet_str = ''.join(wildcard_1_oktet)
    wildcard_2_oktet_str = ''.join(wildcard_2_oktet)
    wildcard_3_oktet_str = ''.join(wildcard_3_oktet)
    wildcard_4_oktet_str = ''.join(wildcard_4_oktet)


    def from2_in10(x):
        size = len(x)
        num10 = 0
        for i in range(0, size):
             num10 = num10 + int(x[i]) * (2**(size - i - 1))
        return num10

    res_wildcard = str(from2_in10(wildcard_1_oktet_str)) + '.' + str(from2_in10(wildcard_2_oktet_str)) + '.' + str(from2_in10(wildcard_3_oktet_str)) + '.' + str(from2_in10(wildcard_4_oktet_str))


# вычисление адреса сети (сравнение байтов откетов ip и mask)

    def network(x, y, z):
        for i in range(8): 
            if x[i] < y[i]: 
                z.append("0") 
            elif x[i] > y[i]: 
                z.append("0") 
            else:
                if x[i] == "1":
                    z.append("1")
                else:
                    z.append("0")

    network_oktet_1 = []
    network_oktet_2 = []
    network_oktet_3 = []
    network_oktet_4 = []

    network(oktet_1_for_ip, oktet_1_for_mask, network_oktet_1)
    network(oktet_2_for_ip, oktet_2_for_mask, network_oktet_2)
    network(oktet_3_for_ip, oktet_3_for_mask, network_oktet_3)
    network(oktet_4_for_ip, oktet_4_for_mask, network_oktet_4)

    network_1_oktet_str = ''.join(network_oktet_1)
    network_2_oktet_str = ''.join(network_oktet_2)
    network_3_oktet_str = ''.join(network_oktet_3)
    network_4_oktet_str = ''.join(network_oktet_4)


# вычисление максимально возможного ip 

    network_4_oktet_str_v2 = int(from2_in10(network_4_oktet_str)) + 1

    res_network = str(from2_in10(network_1_oktet_str)) + '.' + str(from2_in10(network_2_oktet_str)) + '.' + str(from2_in10(network_3_oktet_str)) + '.' + str(network_4_oktet_str_v2)

    res_wildcard = str(from2_in10(wildcard_1_oktet_str)) + '.' + str(from2_in10(wildcard_2_oktet_str)) + '.' + str(from2_in10(wildcard_3_oktet_str)) + '.' + str(from2_in10(wildcard_4_oktet_str))

    network_done_oktet_1 = int(from2_in10(wildcard_1_oktet_str)) + int(from2_in10(network_1_oktet_str)) 
    network_done_oktet_2 = int(from2_in10(wildcard_2_oktet_str)) + int(from2_in10(network_2_oktet_str)) 
    network_done_oktet_3 = int(from2_in10(wildcard_3_oktet_str)) + int(from2_in10(network_3_oktet_str)) 
    network_done_oktet_4 = int(from2_in10(wildcard_4_oktet_str)) + int(from2_in10(network_4_oktet_str) - 1) 
    summ_network_done = str(network_done_oktet_1) + '.' + str(network_done_oktet_2) + '.' + str(network_done_oktet_3) + '.' + str(network_done_oktet_4)


# начало работы с перебором всех возможных адресов

    network_done_oktet_1_min = str(from2_in10(network_1_oktet_str))
    network_done_oktet_2_min = str(from2_in10(network_2_oktet_str))
    network_done_oktet_3_min = str(from2_in10(network_3_oktet_str))
    network_done_oktet_4_min = str(from2_in10(network_4_oktet_str) + 1)

    network_done_oktet_1_min = int(network_done_oktet_1_min)
    network_done_oktet_2_min = int(network_done_oktet_2_min)
    network_done_oktet_3_min = int(network_done_oktet_3_min)
    network_done_oktet_4_min = int(network_done_oktet_4_min)

    write_ip = open("result_ips.txt", 'a')

    if network_done_oktet_2_min < network_done_oktet_2:
        for oktet_2 in range(network_done_oktet_2_min,network_done_oktet_2+1):
            for oktet_3 in range(network_done_oktet_3_min,network_done_oktet_3+1):
                for oktet_4 in range(network_done_oktet_4_min,network_done_oktet_4+1):                    write_ip.write(str(network_done_oktet_1_min) + '.' + str(oktet_2) + '.' + str(oktet_3) + '.' + str(oktet_4) + '\n')

    elif network_done_oktet_3_min < network_done_oktet_3:
        for oktet_3 in range(network_done_oktet_3_min,network_done_oktet_3+1):
            for oktet_4 in range(network_done_oktet_4_min,network_done_oktet_4+1):
                write_ip.write(str(network_done_oktet_1_min) + '.' + str(network_done_oktet_2_min) + '.' + str(oktet_3) + '.' + str(oktet_4) + '\n')

    elif network_done_oktet_4_min < network_done_oktet_4:
        for oktet_4 in range(network_done_oktet_4_min,network_done_oktet_4+1):
            write_ip.write(str(network_done_oktet_1_min) + '.' + str(network_done_oktet_2_min) + '.' + str(network_done_oktet_3_min) + '.' + str(oktet_4) + '\n')

    else:
        error_info()
    
    ip += str(1)

    write_ip.close()


# подсчет количества ip после преобразования (строк в result_ips.txt)

file = open('result_ips.txt')
numline = len(file.readlines())
print(str(numline) + ' ips will be scanned. Saved in result_ips.txt')
print('')


#---------------------- многопоточное вычисление --------------------------
# пример сканирования без многопоточности 

def write_ip_in_file(file_name, ip):
  current_ip = open(file_name + '.txt', 'a')
  current_ip.write(ip + '\n')


def timeout_try_1(ip,port,timeout):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(timeout)
  
  try:
    connect = sock.connect((ip,int(port)))
    print(ip.rstrip('\r\n') + ' ' + port)
    write_ip_in_file(port, ip)
    connect.close()

  except socket.timeout:
    t2 = threading.Thread(target = timeout_try_2, args = (ip.rstrip('\r\n'), port, float('0.1')))
    t2.start()
    #t2.join(0.1)

  except Exception as e:
    #print(ip.rstrip('\r\n') + ' ' + port + ' error')
    pass


def timeout_try_2(ip, port, timeout):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(timeout)

  try:
    connect = sock.connect((ip,int(port)))
    print(ip.rstrip('\r\n') + ' ' + port)
    write_ip_in_file(port, ip)
    connect.close()

  except socket.timeout:
    #print(ip.rstrip('\r\n') + ' ' + port + ' dead')
    pass

  except Exception as e:
    #print(ip.rstrip('\r\n') + ' ' + port + ' error')
    pass

start_time = time.time()

for txt_port in ports:
  result_port_txt_file = open(txt_port + '.txt', 'a')

for port in ports:
    file_result_ips = open('result_ips.txt', 'r')
    for ip in file_result_ips:
        t1 = threading.Thread(target = timeout_try_1, args = (ip.rstrip('\r\n'), port, float('0.01')))
        t1.start()
        t1.join(0.1)

time.sleep(1)

file_result_ips.close()
result_port_txt_file.close()

print('')
print('%s seconds. ' % (time.time() - start_time - 1))
print('')

print('Result:')
for txt_port in ports:
    print('')
    print('Saved in ' + txt_port + '.txt')
print('')
