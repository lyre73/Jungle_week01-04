# def ask(num, startnum):
#     if num == 0:
#         print('____'*(startnum-num)+'"재귀함수가 뭔가요?"')
#         print('____'*(startnum-num)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
#         print('____'*(startnum-num)+'라고 답변하였지.')
#         return
#     else:
#         print('____'*(startnum-num)+'"재귀함수가 뭔가요?"')
#         print('____'*(startnum-num)+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#         print('____'*(startnum-num)+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#         print('____'*(startnum-num)+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         ask(num-1, startnum)
#         print('____'*(startnum-num)+'라고 답변하였지.')

# N = int(input())
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# ask(N, N)

# 
# def ask(num, indent):
#     print('____'*(indent)+'"재귀함수가 뭔가요?"')
#     if num > 0:
#         print('____'*(indent)+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#         print('____'*(indent)+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#         print('____'*(indent)+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         ask(num-1, indent+1)        
#     else:
#         print('____'*(indent)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
#     print('____'*(indent)+'라고 답변하였지.')
#     return

# N = int(input())
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# ask(N, 0)

import sys

def ask(num, indent):
    print('____'*(indent)+'"재귀함수가 뭔가요?"')
    if num > 0:
        print('____'*(indent)+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____'*(indent)+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____'*(indent)+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        ask(num-1, indent+1)        
    else:
        print('____'*(indent)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
    print('____'*(indent)+'라고 답변하였지.')
    return

N = int(sys.stdin.readline())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
ask(N, 0)