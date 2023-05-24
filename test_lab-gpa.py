def vEPJAmYeGzRFUsqwPIuQ(LxoCTNVkBMhwIxGSHCDZ):
	import pandas as pd
	df = pd.read_csv('https://waf.cs.illinois.edu/discovery/gpa.csv')
	df
	if LxoCTNVkBMhwIxGSHCDZ == "_1_0":
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any errors, you PASSED all test cases!
		# - If this cell results in any errors, check your previous cell, make changes, and RE-RUN your code and then this cell.
		assert(len(df) == 64048 ), "This is not the GPA dataset you're looking for"

		## == SUCCESS MESSAGE ==
		# You will only see this message (with the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	### SOLUTION 

	# Option A - Manually
	df['Average GPA'] = (df['A+'] * 4 + df['A'] * 4 + df['A-'] * 3.67 
	                    + df['B+'] * 3.33 + df['B'] * 3 + df['B-'] * 2.67 
	                    + df['C+'] * 2.33 + df['C'] * 2 + df['C-'] * 1.67 
	                    + df['D+'] * 1.33 + df['D'] * 1 + df['D-'] * 0.67 + df['F'] * 0) / df['Students']

	# Option B - Dot Product 

	# When we compute dot product, ensure both these lists are of equal length
	grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
	weights = [4, 4, 3.67, 3.33, 3, 2.67, 2.33, 2, 1.67, 1.33, 1, 0.67, 0]
	df["Average GPA"] =  df[grades].dot(weights) /df["Students"]

	df
	if LxoCTNVkBMhwIxGSHCDZ == "_1_1":

		return
	df_hard = df.nsmallest(50, "Average GPA")
	df_hard
	df_easy = df.nlargest(50, 'Average GPA')
	df_easy
	hard_avg = df_hard['Number'].mean()
	hard_avg
	easy_avg = df_easy['Number'].mean()
	easy_avg
	if LxoCTNVkBMhwIxGSHCDZ == "_1_2":
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any error or output, you PASSED all test cases!
		# - If this cell results in any errors, check your previous cell(s), make changes, and RE-RUN your code and then this cell.
		import math
		assert( len(df_hard) == len(df_easy) == 50 ), "Your df_hard and df_easy should be picking the 50 courses with the lowest / highest average GPA respectively. Please double check that you are selecting 50 courses."
		assert( math.isclose(df_hard['Average GPA'].sum(), 80.30481775738464) ), "Your df_hard is calculated incorrectly. Make sure you are finding the 50 courses with the lowest Average GPA."
		assert( math.isclose(df_easy['Average GPA'].sum(), 199.34775533302954) ), "Your df_easy is calculated incorrectly. Make sure you are finding the 50 courses with the highest Average GPA."
		assert( math.isclose(hard_avg, 166.42) ), "Your calculation for the average course Number of 'hard' courses is incorrect. Make sure you are finding the mean of course numbers of df_hard."
		assert( math.isclose(easy_avg, 372.62) ), "Your calculation for the average course Number of 'easy' courses is incorrect. Make sure you are finding the mean of coure numbers of df_easy."

		## == SUCCESS MESSAGE ==
		# You'll only see this message (With the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	df_subject = df.groupby('Subject').agg('sum').reset_index() 
	df_subject
	if LxoCTNVkBMhwIxGSHCDZ == "_2_1":
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any error or output, you PASSED all test cases!
		# - If this cell results in any errors, check your previous cell(s), make changes, and RE-RUN your code and then this cell.
		import math
		assert( 'df_subject' in vars() ), "Make sure your DataFrame grouped by Subject is named 'df_subject'." 
		assert( len(df_subject) == 170 ), "Make sure you are grouping by 'Subject'. There are 170 Subjects in our original `df`, so the length of `df_subject` should be 170."
		assert( math.isclose(df_subject.Students.mean(), 22003.170588235294) ), "Double-check that you are aggregating your df_subject correctly. "

		## == SUCCESS MESSAGE ==
		# You'll only see this message (With the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	### SOLUTION 

	# Option A - Manually
	df_subject['Average GPA'] = (df_subject['A+'] * 4 + df_subject['A'] * 4 + df_subject['A-'] * 3.67 
	                    + df_subject['B+'] * 3.33 + df_subject['B'] * 3 + df_subject['B-'] * 2.67 
	                    + df_subject['C+'] * 2.33 + df_subject['C'] * 2 + df_subject['C-'] * 1.67 
	                    + df_subject['D+'] * 1.33 + df_subject['D'] * 1 + df_subject['D-'] * 0.67 + df_subject['F'] * 0) / df_subject['Students']

	# Option B - Dot Product 
	# Note you don't have to necessarily redefine the `grades` and `weights` lists if student used .dot() product method for Puzzle 1.1

	grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
	weights = [4, 4, 3.67, 3.33, 3, 2.67, 2.33, 2, 1.67, 1.33, 1, 0.67, 0]
	df_subject['Average GPA'] =  df_subject[grades].dot(weights) /df_subject['Students']

	df_subject
	if LxoCTNVkBMhwIxGSHCDZ == "_2_2":

		return
	hard_subjects = df_subject.nsmallest(10, 'Average GPA')
	hard_subjects
	easy_subjects = df_subject.nlargest(10, 'Average GPA')
	easy_subjects
	if LxoCTNVkBMhwIxGSHCDZ == "_2_3":

		return
	df_subject['Average GPA'].hist()
	if LxoCTNVkBMhwIxGSHCDZ == "_2_4":

		return
	my_subject = df_subject[df_subject['Subject'] == 'IS']
	my_subject
	if LxoCTNVkBMhwIxGSHCDZ == "_2_5":

		return
	df_year = df.groupby('Year').agg('sum').reset_index()
	df_year
	if LxoCTNVkBMhwIxGSHCDZ == "_3_1":
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any errors, you PASSED all test cases!
		# - If this cell results in any errors, check your previous cell, make changes, and RE-RUN your code and then this cell.
		import math
		assert( 'df_year' in vars() ), "Make sure your DataFrame grouped by Year is named 'df_year'." 
		assert( len(df_year) == 13 ), "Make sure you are grouping by 'Year'. There are 13 years in our original `df`, so the length of `df_years` should be 13."
		assert( math.isclose(df_year.Students.mean(), 287733.76923076925) ), "Double-check that you are aggregating your df_year correctly. "

		## == SUCCESS MESSAGE ==
		# You will only see this message (with the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	### SOLUTION

	## Option A - Manually
	df_year['Average GPA'] = (df_year['A+'] * 4 + df_year['A'] * 4 + df_year['A-'] * 3.67 
	                    + df_year['B+'] * 3.33 + df_year['B'] * 3 + df_year['B-'] * 2.67 
	                    + df_year['C+'] * 2.33 + df_year['C'] * 2 + df_year['C-'] * 1.67 
	                    + df_year['D+'] * 1.33 + df_year['D'] * 1 + df_year['D-'] * 0.67 + df_year['F'] * 0) / df_year['Students']

	## Option B - Dot Product 
	# Note you don't have to necessarily redefine the `grades` and `weights` lists if student used .dot() product method for Puzzles 1.1 or 2.1

	grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
	weights = [4, 4, 3.67, 3.33, 3, 2.67, 2.33, 2, 1.67, 1.33, 1, 0.67, 0]
	df_year["Average GPA"] =  df_year[grades].dot(weights) /df_year["Students"]


	df_year
	if LxoCTNVkBMhwIxGSHCDZ == "_3_2":
		# - This read-only cell contains test cases for your previous cell.
		# - If this cell runs without any errors, you PASSED all test cases!
		# - If this cell results in any errors, check your previous cell, make changes, and RE-RUN your code and then this cell.
		import math
		assert( len(df_year) == 13 ), "You shouldn't be changing the length of `df_year` when recomputing Average GPA"
		assert( "Average GPA" in df_year.columns), "Make sure your column is still named 'Average GPA'."
		assert( len(df_year.columns) == 24), "Don't add any new columns to df_year when recalculating the 'Average GPA' column."
		assert( math.isclose(df_year['Average GPA'].mean(), 3.3129267514166796) ), "Your calculation of the Average GPA by Year is incorrect."

		## == SUCCESS MESSAGE ==
		# You will only see this message (with the emoji showing) if you passed all test cases:
		tada = "\N{PARTY POPPER}"
		print(f"{tada} All tests passed! {tada}")
		return
	df_year.plot.line(x='Year',y='Average GPA')
	if LxoCTNVkBMhwIxGSHCDZ == "_3_3":

		return

def test__1_0():
	vEPJAmYeGzRFUsqwPIuQ("_1_0")

def test__1_2():
	vEPJAmYeGzRFUsqwPIuQ("_1_2")

def test__2_1():
	vEPJAmYeGzRFUsqwPIuQ("_2_1")

def test__3_1():
	vEPJAmYeGzRFUsqwPIuQ("_3_1")

def test__3_2():
	vEPJAmYeGzRFUsqwPIuQ("_3_2")

