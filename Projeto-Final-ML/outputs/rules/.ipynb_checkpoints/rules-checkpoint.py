def findDecision(obj): #obj[0]: gender, obj[1]: age, obj[2]: hypertension, obj[3]: heart_disease, obj[4]: ever_married, obj[5]: work_type, obj[6]: Residence_type, obj[7]: avg_glucose_level, obj[8]: bmi, obj[9]: smoking_status
	# {"feature": "avg_glucose_level", "instances": 3566, "metric_value": 0.314, "depth": 1}
	if obj[7] == '91.85':
		return 'False'
	elif obj[7] == '73.0':
		return 'False'
	elif obj[7] == '100.54':
		return 'False'
	elif obj[7] == '67.92':
		return 'False'
	elif obj[7] == '86.06':
		return 'False'
	elif obj[7] == '72.49':
		return 'False'
	elif obj[7] == '68.4':
		return 'False'
	elif obj[7] == '93.55':
		return 'False'
	elif obj[7] == '79.2':
		return 'False'
	elif obj[7] == '91.68':
		return 'False'
	elif obj[7] == '106.41':
		# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0] == 'Male':
			return 'False'
		elif obj[0] == 'Female':
			return 'True'
		else: return 'True'
	elif obj[7] == '71.06':
		return 'False'
	elif obj[7] == '81.77':
		return 'False'
	elif obj[7] == '82.81':
		# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0] == 'Male':
			return 'False'
		elif obj[0] == 'Female':
			return 'True'
		else: return 'True'
	elif obj[7] == '90.43':
		return 'False'
	elif obj[7] == '78.43':
		return 'False'
	elif obj[7] == '88.65':
		return 'False'
	elif obj[7] == '90.77':
		return 'False'
	elif obj[7] == '111.81':
		# {"feature": "heart_disease", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'False':
			return 'False'
		elif obj[3] == 'True':
			return 'True'
		else: return 'True'
	elif obj[7] == '89.11':
		return 'False'
	elif obj[7] == '95.87':
		return 'False'
	elif obj[7] == '103.44':
		return 'False'
	elif obj[7] == '109.51':
		return 'False'
	elif obj[7] == '85.84':
		return 'False'
	elif obj[7] == '95.01':
		return 'False'
	elif obj[7] == '94.96':
		return 'False'
	elif obj[7] == '80.08':
		return 'False'
	elif obj[7] == '65.12':
		return 'False'
	elif obj[7] == '60.98':
		# {"feature": "hypertension", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[2] == 'True':
			return 'False'
		elif obj[2] == 'False':
			return 'True'
		else: return 'True'
	elif obj[7] == '73.29':
		return 'False'
	elif obj[7] == '65.36':
		return 'False'
	elif obj[7] == '88.2':
		# {"feature": "hypertension", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[2] == 'False':
			return 'False'
		elif obj[2] == 'True':
			return 'True'
		else: return 'True'
	elif obj[7] == '80.63':
		return 'False'
	elif obj[7] == '85.81':
		return 'False'
	elif obj[7] == '92.87':
		return 'False'
	elif obj[7] == '90.0':
		# {"feature": "work_type", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[5] == 'Private':
			return 'False'
		elif obj[5] == 'Self-employed':
			return 'True'
		else: return 'True'
	elif obj[7] == '60.22':
		return 'False'
	elif obj[7] == '80.57':
		return 'False'
	elif obj[7] == '89.68':
		return 'False'
	elif obj[7] == '95.36':
		return 'False'
	elif obj[7] == '100.8':
		return 'False'
	elif obj[7] == '56.11':
		# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0] == 'Female':
			return 'False'
		elif obj[0] == 'Male':
			return 'True'
		else: return 'True'
	elif obj[7] == '77.93':
		return 'False'
	elif obj[7] == '77.52':
		return 'False'
	elif obj[7] == '89.61':
		return 'False'
	elif obj[7] == '91.08':
		return 'False'
	elif obj[7] == '84.31':
		return 'False'
	elif obj[7] == '114.32':
		return 'False'
	elif obj[7] == '88.97':
		return 'False'
	elif obj[7] == '86.96':
		return 'False'
	elif obj[7] == '93.88':
		return 'False'
	elif obj[7] == '85.82':
		return 'False'
	elif obj[7] == '80.72':
		return 'False'
	elif obj[7] == '91.65':
		return 'False'
	elif obj[7] == '87.72':
		return 'False'
	elif obj[7] == '74.35':
		return 'False'
	elif obj[7] == '92.82':
		return 'False'
	elif obj[7] == '84.4':
		return 'False'
	elif obj[7] == '74.63':
		# {"feature": "hypertension", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[2] == 'False':
			return 'False'
		elif obj[2] == 'True':
			return 'True'
		else: return 'True'
	elif obj[7] == '69.24':
		return 'False'
	elif obj[7] == '83.16':
		return 'False'
	elif obj[7] == '78.29':
		return 'False'
	elif obj[7] == '75.77':
		return 'False'
	elif obj[7] == '81.51':
		return 'False'
	elif obj[7] == '84.79':
		return 'False'
	elif obj[7] == '81.96':
		return 'False'
	elif obj[7] == '92.86':
		return 'False'
	elif obj[7] == '82.59':
		return 'False'
	elif obj[7] == '83.51':
		return 'False'
	elif obj[7] == '81.59':
		return 'False'
	elif obj[7] == '87.69':
		return 'False'
	elif obj[7] == '102.0':
		return 'False'
	elif obj[7] == '85.62':
		return 'False'
	elif obj[7] == '104.48':
		return 'False'
	elif obj[7] == '70.56':
		return 'False'
	elif obj[7] == '85.03':
		return 'False'
	elif obj[7] == '104.55':
		return 'False'
	elif obj[7] == '73.75':
		return 'False'
	elif obj[7] == '68.37':
		return 'False'
	elif obj[7] == '98.92':
		return 'False'
	elif obj[7] == '83.3':
		return 'False'
	elif obj[7] == '126.35':
		return 'False'
	elif obj[7] == '85.66':
		return 'False'
	elif obj[7] == '70.53':
		return 'False'
	elif obj[7] == '85.17':
		return 'False'
	elif obj[7] == '79.8':
		return 'False'
	elif obj[7] == '99.44':
		return 'False'
	elif obj[7] == '105.52':
		return 'False'
	elif obj[7] == '58.66':
		return 'False'
	elif obj[7] == '79.39':
		return 'False'
	elif obj[7] == '85.04':
		return 'False'
	elif obj[7] == '60.32':
		return 'False'
	elif obj[7] == '133.24':
		return 'False'
	elif obj[7] == '79.44':
		return 'False'
	elif obj[7] == '103.78':
		return 'False'
	elif obj[7] == '70.51':
		return 'False'
	elif obj[7] == '92.32':
		return 'False'
	elif obj[7] == '76.03':
		return 'False'
	elif obj[7] == '114.16':
		return 'False'
	elif obj[7] == '111.08':
		return 'False'
	elif obj[7] == '91.35':
		return 'False'
	elif obj[7] == '103.61':
		return 'False'
	elif obj[7] == '106.35':
		return 'False'
	elif obj[7] == '77.04':
		return 'False'
	elif obj[7] == '84.9':
		return 'False'
	elif obj[7] == '84.13':
		return 'False'
	elif obj[7] == '112.96':
		return 'False'
	elif obj[7] == '110.41':
		return 'False'
	elif obj[7] == '88.83':
		return 'False'
	elif obj[7] == '73.87':
		return 'False'
	elif obj[7] == '85.12':
		return 'False'
	elif obj[7] == '95.08':
		return 'False'
	elif obj[7] == '77.19':
		return 'False'
	elif obj[7] == '81.54':
		return 'False'
	elif obj[7] == '84.43':
		return 'False'
	elif obj[7] == '94.63':
		return 'False'
	elif obj[7] == '77.94':
		return 'False'
	elif obj[7] == '69.77':
		return 'False'
	elif obj[7] == '96.77':
		return 'False'
	elif obj[7] == '73.56':
		return 'False'
	elif obj[7] == '78.16':
		return 'False'
	elif obj[7] == '93.28':
		return 'False'
	elif obj[7] == '90.42':
		return 'False'
	elif obj[7] == '84.49':
		return 'False'
	elif obj[7] == '62.0':
		return 'False'
	elif obj[7] == '74.88':
		return 'False'
	elif obj[7] == '100.31':
		return 'False'
	elif obj[7] == '129.16':
		return 'False'
	elif obj[7] == '108.64':
		return 'False'
	elif obj[7] == '81.25':
		return 'False'
	elif obj[7] == '74.29':
		return 'False'
	elif obj[7] == '71.97':
		return 'False'
	elif obj[7] == '57.56':
		return 'False'
	elif obj[7] == '77.12':
		return 'False'
	elif obj[7] == '62.47':
		return 'False'
	elif obj[7] == '63.71':
		return 'False'
	elif obj[7] == '105.28':
		return 'False'
	elif obj[7] == '84.86':
		return 'False'
	elif obj[7] == '112.54':
		return 'False'
	elif obj[7] == '102.97':
		return 'False'
	elif obj[7] == '144.1':
		return 'False'
	elif obj[7] == '87.1':
		return 'False'
	elif obj[7] == '90.11':
		return 'False'
	elif obj[7] == '86.53':
		return 'False'
	elif obj[7] == '65.3':
		return 'False'
	elif obj[7] == '58.65':
		return 'False'
	elif obj[7] == '111.15':
		return 'False'
	elif obj[7] == '100.47':
		return 'False'
	elif obj[7] == '84.18':
		return 'False'
	elif obj[7] == '92.04':
		return 'False'
	elif obj[7] == '107.47':
		return 'False'
	elif obj[7] == '75.5':
		return 'False'
	elif obj[7] == '83.75':
		return 'False'
	elif obj[7] == '73.27':
		return 'False'
	elif obj[7] == '88.04':
		return 'False'
	elif obj[7] == '82.85':
		return 'False'
	elif obj[7] == '56.75':
		return 'False'
	elif obj[7] == '88.27':
		return 'False'
	elif obj[7] == '77.46':
		return 'False'
	elif obj[7] == '88.38':
		return 'False'
	elif obj[7] == '83.7':
		return 'False'
	elif obj[7] == '97.89':
		return 'False'
	elif obj[7] == '89.18':
		return 'False'
	elif obj[7] == '87.4':
		return 'False'
	elif obj[7] == '82.93':
		return 'False'
	elif obj[7] == '194.53':
		return 'False'
	elif obj[7] == '104.7':
		return 'False'
	elif obj[7] == '107.42':
		return 'False'
	elif obj[7] == '135.19':
		return 'False'
	elif obj[7] == '75.25':
		return 'False'
	elif obj[7] == '67.97':
		return 'False'
	elif obj[7] == '75.19':
		return 'False'
	elif obj[7] == '106.54':
		return 'False'
	elif obj[7] == '91.21':
		return 'False'
	elif obj[7] == '76.26':
		return 'False'
	elif obj[7] == '72.56':
		return 'False'
	elif obj[7] == '95.16':
		return 'False'
	elif obj[7] == '76.64':
		return 'False'
	elif obj[7] == '83.26':
		return 'False'
	elif obj[7] == '90.31':
		return 'False'
	elif obj[7] == '90.3':
		return 'False'
	elif obj[7] == '102.07':
		return 'False'
	elif obj[7] == '142.31':
		return 'False'
	elif obj[7] == '60.6':
		return 'False'
	elif obj[7] == '92.73':
		return 'False'
	elif obj[7] == '82.09':
		return 'False'
	elif obj[7] == '92.11':
		return 'False'
	elif obj[7] == '75.53':
		return 'False'
	elif obj[7] == '97.06':
		return 'False'
	elif obj[7] == '113.21':
		return 'False'
	elif obj[7] == '66.46':
		return 'False'
	elif obj[7] == '68.66':
		return 'False'
	elif obj[7] == '88.57':
		return 'False'
	elif obj[7] == '70.07':
		return 'False'
	elif obj[7] == '94.89':
		return 'False'
	elif obj[7] == '124.16':
		return 'False'
	elif obj[7] == '86.21':
		return 'False'
	elif obj[7] == '89.3':
		return 'False'
	elif obj[7] == '78.05':
		return 'False'
	elif obj[7] == '93.93':
		return 'False'
	elif obj[7] == '117.03':
		return 'False'
	elif obj[7] == '210.0':
		return 'False'
	elif obj[7] == '104.36':
		return 'False'
	elif obj[7] == '111.33':
		return 'False'
	elif obj[7] == '101.19':
		return 'False'
	elif obj[7] == '69.34':
		return 'False'
	elif obj[7] == '84.07':
		return 'False'
	elif obj[7] == '94.15':
		return 'False'
	elif obj[7] == '143.45':
		return 'False'
	elif obj[7] == '112.08':
		return 'False'
	elif obj[7] == '102.1':
		return 'False'
	elif obj[7] == '78.68':
		return 'False'
	elif obj[7] == '90.55':
		return 'False'
	elif obj[7] == '83.14':
		return 'False'
	elif obj[7] == '80.28':
		return 'False'
	elif obj[7] == '93.6':
		return 'False'
	elif obj[7] == '56.85':
		return 'False'
	elif obj[7] == '101.81':
		return 'False'
	elif obj[7] == '82.39':
		return 'False'
	elif obj[7] == '93.51':
		return 'False'
	elif obj[7] == '82.57':
		return 'False'
	elif obj[7] == '58.01':
		return 'False'
	elif obj[7] == '62.68':
		return 'False'
	elif obj[7] == '79.81':
		return 'False'
	elif obj[7] == '57.42':
		return 'False'
	elif obj[7] == '99.0':
		return 'False'
	elif obj[7] == '107.18':
		return 'False'
	elif obj[7] == '108.03':
		return 'False'
	elif obj[7] == '72.61':
		return 'False'
	elif obj[7] == '90.92':
		return 'False'
	elif obj[7] == '102.27':
		return 'False'
	elif obj[7] == '85.33':
		return 'False'
	elif obj[7] == '114.09':
		return 'False'
	elif obj[7] == '84.21':
		return 'False'
	elif obj[7] == '78.85':
		return 'False'
	elif obj[7] == '72.09':
		return 'False'
	elif obj[7] == '78.04':
		return 'False'
	elif obj[7] == '66.55':
		return 'False'
	elif obj[7] == '81.94':
		return 'False'
	elif obj[7] == '82.41':
		return 'False'
	elif obj[7] == '59.74':
		return 'False'
	elif obj[7] == '110.38':
		return 'False'
	elif obj[7] == '107.29':
		return 'False'
	elif obj[7] == '100.85':
		return 'False'
	elif obj[7] == '86.0':
		return 'False'
	elif obj[7] == '111.94':
		return 'False'
	elif obj[7] == '90.16':
		return 'False'
	elif obj[7] == '81.21':
		return 'False'
	elif obj[7] == '69.92':
		return 'False'
	elif obj[7] == '61.1':
		return 'False'
	elif obj[7] == '120.77':
		return 'False'
	elif obj[7] == '73.72':
		return 'False'
	elif obj[7] == '222.29':
		return 'False'
	elif obj[7] == '216.88':
		return 'False'
	elif obj[7] == '92.65':
		return 'False'
	elif obj[7] == '81.68':
		return 'False'
	elif obj[7] == '98.74':
		return 'False'
	elif obj[7] == '181.23':
		return 'False'
	elif obj[7] == '93.04':
		return 'False'
	elif obj[7] == '76.7':
		return 'False'
	elif obj[7] == '95.94':
		return 'False'
	elif obj[7] == '111.1':
		return 'False'
	elif obj[7] == '79.53':
		return 'False'
	elif obj[7] == '70.87':
		return 'False'
	elif obj[7] == '64.66':
		return 'False'
	elif obj[7] == '126.34':
		return 'False'
	elif obj[7] == '86.99':
		return 'False'
	elif obj[7] == '76.42':
		return 'False'
	elif obj[7] == '105.29':
		return 'False'
	elif obj[7] == '80.8':
		return 'False'
	elif obj[7] == '89.06':
		return 'False'
	elif obj[7] == '67.06':
		return 'False'
	elif obj[7] == '71.38':
		return 'False'
	elif obj[7] == '81.73':
		return 'False'
	elif obj[7] == '59.28':
		return 'False'
	elif obj[7] == '62.56':
		return 'False'
	elif obj[7] == '58.39':
		return 'False'
	elif obj[7] == '85.92':
		return 'False'
	elif obj[7] == '82.31':
		return 'False'
	elif obj[7] == '118.55':
		return 'False'
	elif obj[7] == '75.09':
		return 'False'
	elif obj[7] == '56.42':
		return 'False'
	elif obj[7] == '67.87':
		return 'False'
	elif obj[7] == '99.07':
		return 'False'
	elif obj[7] == '97.37':
		return 'False'
	elif obj[7] == '142.12':
		return 'False'
	elif obj[7] == '108.56':
		return 'False'
	elif obj[7] == '83.1':
		return 'False'
	elif obj[7] == '86.4':
		return 'False'
	elif obj[7] == '106.68':
		return 'False'
	elif obj[7] == '87.15':
		return 'False'
	elif obj[7] == '77.16':
		return 'False'
	elif obj[7] == '105.73':
		return 'False'
	elif obj[7] == '89.03':
		return 'False'
	elif obj[7] == '91.34':
		return 'False'
	elif obj[7] == '73.36':
		return 'False'
	elif obj[7] == '124.38':
		return 'False'
	elif obj[7] == '70.03':
		return 'False'
	elif obj[7] == '74.86':
		return 'False'
	elif obj[7] == '71.4':
		return 'False'
	elif obj[7] == '78.11':
		return 'False'
	elif obj[7] == '98.07':
		return 'False'
	elif obj[7] == '92.14':
		return 'False'
	elif obj[7] == '92.95':
		return 'False'
	elif obj[7] == '78.93':
		return 'False'
	elif obj[7] == '208.05':
		return 'False'
	elif obj[7] == '95.44':
		return 'False'
	elif obj[7] == '94.71':
		return 'False'
	elif obj[7] == '62.99':
		return 'False'
	elif obj[7] == '125.89':
		return 'False'
	elif obj[7] == '119.9':
		return 'False'
	elif obj[7] == '88.51':
		return 'False'
	elif obj[7] == '103.94':
		return 'False'
	elif obj[7] == '67.99':
		return 'False'
	elif obj[7] == '91.93':
		return 'False'
	elif obj[7] == '110.68':
		return 'False'
	elif obj[7] == '90.4':
		return 'False'
	elif obj[7] == '65.29':
		return 'False'
	elif obj[7] == '82.44':
		return 'False'
	elif obj[7] == '71.08':
		return 'False'
	elif obj[7] == '102.39':
		return 'False'
	elif obj[7] == '168.15':
		return 'False'
	elif obj[7] == '66.32':
		return 'False'
	elif obj[7] == '91.04':
		return 'False'
	elif obj[7] == '93.58':
		return 'False'
	elif obj[7] == '112.98':
		return 'False'
	elif obj[7] == '85.29':
		return 'False'
	elif obj[7] == '65.98':
		return 'False'
	elif obj[7] == '82.62':
		return 'False'
	elif obj[7] == '105.63':
		return 'False'
	elif obj[7] == '59.67':
		return 'False'
	elif obj[7] == '102.89':
		return 'False'
	elif obj[7] == '88.79':
		return 'False'
	elif obj[7] == '65.47':
		return 'False'
	elif obj[7] == '63.78':
		return 'False'
	elif obj[7] == '56.48':
		return 'False'
	elif obj[7] == '96.02':
		return 'False'
	elif obj[7] == '202.66':
		return 'False'
	elif obj[7] == '56.07':
		return 'False'
	elif obj[7] == '98.05':
		return 'False'
	elif obj[7] == '117.63':
		return 'False'
	elif obj[7] == '85.52':
		return 'False'
	elif obj[7] == '83.88':
		return 'False'
	elif obj[7] == '92.59':
		return 'False'
	elif obj[7] == '83.89':
		return 'False'
	elif obj[7] == '80.42':
		return 'False'
	elif obj[7] == '76.19':
		return 'False'
	elif obj[7] == '129.43':
		return 'False'
	elif obj[7] == '60.61':
		return 'False'
	elif obj[7] == '61.11':
		return 'False'
	elif obj[7] == '89.14':
		return 'False'
	elif obj[7] == '73.5':
		return 'False'
	elif obj[7] == '80.44':
		return 'False'
	elif obj[7] == '206.53':
		return 'False'
	elif obj[7] == '95.04':
		return 'False'
	elif obj[7] == '78.48':
		return 'False'
	elif obj[7] == '87.16':
		return 'False'
	elif obj[7] == '93.85':
		return 'False'
	elif obj[7] == '97.47':
		return 'False'
	elif obj[7] == '79.79':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '68.0':
			return 'True'
		elif obj[1] == '50.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '56.9':
		return 'False'
	elif obj[7] == '86.78':
		return 'False'
	elif obj[7] == '205.23':
		return 'False'
	elif obj[7] == '77.82':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '68.0':
			return 'True'
		elif obj[1] == '50.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '98.09':
		return 'False'
	elif obj[7] == '67.5':
		return 'False'
	elif obj[7] == '60.77':
		return 'False'
	elif obj[7] == '83.07':
		return 'False'
	elif obj[7] == '74.02':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '81.0':
			return 'True'
		elif obj[1] == '20.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '73.48':
		return 'False'
	elif obj[7] == '203.87':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '78.0':
			return 'True'
		elif obj[1] == '63.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '71.5':
		return 'False'
	elif obj[7] == '57.28':
		return 'False'
	elif obj[7] == '81.76':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Male':
			return 'True'
		elif obj[0] == 'Female':
			return 'False'
		else: return 'False'
	elif obj[7] == '78.8':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Female':
			return 'True'
		elif obj[0] == 'Male':
			return 'False'
		else: return 'False'
	elif obj[7] == '87.96':
		return 'False'
	elif obj[7] == '101.52':
		return 'False'
	elif obj[7] == '77.59':
		return 'False'
	elif obj[7] == '62.57':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Female':
			return 'True'
		elif obj[0] == 'Male':
			return 'False'
		else: return 'False'
	elif obj[7] == '74.9':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Female':
			return 'True'
		elif obj[0] == 'Male':
			return 'False'
		else: return 'False'
	elif obj[7] == '93.72':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Female':
			return 'True'
		elif obj[0] == 'Male':
			return 'False'
		else: return 'False'
	elif obj[7] == '95.62':
		return 'False'
	elif obj[7] == '113.01':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Male':
			return 'True'
		elif obj[0] == 'Female':
			return 'False'
		else: return 'False'
	elif obj[7] == '64.4':
		return 'False'
	elif obj[7] == '70.23':
		return 'False'
	elif obj[7] == '77.67':
		return 'False'
	elif obj[7] == '59.91':
		return 'False'
	elif obj[7] == '110.42':
		return 'False'
	elif obj[7] == '220.47':
		return 'False'
	elif obj[7] == '200.28':
		return 'False'
	elif obj[7] == '95.1':
		return 'False'
	elif obj[7] == '140.1':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '76.0':
			return 'True'
		elif obj[1] == '16.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '68.53':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Male':
			return 'True'
		elif obj[0] == 'Female':
			return 'False'
		else: return 'False'
	elif obj[7] == '111.38':
		return 'False'
	elif obj[7] == '203.04':
		return 'False'
	elif obj[7] == '89.44':
		return 'False'
	elif obj[7] == '82.35':
		return 'False'
	elif obj[7] == '114.34':
		return 'False'
	elif obj[7] == '72.71':
		return 'False'
	elif obj[7] == '99.83':
		return 'False'
	elif obj[7] == '77.99':
		return 'False'
	elif obj[7] == '99.76':
		return 'False'
	elif obj[7] == '66.67':
		return 'False'
	elif obj[7] == '72.96':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '74.0':
			return 'True'
		elif obj[1] == '54.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '105.22':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '77.0':
			return 'True'
		elif obj[1] == '22.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '99.23':
		return 'False'
	elif obj[7] == '102.64':
		return 'False'
	elif obj[7] == '88.19':
		return 'False'
	elif obj[7] == '84.48':
		return 'False'
	elif obj[7] == '202.21':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '61.0':
			return 'True'
		elif obj[1] == '76.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '130.07':
		return 'False'
	elif obj[7] == '77.29':
		return 'False'
	elif obj[7] == '82.24':
		return 'False'
	elif obj[7] == '87.81':
		return 'False'
	elif obj[7] == '68.48':
		return 'False'
	elif obj[7] == '67.29':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '78.0':
			return 'True'
		elif obj[1] == '36.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '76.34':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '70.0':
			return 'True'
		elif obj[1] == '20.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '66.3':
		return 'False'
	elif obj[7] == '198.79':
		return 'False'
	elif obj[7] == '84.88':
		return 'False'
	elif obj[7] == '118.82':
		return 'False'
	elif obj[7] == '67.07':
		return 'False'
	elif obj[7] == '69.2':
		return 'False'
	elif obj[7] == '62.6':
		return 'False'
	elif obj[7] == '70.28':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Female':
			return 'True'
		elif obj[0] == 'Male':
			return 'False'
		else: return 'False'
	elif obj[7] == '69.88':
		return 'False'
	elif obj[7] == '80.82':
		return 'False'
	elif obj[7] == '116.44':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Female':
			return 'True'
		elif obj[0] == 'Male':
			return 'False'
		else: return 'False'
	elif obj[7] == '73.18':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Female':
			return 'True'
		elif obj[0] == 'Male':
			return 'False'
		else: return 'False'
	elif obj[7] == '82.72':
		return 'False'
	elif obj[7] == '67.02':
		return 'False'
	elif obj[7] == '61.94':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '67.0':
			return 'True'
		elif obj[1] == '60.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '59.52':
		return 'False'
	elif obj[7] == '120.58':
		return 'False'
	elif obj[7] == '107.59':
		return 'False'
	elif obj[7] == '91.02':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '80.0':
			return 'True'
		elif obj[1] == '34.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '104.86':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Male':
			return 'True'
		elif obj[0] == 'Female':
			return 'False'
		else: return 'False'
	elif obj[7] == '101.13':
		return 'False'
	elif obj[7] == '84.03':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '82.0':
			return 'True'
		elif obj[1] == '42.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '70.16':
		return 'False'
	elif obj[7] == '60.67':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '78.0':
			return 'True'
		elif obj[1] == '63.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '74.11':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '48.0':
			return 'True'
		elif obj[1] == '25.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '82.27':
		return 'False'
	elif obj[7] == '124.37':
		return 'False'
	elif obj[7] == '80.88':
		return 'False'
	elif obj[7] == '65.42':
		return 'False'
	elif obj[7] == '111.04':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '59.0':
			return 'True'
		elif obj[1] == '52.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '203.81':
		return 'False'
	elif obj[7] == '80.0':
		return 'False'
	elif obj[7] == '79.92':
		return 'False'
	elif obj[7] == '111.48':
		return 'False'
	elif obj[7] == '58.63':
		return 'False'
	elif obj[7] == '72.79':
		return 'False'
	elif obj[7] == '70.73':
		return 'False'
	elif obj[7] == '102.87':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Male':
			return 'True'
		elif obj[0] == 'Female':
			return 'False'
		else: return 'False'
	elif obj[7] == '116.98':
		return 'False'
	elif obj[7] == '104.12':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Male':
			return 'True'
		elif obj[0] == 'Female':
			return 'False'
		else: return 'False'
	elif obj[7] == '90.01':
		return 'False'
	elif obj[7] == '64.44':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '80.0':
			return 'True'
		elif obj[1] == '79.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '65.66':
		return 'False'
	elif obj[7] == '69.72':
		return 'False'
	elif obj[7] == '87.62':
		return 'False'
	elif obj[7] == '79.55':
		return 'False'
	elif obj[7] == '58.42':
		return 'False'
	elif obj[7] == '209.5':
		return 'False'
	elif obj[7] == '80.81':
		return 'False'
	elif obj[7] == '205.77':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Female':
			return 'True'
		elif obj[0] == 'Male':
			return 'False'
		else: return 'False'
	elif obj[7] == '68.19':
		return 'False'
	elif obj[7] == '63.98':
		return 'False'
	elif obj[7] == '86.25':
		return 'False'
	elif obj[7] == '88.47':
		return 'False'
	elif obj[7] == '103.43':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '51.0':
			return 'True'
		elif obj[1] == '34.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '81.31':
		return 'False'
	elif obj[7] == '104.21':
		return 'False'
	elif obj[7] == '81.13':
		return 'False'
	elif obj[7] == '97.55':
		return 'False'
	elif obj[7] == '110.18':
		return 'False'
	elif obj[7] == '78.18':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '46.0':
			return 'True'
		elif obj[1] == '44.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '90.9':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '63.0':
			return 'True'
		elif obj[1] == '81.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '65.77':
		return 'False'
	elif obj[7] == '87.06':
		return 'False'
	elif obj[7] == '106.74':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Female':
			return 'True'
		elif obj[0] == 'Male':
			return 'False'
		else: return 'False'
	elif obj[7] == '97.92':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '72.0':
			return 'True'
		elif obj[1] == '24.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '112.09':
		return 'False'
	elif obj[7] == '98.02':
		# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '79.0':
			return 'True'
		elif obj[1] == '37.0':
			return 'False'
		else: return 'False'
	elif obj[7] == '71.22':
		# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Male':
			return 'True'
		elif obj[0] == 'Female':
			return 'False'
		else: return 'False'
	elif obj[7] == '86.36':
		return 'False'
	elif obj[7] == '94.19':
		return 'False'
	elif obj[7] == '69.67':
		return 'False'
	elif obj[7] == '104.66':
		return 'False'
	elif obj[7] == '62.54':
		return 'False'
	elif obj[7] == '142.38':
		return 'False'
	elif obj[7] == '92.26':
		return 'False'
	elif obj[7] == '103.79':
		return 'False'
	elif obj[7] == '76.81':
		return 'False'
	elif obj[7] == '73.04':
		return 'False'
	elif obj[7] == '223.14':
		return 'False'
	elif obj[7] == '104.05':
		return 'False'
	elif obj[7] == '89.02':
		return 'False'
	elif obj[7] == '69.28':
		return 'False'
	elif obj[7] == '74.85':
		return 'False'
	elif obj[7] == '93.62':
		return 'False'
	elif obj[7] == '214.51':
		return 'False'
	elif obj[7] == '174.43':
		return 'False'
	elif obj[7] == '91.19':
		return 'False'
	elif obj[7] == '101.24':
		return 'False'
	elif obj[7] == '83.42':
		return 'False'
	elif obj[7] == '94.45':
		return 'False'
	elif obj[7] == '105.51':
		return 'False'
	elif obj[7] == '105.93':
		return 'False'
	elif obj[7] == '55.96':
		return 'False'
	elif obj[7] == '94.53':
		return 'False'
	elif obj[7] == '84.12':
		return 'False'
	elif obj[7] == '215.92':
		return 'False'
	elif obj[7] == '150.03':
		return 'False'
	elif obj[7] == '198.12':
		return 'False'
	elif obj[7] == '100.75':
		return 'False'
	elif obj[7] == '85.55':
		return 'False'
	elif obj[7] == '118.22':
		return 'False'
	elif obj[7] == '92.34':
		return 'False'
	elif obj[7] == '85.59':
		return 'False'
	elif obj[7] == '111.68':
		return 'False'
	elif obj[7] == '86.03':
		return 'False'
	elif obj[7] == '123.66':
		return 'False'
	elif obj[7] == '73.19':
		return 'False'
	elif obj[7] == '72.64':
		return 'False'
	elif obj[7] == '87.87':
		return 'False'
	elif obj[7] == '217.55':
		return 'False'
	elif obj[7] == '91.05':
		return 'False'
	elif obj[7] == '78.88':
		return 'False'
	elif obj[7] == '103.6':
		return 'False'
	elif obj[7] == '77.91':
		return 'False'
	elif obj[7] == '116.84':
		return 'False'
	elif obj[7] == '97.39':
		return 'False'
	elif obj[7] == '107.82':
		return 'False'
	elif obj[7] == '200.14':
		return 'False'
	elif obj[7] == '108.68':
		return 'False'
	elif obj[7] == '255.17':
		return 'False'
	elif obj[7] == '65.41':
		return 'False'
	elif obj[7] == '83.61':
		return 'False'
	elif obj[7] == '81.11':
		return 'False'
	elif obj[7] == '87.82':
		return 'False'
	elif obj[7] == '240.86':
		return 'False'
	elif obj[7] == '110.87':
		return 'False'
	elif obj[7] == '90.06':
		return 'False'
	elif obj[7] == '73.6':
		return 'False'
	elif obj[7] == '78.0':
		return 'False'
	elif obj[7] == '182.9':
		return 'False'
	elif obj[7] == '75.28':
		return 'False'
	elif obj[7] == '75.82':
		return 'False'
	elif obj[7] == '82.68':
		return 'False'
	elif obj[7] == '90.04':
		return 'False'
	elif obj[7] == '163.82':
		return 'False'
	elif obj[7] == '123.04':
		return 'False'
	elif obj[7] == '107.99':
		return 'False'
	elif obj[7] == '79.94':
		return 'False'
	elif obj[7] == '263.56':
		return 'False'
	elif obj[7] == '118.44':
		return 'False'
	elif obj[7] == '90.22':
		return 'False'
	elif obj[7] == '99.84':
		return 'False'
	elif obj[7] == '235.45':
		return 'False'
	elif obj[7] == '95.88':
		return 'False'
	elif obj[7] == '73.49':
		return 'False'
	elif obj[7] == '115.86':
		return 'False'
	elif obj[7] == '112.77':
		return 'False'
	elif obj[7] == '101.43':
		return 'False'
	elif obj[7] == '86.93':
		return 'False'
	elif obj[7] == '76.51':
		return 'False'
	elif obj[7] == '172.33':
		return 'False'
	elif obj[7] == '55.72':
		return 'False'
	elif obj[7] == '75.67':
		return 'False'
	elif obj[7] == '88.18':
		return 'False'
	elif obj[7] == '95.66':
		return 'False'
	elif obj[7] == '213.33':
		return 'False'
	elif obj[7] == '94.76':
		return 'False'
	elif obj[7] == '83.97':
		return 'False'
	elif obj[7] == '98.55':
		return 'False'
	elif obj[7] == '202.98':
		return 'False'
	elif obj[7] == '60.7':
		return 'False'
	elif obj[7] == '92.22':
		return 'False'
	elif obj[7] == '56.89':
		return 'False'
	elif obj[7] == '93.02':
		return 'False'
	elif obj[7] == '243.59':
		return 'False'
	elif obj[7] == '103.37':
		return 'False'
	elif obj[7] == '97.81':
		return 'False'
	elif obj[7] == '116.04':
		return 'False'
	elif obj[7] == '87.47':
		return 'False'
	elif obj[7] == '169.43':
		return 'False'
	elif obj[7] == '68.41':
		return 'False'
	elif obj[7] == '68.94':
		return 'False'
	elif obj[7] == '192.47':
		return 'False'
	elif obj[7] == '183.87':
		return 'False'
	elif obj[7] == '83.5':
		return 'False'
	elif obj[7] == '64.94':
		return 'False'
	elif obj[7] == '108.71':
		return 'False'
	elif obj[7] == '66.08':
		return 'False'
	elif obj[7] == '82.33':
		return 'False'
	elif obj[7] == '99.65':
		return 'False'
	elif obj[7] == '105.74':
		return 'False'
	elif obj[7] == '216.38':
		return 'False'
	elif obj[7] == '231.95':
		return 'False'
	elif obj[7] == '69.42':
		return 'False'
	elif obj[7] == '71.32':
		return 'False'
	elif obj[7] == '65.48':
		return 'False'
	elif obj[7] == '71.3':
		return 'False'
	elif obj[7] == '102.21':
		return 'False'
	elif obj[7] == '101.57':
		return 'False'
	elif obj[7] == '77.3':
		return 'False'
	elif obj[7] == '104.08':
		return 'False'
	elif obj[7] == '97.97':
		return 'False'
	elif obj[7] == '219.82':
		return 'False'
	elif obj[7] == '81.33':
		return 'False'
	elif obj[7] == '236.79':
		return 'False'
	elif obj[7] == '112.79':
		return 'False'
	elif obj[7] == '126.68':
		return 'False'
	elif obj[7] == '77.68':
		return 'False'
	elif obj[7] == '124.64':
		return 'False'
	elif obj[7] == '95.32':
		return 'False'
	elif obj[7] == '196.61':
		return 'False'
	elif obj[7] == '219.92':
		return 'False'
	elif obj[7] == '226.38':
		return 'False'
	elif obj[7] == '87.41':
		return 'False'
	elif obj[7] == '79.16':
		return 'False'
	elif obj[7] == '99.68':
		return 'False'
	elif obj[7] == '79.77':
		return 'False'
	elif obj[7] == '87.86':
		return 'False'
	elif obj[7] == '112.69':
		return 'False'
	elif obj[7] == '120.94':
		return 'False'
	elif obj[7] == '77.66':
		return 'False'
	elif obj[7] == '100.16':
		return 'False'
	elif obj[7] == '198.32':
		return 'False'
	elif obj[7] == '107.78':
		return 'False'
	elif obj[7] == '101.09':
		return 'False'
	elif obj[7] == '100.08':
		return 'False'
	elif obj[7] == '69.99':
		return 'False'
	elif obj[7] == '83.64':
		return 'False'
	elif obj[7] == '188.13':
		return 'False'
	elif obj[7] == '227.74':
		return 'False'
	elif obj[7] == '94.25':
		return 'False'
	elif obj[7] == '100.05':
		return 'False'
	elif obj[7] == '100.22':
		return 'False'
	elif obj[7] == '213.8':
		return 'False'
	elif obj[7] == '63.63':
		return 'False'
	elif obj[7] == '75.46':
		return 'False'
	elif obj[7] == '89.74':
		return 'False'
	elif obj[7] == '250.8':
		return 'False'
	elif obj[7] == '70.11':
		return 'False'
	elif obj[7] == '217.84':
		return 'False'
	elif obj[7] == '233.59':
		return 'False'
	elif obj[7] == '217.0':
		return 'False'
	elif obj[7] == '57.47':
		return 'False'
	elif obj[7] == '100.12':
		return 'False'
	elif obj[7] == '71.66':
		return 'False'
	elif obj[7] == '78.24':
		return 'False'
	elif obj[7] == '110.28':
		return 'False'
	elif obj[7] == '87.18':
		return 'False'
	elif obj[7] == '238.78':
		return 'False'
	elif obj[7] == '94.38':
		return 'False'
	elif obj[7] == '91.57':
		return 'False'
	elif obj[7] == '231.31':
		return 'False'
	elif obj[7] == '79.89':
		return 'False'
	elif obj[7] == '131.19':
		return 'False'
	elif obj[7] == '65.46':
		return 'False'
	elif obj[7] == '217.4':
		return 'False'
	elif obj[7] == '141.16':
		return 'False'
	elif obj[7] == '190.92':
		return 'False'
	elif obj[7] == '235.54':
		return 'False'
	elif obj[7] == '151.23':
		return 'False'
	elif obj[7] == '197.11':
		return 'False'
	elif obj[7] == '78.97':
		return 'False'
	elif obj[7] == '102.4':
		return 'False'
	elif obj[7] == '189.88':
		return 'False'
	elif obj[7] == '108.18':
		return 'False'
	elif obj[7] == '80.34':
		return 'False'
	elif obj[7] == '87.26':
		return 'False'
	elif obj[7] == '75.73':
		return 'False'
	elif obj[7] == '76.83':
		return 'False'
	elif obj[7] == '98.35':
		return 'False'
	elif obj[7] == '162.24':
		return 'False'
	elif obj[7] == '79.95':
		return 'False'
	elif obj[7] == '97.25':
		return 'False'
	elif obj[7] == '106.01':
		return 'False'
	elif obj[7] == '214.77':
		return 'False'
	elif obj[7] == '130.0':
		return 'False'
	elif obj[7] == '103.15':
		return 'False'
	elif obj[7] == '112.41':
		return 'False'
	elif obj[7] == '82.91':
		return 'False'
	elif obj[7] == '153.6':
		return 'False'
	elif obj[7] == '81.0':
		return 'False'
	elif obj[7] == '84.46':
		return 'False'
	elif obj[7] == '138.02':
		return 'False'
	elif obj[7] == '101.32':
		return 'False'
	elif obj[7] == '208.2':
		return 'False'
	elif obj[7] == '199.42':
		return 'False'
	elif obj[7] == '190.89':
		return 'False'
	elif obj[7] == '71.93':
		return 'False'
	elif obj[7] == '190.13':
		return 'False'
	elif obj[7] == '112.19':
		return 'False'
	elif obj[7] == '149.68':
		return 'False'
	elif obj[7] == '205.97':
		return 'False'
	elif obj[7] == '219.17':
		return 'False'
	elif obj[7] == '63.86':
		return 'False'
	elif obj[7] == '226.73':
		return 'False'
	elif obj[7] == '91.36':
		return 'False'
	elif obj[7] == '143.33':
		return 'False'
	elif obj[7] == '78.02':
		return 'False'
	elif obj[7] == '82.02':
		return 'False'
	elif obj[7] == '60.36':
		return 'False'
	elif obj[7] == '65.33':
		return 'False'
	elif obj[7] == '113.28':
		return 'False'
	elif obj[7] == '160.87':
		return 'False'
	elif obj[7] == '161.95':
		return 'False'
	elif obj[7] == '115.42':
		return 'False'
	elif obj[7] == '73.37':
		return 'False'
	elif obj[7] == '106.08':
		return 'False'
	elif obj[7] == '59.93':
		return 'False'
	elif obj[7] == '105.99':
		return 'False'
	elif obj[7] == '79.27':
		return 'False'
	elif obj[7] == '156.45':
		return 'False'
	elif obj[7] == '72.1':
		return 'False'
	elif obj[7] == '83.13':
		return 'False'
	elif obj[7] == '109.46':
		return 'False'
	elif obj[7] == '267.61':
		return 'False'
	elif obj[7] == '114.05':
		return 'False'
	elif obj[7] == '96.73':
		return 'False'
	elif obj[7] == '72.42':
		return 'False'
	elif obj[7] == '112.46':
		return 'False'
	elif obj[7] == '106.22':
		return 'False'
	elif obj[7] == '104.04':
		return 'False'
	elif obj[7] == '83.58':
		return 'False'
	elif obj[7] == '67.68':
		return 'False'
	elif obj[7] == '71.8':
		return 'False'
	elif obj[7] == '80.92':
		return 'False'
	elif obj[7] == '195.61':
		return 'False'
	elif obj[7] == '63.72':
		return 'False'
	elif obj[7] == '55.64':
		return 'False'
	elif obj[7] == '111.78':
		return 'False'
	elif obj[7] == '231.43':
		return 'False'
	elif obj[7] == '69.23':
		return 'False'
	elif obj[7] == '98.57':
		return 'False'
	elif obj[7] == '82.4':
		return 'False'
	elif obj[7] == '80.96':
		return 'False'
	elif obj[7] == '73.78':
		return 'False'
	elif obj[7] == '108.72':
		return 'False'
	elif obj[7] == '95.38':
		return 'False'
	elif obj[7] == '211.12':
		return 'False'
	elif obj[7] == '69.12':
		return 'False'
	elif obj[7] == '102.48':
		return 'False'
	elif obj[7] == '82.83':
		return 'False'
	elif obj[7] == '122.26':
		return 'False'
	elif obj[7] == '220.26':
		return 'False'
	elif obj[7] == '112.62':
		return 'False'
	elif obj[7] == '105.77':
		return 'False'
	elif obj[7] == '88.88':
		return 'False'
	elif obj[7] == '77.53':
		return 'False'
	elif obj[7] == '116.2':
		return 'False'
	elif obj[7] == '207.62':
		return 'False'
	elif obj[7] == '77.35':
		return 'False'
	elif obj[7] == '239.95':
		return 'False'
	elif obj[7] == '64.02':
		return 'False'
	elif obj[7] == '157.67':
		return 'False'
	elif obj[7] == '161.0':
		return 'False'
	elif obj[7] == '61.96':
		return 'False'
	elif obj[7] == '102.46':
		return 'False'
	elif obj[7] == '176.71':
		return 'False'
	elif obj[7] == '59.62':
		return 'False'
	elif obj[7] == '56.08':
		return 'False'
	elif obj[7] == '114.61':
		return 'False'
	elif obj[7] == '102.11':
		return 'False'
	elif obj[7] == '63.6':
		return 'False'
	elif obj[7] == '102.36':
		return 'False'
	elif obj[7] == '80.76':
		return 'False'
	elif obj[7] == '202.67':
		return 'False'
	elif obj[7] == '56.37':
		return 'False'
	elif obj[7] == '91.82':
		return 'False'
	elif obj[7] == '216.71':
		return 'False'
	elif obj[7] == '90.39':
		return 'False'
	elif obj[7] == '202.55':
		return 'False'
	elif obj[7] == '69.35':
		return 'False'
	elif obj[7] == '227.89':
		return 'False'
	elif obj[7] == '74.53':
		return 'False'
	elif obj[7] == '65.16':
		return 'False'
	elif obj[7] == '91.53':
		return 'False'
	elif obj[7] == '64.92':
		return 'False'
	elif obj[7] == '154.6':
		return 'False'
	elif obj[7] == '204.98':
		return 'False'
	elif obj[7] == '95.98':
		return 'False'
	elif obj[7] == '80.01':
		return 'False'
	elif obj[7] == '72.5':
		return 'False'
	elif obj[7] == '230.78':
		return 'False'
	elif obj[7] == '102.51':
		return 'False'
	elif obj[7] == '65.01':
		return 'False'
	elif obj[7] == '232.12':
		return 'False'
	elif obj[7] == '70.04':
		return 'False'
	elif obj[7] == '97.61':
		return 'False'
	elif obj[7] == '96.37':
		return 'False'
	elif obj[7] == '72.94':
		return 'False'
	elif obj[7] == '107.83':
		return 'False'
	elif obj[7] == '86.09':
		return 'False'
	elif obj[7] == '111.47':
		return 'False'
	elif obj[7] == '69.26':
		return 'False'
	elif obj[7] == '107.21':
		return 'False'
	elif obj[7] == '100.03':
		return 'False'
	elif obj[7] == '221.8':
		return 'False'
	elif obj[7] == '147.12':
		return 'False'
	elif obj[7] == '103.21':
		return 'False'
	elif obj[7] == '81.42':
		return 'False'
	elif obj[7] == '220.24':
		return 'False'
	elif obj[7] == '139.48':
		return 'False'
	elif obj[7] == '67.38':
		return 'False'
	elif obj[7] == '90.21':
		return 'False'
	elif obj[7] == '149.17':
		return 'False'
	elif obj[7] == '139.72':
		return 'False'
	elif obj[7] == '80.22':
		return 'False'
	elif obj[7] == '65.4':
		return 'False'
	elif obj[7] == '103.76':
		return 'False'
	elif obj[7] == '215.81':
		return 'False'
	elif obj[7] == '73.7':
		return 'False'
	elif obj[7] == '106.85':
		return 'False'
	elif obj[7] == '77.06':
		return 'False'
	elif obj[7] == '181.3':
		return 'False'
	elif obj[7] == '140.07':
		return 'False'
	elif obj[7] == '110.36':
		return 'False'
	elif obj[7] == '75.78':
		return 'False'
	elif obj[7] == '62.52':
		return 'False'
	elif obj[7] == '103.17':
		return 'False'
	elif obj[7] == '83.37':
		return 'False'
	elif obj[7] == '131.8':
		return 'False'
	elif obj[7] == '89.87':
		return 'False'
	elif obj[7] == '92.44':
		return 'False'
	elif obj[7] == '90.68':
		return 'False'
	elif obj[7] == '87.51':
		return 'False'
	elif obj[7] == '85.48':
		return 'False'
	elif obj[7] == '84.69':
		return 'False'
	elif obj[7] == '95.47':
		return 'False'
	elif obj[7] == '103.45':
		return 'False'
	elif obj[7] == '86.11':
		return 'False'
	elif obj[7] == '71.37':
		return 'False'
	elif obj[7] == '102.58':
		return 'False'
	elif obj[7] == '214.43':
		return 'False'
	elif obj[7] == '91.13':
		return 'False'
	elif obj[7] == '59.83':
		return 'False'
	elif obj[7] == '142.82':
		return 'False'
	elif obj[7] == '124.49':
		return 'False'
	elif obj[7] == '102.42':
		return 'False'
	elif obj[7] == '97.41':
		return 'False'
	elif obj[7] == '77.55':
		return 'False'
	elif obj[7] == '125.3':
		return 'False'
	elif obj[7] == '109.23':
		return 'False'
	elif obj[7] == '127.57':
		return 'False'
	elif obj[7] == '64.18':
		return 'False'
	elif obj[7] == '140.96':
		return 'False'
	elif obj[7] == '118.81':
		return 'False'
	elif obj[7] == '84.16':
		return 'False'
	elif obj[7] == '82.12':
		return 'False'
	elif obj[7] == '163.02':
		return 'False'
	elif obj[7] == '78.74':
		return 'False'
	elif obj[7] == '86.15':
		return 'False'
	elif obj[7] == '57.17':
		return 'False'
	elif obj[7] == '115.99':
		return 'False'
	elif obj[7] == '72.6':
		return 'False'
	elif obj[7] == '84.7':
		return 'False'
	elif obj[7] == '94.69':
		return 'False'
	elif obj[7] == '151.25':
		return 'False'
	elif obj[7] == '57.77':
		return 'False'
	elif obj[7] == '56.12':
		return 'False'
	elif obj[7] == '69.76':
		return 'False'
	elif obj[7] == '196.81':
		return 'False'
	elif obj[7] == '127.2':
		return 'False'
	elif obj[7] == '107.49':
		return 'False'
	elif obj[7] == '72.33':
		return 'False'
	elif obj[7] == '90.87':
		return 'False'
	elif obj[7] == '158.93':
		return 'False'
	elif obj[7] == '227.68':
		return 'False'
	elif obj[7] == '59.68':
		return 'False'
	elif obj[7] == '94.24':
		return 'False'
	elif obj[7] == '62.62':
		return 'False'
	elif obj[7] == '92.71':
		return 'False'
	elif obj[7] == '228.92':
		return 'False'
	elif obj[7] == '59.07':
		return 'False'
	elif obj[7] == '67.76':
		return 'False'
	elif obj[7] == '160.64':
		return 'False'
	elif obj[7] == '143.47':
		return 'False'
	elif obj[7] == '115.69':
		return 'False'
	elif obj[7] == '84.6':
		return 'False'
	elif obj[7] == '135.74':
		return 'False'
	elif obj[7] == '110.72':
		return 'False'
	elif obj[7] == '72.0':
		return 'False'
	elif obj[7] == '84.78':
		return 'False'
	elif obj[7] == '57.76':
		return 'False'
	elif obj[7] == '148.72':
		return 'False'
	elif obj[7] == '92.21':
		return 'False'
	elif obj[7] == '108.65':
		return 'False'
	elif obj[7] == '248.37':
		return 'False'
	elif obj[7] == '100.96':
		return 'False'
	elif obj[7] == '59.85':
		return 'False'
	elif obj[7] == '90.6':
		return 'False'
	elif obj[7] == '99.35':
		return 'False'
	elif obj[7] == '204.77':
		return 'False'
	elif obj[7] == '83.93':
		return 'False'
	elif obj[7] == '69.53':
		return 'False'
	elif obj[7] == '220.64':
		return 'False'
	elif obj[7] == '164.77':
		return 'False'
	elif obj[7] == '71.02':
		return 'False'
	elif obj[7] == '222.66':
		return 'False'
	elif obj[7] == '223.58':
		return 'False'
	elif obj[7] == '228.2':
		return 'False'
	elif obj[7] == '104.45':
		return 'False'
	elif obj[7] == '87.23':
		return 'False'
	elif obj[7] == '63.16':
		return 'False'
	elif obj[7] == '93.76':
		return 'False'
	elif obj[7] == '103.89':
		return 'False'
	elif obj[7] == '95.29':
		return 'False'
	elif obj[7] == '65.51':
		return 'False'
	elif obj[7] == '92.99':
		return 'False'
	elif obj[7] == '193.81':
		return 'False'
	elif obj[7] == '90.49':
		return 'False'
	elif obj[7] == '80.1':
		return 'False'
	elif obj[7] == '66.59':
		return 'False'
	elif obj[7] == '97.27':
		return 'False'
	elif obj[7] == '92.15':
		return 'False'
	elif obj[7] == '137.91':
		return 'False'
	elif obj[7] == '85.77':
		return 'False'
	elif obj[7] == '137.77':
		return 'False'
	elif obj[7] == '88.5':
		return 'False'
	elif obj[7] == '61.47':
		return 'False'
	elif obj[7] == '62.91':
		return 'False'
	elif obj[7] == '105.19':
		return 'False'
	elif obj[7] == '104.92':
		return 'False'
	elif obj[7] == '104.4':
		return 'False'
	elif obj[7] == '68.79':
		return 'False'
	elif obj[7] == '121.17':
		return 'False'
	elif obj[7] == '82.18':
		return 'False'
	elif obj[7] == '215.33':
		return 'False'
	elif obj[7] == '87.25':
		return 'False'
	elif obj[7] == '74.14':
		return 'False'
	elif obj[7] == '96.81':
		return 'False'
	elif obj[7] == '68.13':
		return 'False'
	elif obj[7] == '201.38':
		return 'False'
	elif obj[7] == '113.65':
		return 'False'
	elif obj[7] == '65.93':
		return 'False'
	elif obj[7] == '141.8':
		return 'False'
	elif obj[7] == '72.01':
		return 'False'
	elif obj[7] == '88.49':
		return 'False'
	elif obj[7] == '88.89':
		return 'False'
	elif obj[7] == '113.57':
		return 'False'
	elif obj[7] == '92.37':
		return 'False'
	elif obj[7] == '94.2':
		return 'False'
	elif obj[7] == '123.81':
		return 'False'
	elif obj[7] == '90.54':
		return 'False'
	elif obj[7] == '90.65':
		return 'False'
	elif obj[7] == '111.65':
		return 'False'
	elif obj[7] == '205.01':
		return 'False'
	elif obj[7] == '192.39':
		return 'False'
	elif obj[7] == '70.29':
		return 'False'
	elif obj[7] == '71.94':
		return 'False'
	elif obj[7] == '67.73':
		return 'False'
	elif obj[7] == '176.78':
		return 'False'
	elif obj[7] == '73.28':
		return 'False'
	elif obj[7] == '109.27':
		return 'False'
	elif obj[7] == '79.96':
		return 'False'
	elif obj[7] == '207.96':
		return 'False'
	elif obj[7] == '85.27':
		return 'False'
	elif obj[7] == '82.25':
		return 'False'
	elif obj[7] == '169.74':
		return 'False'
	elif obj[7] == '93.18':
		return 'False'
	elif obj[7] == '82.86':
		return 'False'
	elif obj[7] == '97.87':
		return 'False'
	elif obj[7] == '223.9':
		return 'False'
	elif obj[7] == '93.78':
		return 'False'
	elif obj[7] == '65.07':
		return 'False'
	elif obj[7] == '228.69':
		return 'True'
	elif obj[7] == '78.45':
		return 'False'
	elif obj[7] == '240.69':
		return 'False'
	elif obj[7] == '213.92':
		return 'False'
	elif obj[7] == '92.23':
		return 'False'
	elif obj[7] == '68.42':
		return 'False'
	elif obj[7] == '212.19':
		return 'False'
	elif obj[7] == '89.0':
		return 'False'
	elif obj[7] == '58.19':
		return 'False'
	elif obj[7] == '62.13':
		return 'False'
	elif obj[7] == '57.1':
		return 'False'
	elif obj[7] == '97.95':
		return 'False'
	elif obj[7] == '77.96':
		return 'False'
	elif obj[7] == '60.13':
		return 'False'
	elif obj[7] == '88.17':
		return 'False'
	elif obj[7] == '84.41':
		return 'False'
	elif obj[7] == '68.72':
		return 'False'
	elif obj[7] == '222.58':
		return 'False'
	elif obj[7] == '66.06':
		return 'False'
	elif obj[7] == '156.43':
		return 'False'
	elif obj[7] == '105.76':
		return 'False'
	elif obj[7] == '73.07':
		return 'False'
	elif obj[7] == '172.86':
		return 'False'
	elif obj[7] == '90.73':
		return 'False'
	elif obj[7] == '166.38':
		return 'False'
	elif obj[7] == '108.14':
		return 'False'
	elif obj[7] == '195.43':
		return 'False'
	elif obj[7] == '200.25':
		return 'False'
	elif obj[7] == '95.33':
		return 'False'
	elif obj[7] == '223.64':
		return 'False'
	elif obj[7] == '85.46':
		return 'False'
	elif obj[7] == '101.56':
		return 'False'
	elif obj[7] == '72.88':
		return 'False'
	elif obj[7] == '70.89':
		return 'False'
	elif obj[7] == '244.3':
		return 'False'
	elif obj[7] == '65.22':
		return 'False'
	elif obj[7] == '106.73':
		return 'False'
	elif obj[7] == '127.4':
		return 'False'
	elif obj[7] == '58.23':
		return 'False'
	elif obj[7] == '69.37':
		return 'False'
	elif obj[7] == '58.64':
		return 'False'
	elif obj[7] == '78.08':
		return 'False'
	elif obj[7] == '105.08':
		return 'False'
	elif obj[7] == '90.28':
		return 'False'
	elif obj[7] == '99.48':
		return 'False'
	elif obj[7] == '70.0':
		return 'False'
	elif obj[7] == '73.2':
		return 'False'
	elif obj[7] == '123.94':
		return 'False'
	elif obj[7] == '152.38':
		return 'False'
	elif obj[7] == '114.54':
		return 'False'
	elif obj[7] == '174.54':
		return 'False'
	elif obj[7] == '73.63':
		return 'False'
	elif obj[7] == '98.52':
		return 'False'
	elif obj[7] == '62.93':
		return 'False'
	elif obj[7] == '76.56':
		return 'False'
	elif obj[7] == '67.9':
		return 'False'
	elif obj[7] == '231.54':
		return 'False'
	elif obj[7] == '66.7':
		return 'False'
	elif obj[7] == '219.8':
		return 'False'
	elif obj[7] == '187.99':
		return 'False'
	elif obj[7] == '234.45':
		return 'False'
	elif obj[7] == '75.47':
		return 'False'
	elif obj[7] == '98.24':
		return 'False'
	elif obj[7] == '75.95':
		return 'False'
	elif obj[7] == '111.79':
		return 'False'
	elif obj[7] == '86.91':
		return 'False'
	elif obj[7] == '90.96':
		return 'False'
	elif obj[7] == '96.98':
		return 'False'
	elif obj[7] == '102.73':
		return 'False'
	elif obj[7] == '110.14':
		return 'False'
	elif obj[7] == '122.43':
		return 'False'
	elif obj[7] == '96.82':
		return 'False'
	elif obj[7] == '88.1':
		return 'False'
	elif obj[7] == '97.68':
		return 'False'
	elif obj[7] == '97.58':
		return 'False'
	elif obj[7] == '74.16':
		return 'False'
	elif obj[7] == '100.93':
		return 'False'
	elif obj[7] == '232.78':
		return 'False'
	elif obj[7] == '120.44':
		return 'False'
	elif obj[7] == '242.62':
		return 'False'
	elif obj[7] == '187.47':
		return 'False'
	elif obj[7] == '89.57':
		return 'False'
	elif obj[7] == '95.31':
		return 'False'
	elif obj[7] == '75.07':
		return 'False'
	elif obj[7] == '106.65':
		return 'False'
	elif obj[7] == '234.06':
		return 'False'
	elif obj[7] == '144.15':
		return 'False'
	elif obj[7] == '58.81':
		return 'False'
	elif obj[7] == '94.14':
		return 'False'
	elif obj[7] == '99.96':
		return 'False'
	elif obj[7] == '104.9':
		return 'False'
	elif obj[7] == '101.76':
		return 'False'
	elif obj[7] == '86.95':
		return 'False'
	elif obj[7] == '74.0':
		return 'False'
	elif obj[7] == '73.98':
		return 'False'
	elif obj[7] == '124.78':
		return 'False'
	elif obj[7] == '191.94':
		return 'False'
	elif obj[7] == '247.87':
		return 'False'
	elif obj[7] == '83.2':
		return 'False'
	elif obj[7] == '88.62':
		return 'False'
	elif obj[7] == '115.71':
		return 'False'
	elif obj[7] == '212.92':
		return 'False'
	elif obj[7] == '229.73':
		return 'False'
	elif obj[7] == '81.36':
		return 'False'
	elif obj[7] == '261.67':
		return 'False'
	elif obj[7] == '98.9':
		return 'False'
	elif obj[7] == '95.19':
		return 'False'
	elif obj[7] == '89.41':
		return 'False'
	elif obj[7] == '71.77':
		return 'False'
	elif obj[7] == '256.74':
		return 'False'
	elif obj[7] == '60.73':
		return 'False'
	elif obj[7] == '89.42':
		return 'False'
	elif obj[7] == '60.17':
		return 'False'
	elif obj[7] == '112.37':
		return 'False'
	elif obj[7] == '80.55':
		return 'False'
	elif obj[7] == '55.93':
		return 'False'
	elif obj[7] == '83.8':
		return 'False'
	elif obj[7] == '84.93':
		return 'False'
	elif obj[7] == '103.08':
		return 'False'
	elif obj[7] == '101.58':
		return 'False'
	elif obj[7] == '112.55':
		return 'False'
	elif obj[7] == '92.96':
		return 'False'
	elif obj[7] == '151.26':
		return 'False'
	elif obj[7] == '192.5':
		return 'False'
	elif obj[7] == '76.08':
		return 'False'
	elif obj[7] == '123.98':
		return 'False'
	elif obj[7] == '99.01':
		return 'False'
	elif obj[7] == '88.0':
		return 'False'
	elif obj[7] == '144.14':
		return 'False'
	elif obj[7] == '105.72':
		return 'False'
	elif obj[7] == '64.37':
		return 'False'
	elif obj[7] == '146.1':
		return 'False'
	elif obj[7] == '221.08':
		return 'False'
	elif obj[7] == '61.42':
		return 'False'
	elif obj[7] == '74.34':
		return 'False'
	elif obj[7] == '106.53':
		return 'False'
	elif obj[7] == '76.35':
		return 'False'
	elif obj[7] == '63.49':
		return 'False'
	elif obj[7] == '145.18':
		return 'False'
	elif obj[7] == '120.56':
		return 'False'
	elif obj[7] == '81.38':
		return 'False'
	elif obj[7] == '84.68':
		return 'False'
	elif obj[7] == '91.89':
		return 'False'
	elif obj[7] == '135.82':
		return 'False'
	elif obj[7] == '79.62':
		return 'False'
	elif obj[7] == '93.3':
		return 'False'
	elif obj[7] == '86.3':
		return 'False'
	elif obj[7] == '83.55':
		return 'False'
	elif obj[7] == '68.07':
		return 'False'
	elif obj[7] == '235.06':
		return 'False'
	elif obj[7] == '57.52':
		return 'False'
	elif obj[7] == '76.98':
		return 'False'
	elif obj[7] == '98.14':
		return 'False'
	elif obj[7] == '112.7':
		return 'False'
	elif obj[7] == '144.33':
		return 'False'
	elif obj[7] == '116.62':
		return 'False'
	elif obj[7] == '86.67':
		return 'False'
	elif obj[7] == '203.27':
		return 'False'
	elif obj[7] == '82.42':
		return 'False'
	elif obj[7] == '126.57':
		return 'False'
	elif obj[7] == '80.54':
		return 'False'
	elif obj[7] == '106.52':
		return 'False'
	elif obj[7] == '89.73':
		return 'False'
	elif obj[7] == '208.39':
		return 'False'
	elif obj[7] == '128.61':
		return 'False'
	elif obj[7] == '227.23':
		return 'False'
	elif obj[7] == '234.5':
		return 'False'
	elif obj[7] == '101.66':
		return 'False'
	elif obj[7] == '71.12':
		return 'False'
	elif obj[7] == '190.67':
		return 'False'
	elif obj[7] == '82.95':
		return 'False'
	elif obj[7] == '82.63':
		return 'False'
	elif obj[7] == '92.75':
		return 'False'
	elif obj[7] == '197.06':
		return 'False'
	elif obj[7] == '216.07':
		return 'False'
	elif obj[7] == '108.82':
		return 'False'
	elif obj[7] == '59.36':
		return 'False'
	elif obj[7] == '87.54':
		return 'False'
	elif obj[7] == '79.98':
		return 'False'
	elif obj[7] == '139.87':
		return 'False'
	elif obj[7] == '100.6':
		return 'False'
	elif obj[7] == '75.9':
		return 'False'
	elif obj[7] == '267.6':
		return 'False'
	elif obj[7] == '215.07':
		return 'False'
	elif obj[7] == '225.35':
		return 'False'
	elif obj[7] == '95.42':
		return 'False'
	elif obj[7] == '107.43':
		return 'False'
	elif obj[7] == '88.68':
		return 'False'
	elif obj[7] == '93.97':
		return 'False'
	elif obj[7] == '124.66':
		return 'False'
	elif obj[7] == '212.87':
		return 'False'
	elif obj[7] == '96.75':
		return 'False'
	elif obj[7] == '71.34':
		return 'False'
	elif obj[7] == '183.43':
		return 'False'
	elif obj[7] == '126.85':
		return 'False'
	elif obj[7] == '74.17':
		return 'False'
	elif obj[7] == '76.04':
		return 'False'
	elif obj[7] == '86.05':
		return 'False'
	elif obj[7] == '185.27':
		return 'False'
	elif obj[7] == '116.95':
		return 'False'
	elif obj[7] == '101.95':
		return 'False'
	elif obj[7] == '104.37':
		return 'False'
	elif obj[7] == '132.88':
		return 'False'
	elif obj[7] == '74.12':
		return 'False'
	elif obj[7] == '176.34':
		return 'False'
	elif obj[7] == '73.76':
		return 'False'
	elif obj[7] == '67.21':
		return 'False'
	elif obj[7] == '111.36':
		return 'False'
	elif obj[7] == '117.31':
		return 'False'
	elif obj[7] == '84.94':
		return 'False'
	elif obj[7] == '68.86':
		return 'False'
	elif obj[7] == '211.83':
		return 'False'
	elif obj[7] == '81.06':
		return 'False'
	elif obj[7] == '215.69':
		return 'False'
	elif obj[7] == '154.67':
		return 'False'
	elif obj[7] == '67.66':
		return 'False'
	elif obj[7] == '153.48':
		return 'False'
	elif obj[7] == '62.63':
		return 'False'
	elif obj[7] == '140.14':
		return 'False'
	elif obj[7] == '111.37':
		return 'False'
	elif obj[7] == '57.06':
		return 'False'
	elif obj[7] == '81.9':
		return 'False'
	elif obj[7] == '124.54':
		return 'False'
	elif obj[7] == '153.34':
		return 'False'
	elif obj[7] == '108.35':
		return 'False'
	elif obj[7] == '118.41':
		return 'False'
	elif obj[7] == '138.51':
		return 'False'
	elif obj[7] == '120.03':
		return 'False'
	elif obj[7] == '91.01':
		return 'False'
	elif obj[7] == '58.72':
		return 'False'
	elif obj[7] == '104.0':
		return 'False'
	elif obj[7] == '174.37':
		return 'False'
	elif obj[7] == '90.52':
		return 'False'
	elif obj[7] == '72.03':
		return 'False'
	elif obj[7] == '211.58':
		return 'False'
	elif obj[7] == '97.04':
		return 'False'
	elif obj[7] == '75.93':
		return 'False'
	elif obj[7] == '95.05':
		return 'False'
	elif obj[7] == '95.02':
		return 'False'
	elif obj[7] == '76.62':
		return 'False'
	elif obj[7] == '83.94':
		return 'False'
	elif obj[7] == '125.2':
		return 'False'
	elif obj[7] == '82.99':
		return 'False'
	elif obj[7] == '89.01':
		return 'False'
	elif obj[7] == '223.78':
		return 'False'
	elif obj[7] == '160.76':
		return 'False'
	elif obj[7] == '70.15':
		return 'False'
	elif obj[7] == '206.49':
		return 'False'
	elif obj[7] == '77.42':
		return 'False'
	elif obj[7] == '117.59':
		return 'False'
	elif obj[7] == '116.68':
		return 'False'
	elif obj[7] == '253.86':
		return 'False'
	elif obj[7] == '203.36':
		return 'False'
	elif obj[7] == '125.87':
		return 'False'
	elif obj[7] == '64.09':
		return 'False'
	elif obj[7] == '175.92':
		return 'False'
	elif obj[7] == '89.29':
		return 'False'
	elif obj[7] == '100.65':
		return 'False'
	elif obj[7] == '81.1':
		return 'False'
	elif obj[7] == '98.3':
		return 'False'
	elif obj[7] == '191.15':
		return 'False'
	elif obj[7] == '96.86':
		return 'False'
	elif obj[7] == '55.84':
		return 'False'
	elif obj[7] == '84.04':
		return 'False'
	elif obj[7] == '92.06':
		return 'False'
	elif obj[7] == '103.69':
		return 'False'
	elif obj[7] == '97.23':
		return 'False'
	elif obj[7] == '86.61':
		return 'False'
	elif obj[7] == '60.02':
		return 'False'
	elif obj[7] == '79.0':
		return 'False'
	elif obj[7] == '137.27':
		return 'False'
	elif obj[7] == '57.83':
		return 'False'
	elif obj[7] == '84.08':
		return 'False'
	elif obj[7] == '234.51':
		return 'False'
	elif obj[7] == '142.64':
		return 'False'
	elif obj[7] == '182.22':
		return 'False'
	elif obj[7] == '67.26':
		return 'False'
	elif obj[7] == '113.45':
		return 'False'
	elif obj[7] == '81.64':
		return 'False'
	elif obj[7] == '57.15':
		return 'False'
	elif obj[7] == '214.73':
		return 'False'
	elif obj[7] == '63.41':
		return 'False'
	elif obj[7] == '106.24':
		return 'False'
	elif obj[7] == '83.01':
		return 'False'
	elif obj[7] == '74.99':
		return 'False'
	elif obj[7] == '61.88':
		return 'False'
	elif obj[7] == '65.67':
		return 'False'
	elif obj[7] == '110.32':
		return 'False'
	elif obj[7] == '119.58':
		return 'False'
	elif obj[7] == '95.18':
		return 'False'
	elif obj[7] == '58.35':
		return 'False'
	elif obj[7] == '115.91':
		return 'False'
	elif obj[7] == '62.64':
		return 'False'
	elif obj[7] == '84.81':
		return 'False'
	elif obj[7] == '217.57':
		return 'False'
	elif obj[7] == '63.28':
		return 'False'
	elif obj[7] == '70.48':
		return 'False'
	elif obj[7] == '120.96':
		return 'False'
	elif obj[7] == '121.83':
		return 'False'
	elif obj[7] == '109.09':
		return 'False'
	elif obj[7] == '76.58':
		return 'False'
	elif obj[7] == '66.71':
		return 'False'
	elif obj[7] == '165.36':
		return 'False'
	elif obj[7] == '68.27':
		return 'False'
	elif obj[7] == '89.32':
		return 'False'
	elif obj[7] == '107.06':
		return 'False'
	elif obj[7] == '65.63':
		return 'False'
	elif obj[7] == '63.82':
		return 'False'
	elif obj[7] == '71.29':
		return 'False'
	elif obj[7] == '119.3':
		return 'False'
	elif obj[7] == '86.58':
		return 'False'
	elif obj[7] == '98.61':
		return 'False'
	elif obj[7] == '69.06':
		return 'False'
	elif obj[7] == '79.6':
		return 'False'
	elif obj[7] == '177.56':
		return 'False'
	elif obj[7] == '132.85':
		return 'False'
	elif obj[7] == '198.84':
		return 'False'
	elif obj[7] == '87.17':
		return 'False'
	elif obj[7] == '84.54':
		return 'False'
	elif obj[7] == '56.87':
		return 'False'
	elif obj[7] == '243.52':
		return 'False'
	elif obj[7] == '73.89':
		return 'False'
	elif obj[7] == '97.99':
		return 'False'
	elif obj[7] == '73.71':
		return 'False'
	elif obj[7] == '89.33':
		return 'False'
	elif obj[7] == '238.27':
		return 'False'
	elif obj[7] == '135.79':
		return 'False'
	elif obj[7] == '82.19':
		return 'False'
	elif obj[7] == '93.2':
		return 'False'
	elif obj[7] == '208.31':
		return 'False'
	elif obj[7] == '121.71':
		return 'False'
	elif obj[7] == '63.27':
		return 'False'
	elif obj[7] == '61.57':
		return 'False'
	elif obj[7] == '113.26':
		return 'False'
	elif obj[7] == '77.45':
		return 'False'
	elif obj[7] == '84.92':
		return 'False'
	elif obj[7] == '129.31':
		return 'False'
	elif obj[7] == '89.43':
		return 'False'
	elif obj[7] == '101.6':
		return 'False'
	elif obj[7] == '231.72':
		return 'False'
	elif obj[7] == '102.13':
		return 'False'
	elif obj[7] == '100.88':
		return 'False'
	elif obj[7] == '103.66':
		return 'False'
	elif obj[7] == '193.8':
		return 'False'
	elif obj[7] == '105.91':
		return 'False'
	elif obj[7] == '84.09':
		return 'False'
	elif obj[7] == '92.64':
		return 'False'
	elif obj[7] == '99.36':
		return 'False'
	elif obj[7] == '135.63':
		return 'False'
	elif obj[7] == '65.45':
		return 'False'
	elif obj[7] == '203.01':
		return 'False'
	elif obj[7] == '110.84':
		return 'False'
	elif obj[7] == '55.12':
		return 'False'
	elif obj[7] == '106.76':
		return 'False'
	elif obj[7] == '74.24':
		return 'False'
	elif obj[7] == '78.7':
		return 'False'
	elif obj[7] == '101.96':
		return 'False'
	elif obj[7] == '216.64':
		return 'False'
	elif obj[7] == '74.28':
		return 'False'
	elif obj[7] == '65.25':
		return 'False'
	elif obj[7] == '159.67':
		return 'False'
	elif obj[7] == '93.96':
		return 'False'
	elif obj[7] == '103.01':
		return 'False'
	elif obj[7] == '92.49':
		return 'False'
	elif obj[7] == '208.85':
		return 'False'
	elif obj[7] == '65.7':
		return 'False'
	elif obj[7] == '107.58':
		return 'False'
	elif obj[7] == '68.17':
		return 'False'
	elif obj[7] == '95.37':
		return 'False'
	elif obj[7] == '106.1':
		return 'False'
	elif obj[7] == '104.03':
		return 'False'
	elif obj[7] == '84.35':
		return 'False'
	elif obj[7] == '118.93':
		return 'False'
	elif obj[7] == '185.28':
		return 'False'
	elif obj[7] == '69.54':
		return 'False'
	elif obj[7] == '62.12':
		return 'False'
	elif obj[7] == '87.2':
		return 'False'
	elif obj[7] == '111.27':
		return 'False'
	elif obj[7] == '217.94':
		return 'False'
	elif obj[7] == '72.53':
		return 'False'
	elif obj[7] == '122.73':
		return 'False'
	elif obj[7] == '69.74':
		return 'False'
	elif obj[7] == '99.94':
		return 'False'
	elif obj[7] == '145.46':
		return 'False'
	elif obj[7] == '157.77':
		return 'False'
	elif obj[7] == '101.85':
		return 'False'
	elif obj[7] == '63.01':
		return 'False'
	elif obj[7] == '68.6':
		return 'False'
	elif obj[7] == '81.78':
		return 'False'
	elif obj[7] == '105.88':
		return 'False'
	elif obj[7] == '116.85':
		return 'False'
	elif obj[7] == '96.21':
		return 'False'
	elif obj[7] == '78.26':
		return 'False'
	elif obj[7] == '58.24':
		return 'False'
	elif obj[7] == '82.53':
		return 'False'
	elif obj[7] == '71.25':
		return 'False'
	elif obj[7] == '129.73':
		return 'False'
	elif obj[7] == '97.6':
		return 'False'
	elif obj[7] == '198.3':
		return 'False'
	elif obj[7] == '100.06':
		return 'False'
	elif obj[7] == '91.09':
		return 'False'
	elif obj[7] == '85.53':
		return 'False'
	elif obj[7] == '125.11':
		return 'False'
	elif obj[7] == '217.79':
		return 'False'
	elif obj[7] == '93.8':
		return 'False'
	elif obj[7] == '90.61':
		return 'False'
	elif obj[7] == '139.2':
		return 'False'
	elif obj[7] == '77.01':
		return 'False'
	elif obj[7] == '105.26':
		return 'False'
	elif obj[7] == '233.47':
		return 'False'
	elif obj[7] == '77.26':
		return 'False'
	elif obj[7] == '95.7':
		return 'False'
	elif obj[7] == '91.28':
		return 'False'
	elif obj[7] == '129.19':
		return 'False'
	elif obj[7] == '97.86':
		return 'False'
	elif obj[7] == '112.33':
		return 'False'
	elif obj[7] == '58.86':
		return 'False'
	elif obj[7] == '103.58':
		return 'False'
	elif obj[7] == '76.12':
		return 'False'
	elif obj[7] == '64.27':
		return 'False'
	elif obj[7] == '134.12':
		return 'False'
	elif obj[7] == '218.1':
		return 'False'
	elif obj[7] == '62.02':
		return 'False'
	elif obj[7] == '117.98':
		return 'False'
	elif obj[7] == '97.34':
		return 'False'
	elif obj[7] == '206.66':
		return 'False'
	elif obj[7] == '116.78':
		return 'False'
	elif obj[7] == '92.43':
		return 'False'
	elif obj[7] == '71.63':
		return 'False'
	elif obj[7] == '87.79':
		return 'False'
	elif obj[7] == '99.64':
		return 'False'
	elif obj[7] == '98.37':
		return 'False'
	elif obj[7] == '218.6':
		return 'False'
	elif obj[7] == '100.71':
		return 'False'
	elif obj[7] == '101.3':
		return 'False'
	elif obj[7] == '79.51':
		return 'False'
	elif obj[7] == '223.26':
		return 'False'
	elif obj[7] == '97.22':
		return 'False'
	elif obj[7] == '172.27':
		return 'False'
	elif obj[7] == '221.83':
		return 'False'
	elif obj[7] == '83.6':
		return 'False'
	elif obj[7] == '77.5':
		return 'False'
	elif obj[7] == '96.28':
		return 'False'
	elif obj[7] == '106.27':
		return 'False'
	elif obj[7] == '173.9':
		return 'False'
	elif obj[7] == '162.72':
		return 'False'
	elif obj[7] == '202.51':
		return 'False'
	elif obj[7] == '105.49':
		return 'False'
	elif obj[7] == '101.53':
		return 'False'
	elif obj[7] == '126.04':
		return 'False'
	elif obj[7] == '79.7':
		return 'False'
	elif obj[7] == '209.15':
		return 'False'
	elif obj[7] == '70.22':
		return 'False'
	elif obj[7] == '83.57':
		return 'False'
	elif obj[7] == '78.28':
		return 'False'
	elif obj[7] == '83.66':
		return 'False'
	elif obj[7] == '196.5':
		return 'False'
	elif obj[7] == '83.78':
		return 'False'
	elif obj[7] == '66.96':
		return 'False'
	elif obj[7] == '103.12':
		return 'False'
	elif obj[7] == '74.15':
		return 'False'
	elif obj[7] == '59.31':
		return 'False'
	elif obj[7] == '63.22':
		return 'False'
	elif obj[7] == '90.07':
		return 'False'
	elif obj[7] == '159.39':
		return 'False'
	elif obj[7] == '89.16':
		return 'False'
	elif obj[7] == '78.23':
		return 'False'
	elif obj[7] == '226.84':
		return 'False'
	elif obj[7] == '104.77':
		return 'False'
	elif obj[7] == '113.84':
		return 'False'
	elif obj[7] == '133.62':
		return 'False'
	elif obj[7] == '111.96':
		return 'False'
	elif obj[7] == '206.62':
		return 'False'
	elif obj[7] == '204.92':
		return 'False'
	elif obj[7] == '56.74':
		return 'False'
	elif obj[7] == '123.83':
		return 'False'
	elif obj[7] == '80.17':
		return 'False'
	elif obj[7] == '72.54':
		return 'False'
	elif obj[7] == '234.35':
		return 'False'
	elif obj[7] == '116.25':
		return 'False'
	elif obj[7] == '96.95':
		return 'False'
	elif obj[7] == '66.24':
		return 'False'
	elif obj[7] == '118.88':
		return 'False'
	elif obj[7] == '75.34':
		return 'False'
	elif obj[7] == '200.73':
		return 'False'
	elif obj[7] == '67.3':
		return 'False'
	elif obj[7] == '99.12':
		return 'False'
	elif obj[7] == '116.49':
		return 'False'
	elif obj[7] == '67.1':
		return 'False'
	elif obj[7] == '72.08':
		return 'False'
	elif obj[7] == '65.44':
		return 'False'
	elif obj[7] == '79.84':
		return 'False'
	elif obj[7] == '62.61':
		return 'False'
	elif obj[7] == '92.35':
		return 'False'
	elif obj[7] == '69.5':
		return 'False'
	elif obj[7] == '219.38':
		return 'False'
	elif obj[7] == '69.48':
		return 'False'
	elif obj[7] == '68.09':
		return 'False'
	elif obj[7] == '84.66':
		return 'False'
	elif obj[7] == '180.45':
		return 'False'
	elif obj[7] == '59.14':
		return 'False'
	elif obj[7] == '85.64':
		return 'False'
	elif obj[7] == '100.01':
		return 'False'
	elif obj[7] == '118.46':
		return 'False'
	elif obj[7] == '94.77':
		return 'False'
	elif obj[7] == '72.12':
		return 'False'
	elif obj[7] == '155.23':
		return 'False'
	elif obj[7] == '206.15':
		return 'False'
	elif obj[7] == '102.84':
		return 'False'
	elif obj[7] == '193.45':
		return 'False'
	elif obj[7] == '76.1':
		return 'False'
	elif obj[7] == '138.55':
		return 'False'
	elif obj[7] == '116.21':
		return 'False'
	elif obj[7] == '103.73':
		return 'False'
	elif obj[7] == '94.11':
		return 'False'
	elif obj[7] == '122.25':
		return 'False'
	elif obj[7] == '84.19':
		return 'False'
	elif obj[7] == '87.5':
		return 'False'
	elif obj[7] == '96.1':
		return 'False'
	elif obj[7] == '108.61':
		return 'False'
	elif obj[7] == '234.27':
		return 'False'
	elif obj[7] == '176.38':
		return 'False'
	elif obj[7] == '75.16':
		return 'False'
	elif obj[7] == '107.74':
		return 'False'
	elif obj[7] == '131.28':
		return 'False'
	elif obj[7] == '125.98':
		return 'False'
	elif obj[7] == '55.47':
		return 'False'
	elif obj[7] == '239.21':
		return 'False'
	elif obj[7] == '196.08':
		return 'False'
	elif obj[7] == '65.79':
		return 'False'
	elif obj[7] == '200.98':
		return 'False'
	elif obj[7] == '85.79':
		return 'False'
	elif obj[7] == '85.18':
		return 'False'
	elif obj[7] == '95.49':
		return 'False'
	elif obj[7] == '81.58':
		return 'False'
	elif obj[7] == '229.94':
		return 'False'
	elif obj[7] == '117.77':
		return 'False'
	elif obj[7] == '66.69':
		return 'False'
	elif obj[7] == '168.68':
		return 'False'
	elif obj[7] == '110.33':
		return 'False'
	elif obj[7] == '77.95':
		return 'False'
	elif obj[7] == '80.35':
		return 'False'
	elif obj[7] == '57.38':
		return 'False'
	elif obj[7] == '70.66':
		return 'False'
	elif obj[7] == '202.06':
		return 'False'
	elif obj[7] == '103.22':
		return 'False'
	elif obj[7] == '63.9':
		return 'False'
	elif obj[7] == '81.32':
		return 'False'
	elif obj[7] == '253.93':
		return 'False'
	elif obj[7] == '207.84':
		return 'False'
	elif obj[7] == '228.26':
		return 'False'
	elif obj[7] == '75.13':
		return 'False'
	elif obj[7] == '91.32':
		return 'False'
	elif obj[7] == '79.42':
		return 'False'
	elif obj[7] == '101.12':
		return 'False'
	elif obj[7] == '57.79':
		return 'False'
	elif obj[7] == '92.97':
		return 'False'
	elif obj[7] == '75.06':
		return 'False'
	elif obj[7] == '71.79':
		return 'False'
	elif obj[7] == '167.16':
		return 'False'
	elif obj[7] == '131.05':
		return 'False'
	elif obj[7] == '103.72':
		return 'False'
	elif obj[7] == '94.75':
		return 'False'
	elif obj[7] == '76.09':
		return 'False'
	elif obj[7] == '61.8':
		return 'False'
	elif obj[7] == '83.73':
		return 'False'
	elif obj[7] == '248.24':
		return 'False'
	elif obj[7] == '103.65':
		return 'False'
	elif obj[7] == '86.19':
		return 'False'
	elif obj[7] == '131.42':
		return 'False'
	elif obj[7] == '69.46':
		return 'False'
	elif obj[7] == '76.78':
		return 'False'
	elif obj[7] == '213.43':
		return 'False'
	elif obj[7] == '115.07':
		return 'False'
	elif obj[7] == '108.63':
		return 'False'
	elif obj[7] == '85.9':
		return 'False'
	elif obj[7] == '63.42':
		return 'False'
	elif obj[7] == '203.76':
		return 'False'
	elif obj[7] == '80.94':
		return 'False'
	elif obj[7] == '88.56':
		return 'False'
	elif obj[7] == '66.16':
		return 'False'
	elif obj[7] == '88.98':
		return 'False'
	elif obj[7] == '87.39':
		return 'False'
	elif obj[7] == '86.85':
		return 'False'
	elif obj[7] == '94.37':
		return 'False'
	elif obj[7] == '254.95':
		return 'False'
	elif obj[7] == '107.33':
		return 'False'
	elif obj[7] == '196.58':
		return 'False'
	elif obj[7] == '236.04':
		return 'False'
	elif obj[7] == '69.94':
		return 'False'
	elif obj[7] == '55.79':
		return 'False'
	elif obj[7] == '189.82':
		return 'False'
	elif obj[7] == '101.06':
		return 'False'
	elif obj[7] == '68.01':
		return 'False'
	elif obj[7] == '193.61':
		return 'False'
	elif obj[7] == '141.37':
		return 'False'
	elif obj[7] == '106.8':
		return 'False'
	elif obj[7] == '61.13':
		return 'False'
	elif obj[7] == '56.64':
		return 'False'
	elif obj[7] == '98.44':
		return 'False'
	elif obj[7] == '230.74':
		return 'False'
	elif obj[7] == '101.46':
		return 'False'
	elif obj[7] == '74.66':
		return 'False'
	elif obj[7] == '205.78':
		return 'False'
	elif obj[7] == '111.24':
		return 'False'
	elif obj[7] == '110.1':
		return 'False'
	elif obj[7] == '77.77':
		return 'False'
	elif obj[7] == '83.59':
		return 'False'
	elif obj[7] == '179.67':
		return 'False'
	elif obj[7] == '216.19':
		return 'False'
	elif obj[7] == '200.91':
		return 'False'
	elif obj[7] == '200.66':
		return 'False'
	elif obj[7] == '228.5':
		return 'False'
	elif obj[7] == '70.43':
		return 'False'
	elif obj[7] == '74.39':
		return 'False'
	elif obj[7] == '87.91':
		return 'False'
	elif obj[7] == '232.29':
		return 'False'
	elif obj[7] == '78.98':
		return 'False'
	elif obj[7] == '100.2':
		return 'False'
	elif obj[7] == '90.44':
		return 'False'
	elif obj[7] == '123.89':
		return 'False'
	elif obj[7] == '91.16':
		return 'False'
	elif obj[7] == '77.07':
		return 'False'
	elif obj[7] == '87.0':
		return 'False'
	elif obj[7] == '145.25':
		return 'False'
	elif obj[7] == '59.43':
		return 'False'
	elif obj[7] == '154.03':
		return 'False'
	elif obj[7] == '139.81':
		return 'False'
	elif obj[7] == '106.84':
		return 'False'
	elif obj[7] == '221.06':
		return 'False'
	elif obj[7] == '69.97':
		return 'False'
	elif obj[7] == '109.39':
		return 'False'
	elif obj[7] == '89.31':
		return 'False'
	elif obj[7] == '163.17':
		return 'False'
	elif obj[7] == '212.62':
		return 'False'
	elif obj[7] == '128.63':
		return 'False'
	elif obj[7] == '84.1':
		return 'False'
	elif obj[7] == '120.15':
		return 'False'
	elif obj[7] == '72.16':
		return 'False'
	elif obj[7] == '64.68':
		return 'False'
	elif obj[7] == '66.47':
		return 'False'
	elif obj[7] == '64.84':
		return 'False'
	elif obj[7] == '158.33':
		return 'False'
	elif obj[7] == '108.96':
		return 'False'
	elif obj[7] == '114.71':
		return 'False'
	elif obj[7] == '82.14':
		return 'False'
	elif obj[7] == '219.67':
		return 'False'
	elif obj[7] == '135.84':
		return 'False'
	elif obj[7] == '90.38':
		return 'False'
	elif obj[7] == '156.69':
		return 'False'
	elif obj[7] == '207.6':
		return 'False'
	elif obj[7] == '158.9':
		return 'False'
	elif obj[7] == '247.97':
		return 'False'
	elif obj[7] == '58.55':
		return 'False'
	elif obj[7] == '96.19':
		return 'False'
	elif obj[7] == '231.15':
		return 'False'
	elif obj[7] == '68.18':
		return 'False'
	elif obj[7] == '186.54':
		return 'False'
	elif obj[7] == '96.14':
		return 'False'
	elif obj[7] == '101.93':
		return 'False'
	elif obj[7] == '110.96':
		return 'False'
	elif obj[7] == '118.85':
		return 'False'
	elif obj[7] == '108.62':
		return 'False'
	elif obj[7] == '146.08':
		return 'False'
	elif obj[7] == '113.41':
		return 'False'
	elif obj[7] == '68.68':
		return 'False'
	elif obj[7] == '119.13':
		return 'False'
	elif obj[7] == '103.29':
		return 'False'
	elif obj[7] == '232.64':
		return 'False'
	elif obj[7] == '82.46':
		return 'False'
	elif obj[7] == '63.57':
		return 'False'
	elif obj[7] == '73.24':
		return 'False'
	elif obj[7] == '57.46':
		return 'False'
	elif obj[7] == '104.16':
		return 'False'
	elif obj[7] == '119.4':
		return 'False'
	elif obj[7] == '120.22':
		return 'False'
	elif obj[7] == '70.19':
		return 'False'
	elif obj[7] == '57.96':
		return 'False'
	elif obj[7] == '81.24':
		return 'False'
	elif obj[7] == '70.91':
		return 'False'
	elif obj[7] == '87.12':
		return 'False'
	elif obj[7] == '95.23':
		return 'False'
	elif obj[7] == '71.18':
		return 'False'
	elif obj[7] == '87.71':
		return 'False'
	elif obj[7] == '207.37':
		return 'False'
	elif obj[7] == '115.52':
		return 'False'
	elif obj[7] == '64.62':
		return 'False'
	elif obj[7] == '78.5':
		return 'False'
	elif obj[7] == '59.11':
		return 'False'
	elif obj[7] == '80.2':
		return 'False'
	elif obj[7] == '208.99':
		return 'False'
	elif obj[7] == '99.72':
		return 'False'
	elif obj[7] == '123.08':
		return 'False'
	elif obj[7] == '75.0':
		return 'False'
	elif obj[7] == '105.9':
		return 'False'
	elif obj[7] == '60.64':
		return 'False'
	elif obj[7] == '82.64':
		return 'False'
	elif obj[7] == '58.89':
		return 'False'
	elif obj[7] == '114.46':
		return 'False'
	elif obj[7] == '73.57':
		return 'False'
	elif obj[7] == '72.04':
		return 'False'
	elif obj[7] == '68.99':
		return 'False'
	elif obj[7] == '80.27':
		return 'False'
	elif obj[7] == '79.22':
		return 'False'
	elif obj[7] == '142.63':
		return 'False'
	elif obj[7] == '222.52':
		return 'False'
	elif obj[7] == '70.38':
		return 'False'
	elif obj[7] == '81.92':
		return 'False'
	elif obj[7] == '83.53':
		return 'False'
	elif obj[7] == '74.06':
		return 'False'
	elif obj[7] == '173.43':
		return 'False'
	elif obj[7] == '106.18':
		return 'False'
	elif obj[7] == '114.21':
		return 'False'
	elif obj[7] == '123.15':
		return 'False'
	elif obj[7] == '184.25':
		return 'False'
	elif obj[7] == '117.69':
		return 'False'
	elif obj[7] == '106.51':
		return 'False'
	elif obj[7] == '55.27':
		return 'False'
	elif obj[7] == '99.2':
		return 'False'
	elif obj[7] == '92.7':
		return 'False'
	elif obj[7] == '106.7':
		return 'False'
	elif obj[7] == '91.0':
		return 'False'
	elif obj[7] == '76.99':
		return 'False'
	elif obj[7] == '93.99':
		return 'False'
	elif obj[7] == '109.68':
		return 'False'
	elif obj[7] == '111.41':
		return 'False'
	elif obj[7] == '62.37':
		return 'False'
	elif obj[7] == '101.28':
		return 'False'
	elif obj[7] == '79.08':
		return 'False'
	elif obj[7] == '92.78':
		return 'False'
	elif obj[7] == '197.1':
		return 'False'
	elif obj[7] == '74.8':
		return 'False'
	elif obj[7] == '64.41':
		return 'False'
	elif obj[7] == '119.34':
		return 'False'
	elif obj[7] == '94.92':
		return 'False'
	elif obj[7] == '103.51':
		return 'False'
	elif obj[7] == '114.5':
		return 'False'
	elif obj[7] == '84.11':
		return 'False'
	elif obj[7] == '78.49':
		return 'False'
	elif obj[7] == '55.34':
		return 'False'
	elif obj[7] == '75.04':
		return 'False'
	elif obj[7] == '109.73':
		return 'False'
	elif obj[7] == '96.78':
		return 'False'
	elif obj[7] == '194.62':
		return 'False'
	elif obj[7] == '70.02':
		return 'False'
	elif obj[7] == '222.21':
		return 'False'
	elif obj[7] == '62.41':
		return 'False'
	elif obj[7] == '55.83':
		return 'False'
	elif obj[7] == '85.83':
		return 'False'
	elif obj[7] == '88.31':
		return 'False'
	elif obj[7] == '103.55':
		return 'False'
	elif obj[7] == '60.26':
		return 'False'
	elif obj[7] == '122.01':
		return 'False'
	elif obj[7] == '186.45':
		return 'False'
	elif obj[7] == '58.47':
		return 'False'
	elif obj[7] == '99.6':
		return 'False'
	elif obj[7] == '186.32':
		return 'False'
	elif obj[7] == '62.49':
		return 'False'
	elif obj[7] == '74.51':
		return 'False'
	elif obj[7] == '91.98':
		return 'False'
	elif obj[7] == '75.87':
		return 'False'
	elif obj[7] == '135.75':
		return 'False'
	elif obj[7] == '100.15':
		return 'False'
	elif obj[7] == '125.38':
		return 'False'
	elif obj[7] == '111.71':
		return 'False'
	elif obj[7] == '94.64':
		return 'False'
	elif obj[7] == '226.7':
		return 'False'
	elif obj[7] == '183.1':
		return 'False'
	elif obj[7] == '102.47':
		return 'False'
	elif obj[7] == '83.23':
		return 'False'
	elif obj[7] == '69.21':
		return 'False'
	elif obj[7] == '84.06':
		return 'False'
	elif obj[7] == '79.13':
		return 'False'
	elif obj[7] == '212.01':
		return 'False'
	elif obj[7] == '89.7':
		return 'False'
	elif obj[7] == '112.64':
		return 'False'
	elif obj[7] == '116.14':
		return 'False'
	elif obj[7] == '94.04':
		return 'False'
	elif obj[7] == '86.6':
		return 'False'
	elif obj[7] == '83.83':
		return 'False'
	elif obj[7] == '106.98':
		return 'False'
	elif obj[7] == '106.97':
		return 'False'
	elif obj[7] == '119.52':
		return 'False'
	elif obj[7] == '88.66':
		return 'False'
	elif obj[7] == '112.95':
		return 'False'
	elif obj[7] == '76.82':
		return 'False'
	elif obj[7] == '91.56':
		return 'False'
	elif obj[7] == '68.35':
		return 'False'
	elif obj[7] == '74.23':
		return 'False'
	elif obj[7] == '110.76':
		return 'False'
	elif obj[7] == '77.65':
		return 'False'
	elif obj[7] == '86.24':
		return 'False'
	elif obj[7] == '121.19':
		return 'False'
	elif obj[7] == '75.56':
		return 'False'
	elif obj[7] == '111.43':
		return 'False'
	elif obj[7] == '219.97':
		return 'False'
	elif obj[7] == '148.91':
		return 'False'
	elif obj[7] == '69.4':
		return 'False'
	elif obj[7] == '58.37':
		return 'False'
	elif obj[7] == '71.2':
		return 'False'
	elif obj[7] == '101.5':
		return 'False'
	elif obj[7] == '111.73':
		return 'False'
	elif obj[7] == '98.54':
		return 'False'
	elif obj[7] == '94.62':
		return 'False'
	elif obj[7] == '112.43':
		return 'False'
	elif obj[7] == '99.67':
		return 'False'
	elif obj[7] == '95.12':
		return 'False'
	elif obj[7] == '85.06':
		return 'False'
	elif obj[7] == '214.05':
		return 'False'
	elif obj[7] == '79.09':
		return 'False'
	elif obj[7] == '98.42':
		return 'False'
	elif obj[7] == '158.31':
		return 'False'
	elif obj[7] == '219.53':
		return 'False'
	elif obj[7] == '59.26':
		return 'False'
	elif obj[7] == '106.43':
		return 'False'
	elif obj[7] == '196.36':
		return 'False'
	elif obj[7] == '141.23':
		return 'False'
	elif obj[7] == '89.99':
		return 'False'
	elif obj[7] == '108.53':
		return 'False'
	elif obj[7] == '85.54':
		return 'False'
	elif obj[7] == '100.83':
		return 'False'
	elif obj[7] == '59.82':
		return 'False'
	elif obj[7] == '105.95':
		return 'False'
	elif obj[7] == '188.11':
		return 'False'
	elif obj[7] == '71.15':
		return 'False'
	elif obj[7] == '205.5':
		return 'False'
	elif obj[7] == '204.86':
		return 'False'
	elif obj[7] == '115.03':
		return 'False'
	elif obj[7] == '79.87':
		return 'False'
	elif obj[7] == '125.26':
		return 'False'
	elif obj[7] == '144.48':
		return 'False'
	elif obj[7] == '93.79':
		return 'False'
	elif obj[7] == '82.01':
		return 'False'
	elif obj[7] == '111.85':
		return 'False'
	elif obj[7] == '92.39':
		return 'False'
	elif obj[7] == '70.35':
		return 'False'
	elif obj[7] == '140.08':
		return 'False'
	elif obj[7] == '80.33':
		return 'False'
	elif obj[7] == '131.51':
		return 'False'
	elif obj[7] == '89.21':
		return 'False'
	elif obj[7] == '91.45':
		return 'False'
	elif obj[7] == '89.63':
		return 'False'
	elif obj[7] == '124.06':
		return 'False'
	elif obj[7] == '99.47':
		return 'False'
	elif obj[7] == '80.93':
		return 'False'
	elif obj[7] == '200.49':
		return 'False'
	elif obj[7] == '75.3':
		return 'False'
	elif obj[7] == '240.71':
		return 'False'
	elif obj[7] == '60.5':
		return 'False'
	elif obj[7] == '134.39':
		return 'False'
	elif obj[7] == '56.18':
		return 'False'
	elif obj[7] == '113.64':
		return 'False'
	elif obj[7] == '80.4':
		return 'False'
	elif obj[7] == '99.82':
		return 'False'
	elif obj[7] == '81.03':
		return 'False'
	elif obj[7] == '109.03':
		return 'False'
	elif obj[7] == '69.61':
		return 'False'
	elif obj[7] == '94.65':
		return 'False'
	elif obj[7] == '64.64':
		return 'False'
	elif obj[7] == '55.32':
		return 'False'
	elif obj[7] == '57.57':
		return 'False'
	elif obj[7] == '98.73':
		return 'False'
	elif obj[7] == '81.18':
		return 'False'
	elif obj[7] == '56.23':
		return 'False'
	elif obj[7] == '118.14':
		return 'False'
	elif obj[7] == '94.34':
		return 'False'
	elif obj[7] == '67.81':
		return 'False'
	elif obj[7] == '86.39':
		return 'False'
	elif obj[7] == '116.38':
		return 'False'
	elif obj[7] == '75.74':
		return 'False'
	elif obj[7] == '149.95':
		return 'False'
	elif obj[7] == '74.98':
		return 'False'
	elif obj[7] == '55.25':
		return 'False'
	elif obj[7] == '87.01':
		return 'False'
	elif obj[7] == '56.99':
		return 'False'
	elif obj[7] == '73.01':
		return 'False'
	elif obj[7] == '89.45':
		return 'False'
	elif obj[7] == '106.56':
		return 'False'
	elif obj[7] == '223.68':
		return 'False'
	elif obj[7] == '63.73':
		return 'False'
	elif obj[7] == '229.2':
		return 'False'
	elif obj[7] == '68.61':
		return 'False'
	elif obj[7] == '193.22':
		return 'False'
	elif obj[7] == '64.99':
		return 'False'
	elif obj[7] == '66.12':
		return 'False'
	elif obj[7] == '73.4':
		return 'False'
	elif obj[7] == '98.1':
		return 'False'
	elif obj[7] == '251.46':
		return 'False'
	elif obj[7] == '89.96':
		return 'False'
	elif obj[7] == '80.85':
		return 'False'
	elif obj[7] == '220.52':
		return 'False'
	elif obj[7] == '76.93':
		return 'False'
	elif obj[7] == '113.1':
		return 'False'
	elif obj[7] == '96.84':
		return 'False'
	elif obj[7] == '121.14':
		return 'False'
	elif obj[7] == '109.56':
		return 'False'
	elif obj[7] == '194.04':
		return 'False'
	elif obj[7] == '75.88':
		return 'False'
	elif obj[7] == '76.5':
		return 'False'
	elif obj[7] == '99.16':
		return 'False'
	elif obj[7] == '63.53':
		return 'False'
	elif obj[7] == '78.65':
		return 'False'
	elif obj[7] == '111.64':
		return 'False'
	elif obj[7] == '204.5':
		return 'False'
	elif obj[7] == '206.25':
		return 'False'
	elif obj[7] == '60.69':
		return 'False'
	elif obj[7] == '67.79':
		return 'False'
	elif obj[7] == '254.63':
		return 'False'
	elif obj[7] == '246.34':
		return 'False'
	elif obj[7] == '93.34':
		return 'False'
	elif obj[7] == '162.3':
		return 'False'
	elif obj[7] == '110.25':
		return 'False'
	elif obj[7] == '69.7':
		return 'False'
	elif obj[7] == '87.03':
		return 'False'
	elif obj[7] == '82.47':
		return 'False'
	elif obj[7] == '57.26':
		return 'False'
	elif obj[7] == '56.47':
		return 'False'
	elif obj[7] == '86.97':
		return 'False'
	elif obj[7] == '78.78':
		return 'False'
	elif obj[7] == '224.71':
		return 'False'
	elif obj[7] == '57.02':
		return 'False'
	elif obj[7] == '115.98':
		return 'False'
	elif obj[7] == '226.11':
		return 'False'
	elif obj[7] == '97.59':
		return 'False'
	elif obj[7] == '79.34':
		return 'False'
	elif obj[7] == '65.59':
		return 'False'
	elif obj[7] == '101.65':
		return 'False'
	elif obj[7] == '210.94':
		return 'False'
	elif obj[7] == '77.92':
		return 'False'
	elif obj[7] == '55.22':
		return 'False'
	elif obj[7] == '78.94':
		return 'False'
	elif obj[7] == '109.69':
		return 'False'
	elif obj[7] == '79.33':
		return 'False'
	elif obj[7] == '79.91':
		return 'False'
	elif obj[7] == '85.35':
		return 'False'
	elif obj[7] == '204.17':
		return 'False'
	elif obj[7] == '117.45':
		return 'False'
	elif obj[7] == '120.06':
		return 'False'
	elif obj[7] == '75.62':
		return 'False'
	elif obj[7] == '138.07':
		return 'False'
	elif obj[7] == '195.04':
		return 'False'
	elif obj[7] == '134.59':
		return 'False'
	elif obj[7] == '83.09':
		return 'False'
	elif obj[7] == '78.42':
		return 'False'
	elif obj[7] == '65.08':
		return 'False'
	elif obj[7] == '79.47':
		return 'False'
	elif obj[7] == '95.52':
		return 'False'
	elif obj[7] == '112.07':
		return 'False'
	elif obj[7] == '140.52':
		return 'False'
	elif obj[7] == '55.67':
		return 'False'
	elif obj[7] == '218.65':
		return 'False'
	elif obj[7] == '83.56':
		return 'False'
	elif obj[7] == '116.76':
		return 'False'
	elif obj[7] == '69.3':
		return 'False'
	elif obj[7] == '67.55':
		return 'False'
	elif obj[7] == '99.29':
		return 'False'
	elif obj[7] == '93.89':
		return 'False'
	elif obj[7] == '82.38':
		return 'False'
	elif obj[7] == '82.21':
		return 'False'
	elif obj[7] == '104.62':
		return 'False'
	elif obj[7] == '81.15':
		return 'False'
	elif obj[7] == '111.61':
		return 'False'
	elif obj[7] == '207.32':
		return 'False'
	elif obj[7] == '87.11':
		return 'False'
	elif obj[7] == '207.64':
		return 'False'
	elif obj[7] == '236.84':
		return 'False'
	elif obj[7] == '100.97':
		return 'False'
	elif obj[7] == '99.21':
		return 'False'
	elif obj[7] == '110.16':
		return 'False'
	elif obj[7] == '123.0':
		return 'False'
	elif obj[7] == '128.28':
		return 'False'
	elif obj[7] == '204.63':
		return 'False'
	elif obj[7] == '89.98':
		return 'False'
	elif obj[7] == '232.89':
		return 'False'
	elif obj[7] == '98.58':
		return 'False'
	elif obj[7] == '92.81':
		return 'False'
	elif obj[7] == '85.16':
		return 'False'
	elif obj[7] == '57.82':
		return 'False'
	elif obj[7] == '87.27':
		return 'False'
	elif obj[7] == '110.91':
		return 'False'
	elif obj[7] == '56.31':
		return 'False'
	elif obj[7] == '111.99':
		return 'False'
	elif obj[7] == '57.51':
		return 'False'
	elif obj[7] == '68.49':
		return 'False'
	elif obj[7] == '60.2':
		return 'False'
	elif obj[7] == '160.0':
		return 'False'
	elif obj[7] == '237.15':
		return 'False'
	elif obj[7] == '99.06':
		return 'False'
	elif obj[7] == '104.33':
		return 'False'
	elif obj[7] == '82.06':
		return 'False'
	elif obj[7] == '231.19':
		return 'False'
	elif obj[7] == '72.62':
		return 'False'
	elif obj[7] == '90.78':
		return 'False'
	elif obj[7] == '70.71':
		return 'False'
	elif obj[7] == '72.36':
		return 'False'
	elif obj[7] == '83.76':
		return 'False'
	elif obj[7] == '63.64':
		return 'False'
	elif obj[7] == '90.1':
		return 'False'
	elif obj[7] == '113.25':
		return 'False'
	elif obj[7] == '110.55':
		return 'False'
	elif obj[7] == '73.69':
		return 'False'
	elif obj[7] == '82.61':
		return 'False'
	elif obj[7] == '89.17':
		return 'False'
	elif obj[7] == '227.91':
		return 'False'
	elif obj[7] == '143.15':
		return 'False'
	elif obj[7] == '116.67':
		return 'False'
	elif obj[7] == '69.17':
		return 'False'
	elif obj[7] == '58.38':
		return 'False'
	elif obj[7] == '86.34':
		return 'False'
	elif obj[7] == '109.59':
		return 'False'
	elif obj[7] == '79.26':
		return 'False'
	elif obj[7] == '78.46':
		return 'False'
	elif obj[7] == '156.18':
		return 'False'
	elif obj[7] == '69.52':
		return 'False'
	elif obj[7] == '108.47':
		return 'False'
	elif obj[7] == '95.2':
		return 'False'
	elif obj[7] == '78.52':
		return 'False'
	elif obj[7] == '114.89':
		return 'False'
	elif obj[7] == '85.22':
		return 'False'
	elif obj[7] == '145.23':
		return 'False'
	elif obj[7] == '74.04':
		return 'False'
	elif obj[7] == '88.81':
		return 'False'
	elif obj[7] == '102.05':
		return 'False'
	elif obj[7] == '112.47':
		return 'False'
	elif obj[7] == '72.84':
		return 'False'
	elif obj[7] == '195.03':
		return 'False'
	elif obj[7] == '170.95':
		return 'False'
	elif obj[7] == '87.98':
		return 'False'
	elif obj[7] == '83.65':
		return 'False'
	elif obj[7] == '123.36':
		return 'False'
	elif obj[7] == '124.45':
		return 'False'
	elif obj[7] == '109.22':
		return 'False'
	elif obj[7] == '110.73':
		return 'False'
	elif obj[7] == '99.14':
		return 'False'
	elif obj[7] == '59.15':
		return 'False'
	elif obj[7] == '77.44':
		return 'False'
	elif obj[7] == '148.24':
		return 'False'
	elif obj[7] == '72.93':
		return 'False'
	elif obj[7] == '215.64':
		return 'False'
	elif obj[7] == '118.51':
		return 'False'
	elif obj[7] == '74.46':
		return 'False'
	elif obj[7] == '221.89':
		return 'True'
	elif obj[7] == '57.92':
		return 'True'
	elif obj[7] == '89.13':
		return 'True'
	elif obj[7] == '133.19':
		return 'True'
	elif obj[7] == '75.02':
		return 'True'
	elif obj[7] == '91.54':
		return 'True'
	elif obj[7] == '111.98':
		return 'True'
	elif obj[7] == '60.94':
		return 'True'
	elif obj[7] == '97.43':
		return 'True'
	elif obj[7] == '185.49':
		return 'True'
	elif obj[7] == '76.13':
		return 'True'
	elif obj[7] == '112.24':
		return 'True'
	elif obj[7] == '137.3':
		return 'True'
	elif obj[7] == '116.69':
		return 'True'
	elif obj[7] == '215.94':
		return 'True'
	elif obj[7] == '86.62':
		return 'True'
	elif obj[7] == '112.16':
		return 'True'
	elif obj[7] == '118.03':
		return 'True'
	elif obj[7] == '195.71':
		return 'True'
	elif obj[7] == '102.16':
		return 'True'
	elif obj[7] == '82.67':
		return 'False'
	elif obj[7] == '231.56':
		return 'True'
	elif obj[7] == '190.14':
		return 'True'
	elif obj[7] == '130.54':
		return 'True'
	elif obj[7] == '182.99':
		return 'True'
	elif obj[7] == '101.45':
		return 'True'
	elif obj[7] == '206.09':
		return 'True'
	elif obj[7] == '263.32':
		return 'True'
	elif obj[7] == '194.37':
		return 'True'
	elif obj[7] == '103.68':
		return 'True'
	elif obj[7] == '72.17':
		return 'True'
	elif obj[7] == '221.79':
		return 'True'
	elif obj[7] == '151.16':
		return 'True'
	elif obj[7] == '68.43':
		return 'True'
	elif obj[7] == '67.41':
		return 'True'
	elif obj[7] == '239.07':
		return 'True'
	elif obj[7] == '223.83':
		return 'True'
	elif obj[7] == '76.57':
		return 'True'
	elif obj[7] == '92.98':
		return 'True'
	elif obj[7] == '271.74':
		return 'True'
	elif obj[7] == '200.62':
		return 'True'
	elif obj[7] == '242.52':
		return 'True'
	elif obj[7] == '114.77':
		return 'True'
	elif obj[7] == '66.03':
		return 'True'
	elif obj[7] == '81.95':
		return 'True'
	elif obj[7] == '97.73':
		return 'True'
	elif obj[7] == '70.94':
		return 'True'
	elif obj[7] == '199.84':
		return 'True'
	elif obj[7] == '162.14':
		return 'True'
	elif obj[7] == '91.92':
		return 'True'
	elif obj[7] == '76.46':
		return 'True'
	elif obj[7] == '197.28':
		return 'True'
	elif obj[7] == '233.94':
		return 'True'
	elif obj[7] == '247.51':
		return 'True'
	elif obj[7] == '69.04':
		return 'False'
	elif obj[7] == '243.53':
		return 'False'
	elif obj[7] == '205.84':
		return 'False'
	elif obj[7] == '57.08':
		return 'False'
	elif obj[7] == '162.96':
		return 'False'
	elif obj[7] == '85.37':
		return 'False'
	elif obj[7] == '97.76':
		return 'True'
	elif obj[7] == '184.4':
		return 'True'
	elif obj[7] == '70.3':
		return 'True'
	elif obj[7] == '208.65':
		return 'True'
	elif obj[7] == '74.96':
		return 'True'
	elif obj[7] == '175.29':
		return 'True'
	elif obj[7] == '109.47':
		return 'True'
	elif obj[7] == '87.85':
		return 'True'
	elif obj[7] == '80.13':
		return 'True'
	elif obj[7] == '90.19':
		return 'True'
	elif obj[7] == '83.24':
		return 'True'
	elif obj[7] == '95.84':
		return 'True'
	elif obj[7] == '205.35':
		return 'True'
	elif obj[7] == '205.33':
		return 'True'
	elif obj[7] == '116.1':
		return 'True'
	elif obj[7] == '210.4':
		return 'True'
	elif obj[7] == '199.86':
		return 'True'
	elif obj[7] == '219.73':
		return 'True'
	elif obj[7] == '250.89':
		return 'True'
	elif obj[7] == '72.73':
		return 'True'
	elif obj[7] == '200.59':
		return 'True'
	elif obj[7] == '93.13':
		return 'True'
	elif obj[7] == '131.41':
		return 'True'
	elif obj[7] == '59.32':
		return 'True'
	elif obj[7] == '212.08':
		return 'True'
	elif obj[7] == '196.92':
		return 'True'
	elif obj[7] == '252.72':
		return 'True'
	elif obj[7] == '84.2':
		return 'True'
	elif obj[7] == '219.72':
		return 'True'
	elif obj[7] == '60.91':
		return 'True'
	elif obj[7] == '78.03':
		return 'True'
	elif obj[7] == '144.9':
		return 'True'
	elif obj[7] == '213.03':
		return 'True'
	elif obj[7] == '243.58':
		return 'True'
	elif obj[7] == '107.26':
		return 'True'
	elif obj[7] == '99.33':
		return 'True'
	elif obj[7] == '58.09':
		return 'True'
	elif obj[7] == '75.32':
		return 'True'
	elif obj[7] == '127.29':
		return 'True'
	elif obj[7] == '124.13':
		return 'True'
	elif obj[7] == '197.54':
		return 'True'
	elif obj[7] == '211.78':
		return 'True'
	elif obj[7] == '195.23':
		return 'True'
	elif obj[7] == '100.98':
		return 'True'
	elif obj[7] == '120.46':
		return 'True'
	elif obj[7] == '105.92':
		return 'True'
	elif obj[7] == '171.23':
		return 'True'
	elif obj[7] == '174.12':
		return 'True'
	elif obj[7] == '186.21':
		return 'True'
	elif obj[7] == '70.09':
		return 'True'
	elif obj[7] == '94.39':
		return 'True'
	elif obj[7] == '80.43':
		return 'True'
	elif obj[7] == '104.51':
		return 'True'
	elif obj[7] == '228.7':
		return 'True'
	elif obj[7] == '214.09':
		return 'True'
	elif obj[7] == '167.41':
		return 'True'
	elif obj[7] == '191.61':
		return 'True'
	elif obj[7] == '221.29':
		return 'True'
	elif obj[7] == '89.22':
		return 'True'
	elif obj[7] == '193.94':
		return 'True'
	elif obj[7] == '233.29':
		return 'True'
	elif obj[7] == '196.71':
		return 'True'
	elif obj[7] == '237.75':
		return 'True'
	elif obj[7] == '249.31':
		return 'True'
	elif obj[7] == '194.99':
		return 'True'
	elif obj[7] == '64.14':
		return 'True'
	elif obj[7] == '235.63':
		return 'True'
	elif obj[7] == '240.59':
		return 'True'
	elif obj[7] == '78.92':
		return 'True'
	elif obj[7] == '190.32':
		return 'True'
	elif obj[7] == '231.61':
		return 'True'
	elif obj[7] == '82.3':
		return 'True'
	elif obj[7] == '191.82':
		return 'True'
	elif obj[7] == '93.05':
		return 'True'
	elif obj[7] == '64.17':
		return 'True'
	elif obj[7] == '129.98':
		return 'True'
	elif obj[7] == '224.1':
		return 'True'
	elif obj[7] == '216.94':
		return 'True'
	elif obj[7] == '76.11':
		return 'True'
	elif obj[7] == '82.28':
		return 'True'
	elif obj[7] == '59.86':
		return 'True'
	elif obj[7] == '259.63':
		return 'True'
	elif obj[7] == '68.02':
		return 'True'
	elif obj[7] == '72.81':
		return 'True'
	elif obj[7] == '226.98':
		return 'True'
	elif obj[7] == '228.56':
		return 'True'
	elif obj[7] == '180.93':
		return 'True'
	elif obj[7] == '185.17':
		return 'True'
	elif obj[7] == '221.58':
		return 'True'
	elif obj[7] == '86.23':
		return 'True'
	elif obj[7] == '72.67':
		return 'True'
	elif obj[7] == '179.12':
		return 'True'
	elif obj[7] == '116.55':
		return 'True'
	elif obj[7] == '96.59':
		return 'True'
	elif obj[7] == '86.94':
		return 'True'
	elif obj[7] == '66.72':
		return 'True'
	elif obj[7] == '240.09':
		return 'True'
	elif obj[7] == '110.85':
		return 'True'
	elif obj[7] == '165.31':
		return 'True'
	elif obj[7] == '88.92':
		return 'True'
	elif obj[7] == '96.97':
		return 'True'
	elif obj[7] == '59.35':
		return 'True'
	elif obj[7] == '84.62':
		return 'False'
	elif obj[7] == '57.33':
		return 'False'
	elif obj[7] == '109.16':
		return 'False'
	elif obj[7] == '217.3':
		return 'False'
	elif obj[7] == '100.09':
		return 'False'
	elif obj[7] == '75.05':
		return 'False'
	elif obj[7] == '70.08':
		return 'False'
	elif obj[7] == '74.2':
		return 'False'
	elif obj[7] == '69.01':
		return 'False'
	elif obj[7] == '87.24':
		return 'False'
	elif obj[7] == '198.69':
		return 'False'
	elif obj[7] == '132.08':
		return 'False'
	elif obj[7] == '98.99':
		return 'False'
	elif obj[7] == '79.14':
		return 'False'
	elif obj[7] == '80.98':
		return 'False'
	elif obj[7] == '111.19':
		return 'False'
	elif obj[7] == '129.53':
		return 'False'
	elif obj[7] == '93.73':
		return 'False'
	elif obj[7] == '77.49':
		return 'False'
	elif obj[7] == '65.38':
		return 'False'
	elif obj[7] == '94.18':
		return 'False'
	elif obj[7] == '196.01':
		return 'False'
	elif obj[7] == '170.05':
		return 'False'
	elif obj[7] == '67.84':
		return 'False'
	elif obj[7] == '95.59':
		return 'False'
	elif obj[7] == '73.73':
		return 'False'
	elif obj[7] == '79.58':
		return 'False'
	elif obj[7] == '205.26':
		return 'False'
	elif obj[7] == '139.9':
		return 'False'
	elif obj[7] == '211.03':
		return 'False'
	elif obj[7] == '225.47':
		return 'False'
	elif obj[7] == '94.48':
		return 'False'
	elif obj[7] == '82.34':
		return 'False'
	elif obj[7] == '180.63':
		return 'False'
	elif obj[7] == '116.66':
		return 'False'
	elif obj[7] == '130.34':
		return 'False'
	elif obj[7] == '97.53':
		return 'False'
	elif obj[7] == '122.31':
		return 'False'
	elif obj[7] == '112.06':
		return 'False'
	elif obj[7] == '201.76':
		return 'False'
	elif obj[7] == '74.44':
		return 'False'
	elif obj[7] == '115.43':
		return 'False'
	elif obj[7] == '96.29':
		return 'False'
	elif obj[7] == '74.64':
		return 'False'
	elif obj[7] == '96.99':
		return 'False'
	elif obj[7] == '78.75':
		return 'False'
	elif obj[7] == '75.29':
		return 'False'
	elif obj[7] == '100.35':
		return 'False'
	elif obj[7] == '193.83':
		return 'False'
	elif obj[7] == '183.34':
		return 'False'
	elif obj[7] == '76.2':
		return 'False'
	elif obj[7] == '93.36':
		return 'False'
	elif obj[7] == '61.29':
		return 'False'
	elif obj[7] == '191.47':
		return 'False'
	elif obj[7] == '239.82':
		return 'False'
	elif obj[7] == '88.53':
		return 'False'
	elif obj[7] == '113.8':
		return 'False'
	elif obj[7] == '189.57':
		return 'False'
	elif obj[7] == '114.25':
		return 'False'
	elif obj[7] == '81.26':
		return 'False'
	elif obj[7] == '87.88':
		return 'False'
	elif obj[7] == '99.97':
		return 'False'
	elif obj[7] == '207.58':
		return 'False'
	elif obj[7] == '210.48':
		return 'False'
	elif obj[7] == '79.3':
		return 'False'
	elif obj[7] == '60.34':
		return 'False'
	elif obj[7] == '68.52':
		return 'False'
	elif obj[7] == '88.78':
		return 'False'
	elif obj[7] == '122.1':
		return 'False'
	elif obj[7] == '74.81':
		return 'False'
	elif obj[7] == '183.45':
		return 'False'
	elif obj[7] == '114.94':
		return 'False'
	elif obj[7] == '104.38':
		return 'False'
	elif obj[7] == '73.31':
		return 'False'
	elif obj[7] == '89.77':
		return 'False'
	elif obj[7] == '80.19':
		return 'False'
	elif obj[7] == '70.92':
		return 'False'
	elif obj[7] == '113.85':
		return 'False'
	elif obj[7] == '79.35':
		return 'False'
	elif obj[7] == '114.01':
		return 'False'
	elif obj[7] == '93.74':
		return 'False'
	elif obj[7] == '98.41':
		return 'False'
	elif obj[7] == '155.43':
		return 'False'
	elif obj[7] == '82.0':
		return 'False'
	elif obj[7] == '71.16':
		return 'False'
	elif obj[7] == '86.86':
		return 'False'
	elif obj[7] == '239.64':
		return 'False'
	elif obj[7] == '79.83':
		return 'False'
	elif obj[7] == '218.46':
		return 'False'
	elif obj[7] == '62.2':
		return 'False'
	elif obj[7] == '69.15':
		return 'False'
	elif obj[7] == '127.71':
		return 'False'
	elif obj[7] == '216.7':
		return 'False'
	elif obj[7] == '71.89':
		return 'False'
	elif obj[7] == '234.58':
		return 'False'
	elif obj[7] == '235.85':
		return 'False'
	elif obj[7] == '243.5':
		return 'False'
	elif obj[7] == '182.2':
		return 'False'
	elif obj[7] == '229.92':
		return 'False'
	elif obj[7] == '215.6':
		return 'False'
	elif obj[7] == '91.61':
		return 'False'
	elif obj[7] == '138.16':
		return 'False'
	elif obj[7] == '75.23':
		return 'False'
	elif obj[7] == '75.18':
		return 'False'
	elif obj[7] == '61.45':
		return 'False'
	elif obj[7] == '146.01':
		return 'False'
	elif obj[7] == '242.3':
		return 'False'
	elif obj[7] == '214.45':
		return 'False'
	elif obj[7] == '129.54':
		return 'False'
	elif obj[7] == '198.21':
		return 'False'
	elif obj[7] == '109.82':
		return 'False'
	elif obj[7] == '60.84':
		return 'False'
	elif obj[7] == '94.61':
		return 'False'
	elif obj[7] == '97.49':
		return 'False'
	elif obj[7] == '206.72':
		return 'False'
	elif obj[7] == '55.78':
		return 'False'
	elif obj[7] == '81.84':
		return 'False'
	elif obj[7] == '94.09':
		return 'False'
	elif obj[7] == '117.92':
		return 'False'
	elif obj[7] == '190.7':
		return 'False'
	elif obj[7] == '113.63':
		return 'False'
	elif obj[7] == '141.24':
		return 'False'
	elif obj[7] == '56.96':
		return 'False'
	elif obj[7] == '137.74':
		return 'False'
	elif obj[7] == '106.23':
		return 'False'
	elif obj[7] == '58.95':
		return 'False'
	elif obj[7] == '81.6':
		return 'False'
	elif obj[7] == '99.92':
		return 'False'
	elif obj[7] == '68.76':
		return 'False'
	elif obj[7] == '91.72':
		return 'False'
	elif obj[7] == '251.6':
		return 'False'
	elif obj[7] == '123.1':
		return 'False'
	elif obj[7] == '97.4':
		return 'False'
	elif obj[7] == '68.34':
		return 'False'
	elif obj[7] == '120.31':
		return 'False'
	elif obj[7] == '74.09':
		return 'False'
	elif obj[7] == '91.6':
		return 'False'
	elif obj[7] == '87.52':
		return 'False'
	elif obj[7] == '213.37':
		return 'False'
	elif obj[7] == '75.39':
		return 'False'
	elif obj[7] == '122.41':
		return 'False'
	elif obj[7] == '223.36':
		return 'False'
	elif obj[7] == '70.21':
		return 'False'
	elif obj[7] == '101.37':
		return 'False'
	elif obj[7] == '178.29':
		return 'False'
	elif obj[7] == '73.02':
		return 'False'
	elif obj[7] == '91.97':
		return 'False'
	elif obj[7] == '99.8':
		return 'False'
	elif obj[7] == '63.69':
		return 'False'
	elif obj[7] == '116.23':
		return 'False'
	elif obj[7] == '101.41':
		return 'False'
	elif obj[7] == '136.8':
		return 'False'
	elif obj[7] == '96.57':
		return 'False'
	elif obj[7] == '66.42':
		return 'False'
	elif obj[7] == '126.82':
		return 'False'
	elif obj[7] == '78.4':
		return 'False'
	elif obj[7] == '209.58':
		return 'False'
	elif obj[7] == '80.05':
		return 'False'
	elif obj[7] == '89.86':
		return 'False'
	elif obj[7] == '110.99':
		return 'False'
	elif obj[7] == '210.78':
		return 'False'
	elif obj[7] == '118.89':
		return 'False'
	elif obj[7] == '72.55':
		return 'False'
	elif obj[7] == '107.41':
		return 'False'
	elif obj[7] == '74.91':
		return 'False'
	elif obj[7] == '82.71':
		return 'False'
	elif obj[7] == '106.02':
		return 'False'
	elif obj[7] == '121.32':
		return 'False'
	elif obj[7] == '113.05':
		return 'False'
	elif obj[7] == '66.17':
		return 'False'
	elif obj[7] == '220.36':
		return 'False'
	elif obj[7] == '73.06':
		return 'False'
	elif obj[7] == '187.88':
		return 'False'
	elif obj[7] == '191.66':
		return 'False'
	elif obj[7] == '63.94':
		return 'False'
	elif obj[7] == '77.73':
		return 'False'
	elif obj[7] == '96.3':
		return 'False'
	elif obj[7] == '107.46':
		return 'False'
	elif obj[7] == '108.33':
		return 'False'
	elif obj[7] == '89.37':
		return 'False'
	elif obj[7] == '217.75':
		return 'False'
	elif obj[7] == '59.2':
		return 'False'
	elif obj[7] == '226.88':
		return 'False'
	elif obj[7] == '58.7':
		return 'False'
	elif obj[7] == '186.4':
		return 'False'
	elif obj[7] == '149.13':
		return 'False'
	elif obj[7] == '68.24':
		return 'False'
	elif obj[7] == '114.76':
		return 'False'
	elif obj[7] == '114.18':
		return 'False'
	elif obj[7] == '74.19':
		return 'False'
	elif obj[7] == '101.89':
		return 'False'
	elif obj[7] == '107.22':
		return 'False'
	elif obj[7] == '101.99':
		return 'False'
	elif obj[7] == '94.47':
		return 'False'
	elif obj[7] == '98.76':
		return 'False'
	elif obj[7] == '116.93':
		return 'False'
	elif obj[7] == '219.96':
		return 'False'
	elif obj[7] == '97.96':
		return 'False'
	elif obj[7] == '197.69':
		return 'False'
	elif obj[7] == '93.14':
		return 'False'
	elif obj[7] == '199.88':
		return 'False'
	elif obj[7] == '77.48':
		return 'False'
	elif obj[7] == '65.34':
		return 'False'
	elif obj[7] == '98.71':
		return 'False'
	elif obj[7] == '170.22':
		return 'False'
	elif obj[7] == '72.39':
		return 'False'
	elif obj[7] == '102.96':
		return 'False'
	elif obj[7] == '80.25':
		return 'False'
	elif obj[7] == '86.57':
		return 'False'
	elif obj[7] == '68.84':
		return 'False'
	elif obj[7] == '158.48':
		return 'False'
	elif obj[7] == '104.02':
		return 'False'
	elif obj[7] == '76.28':
		return 'False'
	elif obj[7] == '107.84':
		return 'False'
	elif obj[7] == '185.0':
		return 'False'
	elif obj[7] == '104.42':
		return 'False'
	elif obj[7] == '128.23':
		return 'False'
	elif obj[7] == '104.23':
		return 'False'
	elif obj[7] == '133.82':
		return 'False'
	elif obj[7] == '102.35':
		return 'False'
	elif obj[7] == '88.48':
		return 'False'
	elif obj[7] == '68.44':
		return 'False'
	elif obj[7] == '94.12':
		return 'False'
	elif obj[7] == '96.24':
		return 'False'
	elif obj[7] == '57.3':
		return 'False'
	elif obj[7] == '101.35':
		return 'False'
	elif obj[7] == '94.03':
		return 'False'
	elif obj[7] == '227.81':
		return 'False'
	elif obj[7] == '134.61':
		return 'False'
	elif obj[7] == '75.92':
		return 'False'
	elif obj[7] == '152.02':
		return 'False'
	elif obj[7] == '120.09':
		return 'False'
	elif obj[7] == '90.15':
		return 'False'
	elif obj[7] == '80.09':
		return 'False'
	elif obj[7] == '189.44':
		return 'False'
	elif obj[7] == '249.29':
		return 'False'
	elif obj[7] == '96.93':
		return 'False'
	elif obj[7] == '211.35':
		return 'False'
	elif obj[7] == '60.96':
		return 'False'
	elif obj[7] == '92.13':
		return 'False'
	elif obj[7] == '80.86':
		return 'False'
	elif obj[7] == '97.24':
		return 'False'
	elif obj[7] == '134.8':
		return 'False'
	elif obj[7] == '74.65':
		return 'False'
	elif obj[7] == '206.59':
		return 'False'
	elif obj[7] == '196.33':
		return 'False'
	elif obj[7] == '242.94':
		return 'False'
	elif obj[7] == '103.06':
		return 'False'
	elif obj[7] == '231.69':
		return 'False'
	elif obj[7] == '92.67':
		return 'False'
	elif obj[7] == '267.76':
		return 'False'
	elif obj[7] == '69.82':
		return 'False'
	elif obj[7] == '74.36':
		return 'False'
	elif obj[7] == '153.38':
		return 'False'
	elif obj[7] == '84.85':
		return 'False'
	elif obj[7] == '135.89':
		return 'False'
	elif obj[7] == '106.13':
		return 'False'
	elif obj[7] == '74.33':
		return 'False'
	elif obj[7] == '95.85':
		return 'False'
	elif obj[7] == '90.36':
		return 'False'
	elif obj[7] == '63.45':
		return 'False'
	elif obj[7] == '122.91':
		return 'False'
	elif obj[7] == '77.63':
		return 'False'
	elif obj[7] == '70.61':
		return 'False'
	elif obj[7] == '124.34':
		return 'False'
	elif obj[7] == '208.06':
		return 'False'
	elif obj[7] == '98.85':
		return 'False'
	elif obj[7] == '65.6':
		return 'False'
	elif obj[7] == '103.28':
		return 'False'
	elif obj[7] == '223.35':
		return 'False'
	elif obj[7] == '65.95':
		return 'False'
	elif obj[7] == '65.28':
		return 'False'
	elif obj[7] == '56.51':
		return 'False'
	elif obj[7] == '90.35':
		return 'False'
	elif obj[7] == '77.86':
		return 'False'
	elif obj[7] == '71.88':
		return 'False'
	elif obj[7] == '121.66':
		return 'False'
	elif obj[7] == '95.46':
		return 'False'
	elif obj[7] == '59.99':
		return 'False'
	elif obj[7] == '90.26':
		return 'False'
	elif obj[7] == '91.9':
		return 'False'
	elif obj[7] == '100.33':
		return 'False'
	elif obj[7] == '89.81':
		return 'False'
	elif obj[7] == '97.32':
		return 'False'
	elif obj[7] == '121.44':
		return 'False'
	elif obj[7] == '83.52':
		return 'False'
	elif obj[7] == '75.27':
		return 'False'
	elif obj[7] == '80.24':
		return 'False'
	elif obj[7] == '69.09':
		return 'False'
	elif obj[7] == '62.67':
		return 'False'
	elif obj[7] == '96.18':
		return 'False'
	elif obj[7] == '186.95':
		return 'False'
	elif obj[7] == '128.72':
		return 'False'
	elif obj[7] == '65.69':
		return 'False'
	elif obj[7] == '107.91':
		return 'False'
	elif obj[7] == '83.85':
		return 'False'
	elif obj[7] == '72.13':
		return 'False'
	elif obj[7] == '94.98':
		return 'False'
	elif obj[7] == '228.42':
		return 'False'
	elif obj[7] == '93.9':
		return 'False'
	elif obj[7] == '121.6':
		return 'False'
	elif obj[7] == '82.13':
		return 'False'
	elif obj[7] == '73.33':
		return 'False'
	elif obj[7] == '212.97':
		return 'False'
	elif obj[7] == '100.41':
		return 'False'
	elif obj[7] == '202.05':
		return 'False'
	elif obj[7] == '71.42':
		return 'False'
	elif obj[7] == '107.5':
		return 'False'
	elif obj[7] == '55.57':
		return 'False'
	elif obj[7] == '58.14':
		return 'False'
	elif obj[7] == '78.79':
		return 'False'
	elif obj[7] == '113.68':
		return 'False'
	elif obj[7] == '114.45':
		return 'False'
	elif obj[7] == '74.55':
		return 'False'
	elif obj[7] == '83.34':
		return 'False'
	elif obj[7] == '97.52':
		return 'False'
	elif obj[7] == '198.24':
		return 'False'
	elif obj[7] == '90.51':
		return 'False'
	elif obj[7] == '97.78':
		return 'False'
	elif obj[7] == '93.0':
		return 'False'
	elif obj[7] == '96.25':
		return 'False'
	elif obj[7] == '63.08':
		return 'False'
	elif obj[7] == '229.21':
		return 'False'
	elif obj[7] == '82.37':
		return 'False'
	elif obj[7] == '151.33':
		return 'False'
	elif obj[7] == '91.46':
		return 'False'
	elif obj[7] == '100.29':
		return 'False'
	elif obj[7] == '87.95':
		return 'False'
	elif obj[7] == '74.01':
		return 'False'
	elif obj[7] == '95.75':
		return 'False'
	elif obj[7] == '85.51':
		return 'False'
	elif obj[7] == '240.81':
		return 'False'
	elif obj[7] == '60.35':
		return 'False'
	elif obj[7] == '118.66':
		return 'False'
	elif obj[7] == '216.4':
		return 'False'
	elif obj[7] == '55.58':
		return 'False'
	elif obj[7] == '65.87':
		return 'False'
	elif obj[7] == '89.28':
		return 'False'
	elif obj[7] == '74.7':
		return 'False'
	elif obj[7] == '81.44':
		return 'False'
	elif obj[7] == '100.02':
		return 'False'
	elif obj[7] == '70.54':
		return 'False'
	elif obj[7] == '205.0':
		return 'False'
	elif obj[7] == '126.39':
		return 'False'
	elif obj[7] == '92.08':
		return 'False'
	elif obj[7] == '95.25':
		return 'False'
	elif obj[7] == '203.44':
		return 'False'
	elif obj[7] == '243.73':
		return 'False'
	elif obj[7] == '55.46':
		return 'False'
	elif obj[7] == '113.87':
		return 'False'
	elif obj[7] == '67.03':
		return 'False'
	elif obj[7] == '96.35':
		return 'False'
	elif obj[7] == '266.59':
		return 'False'
	elif obj[7] == '131.4':
		return 'False'
	elif obj[7] == '58.51':
		return 'False'
	elif obj[7] == '96.0':
		return 'False'
	elif obj[7] == '167.59':
		return 'False'
	elif obj[7] == '98.03':
		return 'False'
	elif obj[7] == '92.9':
		return 'False'
	elif obj[7] == '117.34':
		return 'False'
	elif obj[7] == '80.75':
		return 'False'
	elif obj[7] == '227.04':
		return 'False'
	elif obj[7] == '87.56':
		return 'False'
	elif obj[7] == '84.47':
		return 'False'
	elif obj[7] == '79.57':
		return 'False'
	elif obj[7] == '78.44':
		return 'False'
	elif obj[7] == '64.15':
		return 'False'
	elif obj[7] == '74.5':
		return 'False'
	elif obj[7] == '144.08':
		return 'False'
	elif obj[7] == '78.14':
		return 'False'
	elif obj[7] == '133.58':
		return 'False'
	elif obj[7] == '214.42':
		return 'False'
	elif obj[7] == '233.71':
		return 'False'
	elif obj[7] == '127.21':
		return 'False'
	elif obj[7] == '78.9':
		return 'False'
	elif obj[7] == '160.94':
		return 'False'
	elif obj[7] == '87.94':
		return 'False'
	elif obj[7] == '106.83':
		return 'False'
	elif obj[7] == '84.44':
		return 'False'
	elif obj[7] == '92.16':
		return 'False'
	elif obj[7] == '85.96':
		return 'False'
	elif obj[7] == '202.57':
		return 'False'
	elif obj[7] == '150.1':
		return 'False'
	elif obj[7] == '65.5':
		return 'False'
	elif obj[7] == '78.96':
		return 'False'
	elif obj[7] == '71.59':
		return 'False'
	elif obj[7] == '57.43':
		return 'False'
	elif obj[7] == '87.93':
		return 'False'
	elif obj[7] == '112.12':
		return 'False'
	elif obj[7] == '92.02':
		return 'False'
	elif obj[7] == '86.35':
		return 'False'
	elif obj[7] == '110.78':
		return 'False'
	elif obj[7] == '99.78':
		return 'False'
	elif obj[7] == '201.45':
		return 'False'
	elif obj[7] == '173.14':
		return 'False'
	elif obj[7] == '215.72':
		return 'False'
	elif obj[7] == '101.87':
		return 'False'
	elif obj[7] == '96.69':
		return 'False'
	elif obj[7] == '116.02':
		return 'False'
	elif obj[7] == '127.32':
		return 'False'
	elif obj[7] == '176.25':
		return 'False'
	elif obj[7] == '168.06':
		return 'False'
	elif obj[7] == '75.52':
		return 'False'
	elif obj[7] == '82.15':
		return 'False'
	elif obj[7] == '62.44':
		return 'False'
	elif obj[7] == '145.03':
		return 'False'
	elif obj[7] == '192.16':
		return 'False'
	elif obj[7] == '98.53':
		return 'False'
	elif obj[7] == '105.55':
		return 'False'
	elif obj[7] == '70.52':
		return 'False'
	elif obj[7] == '93.21':
		return 'False'
	elif obj[7] == '88.29':
		return 'False'
	elif obj[7] == '80.18':
		return 'False'
	elif obj[7] == '84.02':
		return 'False'
	elif obj[7] == '77.37':
		return 'False'
	elif obj[7] == '165.99':
		return 'False'
	elif obj[7] == '113.86':
		return 'False'
	elif obj[7] == '79.59':
		return 'False'
	elif obj[7] == '216.0':
		return 'False'
	elif obj[7] == '75.64':
		return 'False'
	elif obj[7] == '95.07':
		return 'False'
	elif obj[7] == '129.97':
		return 'False'
	elif obj[7] == '124.26':
		return 'False'
	elif obj[7] == '219.39':
		return 'False'
	elif obj[7] == '89.95':
		return 'False'
	elif obj[7] == '110.07':
		return 'False'
	elif obj[7] == '60.56':
		return 'False'
	elif obj[7] == '89.83':
		return 'False'
	elif obj[7] == '71.71':
		return 'False'
	elif obj[7] == '173.96':
		return 'False'
	elif obj[7] == '96.06':
		return 'False'
	elif obj[7] == '113.2':
		return 'False'
	elif obj[7] == '65.71':
		return 'False'
	elif obj[7] == '63.32':
		return 'False'
	elif obj[7] == '85.68':
		return 'False'
	elif obj[7] == '247.48':
		return 'False'
	elif obj[7] == '180.8':
		return 'False'
	elif obj[7] == '75.03':
		return 'False'
	elif obj[7] == '117.75':
		return 'False'
	elif obj[7] == '96.04':
		return 'False'
	elif obj[7] == '92.72':
		return 'False'
	elif obj[7] == '61.83':
		return 'False'
	elif obj[7] == '131.99':
		return 'False'
	elif obj[7] == '136.81':
		return 'False'
	elif obj[7] == '239.28':
		return 'False'
	elif obj[7] == '131.3':
		return 'False'
	elif obj[7] == '145.5':
		return 'False'
	elif obj[7] == '77.75':
		return 'False'
	elif obj[7] == '101.25':
		return 'False'
	elif obj[7] == '131.43':
		return 'False'
	elif obj[7] == '231.5':
		return 'False'
	elif obj[7] == '82.89':
		return 'False'
	elif obj[7] == '192.37':
		return 'False'
	elif obj[7] == '79.64':
		return 'False'
	elif obj[7] == '99.4':
		return 'False'
	elif obj[7] == '198.33':
		return 'False'
	elif obj[7] == '191.33':
		return 'False'
	elif obj[7] == '60.06':
		return 'False'
	elif obj[7] == '206.52':
		return 'False'
	elif obj[7] == '86.55':
		return 'False'
	elif obj[7] == '118.61':
		return 'False'
	elif obj[7] == '80.21':
		return 'False'
	elif obj[7] == '65.96':
		return 'False'
	elif obj[7] == '69.22':
		return 'False'
	elif obj[7] == '207.95':
		return 'False'
	elif obj[7] == '134.29':
		return 'False'
	elif obj[7] == '112.94':
		return 'False'
	elif obj[7] == '73.54':
		return 'False'
	elif obj[7] == '69.91':
		return 'False'
	elif obj[7] == '63.95':
		return 'False'
	elif obj[7] == '120.27':
		return 'False'
	elif obj[7] == '131.63':
		return 'False'
	elif obj[7] == '79.36':
		return 'False'
	elif obj[7] == '100.42':
		return 'False'
	elif obj[7] == '155.86':
		return 'False'
	elif obj[7] == '66.01':
		return 'False'
	elif obj[7] == '55.62':
		return 'False'
	elif obj[7] == '62.48':
		return 'False'
	elif obj[7] == '74.43':
		return 'False'
	elif obj[7] == '87.08':
		return 'False'
	elif obj[7] == '80.07':
		return 'False'
	elif obj[7] == '112.2':
		return 'False'
	elif obj[7] == '91.18':
		return 'False'
	elif obj[7] == '148.37':
		return 'False'
	elif obj[7] == '80.97':
		return 'False'
	elif obj[7] == '89.88':
		return 'False'
	elif obj[7] == '62.66':
		return 'False'
	elif obj[7] == '85.0':
		return 'False'
	elif obj[7] == '74.32':
		return 'False'
	elif obj[7] == '100.49':
		return 'False'
	elif obj[7] == '79.73':
		return 'False'
	elif obj[7] == '98.39':
		return 'False'
	elif obj[7] == '128.04':
		return 'False'
	elif obj[7] == '83.27':
		return 'False'
	elif obj[7] == '99.73':
		return 'False'
	elif obj[7] == '161.57':
		return 'False'
	elif obj[7] == '67.75':
		return 'False'
	elif obj[7] == '154.08':
		return 'False'
	elif obj[7] == '74.26':
		return 'False'
	elif obj[7] == '102.37':
		return 'False'
	elif obj[7] == '86.26':
		return 'False'
	elif obj[7] == '140.28':
		return 'False'
	elif obj[7] == '244.28':
		return 'False'
	elif obj[7] == '99.34':
		return 'False'
	elif obj[7] == '59.87':
		return 'False'
	elif obj[7] == '72.76':
		return 'False'
	elif obj[7] == '93.24':
		return 'False'
	elif obj[7] == '154.75':
		return 'False'
	elif obj[7] == '62.81':
		return 'False'
	elif obj[7] == '96.85':
		return 'False'
	elif obj[7] == '251.99':
		return 'False'
	elif obj[7] == '115.13':
		return 'False'
	elif obj[7] == '78.99':
		return 'False'
	elif obj[7] == '191.79':
		return 'False'
	elif obj[7] == '68.8':
		return 'False'
	elif obj[7] == '83.84':
		return 'False'
	elif obj[7] == '94.66':
		return 'False'
	elif obj[7] == '169.97':
		return 'False'
	elif obj[7] == '73.66':
		return 'False'
	elif obj[7] == '87.78':
		return 'False'
	elif obj[7] == '150.27':
		return 'False'
	elif obj[7] == '119.03':
		return 'False'
	elif obj[7] == '237.21':
		return 'False'
	elif obj[7] == '246.53':
		return 'False'
	elif obj[7] == '89.05':
		return 'False'
	elif obj[7] == '98.12':
		return 'False'
	elif obj[7] == '105.59':
		return 'False'
	elif obj[7] == '65.82':
		return 'False'
	elif obj[7] == '64.45':
		return 'False'
	elif obj[7] == '206.33':
		return 'False'
	elif obj[7] == '107.4':
		return 'False'
	elif obj[7] == '100.84':
		return 'False'
	elif obj[7] == '80.15':
		return 'False'
	elif obj[7] == '206.98':
		return 'False'
	elif obj[7] == '227.28':
		return 'False'
	elif obj[7] == '120.07':
		return 'False'
	elif obj[7] == '93.47':
		return 'False'
	elif obj[7] == '80.77':
		return 'False'
	elif obj[7] == '107.98':
		return 'False'
	elif obj[7] == '135.64':
		return 'False'
	elif obj[7] == '163.56':
		return 'False'
	elif obj[7] == '139.43':
		return 'False'
	elif obj[7] == '58.3':
		return 'False'
	elif obj[7] == '98.91':
		return 'False'
	elif obj[7] == '97.5':
		return 'False'
	elif obj[7] == '108.43':
		return 'False'
	elif obj[7] == '76.3':
		return 'False'
	elif obj[7] == '121.27':
		return 'False'
	elif obj[7] == '226.93':
		return 'False'
	elif obj[7] == '93.23':
		return 'False'
	elif obj[7] == '101.02':
		return 'False'
	elif obj[7] == '238.53':
		return 'False'
	elif obj[7] == '79.18':
		return 'False'
	elif obj[7] == '207.79':
		return 'False'
	elif obj[7] == '196.2':
		return 'False'
	elif obj[7] == '231.76':
		return 'False'
	elif obj[7] == '110.47':
		return 'False'
	elif obj[7] == '91.23':
		return 'False'
	elif obj[7] == '157.01':
		return 'False'
	elif obj[7] == '207.45':
		return 'False'
	elif obj[7] == '123.49':
		return 'False'
	elif obj[7] == '65.84':
		return 'False'
	elif obj[7] == '110.6':
		return 'False'
	elif obj[7] == '213.11':
		return 'False'
	elif obj[7] == '77.23':
		return 'False'
	elif obj[7] == '58.48':
		return 'False'
	elif obj[7] == '87.33':
		return 'False'
	elif obj[7] == '102.34':
		return 'False'
	elif obj[7] == '151.3':
		return 'False'
	elif obj[7] == '144.23':
		return 'False'
	elif obj[7] == '227.51':
		return 'False'
	elif obj[7] == '111.13':
		return 'False'
	elif obj[7] == '201.01':
		return 'False'
	elif obj[7] == '95.4':
		return 'False'
	elif obj[7] == '65.9':
		return 'False'
	elif obj[7] == '81.28':
		return 'False'
	elif obj[7] == '102.5':
		return 'False'
	elif obj[7] == '237.58':
		return 'False'
	elif obj[7] == '59.05':
		return 'False'
	elif obj[7] == '158.89':
		return 'False'
	elif obj[7] == '93.17':
		return 'False'
	elif obj[7] == '108.1':
		return 'False'
	elif obj[7] == '88.34':
		return 'False'
	elif obj[7] == '81.02':
		return 'False'
	elif obj[7] == '94.33':
		return 'False'
	elif obj[7] == '88.13':
		return 'False'
	elif obj[7] == '102.77':
		return 'False'
	elif obj[7] == '101.75':
		return 'False'
	elif obj[7] == '113.34':
		return 'False'
	elif obj[7] == '63.33':
		return 'False'
	elif obj[7] == '66.13':
		return 'False'
	elif obj[7] == '67.53':
		return 'False'
	elif obj[7] == '96.58':
		return 'False'
	elif obj[7] == '57.89':
		return 'False'
	elif obj[7] == '127.75':
		return 'False'
	elif obj[7] == '141.15':
		return 'False'
	elif obj[7] == '88.63':
		return 'False'
	elif obj[7] == '104.07':
		return 'False'
	elif obj[7] == '150.45':
		return 'False'
	elif obj[7] == '100.39':
		return 'False'
	elif obj[7] == '195.25':
		return 'False'
	elif obj[7] == '103.48':
		return 'False'
	elif obj[7] == '210.96':
		return 'False'
	elif obj[7] == '239.52':
		return 'False'
	elif obj[7] == '90.84':
		return 'False'
	elif obj[7] == '217.71':
		return 'False'
	elif obj[7] == '133.76':
		return 'False'
	elif obj[7] == '61.36':
		return 'False'
	elif obj[7] == '68.98':
		return 'False'
	elif obj[7] == '96.2':
		return 'False'
	elif obj[7] == '83.12':
		return 'False'
	elif obj[7] == '99.15':
		return 'False'
	elif obj[7] == '61.61':
		return 'False'
	elif obj[7] == '93.68':
		return 'False'
	elif obj[7] == '229.86':
		return 'False'
	elif obj[7] == '78.73':
		return 'False'
	elif obj[7] == '115.92':
		return 'False'
	elif obj[7] == '93.71':
		return 'False'
	elif obj[7] == '76.66':
		return 'False'
	elif obj[7] == '79.69':
		return 'False'
	elif obj[7] == '74.72':
		return 'False'
	elif obj[7] == '101.34':
		return 'False'
	elif obj[7] == '85.07':
		return 'False'
	elif obj[7] == '119.01':
		return 'False'
	elif obj[7] == '121.43':
		return 'False'
	elif obj[7] == '94.22':
		return 'False'
	elif obj[7] == '67.27':
		return 'False'
	elif obj[7] == '197.58':
		return 'False'
	elif obj[7] == '86.37':
		return 'False'
	elif obj[7] == '199.96':
		return 'False'
	elif obj[7] == '86.33':
		return 'False'
	elif obj[7] == '80.47':
		return 'False'
	elif obj[7] == '62.46':
		return 'False'
	elif obj[7] == '103.81':
		return 'False'
	elif obj[7] == '62.25':
		return 'False'
	elif obj[7] == '155.17':
		return 'False'
	elif obj[7] == '103.25':
		return 'False'
	elif obj[7] == '126.99':
		return 'False'
	elif obj[7] == '108.08':
		return 'False'
	elif obj[7] == '108.34':
		return 'False'
	elif obj[7] == '88.41':
		return 'False'
	elif obj[7] == '178.76':
		return 'False'
	elif obj[7] == '112.23':
		return 'False'
	elif obj[7] == '74.79':
		return 'False'
	elif obj[7] == '134.45':
		return 'False'
	elif obj[7] == '71.98':
		return 'False'
	elif obj[7] == '167.31':
		return 'False'
	elif obj[7] == '87.49':
		return 'False'
	elif obj[7] == '72.2':
		return 'False'
	elif obj[7] == '63.37':
		return 'False'
	elif obj[7] == '74.82':
		return 'False'
	elif obj[7] == '97.12':
		return 'False'
	elif obj[7] == '189.45':
		return 'False'
	elif obj[7] == '91.88':
		return 'False'
	elif obj[7] == '144.16':
		return 'False'
	elif obj[7] == '82.56':
		return 'False'
	elif obj[7] == '206.4':
		return 'False'
	elif obj[7] == '71.7':
		return 'False'
	elif obj[7] == '72.02':
		return 'False'
	elif obj[7] == '156.7':
		return 'False'
	elif obj[7] == '138.47':
		return 'False'
	elif obj[7] == '102.54':
		return 'False'
	elif obj[7] == '126.67':
		return 'False'
	elif obj[7] == '237.74':
		return 'False'
	elif obj[7] == '211.88':
		return 'False'
	elif obj[7] == '56.67':
		return 'False'
	elif obj[7] == '81.66':
		return 'False'
	elif obj[7] == '91.63':
		return 'False'
	elif obj[7] == '225.6':
		return 'False'
	elif obj[7] == '95.58':
		return 'False'
	elif obj[7] == '210.23':
		return 'False'
	elif obj[7] == '234.82':
		return 'False'
	elif obj[7] == '81.99':
		return 'False'
	elif obj[7] == '125.29':
		return 'False'
	elif obj[7] == '70.93':
		return 'False'
	elif obj[7] == '89.93':
		return 'False'
	elif obj[7] == '72.06':
		return 'False'
	elif obj[7] == '97.9':
		return 'False'
	elif obj[7] == '230.59':
		return 'False'
	elif obj[7] == '224.63':
		return 'False'
	elif obj[7] == '84.14':
		return 'False'
	elif obj[7] == '85.57':
		return 'False'
	elif obj[7] == '76.55':
		return 'False'
	elif obj[7] == '66.29':
		return 'False'
	elif obj[7] == '58.87':
		return 'False'
	elif obj[7] == '95.57':
		return 'False'
	elif obj[7] == '76.22':
		return 'False'
	elif obj[7] == '155.32':
		return 'False'
	elif obj[7] == '70.67':
		return 'False'
	elif obj[7] == '227.16':
		return 'False'
	elif obj[7] == '58.69':
		return 'False'
	elif obj[7] == '137.94':
		return 'False'
	elif obj[7] == '93.67':
		return 'False'
	elif obj[7] == '79.56':
		return 'False'
	elif obj[7] == '122.46':
		return 'False'
	elif obj[7] == '59.89':
		return 'False'
	elif obj[7] == '88.52':
		return 'False'
	elif obj[7] == '88.82':
		return 'False'
	elif obj[7] == '102.08':
		return 'False'
	elif obj[7] == '209.9':
		return 'False'
	elif obj[7] == '176.48':
		return 'False'
	elif obj[7] == '94.07':
		return 'False'
	elif obj[7] == '111.93':
		return 'False'
	elif obj[7] == '110.53':
		return 'False'
	elif obj[7] == '140.4':
		return 'False'
	elif obj[7] == '61.32':
		return 'False'
	elif obj[7] == '86.04':
		return 'False'
	elif obj[7] == '99.87':
		return 'False'
	elif obj[7] == '113.74':
		return 'False'
	elif obj[7] == '86.68':
		return 'False'
	elif obj[7] == '140.39':
		return 'False'
	elif obj[7] == '95.82':
		return 'False'
	elif obj[7] == '204.05':
		return 'False'
	elif obj[7] == '67.78':
		return 'False'
	elif obj[7] == '116.12':
		return 'False'
	elif obj[7] == '59.63':
		return 'False'
	elif obj[7] == '56.43':
		return 'False'
	elif obj[7] == '199.18':
		return 'False'
	elif obj[7] == '209.26':
		return 'False'
	elif obj[7] == '217.11':
		return 'False'
	elif obj[7] == '222.46':
		return 'False'
	elif obj[7] == '187.52':
		return 'False'
	elif obj[7] == '76.63':
		return 'False'
	elif obj[7] == '65.09':
		return 'False'
	elif obj[7] == '72.52':
		return 'False'
	elif obj[7] == '114.33':
		return 'False'
	elif obj[7] == '196.25':
		return 'False'
	elif obj[7] == '187.87':
		return 'False'
	elif obj[7] == '208.17':
		return 'False'
	elif obj[7] == '146.61':
		return 'False'
	elif obj[7] == '84.56':
		return 'False'
	elif obj[7] == '185.31':
		return 'False'
	elif obj[7] == '102.53':
		return 'False'
	elif obj[7] == '76.68':
		return 'False'
	elif obj[7] == '90.95':
		return 'False'
	elif obj[7] == '213.87':
		return 'False'
	elif obj[7] == '115.23':
		return 'False'
	elif obj[7] == '222.85':
		return 'False'
	elif obj[7] == '79.99':
		return 'False'
	elif obj[7] == '198.36':
		return 'False'
	elif obj[7] == '93.61':
		return 'False'
	elif obj[7] == '75.43':
		return 'False'
	elif obj[7] == '82.84':
		return 'False'
	elif obj[7] == '92.27':
		return 'False'
	elif obj[7] == '217.66':
		return 'False'
	elif obj[7] == '56.84':
		return 'False'
	elif obj[7] == '107.11':
		return 'False'
	elif obj[7] == '99.69':
		return 'False'
	elif obj[7] == '89.75':
		return 'False'
	elif obj[7] == '87.66':
		return 'False'
	elif obj[7] == '178.33':
		return 'False'
	elif obj[7] == '70.45':
		return 'False'
	elif obj[7] == '146.44':
		return 'False'
	elif obj[7] == '65.04':
		return 'False'
	elif obj[7] == '113.4':
		return 'False'
	elif obj[7] == '69.38':
		return 'False'
	elif obj[7] == '66.11':
		return 'False'
	elif obj[7] == '149.62':
		return 'False'
	elif obj[7] == '242.84':
		return 'False'
	elif obj[7] == '216.9':
		return 'False'
	elif obj[7] == '114.88':
		return 'False'
	elif obj[7] == '75.94':
		return 'False'
	elif obj[7] == '71.44':
		return 'False'
	elif obj[7] == '58.29':
		return 'False'
	elif obj[7] == '115.83':
		return 'False'
	elif obj[7] == '71.31':
		return 'False'
	elif obj[7] == '102.28':
		return 'False'
	elif obj[7] == '115.93':
		return 'False'
	elif obj[7] == '68.78':
		return 'False'
	elif obj[7] == '69.18':
		return 'False'
	elif obj[7] == '218.54':
		return 'False'
	elif obj[7] == '82.07':
		return 'False'
	elif obj[7] == '108.2':
		return 'False'
	elif obj[7] == '123.95':
		return 'False'
	elif obj[7] == '58.71':
		return 'False'
	elif obj[7] == '98.46':
		return 'False'
	elif obj[7] == '63.4':
		return 'False'
	elif obj[7] == '97.14':
		return 'False'
	elif obj[7] == '78.34':
		return 'False'
	elif obj[7] == '93.48':
		return 'False'
	elif obj[7] == '107.45':
		return 'False'
	elif obj[7] == '83.86':
		return 'False'
	elif obj[7] == '119.96':
		return 'False'
	elif obj[7] == '70.58':
		return 'False'
	elif obj[7] == '87.7':
		return 'False'
	elif obj[7] == '102.71':
		return 'False'
	elif obj[7] == '56.63':
		return 'False'
	elif obj[7] == '63.19':
		return 'False'
	elif obj[7] == '87.34':
		return 'False'
	elif obj[7] == '82.08':
		return 'False'
	elif obj[7] == '103.35':
		return 'False'
	elif obj[7] == '123.65':
		return 'False'
	elif obj[7] == '99.3':
		return 'False'
	elif obj[7] == '144.2':
		return 'False'
	elif obj[7] == '122.48':
		return 'False'
	elif obj[7] == '215.9':
		return 'False'
	elif obj[7] == '60.74':
		return 'False'
	elif obj[7] == '233.52':
		return 'False'
	elif obj[7] == '110.7':
		return 'False'
	elif obj[7] == '58.25':
		return 'False'
	elif obj[7] == '213.54':
		return 'False'
	elif obj[7] == '83.41':
		return 'False'
	elif obj[7] == '188.69':
		return 'False'
	elif obj[7] == '86.51':
		return 'False'
	elif obj[7] == '219.5':
		return 'False'
	elif obj[7] == '83.79':
		return 'False'
	elif obj[7] == '190.4':
		return 'False'
	elif obj[7] == '80.73':
		return 'False'
	elif obj[7] == '200.16':
		return 'False'
	elif obj[7] == '199.14':
		return 'False'
	elif obj[7] == '81.43':
		return 'False'
	elif obj[7] == '78.59':
		return 'False'
	elif obj[7] == '101.22':
		return 'False'
	elif obj[7] == '105.47':
		return 'False'
	elif obj[7] == '114.47':
		return 'False'
	elif obj[7] == '222.6':
		return 'False'
	elif obj[7] == '64.51':
		return 'False'
	elif obj[7] == '73.41':
		return 'False'
	elif obj[7] == '82.26':
		return 'False'
	elif obj[7] == '109.65':
		return 'False'
	elif obj[7] == '69.11':
		return 'False'
	elif obj[7] == '114.41':
		return 'False'
	elif obj[7] == '103.46':
		return 'False'
	elif obj[7] == '191.48':
		return 'False'
	elif obj[7] == '89.24':
		return 'False'
	elif obj[7] == '70.13':
		return 'False'
	elif obj[7] == '166.29':
		return 'False'
	else: return 'False'
