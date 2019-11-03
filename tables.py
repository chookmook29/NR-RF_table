import random
import math

loop_start = 0
odds_range = ['1:3', '1:2', '1:1', '3:2', '2:1', '3:1', '4:1', '5:1', '6:1']

while loop_start < 1:
	attacker = input('Attacker strength?')
	defender = input('Defender strength?')
	attacker = int(attacker)
	defender = int(defender)
	if attacker >= defender:
		initial_odds = attacker / defender
		if initial_odds >= 1.5 and initial_odds < 2.0:
			odds = '3:2'
			print(odds) 
		else:
			initial_odds = math.floor(initial_odds)
			if initial_odds > 6:
				initial_odds = 6
			odds = f'{initial_odds}:1'
			print(odds) 

	else:
		initial_odds = defender / attacker
		initial_odds = math.ceil(initial_odds)
		if initial_odds > 3:
			print('Automatic CA result!!!')
			initial_odds = 3
		odds = f'1:{initial_odds}'
		print(odds) 
	dice = random.randint(0,5)
	odds_position = odds_range.index(odds)
	shift = 0
	armour_bonus = input('Any armor/shock unit bonus?')
	if armour_bonus == 'y':
			bonus = input('How much?')
			shift += int(bonus)
	combat_support = input('Any blitz/shock marker?')
	if combat_support == 'y':
			shift += 1
	terrain_modifier = input('Defender in forest/marsh/city?')
	if terrain_modifier == 'y':
		shift -= 1
	else:
		mountain_modifier = input('Defender in mountains/Kerch Strait?')
		if mountain_modifier == 'y':
			shift -= 2
		else:
			objective_modifier = input('Defender in objective hexside?')
			if objective_modifier == 'y':
				shift -= 1
	river_modifier = input('All attackers behind river not in winter/long winter turn?')
	if river_modifier == 'y':
		shift -= 1
	winter = input('Axis winter attack?')
	if winter == 'y':
		winter_modifier = input('First long winter turn?')
		if winter_modifier == 'y':
			shift -= 2
		else:
			shift -= 1
	card_bonus = input('Any card bonus?')
	if card_bonus == 'y':
		bonus = input('How much?')
		if bonus == '-1':
			shift -= 1
		else:
			shift += 1
	odds_position += shift 
	if odds_position < 0:
		print('Automatic CA result!!!')
		odds_position = 0
	elif odds_position > 8:
		odds_position = 8

	odds = odds_range[odds_position]

	print(f'Odds shift is {shift}')
	print(f'Final odds are {odds}')
	side = input('Which side?(a, s)')
	formatted_dice = dice + 1
	print(f'Dice roll is {formatted_dice}')

	a13 = ['CA', 'CA', 'CA', '-', 'CB', 'DR']
	a12 = ['CA', 'CA', '-', 'CB', 'DR', 'DR']
	a11 = ['CA', '-', 'CB', 'EX', 'DR', 'DR']
	a32 = ['-', '-', 'CB', 'EX', 'DR', 'DR']
	a21 = ['-', 'CB', 'EX', 'DR', 'DR', 'DS']
	a31 = ['CB', 'EX', 'DR', 'DR', 'DS', 'DD']
	a41 = ['EX', 'DR', 'DR', 'DS', 'DS', 'DD']
	a51 = ['DR', 'DR', 'DS', 'DS', 'DD', 'DD']
	a61 = ['DR', 'DS', 'DS', 'DD', 'DD', 'DD']

	s13 = ['CA', 'CA', 'CA', 'CA', '-', 'CB']
	s12 = ['CA', 'CA', 'CA', '-', 'CB', 'DR']
	s11 = ['CA', 'CA', '-', 'CB', 'EX', 'DR']
	s32 = ['CA', '-', 'CB', 'EX', 'EX', 'DR']
	s21 = ['-', 'CB', 'EX', 'EX', 'DR', 'DR']
	s31 = ['CB', 'EX', 'EX', 'DR', 'DR', 'DS']
	s41 = ['EX', 'EX', 'DR', 'DR', 'DS', 'DS']
	s51 = ['EX', 'EX', 'DR', 'DR', 'DS', 'DD']
	s61 = ['EX', 'DR', 'DR', 'DS', 'DD', 'DD']

	if side == 'a':
		if odds == '1:3':
			result = print(a13[dice])
		elif odds == '1:2':
			result = print(a12[dice])
		elif odds == '1:1':
			result = print(a11[dice])
		elif odds == '3:2':
			result = print(a32[dice])
		elif odds == '2:1':
			result = print(a21[dice])
		elif odds == '3:1':
			result = print(a31[dice])
		elif odds == '4:1':
			result = print(a41[dice])
		elif odds == '5:1':
			result = print(a51[dice])
		else:
			result = print(a61[dice])
	else:
		if odds == '1:3':
			result = print(s13[dice])
		elif odds == '1:2':
			result = print(s12[dice])
		elif odds == '1:1':
			result = print(s11[dice])
		elif odds == '3:2':
			result = print(s32[dice])
		elif odds == '2:1':
			result = print(s21[dice])
		elif odds == '3:1':
			result = print(s31[dice])
		elif odds == '4:1':
			result = print(s41[dice])
		elif odds == '5:1':
			result = print(s51[dice])
		else:
			result = print(s61[dice])
