def findDecision(obj): #obj[0]: gender, obj[1]: age, obj[2]: hypertension, obj[3]: heart_disease, obj[4]: ever_married, obj[5]: work_type, obj[6]: Residence_type, obj[7]: avg_glucose_level, obj[8]: bmi, obj[9]: smoking_status
	# {"feature": "age", "instances": 5110, "metric_value": 0.281, "depth": 1}
	if obj[1]<=65.83704850852197:
		# {"feature": "heart_disease", "instances": 4145, "metric_value": 0.1549, "depth": 2}
		if obj[3]<=0:
			# {"feature": "bmi", "instances": 4046, "metric_value": 0.1402, "depth": 3}
			if obj[8]>9.3:
				# {"feature": "hypertension", "instances": 3929, "metric_value": 0.1246, "depth": 4}
				if obj[2]<=0:
					# {"feature": "avg_glucose_level", "instances": 3695, "metric_value": 0.1084, "depth": 5}
					if obj[7]<=172.60311470795472:
						# {"feature": "ever_married", "instances": 3464, "metric_value": 0.0964, "depth": 6}
						if obj[4] == 'Yes':
							# {"feature": "smoking_status", "instances": 1912, "metric_value": 0.1348, "depth": 7}
							if obj[9] == 'never smoked':
								# {"feature": "Residence_type", "instances": 785, "metric_value": 0.0904, "depth": 8}
								if obj[6] == 'Urban':
									# {"feature": "work_type", "instances": 400, "metric_value": 0.1124, "depth": 9}
									if obj[5] == 'Private':
										# {"feature": "gender", "instances": 274, "metric_value": 0.1315, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[5] == 'Govt_job':
										# {"feature": "gender", "instances": 72, "metric_value": 0.1056, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[5] == 'Self-employed':
										return '0'
									else: return '0'
								elif obj[6] == 'Rural':
									# {"feature": "work_type", "instances": 385, "metric_value": 0.0658, "depth": 9}
									if obj[5] == 'Private':
										# {"feature": "gender", "instances": 264, "metric_value": 0.0643, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[5] == 'Govt_job':
										return '0'
									elif obj[5] == 'Self-employed':
										# {"feature": "gender", "instances": 56, "metric_value": 0.1292, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							elif obj[9] == 'Unknown':
								# {"feature": "gender", "instances": 407, "metric_value": 0.1395, "depth": 8}
								if obj[0] == 'Female':
									# {"feature": "work_type", "instances": 251, "metric_value": 0.0935, "depth": 9}
									if obj[5] == 'Private':
										return '0'
									elif obj[5] == 'Govt_job':
										# {"feature": "Residence_type", "instances": 49, "metric_value": 0.3323, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									elif obj[5] == 'Self-employed':
										return '0'
									else: return '0'
								elif obj[0] == 'Male':
									# {"feature": "work_type", "instances": 156, "metric_value": 0.2046, "depth": 9}
									if obj[5] == 'Private':
										# {"feature": "Residence_type", "instances": 117, "metric_value": 0.215, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									elif obj[5] == 'Govt_job':
										return '0'
									elif obj[5] == 'Self-employed':
										# {"feature": "Residence_type", "instances": 19, "metric_value": 0.2975, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							elif obj[9] == 'smokes':
								# {"feature": "Residence_type", "instances": 368, "metric_value": 0.18, "depth": 8}
								if obj[6] == 'Urban':
									# {"feature": "gender", "instances": 201, "metric_value": 0.1409, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "work_type", "instances": 118, "metric_value": 0.2136, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										elif obj[5] == 'Govt_job':
											return '0'
										elif obj[5] == 'Self-employed':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										return '0'
									else: return '0'
								elif obj[6] == 'Rural':
									# {"feature": "gender", "instances": 167, "metric_value": 0.2233, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "work_type", "instances": 102, "metric_value": 0.1914, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										elif obj[5] == 'Self-employed':
											return '0'
										elif obj[5] == 'Govt_job':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										# {"feature": "work_type", "instances": 65, "metric_value": 0.2698, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										elif obj[5] == 'Govt_job':
											return '0'
										elif obj[5] == 'Self-employed':
											return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							elif obj[9] == 'formerly smoked':
								# {"feature": "work_type", "instances": 352, "metric_value": 0.1717, "depth": 8}
								if obj[5] == 'Private':
									# {"feature": "gender", "instances": 231, "metric_value": 0.2171, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 144, "metric_value": 0.1831, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										# {"feature": "Residence_type", "instances": 87, "metric_value": 0.2691, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[5] == 'Govt_job':
									# {"feature": "Residence_type", "instances": 61, "metric_value": 0.1207, "depth": 9}
									if obj[6] == 'Urban':
										return '0'
									elif obj[6] == 'Rural':
										# {"feature": "gender", "instances": 29, "metric_value": 0.2164, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[5] == 'Self-employed':
									return '0'
								else: return '0'
							else: return '0'
						elif obj[4] == 'No':
							# {"feature": "work_type", "instances": 1552, "metric_value": 0.0416, "depth": 7}
							if obj[5] == 'Private':
								# {"feature": "gender", "instances": 712, "metric_value": 0.0393, "depth": 8}
								if obj[0] == 'Female':
									# {"feature": "Residence_type", "instances": 452, "metric_value": 0.0227, "depth": 9}
									if obj[6] == 'Rural':
										return '0'
									elif obj[6] == 'Urban':
										# {"feature": "smoking_status", "instances": 219, "metric_value": 0.0421, "depth": 10}
										if obj[9] == 'never smoked':
											return '0'
										elif obj[9] == 'Unknown':
											return '0'
										elif obj[9] == 'smokes':
											return '0'
										elif obj[9] == 'formerly smoked':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[0] == 'Male':
									# {"feature": "Residence_type", "instances": 259, "metric_value": 0.0653, "depth": 9}
									if obj[6] == 'Rural':
										# {"feature": "smoking_status", "instances": 134, "metric_value": 0.1119, "depth": 10}
										if obj[9] == 'never smoked':
											return '0'
										elif obj[9] == 'Unknown':
											return '0'
										elif obj[9] == 'smokes':
											return '0'
										elif obj[9] == 'formerly smoked':
											return '0'
										else: return '0'
									elif obj[6] == 'Urban':
										return '0'
									else: return '0'
								elif obj[0] == 'Other':
									return '0'
								else: return '0'
							elif obj[5] == 'children':
								# {"feature": "gender", "instances": 663, "metric_value": 0.0163, "depth": 8}
								if obj[0] == 'Male':
									return '0'
								elif obj[0] == 'Female':
									# {"feature": "Residence_type", "instances": 316, "metric_value": 0.0308, "depth": 9}
									if obj[6] == 'Rural':
										# {"feature": "smoking_status", "instances": 163, "metric_value": 0.0539, "depth": 10}
										if obj[9] == 'Unknown':
											return '0'
										elif obj[9] == 'never smoked':
											return '0'
										elif obj[9] == 'formerly smoked':
											return '0'
										else: return '0'
									elif obj[6] == 'Urban':
										return '0'
									else: return '0'
								else: return '0'
							elif obj[5] == 'Govt_job':
								# {"feature": "gender", "instances": 89, "metric_value": 0.0889, "depth": 8}
								if obj[0] == 'Female':
									return '0'
								elif obj[0] == 'Male':
									# {"feature": "Residence_type", "instances": 36, "metric_value": 0.1831, "depth": 9}
									if obj[6] == 'Rural':
										return '0'
									elif obj[6] == 'Urban':
										# {"feature": "smoking_status", "instances": 15, "metric_value": 0.3534, "depth": 10}
										if obj[9] == 'never smoked':
											return '0'
										elif obj[9] == 'Unknown':
											return '0'
										elif obj[9] == 'formerly smoked':
											return '0'
										elif obj[9] == 'smokes':
											return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							elif obj[5] == 'Self-employed':
								# {"feature": "Residence_type", "instances": 66, "metric_value": 0.1959, "depth": 8}
								if obj[6] == 'Rural':
									return '0'
								elif obj[6] == 'Urban':
									# {"feature": "smoking_status", "instances": 31, "metric_value": 0.3451, "depth": 9}
									if obj[9] == 'never smoked':
										# {"feature": "gender", "instances": 13, "metric_value": 0.3912, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[9] == 'Unknown':
										return '0'
									elif obj[9] == 'smokes':
										return '0'
									elif obj[9] == 'formerly smoked':
										# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0] == 'Male':
											return '0'
										elif obj[0] == 'Female':
											return '1'
										else: return '1'
									else: return '0'
								else: return '0'
							elif obj[5] == 'Never_worked':
								return '0'
							else: return '0'
						else: return '0'
					elif obj[7]>172.60311470795472:
						# {"feature": "ever_married", "instances": 231, "metric_value": 0.2572, "depth": 6}
						if obj[4] == 'Yes':
							# {"feature": "smoking_status", "instances": 193, "metric_value": 0.2941, "depth": 7}
							if obj[9] == 'never smoked':
								# {"feature": "work_type", "instances": 85, "metric_value": 0.2203, "depth": 8}
								if obj[5] == 'Private':
									# {"feature": "gender", "instances": 55, "metric_value": 0.3054, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 34, "metric_value": 0.1914, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										# {"feature": "Residence_type", "instances": 21, "metric_value": 0.4537, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[5] == 'Govt_job':
									return '0'
								elif obj[5] == 'Self-employed':
									return '0'
								else: return '0'
							elif obj[9] == 'formerly smoked':
								# {"feature": "work_type", "instances": 43, "metric_value": 0.5186, "depth": 8}
								if obj[5] == 'Private':
									# {"feature": "Residence_type", "instances": 26, "metric_value": 0.6194, "depth": 9}
									if obj[6] == 'Rural':
										# {"feature": "gender", "instances": 14, "metric_value": 0.3712, "depth": 10}
										if obj[0] == 'Male':
											return '0'
										elif obj[0] == 'Female':
											return '0'
										else: return '0'
									elif obj[6] == 'Urban':
										# {"feature": "gender", "instances": 12, "metric_value": 0.8113, "depth": 10}
										if obj[0] == 'Male':
											return '0'
										elif obj[0] == 'Female':
											return '1'
										else: return '1'
									else: return '0'
								elif obj[5] == 'Govt_job':
									# {"feature": "gender", "instances": 10, "metric_value": 0.469, "depth": 9}
									if obj[0] == 'Male':
										return '0'
									elif obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Rural':
											return '1'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[5] == 'Self-employed':
									return '0'
								else: return '0'
							elif obj[9] == 'smokes':
								# {"feature": "gender", "instances": 36, "metric_value": 0.3095, "depth": 8}
								if obj[0] == 'Female':
									# {"feature": "work_type", "instances": 22, "metric_value": 0.4395, "depth": 9}
									if obj[5] == 'Private':
										# {"feature": "Residence_type", "instances": 14, "metric_value": 0.3712, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									elif obj[5] == 'Self-employed':
										# {"feature": "Residence_type", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									elif obj[5] == 'Govt_job':
										return '0'
									else: return '0'
								elif obj[0] == 'Male':
									return '0'
								else: return '0'
							elif obj[9] == 'Unknown':
								return '0'
							else: return '0'
						elif obj[4] == 'No':
							return '0'
						else: return '0'
					else: return '0'
				elif obj[2]>0:
					# {"feature": "ever_married", "instances": 234, "metric_value": 0.3268, "depth": 5}
					if obj[4] == 'Yes':
						# {"feature": "avg_glucose_level", "instances": 209, "metric_value": 0.3546, "depth": 6}
						if obj[7]<=238.60361450277637:
							# {"feature": "work_type", "instances": 205, "metric_value": 0.3409, "depth": 7}
							if obj[5] == 'Private':
								# {"feature": "smoking_status", "instances": 124, "metric_value": 0.2795, "depth": 8}
								if obj[9] == 'never smoked':
									# {"feature": "Residence_type", "instances": 58, "metric_value": 0.1257, "depth": 9}
									if obj[6] == 'Rural':
										return '0'
									elif obj[6] == 'Urban':
										# {"feature": "gender", "instances": 27, "metric_value": 0.2285, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[9] == 'smokes':
									# {"feature": "gender", "instances": 30, "metric_value": 0.3534, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 17, "metric_value": 0.3228, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										# {"feature": "Residence_type", "instances": 13, "metric_value": 0.3912, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[9] == 'formerly smoked':
									# {"feature": "Residence_type", "instances": 22, "metric_value": 0.4395, "depth": 9}
									if obj[6] == 'Urban':
										# {"feature": "gender", "instances": 13, "metric_value": 0.3912, "depth": 10}
										if obj[0] == 'Male':
											return '0'
										elif obj[0] == 'Female':
											return '0'
										else: return '0'
									elif obj[6] == 'Rural':
										# {"feature": "gender", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[0] == 'Male':
											return '0'
										elif obj[0] == 'Female':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[9] == 'Unknown':
									# {"feature": "gender", "instances": 14, "metric_value": 0.3712, "depth": 9}
									if obj[0] == 'Male':
										return '0'
									elif obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							elif obj[5] == 'Self-employed':
								# {"feature": "gender", "instances": 43, "metric_value": 0.3651, "depth": 8}
								if obj[0] == 'Male':
									# {"feature": "smoking_status", "instances": 27, "metric_value": 0.2285, "depth": 9}
									if obj[9] == 'never smoked':
										return '0'
									elif obj[9] == 'smokes':
										# {"feature": "Residence_type", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									elif obj[9] == 'formerly smoked':
										return '0'
									elif obj[9] == 'Unknown':
										return '0'
									else: return '0'
								elif obj[0] == 'Female':
									# {"feature": "smoking_status", "instances": 16, "metric_value": 0.5436, "depth": 9}
									if obj[9] == 'never smoked':
										# {"feature": "Residence_type", "instances": 10, "metric_value": 0.7219, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									elif obj[9] == 'Unknown':
										return '0'
									elif obj[9] == 'formerly smoked':
										return '0'
									elif obj[9] == 'smokes':
										return '0'
									else: return '0'
								else: return '0'
							elif obj[5] == 'Govt_job':
								# {"feature": "Residence_type", "instances": 38, "metric_value": 0.4855, "depth": 8}
								if obj[6] == 'Urban':
									# {"feature": "gender", "instances": 19, "metric_value": 0.6292, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "smoking_status", "instances": 11, "metric_value": 0.4395, "depth": 10}
										if obj[9] == 'never smoked':
											return '0'
										elif obj[9] == 'smokes':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										# {"feature": "smoking_status", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[9] == 'smokes':
											return '0'
										elif obj[9] == 'formerly smoked':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[6] == 'Rural':
									# {"feature": "gender", "instances": 19, "metric_value": 0.2975, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "smoking_status", "instances": 12, "metric_value": 0.4138, "depth": 10}
										if obj[9] == 'never smoked':
											return '0'
										elif obj[9] == 'Unknown':
											return '0'
										elif obj[9] == 'formerly smoked':
											return '0'
										elif obj[9] == 'smokes':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										return '0'
									else: return '0'
								else: return '0'
							else: return '0'
						elif obj[7]>238.60361450277637:
							# {"feature": "gender", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0] == 'Male':
								# {"feature": "work_type", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'Private':
									return '1'
								elif obj[5] == 'Self-employed':
									return '0'
								else: return '0'
							elif obj[0] == 'Female':
								return '0'
							else: return '0'
						else: return '0'
					elif obj[4] == 'No':
						return '0'
					else: return '0'
				else: return '0'
			elif obj[8]<=9.3:
				# {"feature": "hypertension", "instances": 117, "metric_value": 0.5033, "depth": 4}
				if obj[2]<=0:
					# {"feature": "ever_married", "instances": 96, "metric_value": 0.5721, "depth": 5}
					if obj[4] == 'Yes':
						# {"feature": "avg_glucose_level", "instances": 57, "metric_value": 0.7425, "depth": 6}
						if obj[7]>67.02:
							# {"feature": "smoking_status", "instances": 56, "metric_value": 0.7496, "depth": 7}
							if obj[9] == 'smokes':
								# {"feature": "Residence_type", "instances": 21, "metric_value": 0.2762, "depth": 8}
								if obj[6] == 'Urban':
									# {"feature": "gender", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "work_type", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										else: return '0'
									elif obj[0] == 'Female':
										return '0'
									else: return '0'
								elif obj[6] == 'Rural':
									return '0'
								else: return '0'
							elif obj[9] == 'Unknown':
								# {"feature": "work_type", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[5] == 'Private':
									# {"feature": "Residence_type", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[6] == 'Urban':
										# {"feature": "gender", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[0] == 'Male':
											return '0'
										elif obj[0] == 'Female':
											return '0'
										else: return '0'
									elif obj[6] == 'Rural':
										# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0] == 'Female':
											return '1'
										elif obj[0] == 'Male':
											return '1'
										else: return '1'
									else: return '1'
								elif obj[5] == 'Self-employed':
									return '0'
								elif obj[5] == 'Govt_job':
									return '0'
								else: return '0'
							elif obj[9] == 'formerly smoked':
								# {"feature": "work_type", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[5] == 'Private':
									# {"feature": "Residence_type", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[6] == 'Rural':
										# {"feature": "gender", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[0] == 'Male':
											return '0'
										elif obj[0] == 'Female':
											return '1'
										else: return '1'
									elif obj[6] == 'Urban':
										return '1'
									else: return '1'
								elif obj[5] == 'Self-employed':
									# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0] == 'Male':
										return '1'
									elif obj[0] == 'Female':
										return '0'
									else: return '0'
								elif obj[5] == 'Govt_job':
									return '0'
								else: return '0'
							elif obj[9] == 'never smoked':
								# {"feature": "gender", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[0] == 'Female':
									# {"feature": "Residence_type", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[6] == 'Rural':
										# {"feature": "work_type", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[5] == 'Self-employed':
											return '1'
										elif obj[5] == 'Govt_job':
											return '0'
										elif obj[5] == 'Private':
											return '0'
										else: return '0'
									elif obj[6] == 'Urban':
										# {"feature": "work_type", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										elif obj[5] == 'Govt_job':
											return '1'
										else: return '1'
									else: return '1'
								elif obj[0] == 'Male':
									return '0'
								else: return '0'
							else: return '0'
						elif obj[7]<=67.02:
							return '0'
						else: return '0'
					elif obj[4] == 'No':
						# {"feature": "Residence_type", "instances": 39, "metric_value": 0.172, "depth": 6}
						if obj[6] == 'Rural':
							return '0'
						elif obj[6] == 'Urban':
							# {"feature": "avg_glucose_level", "instances": 19, "metric_value": 0.2975, "depth": 7}
							if obj[7]>70.37:
								return '0'
							elif obj[7]<=70.37:
								# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0] == 'Female':
									return '1'
								elif obj[0] == 'Male':
									return '0'
								else: return '0'
							else: return '1'
						else: return '0'
					else: return '0'
				elif obj[2]>0:
					return '0'
				else: return '0'
			else: return '0'
		elif obj[3]>0:
			# {"feature": "smoking_status", "instances": 99, "metric_value": 0.561, "depth": 3}
			if obj[9] == 'never smoked':
				return '0'
			elif obj[9] == 'smokes':
				# {"feature": "bmi", "instances": 29, "metric_value": 0.7973, "depth": 4}
				if obj[8]<=35.434998220644175:
					# {"feature": "gender", "instances": 23, "metric_value": 0.4262, "depth": 5}
					if obj[0] == 'Male':
						# {"feature": "avg_glucose_level", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[7]<=225.35:
							# {"feature": "Residence_type", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[6] == 'Rural':
								# {"feature": "hypertension", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[2]<=0:
									# {"feature": "ever_married", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[4] == 'Yes':
										# {"feature": "work_type", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										else: return '0'
									elif obj[4] == 'No':
										return '0'
									else: return '0'
								elif obj[2]>0:
									return '0'
								else: return '0'
							elif obj[6] == 'Urban':
								return '0'
							else: return '0'
						elif obj[7]>225.35:
							return '1'
						else: return '1'
					elif obj[0] == 'Female':
						return '0'
					else: return '0'
				elif obj[8]>35.434998220644175:
					# {"feature": "avg_glucose_level", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[7]>68.09:
						return '1'
					elif obj[7]<=68.09:
						return '0'
					else: return '0'
				else: return '1'
			elif obj[9] == 'formerly smoked':
				# {"feature": "bmi", "instances": 27, "metric_value": 0.3809, "depth": 4}
				if obj[8]<=33.0:
					return '0'
				elif obj[8]>33.0:
					# {"feature": "gender", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[0] == 'Male':
						# {"feature": "avg_glucose_level", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=150.45:
							# {"feature": "hypertension", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Residence_type", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6] == 'Rural':
									return '0'
								elif obj[6] == 'Urban':
									return '1'
								else: return '1'
							elif obj[2]>0:
								return '0'
							else: return '0'
						elif obj[7]>150.45:
							return '1'
						else: return '1'
					elif obj[0] == 'Female':
						return '0'
					else: return '0'
				else: return '0'
			elif obj[9] == 'Unknown':
				# {"feature": "avg_glucose_level", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=199.38:
					# {"feature": "bmi", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[8]>28.8:
						return '0'
					elif obj[8]<=28.8:
						# {"feature": "work_type", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5] == 'Govt_job':
							return '1'
						elif obj[5] == 'Private':
							return '0'
						else: return '0'
					else: return '1'
				elif obj[7]>199.38:
					return '1'
				else: return '1'
			else: return '0'
		else: return '0'
	elif obj[1]>65.83704850852197:
		# {"feature": "bmi", "instances": 965, "metric_value": 0.6383, "depth": 2}
		if obj[8]>9.3:
			# {"feature": "avg_glucose_level", "instances": 893, "metric_value": 0.6015, "depth": 3}
			if obj[7]>55.23:
				# {"feature": "hypertension", "instances": 892, "metric_value": 0.6019, "depth": 4}
				if obj[2]<=0:
					# {"feature": "heart_disease", "instances": 692, "metric_value": 0.5456, "depth": 5}
					if obj[3]<=0:
						# {"feature": "work_type", "instances": 577, "metric_value": 0.5181, "depth": 6}
						if obj[5] == 'Private':
							# {"feature": "smoking_status", "instances": 283, "metric_value": 0.5785, "depth": 7}
							if obj[9] == 'never smoked':
								# {"feature": "ever_married", "instances": 103, "metric_value": 0.5735, "depth": 8}
								if obj[4] == 'Yes':
									# {"feature": "Residence_type", "instances": 94, "metric_value": 0.551, "depth": 9}
									if obj[6] == 'Urban':
										# {"feature": "gender", "instances": 51, "metric_value": 0.4627, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[6] == 'Rural':
										# {"feature": "gender", "instances": 43, "metric_value": 0.6409, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[4] == 'No':
									# {"feature": "gender", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '1'
										else: return '1'
									elif obj[0] == 'Male':
										return '0'
									else: return '0'
								else: return '0'
							elif obj[9] == 'formerly smoked':
								# {"feature": "ever_married", "instances": 85, "metric_value": 0.5558, "depth": 8}
								if obj[4] == 'Yes':
									# {"feature": "gender", "instances": 82, "metric_value": 0.5687, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "Residence_type", "instances": 50, "metric_value": 0.6343, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									elif obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 32, "metric_value": 0.4489, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[4] == 'No':
									return '0'
								else: return '0'
							elif obj[9] == 'Unknown':
								# {"feature": "ever_married", "instances": 62, "metric_value": 0.6374, "depth": 8}
								if obj[4] == 'Yes':
									# {"feature": "Residence_type", "instances": 59, "metric_value": 0.6565, "depth": 9}
									if obj[6] == 'Rural':
										# {"feature": "gender", "instances": 30, "metric_value": 0.5665, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[6] == 'Urban':
										# {"feature": "gender", "instances": 29, "metric_value": 0.7355, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[4] == 'No':
									return '0'
								else: return '0'
							elif obj[9] == 'smokes':
								# {"feature": "ever_married", "instances": 33, "metric_value": 0.5328, "depth": 8}
								if obj[4] == 'Yes':
									# {"feature": "Residence_type", "instances": 31, "metric_value": 0.5548, "depth": 9}
									if obj[6] == 'Urban':
										# {"feature": "gender", "instances": 20, "metric_value": 0.469, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[6] == 'Rural':
										# {"feature": "gender", "instances": 11, "metric_value": 0.684, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[4] == 'No':
									return '0'
								else: return '0'
							else: return '0'
						elif obj[5] == 'Self-employed':
							# {"feature": "smoking_status", "instances": 210, "metric_value": 0.4537, "depth": 7}
							if obj[9] == 'never smoked':
								# {"feature": "gender", "instances": 95, "metric_value": 0.5759, "depth": 8}
								if obj[0] == 'Female':
									# {"feature": "ever_married", "instances": 74, "metric_value": 0.4942, "depth": 9}
									if obj[4] == 'Yes':
										# {"feature": "Residence_type", "instances": 66, "metric_value": 0.5328, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									elif obj[4] == 'No':
										return '0'
									else: return '0'
								elif obj[0] == 'Male':
									# {"feature": "ever_married", "instances": 21, "metric_value": 0.7919, "depth": 9}
									if obj[4] == 'Yes':
										# {"feature": "Residence_type", "instances": 19, "metric_value": 0.7425, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									elif obj[4] == 'No':
										# {"feature": "Residence_type", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Urban':
											return '1'
										else: return '1'
									else: return '1'
								else: return '0'
							elif obj[9] == 'formerly smoked':
								# {"feature": "ever_married", "instances": 63, "metric_value": 0.3999, "depth": 8}
								if obj[4] == 'Yes':
									# {"feature": "Residence_type", "instances": 57, "metric_value": 0.4288, "depth": 9}
									if obj[6] == 'Urban':
										# {"feature": "gender", "instances": 30, "metric_value": 0.3534, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[6] == 'Rural':
										# {"feature": "gender", "instances": 27, "metric_value": 0.5033, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[4] == 'No':
									return '0'
								else: return '0'
							elif obj[9] == 'Unknown':
								# {"feature": "gender", "instances": 33, "metric_value": 0.1959, "depth": 8}
								if obj[0] == 'Female':
									return '0'
								elif obj[0] == 'Male':
									# {"feature": "Residence_type", "instances": 12, "metric_value": 0.4138, "depth": 9}
									if obj[6] == 'Urban':
										# {"feature": "ever_married", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[4] == 'Yes':
											return '0'
										elif obj[4] == 'No':
											return '0'
										else: return '0'
									elif obj[6] == 'Rural':
										return '0'
									else: return '0'
								else: return '0'
							elif obj[9] == 'smokes':
								# {"feature": "Residence_type", "instances": 19, "metric_value": 0.2975, "depth": 8}
								if obj[6] == 'Urban':
									# {"feature": "gender", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "ever_married", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[4] == 'Yes':
											return '0'
										elif obj[4] == 'No':
											return '0'
										else: return '0'
									elif obj[0] == 'Female':
										return '0'
									else: return '0'
								elif obj[6] == 'Rural':
									return '0'
								else: return '0'
							else: return '0'
						elif obj[5] == 'Govt_job':
							# {"feature": "ever_married", "instances": 84, "metric_value": 0.4537, "depth": 7}
							if obj[4] == 'Yes':
								# {"feature": "smoking_status", "instances": 77, "metric_value": 0.3948, "depth": 8}
								if obj[9] == 'never smoked':
									# {"feature": "gender", "instances": 32, "metric_value": 0.5436, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 23, "metric_value": 0.6666, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										return '0'
									else: return '0'
								elif obj[9] == 'formerly smoked':
									# {"feature": "Residence_type", "instances": 20, "metric_value": 0.2864, "depth": 9}
									if obj[6] == 'Rural':
										return '0'
									elif obj[6] == 'Urban':
										# {"feature": "gender", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[0] == 'Male':
											return '0'
										elif obj[0] == 'Female':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[9] == 'Unknown':
									return '0'
								elif obj[9] == 'smokes':
									# {"feature": "Residence_type", "instances": 10, "metric_value": 0.469, "depth": 9}
									if obj[6] == 'Rural':
										# {"feature": "gender", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[6] == 'Urban':
										return '0'
									else: return '0'
								else: return '0'
							elif obj[4] == 'No':
								# {"feature": "Residence_type", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[6] == 'Urban':
									# {"feature": "smoking_status", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[9] == 'smokes':
										# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0] == 'Female':
											return '1'
										else: return '1'
									elif obj[9] == 'Unknown':
										return '1'
									elif obj[9] == 'formerly smoked':
										return '0'
									else: return '0'
								elif obj[6] == 'Rural':
									return '0'
								else: return '0'
							else: return '0'
						else: return '0'
					elif obj[3]>0:
						# {"feature": "work_type", "instances": 115, "metric_value": 0.6666, "depth": 6}
						if obj[5] == 'Private':
							# {"feature": "smoking_status", "instances": 60, "metric_value": 0.7838, "depth": 7}
							if obj[9] == 'never smoked':
								# {"feature": "ever_married", "instances": 26, "metric_value": 0.7793, "depth": 8}
								if obj[4] == 'Yes':
									# {"feature": "gender", "instances": 24, "metric_value": 0.8113, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 14, "metric_value": 0.9403, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										# {"feature": "Residence_type", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[4] == 'No':
									return '0'
								else: return '0'
							elif obj[9] == 'formerly smoked':
								# {"feature": "ever_married", "instances": 19, "metric_value": 0.7425, "depth": 8}
								if obj[4] == 'Yes':
									# {"feature": "gender", "instances": 18, "metric_value": 0.7642, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "Residence_type", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									elif obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[4] == 'No':
									return '0'
								else: return '0'
							elif obj[9] == 'smokes':
								# {"feature": "Residence_type", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[6] == 'Urban':
									# {"feature": "gender", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "ever_married", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4] == 'Yes':
											return '1'
										else: return '1'
									elif obj[0] == 'Female':
										# {"feature": "ever_married", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4] == 'No':
											return '1'
										else: return '1'
									else: return '1'
								elif obj[6] == 'Rural':
									return '0'
								else: return '0'
							elif obj[9] == 'Unknown':
								# {"feature": "gender", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[0] == 'Male':
									# {"feature": "Residence_type", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[6] == 'Rural':
										# {"feature": "ever_married", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4] == 'Yes':
											return '0'
										else: return '0'
									elif obj[6] == 'Urban':
										return '0'
									else: return '0'
								elif obj[0] == 'Female':
									return '0'
								else: return '0'
							else: return '0'
						elif obj[5] == 'Self-employed':
							# {"feature": "ever_married", "instances": 45, "metric_value": 0.4328, "depth": 7}
							if obj[4] == 'Yes':
								# {"feature": "smoking_status", "instances": 41, "metric_value": 0.4612, "depth": 8}
								if obj[9] == 'Unknown':
									# {"feature": "gender", "instances": 14, "metric_value": 0.3712, "depth": 9}
									if obj[0] == 'Male':
										return '0'
									elif obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[6] == 'Rural':
											return '0'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[9] == 'formerly smoked':
									# {"feature": "gender", "instances": 12, "metric_value": 0.65, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "Residence_type", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									elif obj[0] == 'Female':
										# {"feature": "Residence_type", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Rural':
											return '1'
										elif obj[6] == 'Urban':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[9] == 'smokes':
									# {"feature": "gender", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "Residence_type", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[6] == 'Urban':
											return '0'
										elif obj[6] == 'Rural':
											return '0'
										else: return '0'
									elif obj[0] == 'Female':
										return '0'
									else: return '0'
								elif obj[9] == 'never smoked':
									return '0'
								else: return '0'
							elif obj[4] == 'No':
								return '0'
							else: return '0'
						elif obj[5] == 'Govt_job':
							# {"feature": "gender", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[0] == 'Male':
								# {"feature": "smoking_status", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[9] == 'never smoked':
									# {"feature": "ever_married", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[4] == 'Yes':
										# {"feature": "Residence_type", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Rural':
											return '1'
										else: return '1'
									elif obj[4] == 'No':
										return '0'
									else: return '0'
								elif obj[9] == 'formerly smoked':
									return '0'
								else: return '0'
							elif obj[0] == 'Female':
								return '0'
							else: return '0'
						else: return '0'
					else: return '0'
				elif obj[2]>0:
					# {"feature": "ever_married", "instances": 200, "metric_value": 0.7602, "depth": 5}
					if obj[4] == 'Yes':
						# {"feature": "Residence_type", "instances": 181, "metric_value": 0.6969, "depth": 6}
						if obj[6] == 'Rural':
							# {"feature": "heart_disease", "instances": 93, "metric_value": 0.751, "depth": 7}
							if obj[3]<=0:
								# {"feature": "smoking_status", "instances": 74, "metric_value": 0.8004, "depth": 8}
								if obj[9] == 'never smoked':
									# {"feature": "gender", "instances": 44, "metric_value": 0.7309, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "work_type", "instances": 27, "metric_value": 0.8256, "depth": 10}
										if obj[5] == 'Self-employed':
											return '0'
										elif obj[5] == 'Private':
											return '0'
										elif obj[5] == 'Govt_job':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										# {"feature": "work_type", "instances": 17, "metric_value": 0.5226, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										elif obj[5] == 'Self-employed':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[9] == 'formerly smoked':
									# {"feature": "gender", "instances": 20, "metric_value": 0.9341, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "work_type", "instances": 13, "metric_value": 0.8905, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										elif obj[5] == 'Govt_job':
											return '0'
										elif obj[5] == 'Self-employed':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										# {"feature": "work_type", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[5] == 'Self-employed':
											return '0'
										elif obj[5] == 'Private':
											return '1'
										else: return '1'
									else: return '0'
								elif obj[9] == 'smokes':
									# {"feature": "work_type", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[5] == 'Private':
										return '0'
									elif obj[5] == 'Self-employed':
										# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0] == 'Female':
											return '1'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									else: return '1'
								elif obj[9] == 'Unknown':
									# {"feature": "gender", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[0] == 'Female':
										return '0'
									elif obj[0] == 'Male':
										# {"feature": "work_type", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'Self-employed':
											return '1'
										else: return '1'
									else: return '1'
								else: return '0'
							elif obj[3]>0:
								# {"feature": "gender", "instances": 19, "metric_value": 0.4855, "depth": 8}
								if obj[0] == 'Male':
									# {"feature": "work_type", "instances": 13, "metric_value": 0.6194, "depth": 9}
									if obj[5] == 'Private':
										# {"feature": "smoking_status", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[9] == 'never smoked':
											return '0'
										elif obj[9] == 'smokes':
											return '1'
										elif obj[9] == 'Unknown':
											return '0'
										elif obj[9] == 'formerly smoked':
											return '0'
										else: return '0'
									elif obj[5] == 'Self-employed':
										return '0'
									elif obj[5] == 'Govt_job':
										return '0'
									else: return '0'
								elif obj[0] == 'Female':
									return '0'
								else: return '0'
							else: return '0'
						elif obj[6] == 'Urban':
							# {"feature": "heart_disease", "instances": 88, "metric_value": 0.6321, "depth": 7}
							if obj[3]<=0:
								# {"feature": "work_type", "instances": 71, "metric_value": 0.5864, "depth": 8}
								if obj[5] == 'Private':
									# {"feature": "smoking_status", "instances": 33, "metric_value": 0.5328, "depth": 9}
									if obj[9] == 'never smoked':
										# {"feature": "gender", "instances": 16, "metric_value": 0.6962, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '0'
										else: return '0'
									elif obj[9] == 'formerly smoked':
										return '0'
									elif obj[9] == 'smokes':
										# {"feature": "gender", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[0] == 'Female':
											return '0'
										elif obj[0] == 'Male':
											return '1'
										else: return '1'
									elif obj[9] == 'Unknown':
										return '0'
									else: return '0'
								elif obj[5] == 'Self-employed':
									# {"feature": "gender", "instances": 30, "metric_value": 0.7219, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "smoking_status", "instances": 20, "metric_value": 0.8113, "depth": 10}
										if obj[9] == 'never smoked':
											return '0'
										elif obj[9] == 'formerly smoked':
											return '0'
										elif obj[9] == 'Unknown':
											return '0'
										else: return '0'
									elif obj[0] == 'Male':
										# {"feature": "smoking_status", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[9] == 'formerly smoked':
											return '0'
										elif obj[9] == 'never smoked':
											return '1'
										elif obj[9] == 'smokes':
											return '0'
										elif obj[9] == 'Unknown':
											return '0'
										else: return '0'
									else: return '0'
								elif obj[5] == 'Govt_job':
									return '0'
								else: return '0'
							elif obj[3]>0:
								# {"feature": "work_type", "instances": 17, "metric_value": 0.7871, "depth": 8}
								if obj[5] == 'Private':
									# {"feature": "smoking_status", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[9] == 'formerly smoked':
										# {"feature": "gender", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[0] == 'Male':
											return '0'
										elif obj[0] == 'Female':
											return '0'
										else: return '0'
									elif obj[9] == 'never smoked':
										return '0'
									elif obj[9] == 'smokes':
										return '1'
									else: return '1'
								elif obj[5] == 'Self-employed':
									return '0'
								elif obj[5] == 'Govt_job':
									# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "smoking_status", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9] == 'formerly smoked':
											return '1'
										else: return '1'
									else: return '1'
								else: return '1'
							else: return '0'
						else: return '0'
					elif obj[4] == 'No':
						# {"feature": "smoking_status", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[9] == 'never smoked':
							# {"feature": "Residence_type", "instances": 13, "metric_value": 0.9612, "depth": 7}
							if obj[6] == 'Urban':
								# {"feature": "gender", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[0] == 'Female':
									return '1'
								elif obj[0] == 'Male':
									# {"feature": "work_type", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5] == 'Private':
										# {"feature": "heart_disease", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]<=0:
											return '1'
										else: return '1'
									elif obj[5] == 'Govt_job':
										return '0'
									else: return '0'
								else: return '0'
							elif obj[6] == 'Rural':
								# {"feature": "gender", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0] == 'Male':
									# {"feature": "heart_disease", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>0:
										# {"feature": "work_type", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'Govt_job':
											return '1'
										elif obj[5] == 'Private':
											return '0'
										else: return '0'
									elif obj[3]<=0:
										return '1'
									else: return '1'
								elif obj[0] == 'Female':
									return '0'
								else: return '0'
							else: return '0'
						elif obj[9] == 'formerly smoked':
							# {"feature": "work_type", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5] == 'Self-employed':
								return '0'
							elif obj[5] == 'Private':
								return '1'
							elif obj[5] == 'Govt_job':
								return '1'
							else: return '1'
						elif obj[9] == 'smokes':
							return '0'
						elif obj[9] == 'Unknown':
							return '0'
						else: return '0'
					else: return '1'
				else: return '0'
			elif obj[7]<=55.23:
				return '0'
			else: return '0'
		elif obj[8]<=9.3:
			# {"feature": "avg_glucose_level", "instances": 72, "metric_value": 0.9316, "depth": 3}
			if obj[7]>57.92:
				# {"feature": "ever_married", "instances": 71, "metric_value": 0.9229, "depth": 4}
				if obj[4] == 'Yes':
					# {"feature": "smoking_status", "instances": 65, "metric_value": 0.8905, "depth": 5}
					if obj[9] == 'Unknown':
						# {"feature": "heart_disease", "instances": 21, "metric_value": 0.9852, "depth": 6}
						if obj[3]<=0:
							# {"feature": "hypertension", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Residence_type", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[6] == 'Urban':
									# {"feature": "work_type", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[5] == 'Private':
										# {"feature": "gender", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[0] == 'Male':
											return '1'
										elif obj[0] == 'Female':
											return '1'
										else: return '1'
									elif obj[5] == 'Govt_job':
										# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0] == 'Female':
											return '1'
										else: return '1'
									elif obj[5] == 'Self-employed':
										return '1'
									else: return '1'
								elif obj[6] == 'Rural':
									return '1'
								else: return '1'
							elif obj[2]>0:
								# {"feature": "work_type", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[5] == 'Self-employed':
									# {"feature": "Residence_type", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6] == 'Rural':
										# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0] == 'Male':
											return '1'
										else: return '1'
									elif obj[6] == 'Urban':
										return '0'
									else: return '0'
								elif obj[5] == 'Private':
									return '0'
								else: return '0'
							else: return '0'
						elif obj[3]>0:
							# {"feature": "Residence_type", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[6] == 'Rural':
								return '0'
							elif obj[6] == 'Urban':
								# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0] == 'Male':
									# {"feature": "hypertension", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2]<=0:
										# {"feature": "work_type", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							else: return '0'
						else: return '0'
					elif obj[9] == 'never smoked':
						# {"feature": "gender", "instances": 16, "metric_value": 0.5436, "depth": 6}
						if obj[0] == 'Female':
							return '0'
						elif obj[0] == 'Male':
							# {"feature": "heart_disease", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Residence_type", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6] == 'Rural':
									# {"feature": "hypertension", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2]>0:
										# {"feature": "work_type", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'Private':
											return '1'
										elif obj[5] == 'Self-employed':
											return '0'
										else: return '0'
									elif obj[2]<=0:
										return '1'
									else: return '1'
								elif obj[6] == 'Urban':
									return '0'
								else: return '0'
							elif obj[3]>0:
								return '0'
							else: return '0'
						else: return '0'
					elif obj[9] == 'formerly smoked':
						# {"feature": "heart_disease", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Residence_type", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[6] == 'Urban':
								# {"feature": "hypertension", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[2]<=0:
									# {"feature": "gender", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "work_type", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[5] == 'Private':
											return '0'
										elif obj[5] == 'Self-employed':
											return '0'
										elif obj[5] == 'Govt_job':
											return '0'
										else: return '0'
									elif obj[0] == 'Female':
										# {"feature": "work_type", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'Self-employed':
											return '1'
										else: return '1'
									else: return '1'
								elif obj[2]>0:
									# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0] == 'Male':
										return '1'
									elif obj[0] == 'Female':
										return '0'
									else: return '0'
								else: return '1'
							elif obj[6] == 'Rural':
								# {"feature": "work_type", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[5] == 'Self-employed':
									# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "hypertension", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2]<=0:
											return '1'
										else: return '1'
									else: return '1'
								elif obj[5] == 'Govt_job':
									return '1'
								elif obj[5] == 'Private':
									return '1'
								else: return '1'
							else: return '1'
						elif obj[3]>0:
							return '0'
						else: return '0'
					elif obj[9] == 'smokes':
						# {"feature": "heart_disease", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[3]<=0:
							return '0'
						elif obj[3]>0:
							# {"feature": "hypertension", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=0:
								# {"feature": "work_type", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5] == 'Self-employed':
									return '0'
								elif obj[5] == 'Private':
									# {"feature": "Residence_type", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6] == 'Urban':
										return '1'
									elif obj[6] == 'Rural':
										return '0'
									else: return '0'
								else: return '1'
							elif obj[2]>0:
								return '1'
							else: return '1'
						else: return '0'
					else: return '0'
				elif obj[4] == 'No':
					# {"feature": "smoking_status", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[9] == 'Unknown':
						return '1'
					elif obj[9] == 'never smoked':
						# {"feature": "hypertension", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>0:
							return '1'
						elif obj[2]<=0:
							return '0'
						else: return '0'
					elif obj[9] == 'smokes':
						return '0'
					else: return '0'
				else: return '1'
			elif obj[7]<=57.92:
				return '1'
			else: return '1'
		else: return '0'
	else: return '0'
