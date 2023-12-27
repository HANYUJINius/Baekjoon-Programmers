def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(denum1, num1, denum2, num2):
    mo = num1 * num2
    ja = denum1 * num2 + denum2 * num1
    
    #최대공약수 계산
    gcd_value = gcd(mo,ja)

    #gcd 로 나눈 값을 answer에 담기
    answer = [ja / gcd_value, mo / gcd_value]
    return answer
