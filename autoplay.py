import atx
import sys
from pymsgbox import alert
from combat import Battle


def main(battle_name, need_formation=False):

    device = atx.connect("4200c49cf2faa381")
    
    battle = Battle(battle_name, need_formation)
    battle.run(device)


if __name__ == '__main__':
    '''
    launch gui editor: py -2 -m atx gui
    name on google play: Girl's Frontline
    apk : http://gf.txwy.tw/gfapk
    '''
    try:
        main(*sys.argv[1:])
    except Exception as error:
        print(error)
        alert(title="oops", text="Something Wrong", button='OK')
