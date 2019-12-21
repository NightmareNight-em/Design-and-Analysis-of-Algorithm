# -*- coding: utf-8 -*-
"""DAA_Assignment_week6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GYbcpwvziokZiCEf5_WgQqL3gSdStm-e
"""

n,p,f=map(int,input().split())
morning=list(map(int,input().split()))
evening=list(map(int,input().split()))
morning_sorted=quicksort(morning,0,n-1)
evening_sorted=quicksort(evening,0,n-1)
#print(morning_sorted,evening_sorted)
min=0
for i in range(n):
  if (morning_sorted[i]+evening_sorted[n-i-1])>p:
    min+=((morning_sorted[i]+evening_sorted[n-i-1])-p)*f
print(min)

def quicksort(ar,l,r):
  y=0
  if r-l<1:
    return
  
  y=l+1
  for g in range(l+1,r+1):
    if ar[g]<ar[l]:
      ar=swap(ar,y,g)
      y+=1
  #print('y:',y,'l:',l)  
  ar=swap(ar,l,y-1)
  #print(ar)
  quicksort(ar,l,y-1)
  quicksort(ar,y,r)
  return ar

def swap(a,L,R):
  temp=a[L]
  a[L]=a[R]
  a[R]=temp
  return a

