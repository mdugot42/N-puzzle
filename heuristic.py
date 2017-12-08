def outOfPlace(state):
	r = 0
	for j in range(state.solver.size):
		for i in range(state.solver.size):
			if (state.grid[j][i] != state.solver.goal.grid[i][j]):
				r += 1
	return r

def manhattanDistance(state):
	r = 0
	for j in range(state.solver.size):
		for i in range(state.solver.size):
			gy, gx = state.solver.getGoalPoint(state.grid[j][i])
			r += abs(gy-j) + abs(gx-i)
#			print(str(j)+":"+str(i)+"="+str(state.grid[j][i]))
#			print(str(state.grid[j][i])+"->"+str(gy)+":"+str(gx))
#			print("d="+str(abs(gy-j) + abs(gx-i)))
	return r
