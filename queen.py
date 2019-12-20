arr = [['+', '+', 'p'],['+', 'm', '+'],['+', '+', '+']]

def move(n, i, j, arr, path):
  if(arr[i][j] == 'p'):
    return path
  if(i < n-1 and arr[i+1][j] != '-'):
    arr[i][j] = '-'
    return move(n, i+1, j, arr, path + ' DOWN')          
  if(i > 0 and arr[i-1][j] != '-'):
    arr[i][j] = '-'
    return move(n, i-1, j, arr, path + ' \nUP')
  if(j > 0 and arr[i][j-1] != '-'):
    arr[i][j] = '-'
    return move(n, i, j-1, arr, path + ' \nLEFT')
  if(j < n-1 and arr[i][j+1] != '-'):  
    arr[i][j] = '-'
    return move(n, i, j+1, arr, path  + ' \nRIGHT')
  return ''

print(move(3, 1, 1, arr, ''))
