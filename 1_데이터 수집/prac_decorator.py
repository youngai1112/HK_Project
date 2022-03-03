# 1. 에러나는 부분을 찾아서 소스와 코드를 하나하나 수정해야 한다.

def extract_data_dart(soup):
# 에러 발생

    # 에러나는 부분 예외처리
    try:
        print(0)
    except:
        pass

def extract_data_naverFinance(soup):
# 에러 발생

    # 에러나는 부분 예외처리
    try:
        print(0)
    except:
        pass


def extract_data_invest(soup):
# 에러 X



#############################################################################

# 2. 함수를 호출해서 재사용
# 에러가 발생하는 부분은 여러 번 작성해서 실행해야 할까 ?
#   No ! : Decorator를 사용하면 된다.
def deco(fun):

    def anyName():
        try:
            fun()
        except:
            pass
    
    return anyName

@deco   # 소스코드의 재사용성을 위해 decorator 사용
def extract_data_dart(soup):

@deco
def extract_data_naverFinance(soup):

def extract_data_invest(soup):
