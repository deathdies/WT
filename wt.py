#!/usr/bin/python3
#-*- coding: utf-8 -*-
#Coded By de@hdies
#Webmaster Indexing Tools
import time, sys, os
from time import sleep
C = '\x1b[96m'
Y = '\x1b[93m'
G = '\x1b[92m'
R = '\x1b[91m'
NC = '\x1b[m'
DR = '\033[2;31m'
DY = '\033[2;33m'
DG = '\033[2;32m'
DW = '\033[2;37m'
DC = '\033[2;36m'
BW = '\x1b[47;30m'
BR = '\x1b[47;41m'

def sp(seco):
  for cia in seco + '\n':
    sys.stdout.write(cia)
    sys.stdout.flush()
    time.sleep(random.random() * 0.03)

def ret(x):
  for remaining in range(x, 0, -1):
    sys.stdout.write('{}  • {}Retrying.                        \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{}  • {}Retrying..                       \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{}  • {}Retrying..!                      \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{}  • {}Retrying..!!                     \r'.format(NC, DW, remaining))
    sleep(0.25)

def tung(x):
  for remaining in range(x, 0, -1):
    sys.stdout.write('{}  • • • • • • • • • {}|                    \r'.format(NC, DW, remaining))
    sleep(0.1)
    sys.stdout.write('{}  • • • • • • • • • {}/                    \r'.format(NC, DW, remaining))
    sleep(0.1)
    sys.stdout.write('{}  • • • • • • • • • {}-                    \r'.format(NC, DW, remaining))
    sleep(0.1)
    sys.stdout.write('{}  • • • • • • • • • {}\                    \r'.format(NC, DW, remaining))
    sleep(0.1)

def tungs(x):
  for remaining in range(x, 0, -1):
    sys.stdout.write('{}  • {}Please Wait.                        \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{}  • {}Please Wait..                       \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{}  • {}Please Wait..!                      \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{}  • {}Please Wait..!!                     \r'.format(NC, DW, remaining))
    sleep(0.25)

def tungss(x):
  for remaining in range(x, 0, -1):
    sys.stdout.write('{} • {}Installing New Version.                        \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{} • {}Installing New Version..                       \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{} • {}Installing New Version..!                      \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{} • {}Installing New Version..!!                     \r'.format(NC, DW, remaining))
    sleep(0.25)

def welcome():
  welkom = ('Dont Forget To Sleep|Dont Forget To Eat|Dont Forget To Rest|Dont Forget To Happy|Dont Forget To FapFap')
  welkomin = list(map(str, welkom.split('|')))
  slmtdtg = random.choice(welkomin)
  sp(f'{NC}  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •\n  •')
  tung(5)
  sp(f'{NC}  • Coded By {DC}de@hdies{NC}')
  print(f'{NC}  • {DY}{slmtdtg}{DW}..!! :){NC}')
  sleep(3)

def lgv():
  os.system('clear')
  print(f'{NC}    wwzapd         dlzazw      {NC}')
  print(f'{NC}   an{R}#{NC}zncmqzepweeirzpas{R}#{NC}xz     {NC}')
  print(f'{NC} apez{R}##{NC}Qq{C}NEW {G}VERSION{NC}mM{R}##{NC}dcmv   {NC}')
  print(f'{NC}zwepd{R}####{NC}q{Y}AVAILABLE{NC}a{R}####{NC}ezqpa  {NC}')
  print(f'{NC}ezqpdkapeifjeeazezqpdkazdkwqz  {NC}')
  print(f'{NC} ezqpdksz{DW}##{NC}wepuizp{DW}##{NC}wzeiapdk   {NC}')
  print(f'{NC}  zqpakdpa{DW}#{NC}azwewep{DW}#{NC}zqpdkqze    {NC}')
  print(f'{NC}    apqxalqpewenwazqmzazq      {NC}')
  print(f'{NC}     mn{DW}##{NC}=={DW}#######{NC}=={DW}##{NC}qp       {NC}')
  print(f'{NC}      qw{DW}##{NC}={DW}#######{NC}={DW}##{NC}zl        {NC}')
  print(f'{NC}      z0{DW}######{R}={DW}######{NC}0a        {NC}')
  print(f'{NC}       qp{DW}#####{R}={DW}#####{NC}mq         {NC}')
  print(f'{NC}       az{DW}####{R}==={DW}####{NC}mn         {NC}')
  print(f'{NC}        ap{DW}#########{NC}qz          {NC}')
  print(f'{NC}         9qlzskwdewz           {NC}')
  print(f'{NC}          zqw{C}v02{NC}aiw            {NC}')
  print(f'{NC}            qoqpe              {NC}')
  print(f'{NC} • • • • • • • • • • • • • {BR}  WEBMASTER  {NC}')

