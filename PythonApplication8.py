def gkatn1(void):
     import random
     computer = random.randint(1,3) # 1은 가위. 2는 바위, 3은 보다.
     a=char(input("가위, 바위, 보 중에서 하나를 입력하시오. : "))
     if(a=="가위") :
       if(computer==1) :
           print("컴퓨터가 이겼습니다. ")
       if(computer==2):
         print("컴퓨터가 바위로 이겼습니다.")
         gkatn1()
       if(computer==3):
         print("사용자가 가위로 이겼습니다.(컴퓨터는 보)")
         gkatn2()
     elif(player=="바위") :
       if(computer==2) :
           print("컴퓨터가 이겼습니다. ")
       if(computer==3):
           print("컴퓨터가 보로 이겼습니다.")
           gkatn1()
       if(computer==1):
           print("사용자가 바위로 이겼습니다.(컴퓨터는 가위)")
           gkatn2()
     elif(player=="보") :
       if(computer==3) :
          print("컴퓨터가 이겼습니다. ")
       if(computer==1):
          print("컴퓨터가 가위로 이겼습니다.")
          gkatn1()
       if(computer==2):
          print("사용자가 보로 이겼습니다.(컴퓨터는 바위)")
          gkatn2()
     else:
         print("잘못 입력하셨습니다. 처음부터 다시 시작합니다.")
         main()

def gkatn2(void):
     import random
     computer = random.randint(1,3) # 1은 가위. 2는 바위, 3은 보다.
     a=char(input("가위, 바위, 보 중에서 하나를 입력하시오. : "))
     if(a=="가위") :
       if(computer==1) :
           print("사용자가 이겼습니다. ")
       if(computer==2):
         print("컴퓨터가 바위로 이겼습니다.")
         gkatn1()
       if(computer==3):
         print("사용자가 가위로 이겼습니다.(컴퓨터는 보)")
         gkatn2()
     elif(player=="바위") :
       if(computer==2) :
           print("사용자가 이겼습니다. ")
       if(computer==3):
           print("컴퓨터가 보로 이겼습니다.")
           gkatn1()
       if(computer==1):
           print("사용자가 바위로 이겼습니다.(컴퓨터는 가위)")
           gkatn2()
     elif(player=="보") :
       if(computer==3) :
          print("사용자가 이겼습니다. ")
       if(computer==1):
          print("컴퓨터가 가위로 이겼습니다.")
          gkatn1()
       if(computer==2):
          print("사용자가 보로 이겼습니다.(컴퓨터는 바위)")
          gkatn2()
     else:
         print("잘못 입력하셨습니다. 처음부터 다시 시작합니다.")
         main()
def main():
 while(1):
  import random
  computer = random.randint(1,3) # 1은 가위. 2는 바위, 3은 보다.
  player=input("가위, 바위, 보 중에서 하나를 입력하시오. : ")
  if(player=="가위") : 
    if(computer==1) :
        same = input("비겼습니다. 다시 하시려면 r을 누르세요. ")
        if(same=='r'):
            continue;
    if(computer==2):
        print("컴퓨터가 바위로 이겼습니다.")
        gkatn1()
    if(computer==3):
        print("사용자가 가위로 이겼습니다.(컴퓨터는 보)")
        gkatn2()
  if(player=="바위") :
    if(computer==2) :
        same = print("비겼습니다. 다시 하시려면 r을 누르세요. ")
        if(same=='r'):
            continue;
    if(computer==3):
        print("컴퓨터가 보로 이겼습니다.")
        gkatn1()
    if(computer==1):
        print("사용자가 바위로 이겼습니다.(컴퓨터는 가위)")
        gkatn2()
  if(player=="보") :
    if(computer==3) :
        same = print("비겼습니다. 다시 하시려면 r을 누르세요. ")
        if(same=='r'):
            continue;
    if(computer==1):
        print("컴퓨터가 가위로 이겼습니다.")
        gkatn1()
    if(computer==2):
        print("사용자가 보로 이겼습니다.(컴퓨터는 바위)")
        gkatn2()
  else:
         print("잘못 입력하셨습니다. 처음부터 다시 시작합니다.")
         main()
main()