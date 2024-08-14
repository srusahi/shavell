# Заходи в наш тгк за обновлениями! t.me/projecthikari
from colorama import Fore, Style, init
init()
# Цвета
dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL
# Баннер и меню
def Banner():
    print(f'''
{blueb}╔───────────────────────────────────────────────────────────────────────╗
│                               SHAVEL TOOL                             {blueb}│
│                  {white}Channel{dcyan}:{cyan}t.me/MUSASHI_NO_WAT                          {blueb}│
│                  {white}Developer{dcyan}:{cyan}@MUSASHI_TYPK                              {blueb}│           
╚───────────────────────────────────────────────────────────────────────╝
{dcyan}[{white}ВНИМАНИЕ{dcyan}]{cyan} взломал by @MUSASHI_TYPK''')
def Menu():
    print(f'''{blueb}╔─────────────────────╦─────────────────────────────────────────────────╗
│       {dcyan}[{white}OSINT{dcyan}]{blueb}       │           {dcyan}[{white}Разнообразные инструменты{dcyan}]{blueb}           │
╠─────────────────────╬─────────────────────────────────────────────────╣
├ {white}1{dcyan}. {white}Поиск по номеру{blueb}  ├ {white}5{dcyan}. {white}Добавить бд{blueb}                                  │
╠─────────────────────┼─────────────────────────────────────────────────╣
├ {white}2{dcyan}. {white}Поиск по IP{blueb}      ├ {white}6{dcyan}. {white}скоро...{blueb}                                     │
╠─────────────────────┼─────────────────────────────────────────────────╣
├ {white}3{dcyan}. {white}Поиск по VK{blueb}      ├ {white}7{dcyan}. {white}Dos{blueb}                                          │
╠─────────────────────┼─────────────────────────────────────────────────╣
├ {white}4{dcyan}. {white}скоро...{blueb}           ├ {white}8{dcyan}. {white}Web-crawler{blueb}                                │
╚─────────────────────┴─────────────────────────────────────────────────╝''')
