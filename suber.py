import concurrent.futures,socket,sys,time
from colorama import Fore,Style

if len(sys.argv) < 3:
    print(
        Style.RESET_ALL + Fore.RED + "Usage : %s site.com [list_of_subdomains.txt] [AUTO-SAVE]\nAttention ! Don't use it against military websites." %
        sys.argv[0].split('/')[-1] + Style.RESET_ALL)
    sys.exit()
else:
    print(Style.RESET_ALL + Fore.RED + "Attention ! Don't use it against military websites." + Style.RESET_ALL)
    pass

file = open(sys.argv[2],'r')
subs_list = []
for line in file:
        subs_list.append(line.strip('\n'))
file.close()
t1 = time.perf_counter()
def SubsChecker(sub):
    target = '%s.%s' % (sub, sys.argv[1])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #s.settimeout(0.5)
    try:
        con = s.connect((target, 80))
        print(Fore.GREEN,target,'-- Found !'+Style.RESET_ALL)
        result = open('./reports/'+sys.argv[1]+'.html', 'a')
        result.write('<p><a href="http://'+target+'">'+target+'</a></p>'+'\n')
        con.close()
        
    except:
        pass
    result.close()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(SubsChecker, subs_list)

t2 = time.perf_counter()
t3 = (t2-t1)/60
print(Style.RESET_ALL+Fore.CYAN+f'Finished in {t3} minutes'+Style.RESET_ALL)