def lg():
  os.system('clear')
  print(f'{NC} • {BR} Created By de@hdies {NC} • • •')
  print(f'{NC} • {BW} Webmaster Indexing Tools {NC} • • •')
  print(f'{NC}•  {Y}Main {C}Menu{NC}: => {R}v0.1{NC}')
  print(f'{NC}•    {C}01{NC}) {G}Bing!{NC}  {C}04{NC}) {G}Check Index{NC}')
  print(f'{NC}•    {C}02{NC}) {G}Google{NC} {C}05{NC}) {G}Tutorial For Use{NC}')
  print(f'{NC}•    {DY}03{DW}) {DR}Yandex{NC}')
  print(f'{NC}•  {R}x{NC})  <= {R}Exit{NC}')

def lg2():
  os.system('clear')
  print(f'{NC} • {BR} Created By de@hdies {NC} • • •')
  print(f'{NC} • {BW} Webmaster Indexing Tools {NC} • • •')
  print(f'{NC}•  {Y}Menu{NC}: => {R}Check Index{NC}')
  print(f'{NC}•    {C}01{NC}) {G}Check Index {Y}AOL{NC}    {C}05{NC}) {G}Check Index {Y}Google{NC}')
  print(f'{NC}•    {C}02{NC}) {G}Check Index {Y}ASK{NC}    {C}06{NC}) {G}Check Index {Y}Yahoo{NC}')
  print(f'{NC}•    {DY}03{DW}) {DC}Check Index {DR}Bing!{NC}  {DY}07{DW}) {DC}Check Index {DR}Yandex{NC}')
  print(f'{NC}•    {DY}04{DW}) {DC}Check Index {DR}Ecosia{NC} {DY}08{DW}) {DC}Check Index {DR}DuckDuckGo{NC}')
  print(f'{NC}•  {R}x{NC})  <= {Y}Back{NC}')

try:
  import re, json, random, httplib2, queue, platform, traceback, threading, urllib.parse, requests.packages.urllib3
  import requests as req
  from bs4 import BeautifulSoup as bs
  from fake_useragent import UserAgent
  from oauth2client.service_account import ServiceAccountCredentials
  requests.packages.urllib3.disable_warnings()

except ImportError:
  lg()
  print(f'{NC} • • • • • • • • • • • • • {BR}  WEBMASTER  {NC}')
  print(f'{NC} • {C}Modules {R}Required{NC}..!!')
  print(f'{NC} • {Y}Trying To {G}Install Modules{NC}..!!')
  print(f'{NC} • • • • • • • • • • • • • {BW}    TOOLS    {NC}')
  tungs(5)
  os.system('clear')
  os.system('apt-get upgrade -y')
  os.system('apt-get install pip -y')
  os.system('python3 -m pip install --upgrade pip')
  os.system('python3 -m pip install fake_useragent oauth2client requests bs4')
  lg()
  print(f'{NC} • • • • • • • • • • • • • {BR}  WEBMASTER  {NC}')
  print(f'{NC} • {G}All Modules {C}Installed{NC}..!!')
  print(f'{NC} • {C}Please Rerun {Y}This Tools{NC}..!!')
  tungs(3)
  exit(f'                    \r')

except KeyboardInterrupt:
  exit(f'{NC}\n • {R}Keyboard Interupted{NC}..!!')

except Exception as e:
  try:
    print(f'{NC} • {DW}=> {DY}Something Went {DR}Wrong{DW}..!!{NC}')
  finally:
    e = None
    del e
    sleep(1)
    exit()

