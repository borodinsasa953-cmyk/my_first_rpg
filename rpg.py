import random
import os

gold_mlu = 1
hp_mlu = 1
dmg_mlu = 1
game_state = 'main_menu'
hero_name = ''
hero_hp = 100
hero_max_hp = 100
hero_gold = 10
hero_xp = 0
hero_lvl = 1
hero_bonus_damage = 0
weapon =  ''
weapon_damage = 0
armor  = ''
armor_defence = 0
kills = 0
events = ['fight','trupp','find_potion','find_gold', 'find_weapon']
enemies ={'goblin':{
    'name':'Гоблин',
    'hp': 50,
    'dmin': 5,
    'dmax': 11,
    'gold': 15
},
'orc':{
    'name':'Орк',
        'hp': 70,
        'dmin': 7,
        'dmax': 13,
        'gold': 25
},
'skelet':{
    'name': 'Скелет',
    'hp': 30,
    'dmin': 10,
    'dmax': 18

},
'boss':{
    'name':'Король гоблинов',
        'hp': 125,
        'dmin': 17,
        'dmax': 27,
        'gold': 100
}
}
def start_battle(enemy_data,hero_hp,hero_bonus_damage,weapon_damage,armor_defence,hero_max_hp,hero_xp,hero_lvl, kills):
        enemy_hp = int(enemy_data['hp'] * hp_mlu)
        enemy_name = enemy_data['name']
        enemy_dmin = enemy_data ['dmin']
        enemy_dmax = enemy_data['dmax']
        print(f'На тебя напал {enemy_name}!')
        while enemy_hp > 0 and hero_hp > 0:
                    print(f'Здоровье противника: {enemy_hp}')  
                    print(f'Ваше здоровье: {hero_hp}')   
                    action = input('1. Ударить.\n2. Полечиться\nВыбор: ')
                    if action == '1':
                        base_hero_damage = random.randint(3,10)
                        hero_damage = base_hero_damage + hero_bonus_damage + weapon_damage
                        enemy_hp = max(0,enemy_hp - hero_damage)
                        print(f'Вы ударили противника на {hero_damage} урона!')
                    elif action == '2':
                        print ('Вы лечитесь...')
                        hero_hp = min((hero_hp+random.randint(8,19)), hero_max_hp)
                    if enemy_hp > 0:
                        print('Противник атакует!')
                        random_damage = random.randint(enemy_dmin, enemy_dmax)
                        actual_damage =int( max(0, random_damage * dmg_mlu - armor_defence))
                        hero_hp = hero_hp - actual_damage
                        print(f'Враг ударил на {actual_damage} урона!')
                    if enemy_hp <= 0:
                        print ('Враг побежден!')
                        kills += 1
                        reward_gold = int(enemy_data['gold'] * gold_mlu)
                        reward_xp = 15
                        print(f'Ты получил {reward_gold} золота и {reward_xp} XP!')
                        hero_xp = hero_xp + 15
                        print(f'Ты получил 15 XP! Всего XP: {hero_xp}')
                        if hero_xp >= 30:
                            hero_lvl = hero_lvl + 1
                            hero_xp = hero_xp - 30
                            hero_bonus_damage = hero_bonus_damage + 2
                            hero_hp = hero_hp + 20
                            hero_max_hp = hero_max_hp + 20
                            print('УРОВЕНЬ ПОВЫШЕН! Ты стал сильнее!')
                            print(f'Теперь твой уровень: {hero_lvl}')
                        return hero_hp, reward_gold,hero_xp,hero_lvl,hero_bonus_damage,hero_max_hp, kills
                    if hero_hp<=0:
                        print('GAME OVER')
                        input('Нажми Enter')
                        return hero_hp, 0 , hero_xp, hero_lvl, hero_bonus_damage, hero_max_hp,kills
                       
