import csv

def generate_load_guest_table_script(guestFilePath):
	queryPrefix = """INSERT INTO guests (code, party, name, "rehearsalInvite", "welcomeReceptionInvite", "brunchInvite") VALUES ("""

	with open(guestFilePath, newline='') as f:
		reader = csv.reader(f)
		party = 0
		next(reader, None)
		for row in reader:
			party += 1
			pk = row[0]
			rehearsal = row[1]
			welcome = row[2]
			brunch = row[3]

			for i in range(4, len(row)):
				if row[i]:
					query = queryPrefix
					query += "'" + pk + "'" + ", " 
					query += str(party) + ", " 
					query += "'" + row[i] + "', "
					query += rehearsal + ", "
					query += welcome + ", "
					query += brunch + ");"
					print(query)

def generate_load_response_table_script():
	reherarsalDinnerEvent = "Rehearsal Dinner"
	rehearsalDinnerResponses = ["Peppercorn Crusted Beef", "Chicken Marsala", "Salmon Florentine", "Pasta Primavera (v)", "Can\\'t attend"]
	rehearsalDinnerDate = "Fri Aug 10, 6-8pm"

	welcomeReceptionEvent = "Welcome Reception"
	welcomeReceptionResponses = ["Attending", "Can\\'t attend"]
	welcomeReceptionDate = "Fri Aug 10, 8-10pm"

	weddingReceptionEvent = "Wedding Reception"
	weddingReceptionResponses = ["Chicken", "Vegetarian", "Can\\'t attend"]
	weddingReceptionDate = "Sat Aug 11, 5pm"

	sundayBrunchEvent = "Sunday Brunch"
	sundayBrunchResponses = ["Attending","Can\\'t attend"]
	sundayBrunchDate = "Sun Aug 12"

	queryPrefix = """INSERT INTO rsvpchoices (event, response, date) VALUES ("""
	for response in rehearsalDinnerResponses:
		queryString = queryPrefix
		queryString += "'" + reherarsalDinnerEvent + "', "
		queryString += "E'" + response + "', "
		queryString += "'" + rehearsalDinnerDate + "');"
		print(queryString)

	for response in welcomeReceptionResponses:
		queryString = queryPrefix
		queryString += "'" + welcomeReceptionEvent + "', "
		queryString += "E'" + response + "', "
		queryString += "'" + welcomeReceptionDate + "');"
		print(queryString)

	for response in weddingReceptionResponses:
		queryString = queryPrefix
		queryString += "'" + weddingReceptionEvent + "', "
		queryString += "E'" + response + "', "
		queryString += "'" + weddingReceptionDate + "');"
		print(queryString)

	for response in sundayBrunchResponses:
		queryString = queryPrefix
		queryString += "'" + sundayBrunchEvent + "', "
		queryString += "E'" + response + "', "
		queryString += "'" + weddingReceptionDate + "');"
		print(queryString)




