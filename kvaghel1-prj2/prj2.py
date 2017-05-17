import sys

cache_matrix = [[0,0,0,0] for x in range(3)]

for line in sys.stdin:
	#a = raw_input()
	a = line
	#1r0
	cache_num = int(a[0])
	command = str(a[1])
	line_num = int(a[2])
	print "--------------------------------------"
	print a
	#0-Invalid, 1-Exclusive , 2-Shared, 3-Modified, 4-Owned
	if command == "r":
		if cache_matrix[cache_num][line_num] != 0:
			#Read Hit
			if cache_matrix[cache_num][line_num] == 1:
				#print cache_matrix
				print "Hit"
				print "E -> E"
			elif cache_matrix[cache_num][line_num] == 3:
				#print cache_matrix
				print "Hit Dirty"
				print "M -> M"
			elif cache_matrix[cache_num][line_num] == 2:
				#print cache_matrix
				print "Hit"
				print "S -> S"
			elif cache_matrix[cache_num][line_num] == 4:
				#print cache_matrix
				print "Hit Dirty"
				print "O -> O"
			else:
				print "Erroorrrr !"
		elif cache_matrix[cache_num][line_num] == 0:
			#Read Miss
			print "Cache",str(cache_num)+",","Miss",line_num
			f = False
			print ""
			for i in xrange(3):
				if i == cache_num:
					pass
				else:
					print "Cache",str(i)+",","Bus Read",line_num
					if cache_matrix[i][line_num] == 0:
						#Can't reach here
						#print cache_matrix
						print "Miss"
						print "I -> I"
					
					elif cache_matrix[i][line_num] == 1:
						#print cache_matrix
						print "Hit"
						print "E -> S"
						#cache_matrix[cache_num][line_num] = 2
						cache_matrix[i][line_num] = 2
						f = True
						

					elif cache_matrix[i][line_num] == 2:
						# print cache_matrix
						print "Hit"
						print "S -> S"
						#cache_matrix[cache_num][line_num] = 2
						cache_matrix[i][line_num] = 2
						f = True
						

					elif cache_matrix[i][line_num] == 3:
						#print cache_matrix
						print "Hit Dirty"
						print "M -> O"
						#cache_matrix[cache_num][line_num] = 4
						cache_matrix[i][line_num] = 4
						f = True
					elif cache_matrix[i][line_num] == 4:
						#print cache_matrix
						print "Hit Dirty"
						print "O -> O"
						# cache_matrix[cache_num][line_num] = 4
						# cache_matrix[i][line_num] = 2
						f = True
					else:
						print "Bus Read Error !"
					print "End Bus Read\n"
			if f:
				#print cache_matrix
				print "Cache ",cache_num
				print "I -> S"
				cache_matrix[cache_num][line_num] = 2
				
			else:
				#print cache_matrix
				print "Cache ",cache_num
				print "I -> E"
				cache_matrix[cache_num][line_num] = 1
				print "MEMORY READ"

	
	elif command == "w":
			if cache_matrix[cache_num][line_num] == 0:
				#Write Miss
				#print cache_matrix
				print "Miss"
				print ""
				for i in xrange(3):
					if i == cache_num:
						pass
					else:
						print "Cache",i,"Bus Write",line_num
						if cache_matrix[i][line_num] == 0:
							#print cache_matrix
							print "Miss"
							print "I -> I"

						elif cache_matrix[i][line_num] == 1:
							#print cache_matrix
							print "Hit"
							print "E -> I"
							#cache_matrix[cache_num][line_num] = 0
							cache_matrix[i][line_num] = 0

						elif cache_matrix[i][line_num] == 2:
							#print cache_matrix
							print "Hit"
							print "S -> I"
							#cache_matrix[cache_num][line_num] = 0
							cache_matrix[i][line_num] = 0

						elif cache_matrix[i][line_num] == 3:
							#print cache_matrix
							print "Hit Dirty"
							print "Flush"
							print "M -> I"
							#cache_matrix[cache_num][line_num] = 0
							cache_matrix[i][line_num] = 0

						elif cache_matrix[i][line_num] == 4:
							#print cache_matrix
							print "Hit Dirty"
							print "Flush"
							print "O -> I"
							#cache_matrix[cache_num][line_num] = 0
							cache_matrix[i][line_num] = 0
						else:
							print "Bus Write Error !"
						print "End Bus Write"
				else:
					#print "Cache ",cache_num
					print "I -> M"
					print ""
					cache_matrix[cache_num][line_num] = 3
					#print "MEMORY WRITE"
			else:
				#Write Hit
				if cache_matrix[cache_num][line_num] == 1:
					print "Hit"
					print "E -> M"
					print ""
					cache_matrix[cache_num][line_num] = 3

				elif cache_matrix[cache_num][line_num] == 2:
					print "Hit"
					#print "S -> M"
					cache_matrix[cache_num][line_num] = 3
					for i in range(3):
						if i == cache_num:
							pass
						else:
							#print "Cache",i,"Bus Write",line_num
							if cache_matrix[i][line_num] == 0:
								print "Cache",i,"Bus Write",line_num
								#print cache_matrix
								print "Miss"
								print "I -> I"
								print "End Bus Write"

							if cache_matrix[i][line_num] == 1:
								#print cache_matrix
								print "Cache",i,"Bus Write",line_num
								print "Hit"
								print "E -> I"
								cache_matrix[cache_num][line_num] = 3
								cache_matrix[i][line_num] = 0
								print "End Bus Write"

							elif cache_matrix[i][line_num] == 2:
								#print cache_matrix
								print "Cache",i,"Bus Write",line_num
								print "Hit"
								print "S -> I"
								cache_matrix[cache_num][line_num] = 3
								cache_matrix[i][line_num] = 0
								print "End Bus Write"

							elif cache_matrix[i][line_num] == 3:
								#print cache_matrix
								print "Cache",i,"Bus Write",line_num
								print "Hit Dirty"
								print "Flush"
								print "M -> I"
								cache_matrix[cache_num][line_num] = 3
								cache_matrix[i][line_num] = 0
								print "End Bus Write"

							elif cache_matrix[i][line_num] == 4:
								#print cache_matrix
								print "Cache",i,"Bus Write",line_num
								print "Hit Dirty"
								print "Flush"
								print "O -> I"
								cache_matrix[cache_num][line_num] = 3
								cache_matrix[i][line_num] = 0
								print "End Bus Write"

							else:
								pass
								#print "Bus Write Error !"
					print "S -> M"
					print ""

				elif cache_matrix[cache_num][line_num] == 3:
					print "Hit Dirty"
					print "M -> M"
					print ""
					

				elif cache_matrix[cache_num][line_num] == 4:
					print "Hit"
					for i in range(3):
						if i == cache_num:
							pass
						else:
							#print "Cache",i,"Bus Write",line_num
							if cache_matrix[i][line_num] == 0:
								#print cache_matrix
								print "Cache",i,"Bus Write",line_num
								print "Miss"
								print "I -> I"
								print "End Bus Write"

							if cache_matrix[i][line_num] == 1:
								#print cache_matrix
								print "Cache",i,"Bus Write",line_num
								print "Hit"
								print "E -> I"
								cache_matrix[cache_num][line_num] = 3
								cache_matrix[i][line_num] = 0
								print "End Bus Write"

							elif cache_matrix[i][line_num] == 2:
								#print cache_matrix
								print "Cache",i,"Bus Write",line_num
								print "Hit"
								print "S -> I"
								cache_matrix[cache_num][line_num] = 3
								cache_matrix[i][line_num] = 0
								print "End Bus Write"

							elif cache_matrix[i][line_num] == 3:
								#print cache_matrix
								print "Cache",i,"Bus Write",line_num
								print "Hit Dirty"
								print "Flush"
								print "M -> I"
								cache_matrix[cache_num][line_num] = 3
								cache_matrix[i][line_num] = 0
								print "End Bus Write"

							elif cache_matrix[i][line_num] == 4:
								#print cache_matrix
								print "Cache",i,"Bus Write",line_num
								print "Hit Dirty"
								print "Flush"
								print "O -> I"
								cache_matrix[cache_num][line_num] = 3
								cache_matrix[i][line_num] = 0
								print "End Bus Write"

							else:
								pass
								#print "Bus Write Error !"
							print "O -> M"
							print ""
					
	elif command == "e":
		if cache_matrix[cache_num][line_num] == 0:
			print "I -> I"
			print ""

		elif cache_matrix[cache_num][line_num] == 1:
			print "E -> I"
			print ""
			cache_matrix[cache_num][line_num] = 0

		elif cache_matrix[cache_num][line_num] == 2:
			print "S -> I"
			print ""
			f = False
			for i in range(3):
				if f:
					break
				if cache_matrix[i][line_num] == 2:
					cache_matrix[i][line_num] = 0
					f = True
			else:
				for i in xrange(3):
					if cache_matrix[i][line_num] == 4:
						cache_matrix[i][line_num] = 3

		elif cache_matrix[cache_num][line_num] == 3:
			print "Flush"
			print "M -> I"
			print ""
			cache_matrix[cache_num][line_num] = 0



		elif cache_matrix[cache_num][line_num] == 4:
			print "Flush"
			print "O -> I"
			print ""
			f = False
			for i in xrange(3):
				if f:
					break
				if cache_matrix[cache_num][line_num] == 2:
					cache_matrix[cache_num][line_num] = 1
					f = True
