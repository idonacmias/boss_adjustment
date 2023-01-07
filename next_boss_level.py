def boss(level, last, con, all_levels_data):
	level_data = all_levels_data[level-1]
	for data in level_data['boss_option_in_level']:
		if is_boss_adjasment(data, last, con):
			print(f'next_boss {data["next_boss"]}')
			return data['next_boss']

	else:
		print(f'{level_data["defualt"]}')
		return level_data["defualt"]

def is_boss_adjasment(data, last_bot, player_streak):
	if data['last'] == last_bot and data['condition'] == player_streak:
		return True

if __name__ == '__main__':
	all_levels_data = [{'boss_option_in_level': [{'last': 3, 'condition' : -2, 'next_boss' : 2}],
	 			  'defualt' : 3},
	 			  
	 			  {'boss_option_in_level': [{'last': 3, 'condition' : -3, 'next_boss' : 2}],
	 			  'defualt' : 3},
	 			  
	 			  {'boss_option_in_level': [{'last': 3, 'condition' : -2, 'next_boss' : 2}],
	 			  'defualt' : 3},
	 			  
	 			  {'boss_option_in_level': [{'last': 4, 'condition' : 3, 'next_boss' : 6},
							   			   {'last': 6, 'condition' : -3, 'next_boss' : 4},
							 			   {'last': 4, 'condition' : -4, 'next_boss' : 3},
							 			   {'last': 4, 'condition' : -3, 'next_boss' : 3}],
	 			  'defualt' : 4},
	 			  
	 			  {'boss_option_in_level': [{'last': 4, 'condition' : 3, 'next_boss' : 6},
							   			   {'last': 6, 'condition' : -3, 'next_boss' : 4},
							 			   {'last': 4, 'condition' : -4, 'next_boss' : 3},
							 			   {'last': 4, 'condition' : -3, 'next_boss' : 3}],
	 			  'defualt' : 4},
	 			  
	 			  ]


	boss(level=4, last=6, con=-3, all_levels_data=all_levels_data) #4
	boss(5, 4, 3, all_levels_data)  #6