#!/usr/bin/python
import math 

possiblePaths = []
def displayPathtoPrincess(n, i, j, arr, path):
  if(arr[i][j] == 'p'):
    possiblePaths.append(path)
  if(i < n-1 and arr[i+1][j] != '+'):
    arr[i][j] = '+'
    displayPathtoPrincess(n, i+1, j, arr, path + ['DOWN'])          
  if(i > 0 and arr[i-1][j] != '+'):
    arr[i][j] = '+'
    displayPathtoPrincess(n, i-1, j, arr, path + ['UP'])
  if(j > 0 and arr[i][j-1] != '+'):
    arr[i][j] = '+'
    displayPathtoPrincess(n, i, j-1, arr, path + ['LEFT'])
  if(j < n-1 and arr[i][j+1] != '+'):  
    arr[i][j] = '+'
    displayPathtoPrincess(n, i, j+1, arr, path + ['RIGHT'])
  return True

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(list(input().strip()))

displayPathtoPrincess(m, math.floor(m/2), math.floor(m/2) , grid, list([]))

bestPath = []
for path in possiblePaths:
  if(len(path)> len(bestPath)):
    bestPath = path
print('\n'.join(bestPath))  
