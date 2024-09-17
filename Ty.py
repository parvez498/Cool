import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json,ipaddress
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

### HEADERS ###

def banner():
    print("""
\033[1;94m __       _           _ _       _    _                 
\033[1;95m/ _\ ___ | |__   __ _(_) |__   | | _| |__   __ _ _ __  
\033[1;94m\ \ / _ \| '_ \ / _` | | '_ \  | |/ / '_ \ / _` | '_ \ 
\033[1;95m_\ \ (_) | | | | (_| | | |_) | |   <| | | | (_| | | | |
\033[1;94m\__/\___/|_| |_|\__,_|_|_.__/  |_|\_\_| |_|\__,_|_| |_|
                                                       
 """)

host="https://mbasic.facebook.com"
ok = []
cp = []
ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 =
