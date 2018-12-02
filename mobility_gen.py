''' works for python 2.7 '''
'''use this script to generate the time entries of mobility.txt and paste the '''
for i in range(1,25):
  print'$time ' + str(i) + ' "$node_(4) 2000 ' + str(50*4*i) + ' 0"'
  
''' add entries for more node if you wish to'''
