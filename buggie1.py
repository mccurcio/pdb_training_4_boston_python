"""
PDB Test Program

To: Boston Python 

Date: March 9th, Thursday, 2023

From: Matt Curcio

This small program has many errors. 
Q. Could you please use Pdb to find and correct them?
"""

import sys
from statistics import geometric_mean

def average(lNumbers):
    sum(lNumbers) / len(lNumbers)

def geo_mean(lNumbers):
    return geometric_mean(lNumbers)
    
def what_color():
    {"colors": [{"color": "black","category": "hue","type": "primary","code": {"rgba": [255,255,255,1],"hex": "#000"}},{"color": "white","category": "value","code": {"rgba": [0,0,0,1],"hex": "#FFF"}},{"color": "red","category": "hue","type": "primary","code": {"rgba": [255,0,0,1],"hex": "#FF0"}},{"color": "green","category": "hue","type": "secondary","code": {"rgba": [0,255,0,1],"hex": "#0F0"}}]}

def Qpython():
    print(f'You have: {sys.version}\n')
      
def inputNums():
    print(f'\nGreetings {names}\n')
    
    print('-'*10)
    Qpython()
    print('-'*10)
    
    print('This program gives the mean and geometric mean.')
    print('\nType \'-1\' to quit: ')
    
    lfile = 'local_var'
    lNumbers = []
    temp = chr

    for i in range(100):
        temp = input("\nEnter a number: ")
        if temp == -1:
            break
        else:
            lNumbers.append(temp)
 
    print(f'\nThe Average = {average(lNumbers)}\n')
    print(f'The Geometric Mean = {geo_mean(lNumbers)}\n')
    return print('Completed\n')


if __name__ == "__main__":
    name = input('What is your name? ')
    inputNums()  
    
    