while True:
    if game_state == 'main_menu':
        print('\n============================')
        print('ДОБРО ПОЖАЛОВАТЬ В RPG')
        print ('===========================')
        print('1. Начать игру')
        print('2. Правила')
        print('3. Магазин')
        print('4. Выбор уровня сложности')
        print('5. Выход')
        choice = input('Выбери действие: ')
        if choice == '1':
            hero_name = input('Герой,как тебя зовут? ')
            print (hero_name, 'начнем приключение!')
            game_state = 'game'
        elif choice == '2':
            game_state = 'rules'  
        elif choice == '3':
            game_state = 'shop'
        elif choice == '5':
            print('Выходим из игры, до встречи')
            break
        elif choice == '4':
            print('------------------------')
            print('Выбор уровня сложности:')
            print('1. Легкий')
            print('2. Нормальный (По умолчанию)')
            print('3. Сложный')
            print('4. Выйти в меню')
            diff_choice = input('Выберите действие: ')
            if diff_choice == '1':
                gold_mlu = 0.7
                hp_mlu = 0.8
                dmg_mlu = 0.8
                print('Сложность изменена на легкую')
            elif diff_choice == '2':
                gold_mlu = 1
                hp_mlu = 1
                dmg_mlu = 1
                print('Сложность изменена на среднюю')
            elif diff_choice == '3':
                gold_mlu = 1.5
                hp_mlu = 1.5
                dmg_mlu = 1.25
            elif diff_choice == '4':
                game_state = 'main_menu'
            

        else:
            print('Такого действия нет!')
    elif game_state == 'rules':
        print ('\n---ПРАВИЛА---')
        print ('-Ты - герой. Твоя цель выжить и найти сокровища')
        print ('-У тебя есть здоровье(HP) и золото.')
        input ('Нажми Enter чтобы вернуться в меню ')
        game_state = 'main_menu'
    elif game_state == 'game':
        print('Золото:', hero_gold)
        print(f'Здоровье:  {hero_hp} / {hero_max_hp}')
        print(f'Уровень:  {hero_lvl}')
        print('Опыт: ',hero_xp, '/30' )
        print('Бонус урона: +', hero_bonus_damage)
        print('Оружие: ', weapon)
        print('Броня: ', armor)
        print('Убийства: ', kills)
        print('-----------------------')
        print('1.Идти дальше')
        print('2.Выйти в меню')
        game_choice = input('Выбери действие: ')
        if game_choice == '1':
            random_event = random.choice(events)
            if random_event == 'find_potion':
                print('Ты нашел зелье, здоровье восстановлено!')
                print('-----------------------')
                health = random.randint(1, 20)
                hero_hp = min(hero_hp + health, hero_max_hp)
            elif random_event == 'find_weapon':
                print('Ты нашел меч! Урон увеличен!')
                weapon_damage = 5
                if weapon == 'Алмазный меч':
                    weapon = 'Алмазный меч'
                else:
                    weapon = 'Стальной меч'
            elif random_event == 'find_gold':
                print('Ты нашел золото!')
                print('-----------------------')
                gold = random.randint(1,10)
                hero_gold = hero_gold + gold
            elif random_event == 'trupp':
                print('Ты попал в ловушку! Часть здоровья утрачена!')
                hurt = random.randint(1,15)
                hero_hp = hero_hp - hurt
                if hero_hp<= 0:
                    kills = 0
                    hero_gold = 0
                    hero_hp = 100
                    hero_max_hp = 100
                    hero_xp = 0
                    hero_lvl = 1
                    weapon = ''
                    armor = ''
                    armor_defence = 0
                    weapon_damage = 0
                    game_state = 'main_menu'
                    print('GAME OVER')
                    input('Нажми Enter')
                    game_state = 'main_menu'
            elif random_event == 'fight':
                if kills >= 10:
                    chosen_enemy = enemies['boss']
                else:
                    normal_enemies =['goblin', 'orc']
                    random_key = random.choice(normal_enemies)
                    chosen_enemy = enemies[random_key]
                hero_hp,reward_gold, hero_xp, hero_lvl, hero_bonus_damage,hero_max_hp,kills = start_battle(chosen_enemy,hero_hp,hero_bonus_damage,weapon_damage,armor_defence,hero_max_hp,hero_xp,hero_lvl,kills)
                hero_gold = hero_gold + reward_gold
                if hero_hp<=0:
                    print('GAME OVER')
                    input('Нажми Enter...')
                    kills = 0
                    hero_gold = 0
                    hero_hp = 100
                    hero_max_hp = 100
                    hero_xp = 0
                    hero_lvl = 1
                    weapon = ''
                    armor = ''
                    armor_defence = 0
                    weapon_damage = 0
                    game_state = 'main_menu'
    
                    game_state = 'main_menu'
                elif chosen_enemy['name'] == 'Король гоблинов':
                    print('=========================================')
                    print('ПОЗДРАЛЯЮ! ТЫ УБИЛ КОРОЛЯ ГОБЛИНОВ!')
                    print('=========================================')
                    print('Ты спас деревню и стал настоящим героем!')
                    input('Нажми Enter чтобы продолжить')
                    kills = 0
                    hero_gold = 0
                    hero_hp = 100
                    hero_max_hp = 100
                    hero_xp = 0
                    hero_lvl = 1
                    weapon = ''
                    armor = ''
                    armor_defence = 0
                    weapon_damage = 0
                    game_state = 'main_menu'
                else:
                    game_state = 'game'
        elif game_choice == '2':
            game_state = 'main_menu'
    elif game_state == 'shop':
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('--------МАГАЗИН------------')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print()
        print('1. Купить алмазный меч(50 золота)')
        print('2. Купить зелье излечения(20 золота)')
        print('3. Купить броню(40 золота)')
        print('4. Выйти в меню')
        shop_choice = input('Выберите действие: ')
        if shop_choice == '1':
            if hero_gold >= 50:
                hero_gold-=50
                weapon = 'Алмазный меч'
                weapon_damage = 15
                print('Поздравляю! Вы купили меч!')
            else:
                print('Недостаточно золота!')
                input('Нажми Enter чтобы продолжить')
        elif shop_choice == '2':
            if hero_gold >= 20:
                if hero_hp == hero_max_hp:
                    print('Ваше здоровье и так полное!')
                    input('Нажми Enter чтобы продолжить')
                else:
                    hero_gold-=20
                    hero_hp = hero_max_hp
                    print('Вы вылечились!')
                    input('Нажми Enter чтобы продолжить')
            else:
                print('Недостаточно золота')
                input('Нажми Enter чтобы продолжить')
        elif shop_choice == '3':
            if hero_gold >= 40:
                hero_gold-=40
                armor = 'Кольчуга'
                armor_defence = 3
                print('Поздравляю вы купили броню!')
                input('Нажми Enter чтобы продолжить')
            else:
                print('Недостаточно золота')
                input('Нажми Enter чтобы продолжить')
        elif shop_choice == '4':
            game_state = 'main_menu'
        else:
            print('Нет такого действия')
            input('Нажми Enter чтобы продолжить')

               