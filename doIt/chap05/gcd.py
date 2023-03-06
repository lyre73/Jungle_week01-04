# 유클리드 호제법으로 최대 공약수 구하기

def gcd(x: int, y: int) -> int:
        """정숫값 x와 y의 최대 공약수를 반환"""

        if y == 0:
                return x
        else:
                return gcd(y, x % y)
        
if __name__ == '__main__':
        print(f'최대공약수: {gcd(int(input()), int(input()))}')