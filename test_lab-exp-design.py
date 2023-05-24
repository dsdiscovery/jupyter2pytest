def zdERksQJviOnLbgMdvRB(eowMLKmIashYwHditgHn):
	import pandas as pd 
	df = pd.read_csv("https://waf.cs.illinois.edu/discovery/hello-sp23.csv")
	df.columns.tolist()
	# Student answers will depend on their group's binary question. 
	# If they did not have a group, they can pick any binary question. 

	analysis_column =  'Are you a morning person?'
	analysis_column
	if eowMLKmIashYwHditgHn == "_1_0":
		## == CHECKPOINT TEST CASE ==
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any error our output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cell, make changes, and RE-RUN your code and then this cell.
		assert( 'df' in vars() ), "You do not have a DataFrame called `df`."
		assert( len(df) <= 385 and len(df) >= 365), "You have not loaded the correct Hello dataset"
		assert( analysis_column in df ), "Make certain your analysis_column string is EXACTLY as it appears in the Hello Dataset."

		## == SUCCESS MESSAGE ==
		# You will only see this message (with the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	df1 = df [ df[analysis_column] == 'Yes' ]
	df1
	df2 = df [ df[analysis_column] == "No" ] 
	df2
	if eowMLKmIashYwHditgHn == "_1_1":

		return
	treatment = df.sample(frac=0.5)
	treatment
	control = df.sample(frac=0.5)
	control
	if eowMLKmIashYwHditgHn == "_2":
		## == CHECKPOINT TEST CASE ==
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any error our output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cell, make changes, and RE-RUN your code and then this cell.
		assert( 'df' in vars() ), "You do not have a DataFrame called `df`."
		assert( 'treatment' in vars() ), "You do not have a DataFrame called `treatment`."
		assert( 'control' in vars() ), "You do not have a DataFrame called `control`."
		assert( len(treatment) == len(control) ), "The `treatment` and `control` groups must be the same size."
		assert( abs((len(df) / 2) - len(treatment)) <= 1 ), "The `treatment` group size must be 50% of the `df`"
		assert( abs((len(df) / 2) - len(control)) <= 1 ), "The `control` group size must be 50% of the `df`"


		## == SUCCESS MESSAGE ==
		# You will only see this message (with the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	control = df [ ~df.index.isin(treatment.index) ]
	control
	if eowMLKmIashYwHditgHn == "_2_3":
		## == CHECKPOINT TEST CASE ==
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any error our output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cell, make changes, and RE-RUN your code and then this cell.
		assert( 'df' in vars() ), "You do not have a DataFrame called `df`."
		assert( 'treatment' in vars() ), "You do not have a DataFrame called `treatment`."
		assert( 'control' in vars() ), "You do not have a DataFrame called `control`."
		assert( abs((len(df) / 2) - len(treatment)) <= 1 ), "The `treatment` group size must be 50% of the `df`"
		assert( abs((len(df) / 2) - len(control)) <= 1 ), "The `control` group size must be 50% of the `df`"
		assert( len(df[ df.index.isin(treatment.index) & df.index.isin(control.index) ]) == 0), "The `treatment` and `control` groups have some overlap!  There must be no overlap."

		## == SUCCESS MESSAGE ==
		# You will only see this message (with the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	df1_treatment = df1.sample(frac=0.5)
	df1_treatment
	# This code can be tricky - double or triple check DataFrame references if students are encountering issues!
	df1_control = df1 [ ~df1.index.isin(df1_treatment.index) ]
	df1_control
	if eowMLKmIashYwHditgHn == "_3_1":
		## == CHECKPOINT TEST CASE ==
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any error our output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cell, make changes, and RE-RUN your code and then this cell.
		assert( 'df1_treatment' in vars() ), "You do not have a DataFrame called `df1_treatment`."
		assert( 'df1_control' in vars() ), "You do not have a DataFrame called `df1_control`."
		assert( len(df[ df.index.isin(df1_treatment.index) & df.index.isin(df1_control.index) ]) == 0), "The `df1_treatment` and `df1_control` groups have some overlap!  There must be no overlap."
		assert( len(df[ df.index.isin(df1_treatment.index) & df.index.isin(df2.index) ]) == 0), "The `df1_treatment` and `df2` groups have some overlap!  There must be no overlap."
		assert( len(df[ df.index.isin(df1_control.index) & df.index.isin(df2.index) ]) == 0), "The `df1_control` and `df2` groups have some overlap!  There must be no overlap."

		## == SUCCESS MESSAGE ==
		# You will only see this message (with the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	df2_treatment = df2.sample(frac=0.5)
	df2_treatment
	df2_control = df2 [ ~df2.index.isin(df2_treatment.index) ]
	df2_control
	if eowMLKmIashYwHditgHn == "_3_2":
		## == CHECKPOINT TEST CASE ==
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any error our output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cell, make changes, and RE-RUN your code and then this cell.
		assert( 'df2_treatment' in vars() ), "You do not have a DataFrame called `df2_treatment`."
		assert( 'df2_control' in vars() ), "You do not have a DataFrame called `df2_control`."
		assert( len(df[ df.index.isin(df2_treatment.index) & df.index.isin(df2_control.index) ]) == 0), "The `df2_treatment` and `df2_control` groups have some overlap!  There must be no overlap."
		assert( len(df[ df.index.isin(df2_treatment.index) & df.index.isin(df1.index) ]) == 0), "The `df2_treatment` and `df1` groups have some overlap!  There must be no overlap."
		assert( len(df[ df.index.isin(df2_control.index) & df.index.isin(df1.index) ]) == 0), "The `df2_control` and `df1` groups have some overlap!  There must be no overlap."


		## == SUCCESS MESSAGE ==
		# You will only see this message (with the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	treatment = pd.concat([df1_treatment, df2_treatment])
	treatment
	control = pd.concat([df1_control, df2_control])
	control
	if eowMLKmIashYwHditgHn == "_3_3":
		## == CHECKPOINT TEST CASE ==
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any error our output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cell, make changes, and RE-RUN your code and then this cell.
		assert( len(df[ df.index.isin(treatment.index) & df.index.isin(control.index) ]) == 0), "The `treatment` and `control` groups have some overlap!  There must be no overlap."

		## == SUCCESS MESSAGE ==
		# You will only see this message (with the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return

def test__1_0():
	zdERksQJviOnLbgMdvRB("_1_0")

def test__2():
	zdERksQJviOnLbgMdvRB("_2")

def test__2_3():
	zdERksQJviOnLbgMdvRB("_2_3")

def test__3_1():
	zdERksQJviOnLbgMdvRB("_3_1")

def test__3_2():
	zdERksQJviOnLbgMdvRB("_3_2")

def test__3_3():
	zdERksQJviOnLbgMdvRB("_3_3")

