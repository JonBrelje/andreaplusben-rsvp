import csv

def generate_load_db_script(guestFilePath):
	queryPrefix = """INSERT INTO guests3 (code, party, name, "rehearsalInvite", "welcomeReceptionInvite") VALUES ("""

	with open(guestFilePath, newline='') as f:
		reader = csv.reader(f)
		party = 0
		next(reader, None)
		for row in reader:
			party += 1
			pk = row[0]
			rehearsal = row[1]
			welcome = row[2]

			for i in range(3, len(row)):
				if row[i]:
					query = queryPrefix
					query += "'" + pk + "'" + ", " 
					query += str(party) + ", " 
					query += "'" + row[i] + "', "
					query += rehearsal + ", "
					query += welcome + ");"
					print(query)