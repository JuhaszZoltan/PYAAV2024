from colorama import Fore # PS: python -m pip install colorama
from resources.dgnms import dognames
from random import choice

# ---  colorama colors: ---
R:str = Fore.LIGHTRED_EX
G:str = Fore.LIGHTGREEN_EX
B:str = Fore.LIGHTBLUE_EX
Y:str = Fore.LIGHTYELLOW_EX
RES:str = Fore.RESET

# --- vowels for task 2 ---
VWLS:str = 'aeiou'

# ---  class for task 3 ---
class Event:
    def __init__(self, row:str) -> None:
        prts:list[str] = row.strip().split(';')
        self.year:int = int(prts[0])
        self.country:str = prts[1]
        self.city:str = prts[2]
        self.medals:dict[str, int] = {
            'gold': int(prts[3]),
            'silver': int(prts[4]),
            'bronze': int(prts[5]),
        }
        self.total_medals:int = sum(self.medals.values())

def f01() -> None:
    a:int = int(input(f'\n{RES}írja be az "a" értékét: {Y}'))
    b:int = int(input(f'{RES}írja be az "b" értékét: {Y}'))
    e = round(a / b, 2)
    print(f"{RES}{a} / {b} = {e}")
    print(f'a(z) {e} {f"{R}NEM OSZTHATÓ" if e % 5 else f"{G}OSZTHATÓ"} {RES}5-el\n')


def f02() -> None:
    rndogname:str = choice(dognames)
    no_mgh:int = 0
    for chr in rndogname.lower():
        if chr in VWLS: no_mgh += 1
    print(f'\nsorsolt név: {B}{rndogname}{RES}', end=' ')
    print(f'[magánhangzók száma: {G}{no_mgh}{RES}]')
    while input(f'tetszik ez a név?: {R}') != 'igen':
        print(f'{RES}új név: {B}{choice(dognames)}{RES}')
    print(f'{RES}Gratulálok, jó választás! Viszont látásra!\n')


def f03() -> None:
    events:list[Event] = []
    file = open('resources/paralimpia.txt', 'r', encoding='utf-8')
    for r in file: events.append(Event(r))
    #-- 3.1 ----------------
    print(f'\n3.1: Eddig {Y}{len(events)}{RES} verseny került megrendezésre.')
    #-- 3.2 ----------------
    print(f'3.2: A legutóbbi versenyt {Y}{events[-1].country}{RES} rendezte.')
    #-- 3.3 ----------------
    gsum:int = 0
    for e in events: gsum += e.medals['gold']
    print(f'3.3: A magyar sportolók eddig {Y}{gsum}{RES} aranyérmet szereztek.')
    #-- 3.4 ----------------
    nomed:int = 0
    for e in events:
        if e.total_medals == 0: nomed += 1
    print(f'3.4: Eddig {Y}{nomed}{RES} alkalom volt, amikor nem volt magyar dobogós.')
    #-- 3.5 ----------------
    mi:int = 0
    for i in range(1, len(events)):
        if events[i].total_medals >events[mi].total_medals: mi = i
    print(f'3.5: A legtöbb érmet a {Y}{events[mi].city}{RES}i paralimpián szerezték.\n')