else:
  try:
    dapat = []
    nodpt = []
    n = 10
    q = queue.Queue()
    ses = requests.Session()
    ua = UserAgent()
    hider = {'User-Agent':str(ua.chrome)}

    #Reconnect
    def recon():
      while True:
        try:
          raw = req.get('https://www.bing.com/', headers=hider, cookies={'CONSENT': 'YES+1'}, timeout=10, verify=False)
          if raw.status_code:
            break
        except:
          ret(1)
      return True

    #Request Indexing Bing!
    def bing(Site, Api_Keys, List):
      lg()
      print(f'{NC} • • • • • • • • • • • • • {BW}    BING!    {NC}')
      print(f'{NC}  • • • • • {Y}Information{DW}..!!{NC}')
      print(f'{NC}  • • {DC}Site URL {DW}=> {DG}{Site}{NC}')
      print(f'{NC}  • • {DC}API Keys {DW}=> {DG}{Api_Keys}{NC}')
      print(f'{NC}  • • • • • • • • • • • • • • • • • • • •')
      print(f'{NC}  • • • • • Start Request Index • • • • •')
      count = 0
      for Lists in List:
        count += 1
        Listna = Lists.strip()
        url = f'https://ssl.bing.com/webmaster/api.svc/json/SubmitUrlbatch?apikey={Api_Keys}'
        hider = {'Host': 'ssl.bing.com', 'Content-type': 'application/json; charset=utf-8'}
        dat = '{"siteUrl": "'+Site+'", "urlList": ["'+ str(Listna) +'"]}'
        res = ses.post(url, headers=hider, data=dat, cookies={'CONSENT': 'YES+1'}, timeout=10, verify=False)
        if res.status_code == 200:
          print(f'{NC}  • {C}{count}{NC}) {Y}Status {G}{res.status_code} {DW}=> {DW}...{C}{Listna[12:40]}{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          dapat.append(f'{Listna}')
          with open('Bing/Report.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] {res.status_code} : SUCCESSED => {Listna}\n')
          s.close()
        elif res.status_code == 400:
          print(f'{NC}  • {C}{count}{NC}) {Y}Status {C}{res.status_code} {DW}=> ...{NC}{Y}RESOURCE_EXHAUSTED{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          nodpt.append(f'{Listna}')
          with open('Bing/Report.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] {res.status_code} : RESOURCE_EXHAUSTED => {Listna}\n')
          s.close()
        else:
          print(f'{NC}  • {C}{count}{NC}) {Y}Status {R}NULL{DW}..!! => ...{NC}{R}ERROR{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          nodpt.append(f'{Listna}')
          with open('Bing/Report.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] NULL..!! : SOMETHING WRONG..!! => {Listna}\n')
          s.close()
      print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
      print(f'{NC} • • • • • • • • • • • • • {BR}  INDEXING!  {NC}')
      print(f'{NC}•  ✓{G} DONE{NC}..!!')
      print(f'{NC}• {G}Request Done {C}{len(dapat)} {Y}URL {NC}')
      print(f'{NC}• {R}Request Failed {C}{len(nodpt)} {Y}URL {NC}')
      print(f'{NC}• {C}Saved {DW}=> {NC}{G}Bing/Report.txt{NC}')
      print(f'{NC} • • • • • • • • • • • • • {BW}    BING!    {NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
      exit()

    #Request Indexing Google
    def google(urlList):
      lg()
      print(f'{NC} • • • • • • • • • • • • • {BW}    BING!    {NC}')
      print(f'{NC}  • • • • • Start Request Index • • • • •')
      skop = [ 'https://www.googleapis.com/auth/indexing' ]
      poin = 'https://indexing.googleapis.com/v3/urlNotifications:publish'
      kunci = 'Google/keys.json'
      credentials = ServiceAccountCredentials.from_json_keyfile_name(kunci, scopes=skop)
      http = credentials.authorize(httplib2.Http())
      count = 0
      for index, item in enumerate(urlList):
        count += 1
        content = {
          'url': item,
          'type': 'URL_UPDATED'
        }
        response, content = http.request(poin, method='POST', body=json.dumps(content))
        statna = response['status']
        if statna == '200':
          print(f'{NC}  • {C}{count}{NC}) {Y}Status {G}{response["status"]} {DW}=> {DW}...{C}{item[12:40]}{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          dapat.append(f'{item}')
          with open('Google/Report.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] {response["status"]} : SUCCESSED => {item}')
          s.close()
        elif statna == '429':
          print(f'{NC}  • {C}{count}{NC}) {Y}Status {C}{response["status"]} {DW}=> ...{Y}RESOURCE_EXHAUSTED{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          nodpt.append(item)
          with open('Google/Report.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] {response["status"]} : RESOURCE_EXHAUSTED => {item}')
          s.close()
        elif statna == '403':
          print(f'{NC}  • {C}{count}{NC}) {Y}Status {R}{response["status"]} {DW}=> ...{R}PERMISSION_DENIED{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          nodpt.append(item)
          with open('Google/Report.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] {response["status"]} : PERMISSION_DENIED => {item}')
          s.close()
        elif statna == '400':
          print(f'{NC}  • {C}{count}{NC}) {Y}Status {R}{response["status"]} {DW}=> ...{R}INVALID_ARGUMENT{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          nodpt.append(item)
          with open('Google/Report.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] {response["status"]} : INVALID_ARGUMENT => {item}')
          s.close()
        else:
          print(f'{NC}  • {C}{count}{NC}) {Y}Status {R}NULL {DW}=> {DW}...{R}KESALAHAN{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          nodpt.append(item)
          with open('Google/Report.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] NULL : ERROR..!! => {item}')
          s.close()
      print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
      print(f'{NC} • • • • • • • • • • • • • {BR}  INDEXING!  {NC}')
      print(f'{NC}•  ✓{G} DONE{NC}..!!')
      print(f'{NC}• {G}Request Done {C}{len(dapat)} {Y}URL {NC}')
      print(f'{NC}• {R}Request Failed {C}{len(nodpt)} {Y}URL {NC}')
      print(f'{NC}• {C}Saved {DW}=> {NC}{G}Google/Report.txt{NC}')
      print(f'{NC} • • • • • • • • • • • • • {BW}   GOOGLE!   {NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
      exit()

    #Check Index Page AOL
    def cekInAo(site):
      count = 0
      url = 'https://search.aol.com/aol/search?q=site:' + site + '&hl=en'
      res = bs(ses.get(url, headers=hider, cookies={'CONSENT': 'YES+1'}, timeout=10, verify=False).content, 'html.parser').findAll('span', {'class': 'fz-ms'})
      if res:
        for sitena in res:
          count += 1
          a = sitena.text
          print(f'{NC}  • {C}{count}{NC}) {G}Indexed{DW}!! => ...{NC}{C}{a[12:40]}{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          dapat.append(f'{a}')
          with open('Check/R_In_AOL.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] Indexed => {a}\n')
          s.close()
        print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
        print(f'{NC} • • • • • • • • • • • • • {BR}    CHECK    {NC}')
        print(f'{NC}•  ✓{G} DONE{NC}..!!')
        print(f'{NC}• {G}Indexed Only {C}{len(dapat)} {Y}URL {NC}')
        print(f'{NC}• {R}Remaining Unindexed{NC}..!!')
        print(f'{NC}• {C}Saved {DW}=> {NC}{G}Check/R_In_AOL.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • {BW}     AOL     {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
        exit()
      else:
        print(f'{NC}   • {DW}=> {DR}Site Not In {Y}Search Engines{DW}..!!{NC}')
        tungs(5)
        main()

    #Check Index Page ASK
    def cekInAs(site):
      count = 0
      url = f'https://www.ask.com/web?q=site:{site}'
      res = bs(ses.get(url, headers=hider, cookies={'CONSENT': 'YES+1'}, timeout=10, verify=False).content, 'html.parser')
      a = res.find('ul', {'class': 'PartialWebPagination-buttons'})
      if a:
        b = a.find_all('li')[1]
        c = b.find('a')['href']
        d = f'https://www.ask.com{c[:-1]}'
        for e in res.find_all('div', {'class': 'PartialSearchResults-item-url'}):
          count += 1
          f = e.get_text()
          print(f'{NC}  • {C}{count}{NC}) {G}Indexed{DW}!! => ...{NC}{C}{f[4:30]}{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          dapat.append(f'{f}')
          with open('Check/R_In_ASK.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] Indexed => {f}\n')
          s.close()
        for g in range(2, 10000):
          url2 = f'{d}{g}'
          res2 = bs(req.get(url2, headers=hider, cookies={'CONSENT': 'YES+1'}, timeout=10, verify=False).content, 'html.parser').find_all('div', {'class': 'PartialSearchResults-item-url'})
          if res2:
            for h in res2:
              count += 1
              i = h.get_text()
              print(f'{NC}  • {C}{count}{NC}) {G}Indexed{DW}!! => ...{NC}{C}{i[4:30]}{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
              dapat.append(f'{i}')
              with open('Check/R_In_ASK.txt', 'a') as (s):
                s.write(f'[ By de@Hdies ] Indexed => {i}\n')
              s.close()
          else:
            print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
            print(f'{NC} • • • • • • • • • • • • • {BR}    CHECK    {NC}')
            print(f'{NC}•  ✓{G} DONE{NC}..!!')
            print(f'{NC}• {G}Indexed Only {C}{len(dapat)} {Y}URL {NC}')
            print(f'{NC}• {R}Remaining Unindexed{NC}..!!')
            print(f'{NC}• {C}Saved {DW}=> {NC}{G}Check/R_In_ASK.txt{NC}')
            print(f'{NC} • • • • • • • • • • • • • {BW}     ASK     {NC}')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
            exit()
      else:
        print(f'{NC}   • {DW}=> {DR}Site Not In {Y}Search Engines{DW}..!!{NC}')
        tungs(5)
        main()

    #Check Indexing BING!

    #Check Indexing Ecosia

    #Check Indexing Google
    def cekInGo(List):
      class ThreadClass(threading.Thread):
        def __init__(self, ini, q):
          threading.Thread.__init__(self)
          self.ini = ini
          self.q = q
        def run(self):
          while True:
            Listn = self.q.get()
            try:
              url = 'https://www.google.com/search?q=site:' + Listn + '&hl=en'
              res = bs(ses.get(url, headers=hider, cookies={'CONSENT': 'YES+1'}, timeout=10, verify=False).content, 'html.parser')
              noIn = re.compile('did not match any documents')
              if res(text=noIn):
                print(f'{NC}  • {C}× {NC}) {R}Not Index {DW}=> ...{NC}{Y}{Listn[12:40]}{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
                nodpt.append(f'{Listn}')
                with open('Check/R_In_Google.txt', 'a') as (s):
                  s.write(f'[ By de@Hdies ] Not Indexed => {Listn}\n')
                s.close()
              else:
                print(f'{NC}  • {C}√ {NC}) {G}Indexed{DW}!! => ...{NC}{C}{Listn[12:40]}{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
                dapat.append(f'{Listn}')
                with open('Check/R_In_Google.txt', 'a') as (s):
                  s.write(f'[ By de@Hdies ] Indexed => {Listn}\n')
                s.close()
            except:
              recon()
            finally:
              self.q.task_done()
      for ini in range(n):
        t = ThreadClass(ini, q)
        t.daemon = True
        t.start()
      for Listna in List:
        Listn = Listna.strip()
        q.put(Listn)
      q.join()
      print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
      print(f'{NC} • • • • • • • • • • • • • {BR}    CHECK    {NC}')
      print(f'{NC}•  ✓{G} DONE{NC}..!!')
      print(f'{NC}• {G}Indexed {C}{len(dapat)} {Y}URL {NC}')
      print(f'{NC}• {R}Not Index {C}{len(nodpt)} {Y}URL {NC}')
      print(f'{NC}• {C}Saved {DW}=> {NC}{G}Check/R_In_Google.txt{NC}')
      print(f'{NC} • • • • • • • • • • • • • {BW}   GOOGLE!   {NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
      exit()

    #Check Index Page YAHOO!
    def cekInYa(site):
      count = 0
      url = 'https://search.yahoo.com/search?p=site:' + site + '&ei=UTF-8&nojs=1'
      res = bs(ses.get(url, headers=hider, cookies={'CONSENT': 'YES+1'}, timeout=10, verify=False).content, 'html.parser').findAll('a', {'data-matarget': 'algo'})
      if res:
        for sitena in res:
          count += 1
          a = sitena['href']
          b = a.rsplit('RU=', 1)[1]
          c = b.replace('%2f', '/')
          d = c.split('RK=', 1)[0]
          e = d.replace('%3a', ':')
          print(f'{NC}  • {C}{count}{NC}) {G}Indexed{DW}!! => ...{NC}{C}{e[12:35]}{DW}...{NC}', sep=' ', end='\n', file=sys.stdout, flush=False)
          dapat.append(f'{e}')
          with open('Check/R_In_Yahoo.txt', 'a') as (s):
            s.write(f'[ By de@Hdies ] Indexed => {e}\n')
          s.close()
        print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
        print(f'{NC} • • • • • • • • • • • • • {BR}    CHECK    {NC}')
        print(f'{NC}•  ✓{G} DONE{NC}..!!')
        print(f'{NC}• {G}Indexed Only {C}{len(dapat)} {Y}URL {NC}')
        print(f'{NC}• {R}Remaining Unindexed{NC}..!!')
        print(f'{NC}• {C}Saved {DW}=> {NC}{G}Check/R_In_AOL.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • {BW}    YAHOO    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • •')
        exit()
      else:
        print(f'{NC}   • {DW}=> {DR}Site Not In {Y}Search Engines{DW}..!!{NC}')
        tungs(5)
        main()

    #Check Indexing Yandex

    #Check Indexing DuckDuckGo

    #Main Menu
    def main():
      lg()
      print(f'{NC} • • • • • • • • • • • • • {BR}  WEBMASTER  {NC}')
      Pilih_Menu = input(f'{NC}  • {Y}Choose {C}Menu {NC}=>{DW} ')

      #Empty Input
      if Pilih_Menu == '':
        print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
        sleep(1)
        main()

      #Request Indexing Bing!
      elif Pilih_Menu == '1':
        lg()
        print(f'{NC} • • • • • • • • • • • • • {BW}    BING!    {NC}')
        if os.path.exists('Bing/site_bing.txt') and os.path.exists('Bing/key_bing.txt') == True:
          with open('Bing/site_bing.txt', 'r') as (s):
            Site = s.readline()
          s.close()
          with open('Bing/key_bing.txt', 'r') as (a):
            Api_Keys = a.readline()
          a.close()
          lg()
          print(f'{NC} • • • • • • • • • • • • • {BW}    BING!    {NC}')
          print(f'{NC}  • • • • • {Y}Information{DW}..!!{NC}')
          print(f'{NC}  • • {DC}Site URL {DW}=> {DG}{Site}{NC}')
          print(f'{NC}  • • {DC}API Keys {DW}=> {DG}{Api_Keys}{NC}')
          Links = input(f'{NC}  • {Y}Insert {C}File {Y}List {NC}=>{DW} ')
          with open(Links, 'r') as (l):
            List = l.readlines()
          l.close()
          tungs(3)
          bing(Site, Api_Keys, List)
        else:
          Sitena = input(f'{NC}  • {Y}Insert {C}Site {Y}URL {NC}=>{DW} ')
          with open('Bing/site_bing.txt', 'w') as (sna):
            sna.write(f'{Sitena}')
          sna.close()
          print(f'{NC}  • {DG}Site {DY}Save On {DW}=> {DC}Bing/site_bing.txt{NC}')
          sleep(1)
          Apina = input(f'{NC}  • {Y}Insert {C}API {Y}Keys {NC}=>{DW} ')
          with open('Bing/key_bing.txt', 'w') as (ana):
            ana.write(f'{Apina}')
          ana.close()
          print(f'{NC}  • {DG}API Keys {DY}Saved On {DW}=> {DC}Bing/key_bing.txt{NC}')
          sleep(1)
          with open('Bing/site_bing.txt', 'r') as (s):
            Site = s.readline()
          s.close()
          with open('Bing/key_bing.txt', 'r') as (a):
            Api_Keys = a.readline()
          a.close()
          lg()
          print(f'{NC} • • • • • • • • • • • • • {BW}    BING!    {NC}')
          print(f'{NC}  • • • • • {Y}Information{DW}..!!{NC}')
          print(f'{NC}  • • {DC}Site URL {DW}=> {DG}{Site}{NC}')
          print(f'{NC}  • • {DC}API Keys {DW}=> {DG}{Api_Keys}{NC}')
          Links = input(f'{NC}  • {Y}Insert {C}File {Y}List {NC}=>{DW} ')
          with open(Links, 'r') as (l):
            List = l.readlines()
          l.close()
          tungs(3)
          bing(Site, Api_Keys, List)

      #Request Indexing Google
      elif Pilih_Menu == '2':
        lg()
        print(f'{NC} • • • • • • • • • • • • • {BW}   GOOGLE!   {NC}')
        Links = input(f'{NC}  • {Y}Insert {C}File {Y}List {NC}=>{DW} ')
        with open(Links, 'r') as (l):
          urlList = l.readlines()
        l.close()
        if os.path.isfile('Google/keys.json'):
          tungs(3)
          google(urlList)
        else:
          print(f'{NC}  • {DG}API Keys {DY}Not Found{DW} => {DC}Google/keys.json{NC}')
          sleep(3)
          exit()

      #Request Indexing Yandex
      elif Pilih_Menu == '3':
        print(f'{NC} • {DY}This {DC}Menu {DW}=>{NC}\n • {DR}Useable Yet{DW}..!!{NC}')
        print(f'{NC} • • • • • • • • • • • • • {BW}   YANDEX!   {NC}')
        enters = input(f'  • {C}Enter {Y}To Back {DW}=>{NC} ')
        if enters == '':
          main()
        else:
          print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
          sleep(1)
          main()

      #Check Index Page
      elif Pilih_Menu == '4':
        lg2()
        print(f'{NC} • • • • • • • • • • • • • {BW} CHECK INDEX {NC}')
        Menu_Index = input(f'  • {Y}Choose {C}Menu {NC}=>{DW} ')

        #Check Index Page Wrong Input
        if Menu_Index == '':
          print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
          sleep(1)
          main()

        #Check Index Page AOL
        elif Menu_Index == '1':
          lg2()
          print(f'{NC} • • • • • • • • • • • • • {BW}  CHECK AOL  {NC}')
          site = input(f'  • {Y}Input {G}URL {C}Site {NC}=>{DW} ')
          sipot = site.split('http')[0]
          if site != sipot:
            lg2()
            print(f'{NC} • • • • • • • • • • • • • {BW}  CHECK AOL  {NC}')
            print(f'{NC}  • • • • Start Index Check {C}AOL! {NC}• • • •')
            tungs(3)
            cekInAo(site)
          else:
            print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
            sleep(1)
            print(f'{NC}   • {DY}Format {DW}=> {DG}https://www.example.com{NC}')
            sleep(3)
            main()

        #Check Index Page ASK
        elif Menu_Index == '2':
          lg2()
          print(f'{NC} • • • • • • • • • • • • • {BW}  CHECK ASK  {NC}')
          site = input(f'  • {Y}Input {G}URL {C}Site {NC}=>{DW} ')
          sipot = site.split('http')[0]
          if site != sipot:
            lg2()
            print(f'{NC} • • • • • • • • • • • • • {BW}  CHECK ASK  {NC}')
            print(f'{NC}  • • • • Start Index Check {C}ASK! {NC}• • • •')
            tungs(3)
            cekInAs(site)
          else:
            print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
            sleep(1)
            print(f'{NC}   • {DY}Format {DW}=> {DG}https://www.example.com{NC}')
            sleep(3)
            main()

        #Check Index Page BING
        elif Menu_Index == '3':
          print(f'{NC} • {DY}This {DC}Menu {DW}=>{NC}\n • {DR}Useable Yet{DW}..!!{NC}')
          print(f'{NC} • • • • • • • • • • • • • {BW} CHECK BING! {NC}')
          enters = input(f'  • {C}Enter {Y}To Back {DW}=>{NC} ')
          if enters == '':
            main()
          else:
            print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
            sleep(1)
            main()

        #Check Index Page ECOSIA
        elif Menu_Index == '4':
          print(f'{NC} • {DY}This {DC}Menu {DW}=>{NC}\n • {DR}Useable Yet{DW}..!!{NC}')
          print(f'{NC} • • • • • • • • • • • • {BW} CHECK ECOSIA! {NC}')
          enters = input(f'  • {C}Enter {Y}To Back {DW}=>{NC} ')
          if enters == '':
            main()
          else:
            print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
            sleep(1)
            main()

        #Check Index Page GOOGLE
        elif Menu_Index == '5':
          lg2()
          print(f'{NC} • • • • • • • • • • • {BW}  CHECK GOOGLE!  {NC}')
          Lists = input(f'{NC}  • {Y}Insert {C}File {Y}List {NC}=>{DW} ')
          if os.path.isfile(f'{Lists}'):
            with open(Lists, 'r') as (l):
              List = l.readlines()
            l.close()
            lg2()
            print(f'{NC} • • • • • • • • • • • {BW}  CHECK GOOGLE!  {NC}')
            print(f'{NC}  • • •  Start Index Check {C}GOOGLE {NC} • • •')
            tungs(3)
            cekInGo(List)
          else:
            print(f'{NC}   • {DY}ERROR {DW}=> {DR}File {DC}{Lists} {DY}Not Found{DW}..!!{NC}')
            sleep(3)
            main()

        #Check Index Page YAHOO!
        elif Menu_Index == '6':
          lg2()
          print(f'{NC} • • • • • • • • • • • • {BW}  CHECK YAHOO  {NC}')
          site = input(f'  • {Y}Input {G}URL {C}Site {NC}=>{DW} ')
          sipot = site.split('http')[0]
          if site != sipot:
            lg2()
            print(f'{NC} • • • • • • • • • • • • {BW}  CHECK YAHOO  {NC}')
            print(f'{NC}  • • •  Start Index Check {C}YAHOO! {NC} • • •')
            tungs(3)
            cekInYa(site)
          else:
            print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
            sleep(1)
            print(f'{NC}   • {DY}Format {DW}=> {DG}https://www.example.com{NC}')
            sleep(3)
            main()

        #Check Index Page YANDEX
        elif Menu_Index == '7':
          print(f'{NC} • {DY}This {DC}Menu {DW}=>{NC}\n • {DR}Useable Yet{DW}..!!{NC}')
          print(f'{NC} • • • • • • • • • • • • {BW} CHECK YANDEX! {NC}')
          enters = input(f'  • {C}Enter {Y}To Back {DW}=>{NC} ')
          if enters == '':
            main()
          else:
            print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
            sleep(1)
            main()

        #Check Index Page DuckDuckGo
        elif Menu_Index == '8':
          print(f'{NC} • {DY}This {DC}Menu {DW}=>{NC}\n • {DR}Useable Yet{DW}..!!{NC}')
          print(f'{NC} • • • • • • • • • • • • {BW} CHECK DuDuGo! {NC}')
          enters = input(f'  • {C}Enter {Y}To Back {DW}=>{NC} ')
          if enters == '':
            main()
          else:
            print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
            sleep(1)
            main()

        #Check Index Page Back
        elif Menu_Index == 'x':
          main()

        #Check Index Page Wrong Input
        else:
          print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
          sleep(1)
          main()

      #Exit
      elif Pilih_Menu == 'x':
        exit()

      #Wrong Input
      else:
        print(f'{NC}   • {DW}=> {DR}Wrong Input{DW}..!!{NC}')
        sleep(1)
        main()

    if __name__ == '__main__':
      #welcome()
      ver = 'v0.2'
      vres = req.get(f'https://raw.githubusercontent.com/deathdies/version/main/Webmaster-Tools/{ver}', headers=hider,cookies={'CONSENT': 'YES+1'}, timeout=10, verify=False).status_code
      if vres == 200:
        if not os.path.exists('Bing'):
          os.mkdir('Bing')
        else:
          pass
        if not os.path.exists('Google'):
          os.mkdir('Google')
        else:
          pass
        if not os.path.exists('Check'):
          os.mkdir('Check')
        else:
          pass
        main()
      else:
        lgv()
        tungss(3)
        os.system('rm wt.py')
        os.system('wget -q -P https://raw.githubusercontent.com/deathdies/WT/main/wt.py')
        lg()
        tung(3)
        exit(f'{NC} • {Y}Upgrade {C}Version {NC}=> {G}DONE{NC}..!!')
  except KeyboardInterrupt:
    exit(f'{NC}\r   •  {DW}=> {DR}Keyboard Interupted{DW}..!!{NC}')
  except FileNotFoundError:
    print(f'{NC}   • {DY}ERROR {DW}=> {DR}File Not Found{DW}..!!{NC}')
    sleep(2)
    main()
  except Exception as e:
   try:
     print(f'{NC}   •  {DW}=> {DY}Something Went {DR}Wrong{DW}..!!{NC}')
   finally:
     e = None
     del e
     sleep(1)
     exit()
