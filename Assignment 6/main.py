from Graph import *
import pickle


graphfile = open('graphdata.pkl', 'rb')
g = pickle.load(graphfile)
bfs_list = list(g.bfs_paths(1, 8))
dfs_list = list(g.dfs_paths(1, 11))

bfs_pickle = open('bfs_result.pkl', 'wb')
pickle.dump(bfs_list, bfs_pickle)

dfs_pickle = open('dfs_result.pkl', 'wb')
pickle.dump(dfs_list, dfs_pickle)

print (bfs_list)
print (len(bfs_list))
print (dfs_list)
print (len(dfs_list))
# for key,value in g.graph.items():
# 	print(key, " : ", value)
# for i in range(12):
# 	for j in range(12):
# 		try:
# 			bfs_list = list(g.bfs_paths(i, j))
# 			dfs_list = list(g.dfs_paths(i, j))
		
# 			print(bfs_list, "  ", dfs_list)
# 		except:
# 			print("None", i, " ", j)
# bfs_result = open('bfs_result.pkl', 'rb')
# bfs_result = pickle.load(bfs_result)
# dfs_result = open('dfs_result.pkl', 'rb')
# dfs_result = pickle.load(dfs_result)
# print(bfs_result)
# print(dfs_result)