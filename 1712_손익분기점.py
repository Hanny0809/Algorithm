'''
월드전자는 노트북을 제조하고 판매하는 회사이다. 노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용이 들며,
한 대의 노트북을 생산하는 데에는 재료비와 인건비 등 총 B만원의 가변 비용이 든다고 한다.
예를 들어 A=1,000, B=70이라고 하자. 이 경우 노트북을 한 대 생산하는 데는 총 1,070만원이 들며, 열 대 생산하는 데는 총 1,700만원이 든다.
노트북 가격이 C만원으로 책정되었다고 한다. 일반적으로 생산 대수를 늘려 가다 보면 어느 순간 총 수입(판매비용)이 총 비용(=고정비용+가변비용)보다
많아지게 된다. 최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점(BREAK-EVEN POINT)이라고 한다.
A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.
'''

a, b, c = map(int, input().split())

if b >= c:
    print('-1')
else:
    print(a//(c-b)+1)


'''
a는 고정비용, b는 가변비용, c는 노트북 가격으로 변수를 설정하고 입력받는다.
판매량을 N이라고 한다면 C*N = A + B*N으로 나타낼 수 있다. 이 식을 판매량인 N을 구하는 식으로 바꾸면 N= A/(C-B)가 된다. if조건식으로 
손익분기점이 존재하지 않을 때 -1을 출력한다.
가변비용이 노트북 가격보다 크면 손익분기점은 존재하지 않는다. 총수입을 구하는 식 C*N = A + B*N을 다시 보면 고정비용 A가 아무리 크더라도 
노트북 가격 C가 가변비용 B보다 크다면 판매량을 늘려서 손익분기점을 넘길 수 있다.
즉, B가 C보다 큰 경우에 손익분기점은 존재하지 않는다.
손익분기점이 발생하는 때의 판매량을 식으로 나타내면 N= A/(C-B)이지만 이 식은 손익분기점인 때가 되고 최초로 이익이 발생하는 시점은 이 식에서 
보다 판매량을 하나 더 더해야 한다.
그런데 파이썬에서 이 식을 코드로 작성하면 실수 형태로 출력이 된다. 그렇기 때문에 정수로 출력하기 위해서 // 연산자로 나눗셈의 몫을 구해야 한다.
'''