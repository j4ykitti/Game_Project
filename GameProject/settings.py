#setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 32

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../Font/BADABB.ttf'
UI_FONT_SIZE = 30

#general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#000000'
TEXT_COLOR = '#EEEEEE'

#ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 20,'graphic':'../Weapon/Sword/full.png'},
    'spear': {'cooldown': 200,'damage': 30,'graphic':'../Weapon/Spear/full.png'},
    'cleaver': {'cooldown': 300,'damage':50,'graphic':'../Weapon/Cleaver/full.png'}
    
}


#magic
magic_data = {
    'flame' : {'strength': 5,'cost': 20,'graphic':'../Magic/Fire/full.png'},
    'ice' : {'strength': 10,'cost': 30,'graphic':'../Magic/Ice/full.png'},
    'heal' : {'strength': 20,'cost': 10,'graphic':'../Magic/Heal/full.png'}

}


#enemies
monster_data = {
    'dragon':{'health':100,'exp':100,'damage':20,'attack_type': 'thunder', 'attack_sound':'../','speed': 4,'resistance':3,'attack_radius': 80,'notice_radius': 250,'atk_cooldown':40},
    'butterfly':{'health':150,'exp':150,'damage':25,'attack_type': 'slash', 'attack_sound':'../','speed': 4,'resistance':5,'attack_radius': 80,'notice_radius': 250,'atk_cooldown':40},
    'skull':{'health':125,'exp':200,'damage':35,'attack_type': 'fireball', 'attack_sound':'../','speed': 5,'resistance':2,'attack_radius': 120,'notice_radius': 250,'atk_cooldown':40},
    'cyclop':{'health':1250,'exp':2000,'damage':35,'attack_type': 'claw', 'attack_sound':'../','speed': 4,'resistance':10,'attack_radius': 80,'notice_radius': 250,'atk_cooldown':500}
}