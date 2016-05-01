import csv

survey_id_courses_started = {}
courses_dict = {0:0}
screen_name_courses_started = {}

with open ('earth_Spring2015/EarthSciences_ResGeo202_Spring2015_survey_responses.csv', 'r') as csvfile :
	lines = csv.reader(csvfile, delimiter = ',', quotechar = '"')
	for line in lines :
		# How many open online courses have you started before this one? 
		if line[0] == "SV_dhGmpvbbuyNZEA5" and line[2] == "Q2.3" :
			if line[4] == "" or line[4] == ".5" :
				survey_id_courses_started[line[1]] = 0
				courses_dict[0] += 1
			# elif line[4] == ".5" :
			# 	print line
			# elif line[4] == "202" :
			# 	print line
			else :
				num_course = int(line[4])
				survey_id_courses_started[line[1]] = num_course
				if num_course in courses_dict :
					courses_dict[num_course] += 1
				else :
					courses_dict[num_course] = 1

# print courses_dict	
# print len(survey_id_courses_started)

with open('earth_Spring2015/EarthSciences_ResGeo202_Spring2015_survey_response_metadata.csv', 'r') as csvfile :
	lines = csv.reader(csvfile, delimiter = ',', quotechar = '"')
	for line in lines :
		if line[0] == "SV_dhGmpvbbuyNZEA5" and line[1] in survey_id_courses_started :
			screen_name_courses_started[line[2]] = survey_id_courses_started[line[1]]

# print len(screen_name_courses_started)
# count = 0
# for i in screen_name_courses_started :
# 	print i, screen_name_courses_started[i]
# 	count += 1
# 	if count > 20:
# 		break