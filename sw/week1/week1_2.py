#2 연월일 
n=int(input())
for i in range(1,n+1):
  num=input()
  if int(num[4:6])>=1 and int(num[4:6])<=12:
    if int(num[4:6])==2:
      if int(num[6:8])<=28:
        print(f'#{i} ' + num[:4]+'/'+num[4:6]+'/'+num[6:])
      else:
        print(f'#{i} ',-1)
    elif int(num[4:6]) ==4 or int(num[4:6]) ==6 or int(num[4:6]) ==9 or int(num[4:6]) ==11:
      if int(num[6:8])<=30:
        print(f'#{i} ' + num[:4]+'/'+num[4:6]+'/'+num[6:])
      else:
        print(f'#{i} ',-1)
    elif int(num[4:6]) ==1 or int(num[4:6]) ==3 or int(num[4:6]) ==5 or int(num[4:6]) ==7 or int(num[4:6]) ==8 or int(num[4:6]) ==10 or int(num[4:6]) ==12:
      if int(num[6:8])<=31:
        print(f'#{i} ' + num[:4]+'/'+num[4:6]+'/'+num[6:])
      else:
        print(f'#{i} ',-1)

    else:
        print(f'#{i} ',-1)
  else:
    print(f'#{i} ',-1)