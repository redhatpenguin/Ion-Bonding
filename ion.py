import time
periodic_table = [
    ['h','수소'],['he','헬륨'],['li','리튬'],['be','베릴륨'],['b','붕소'],
    ['c','탄소'],['n','네온'],['o','산소'],['f','플루오린'],['ne','네온'],
    ['na','나트륨'],['mg','마그네슘'],['al','알루미늄'],['si','규소'],
    ['p','인'],['s','황'],['cl','염소'],['ar','아르곤'],['k','칼륨'],
    ['ca','칼슘'],['sc','스칸듐'],['ti','타이타늄'],['v','바나듐'],['cr','크로뮴'],
    ['mn','망가니즈'],['fe','철'],['co','코발트'],['ni','니켈'],['cu'],['zn'],
    ['ga'],['ge'],['as'],['se'],['br'],['kr'],['rb'],['sr'],['y'],['zr'],['nb'],['mo'],['tc'],['ru'],['rh'],['pd'],['ag'],['cd'],['in'],['sn'],['sb'],['te'],['i'],['xe'],['cs'],['ba'],['la'],['ce'],['pr'],['nd'],['pm']
,['sm'],['eu'],['gd'],['tb'],['dy'],['jp'],['er'],['tm'],['yb'],['lu'],['hf'],['ta'],[],[]
,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

def leastCommonMultipul(a,b): 
    '''최소공배수를 구해주는 합수'''
    for i in range(max(a,b),(a*b+1)):
        if i % a == 0 and i % b == 0:
            return i
    
def get_sub(x):
    """function to convert to subscript"""
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

def getElementInfo(a):       
    '''원소 입력  =>  return [원소기호, 원소 번호] '''
    for item in periodic_table:
        if a.lower() in item:
            number = periodic_table.index(item) + 1
            name = item[0].title()
            return [name,number]
    return 'no'

def getIon(eleInfo):     
    '''
    [원소기호,원소번호] 입력 => [원소기호, 이온일 때 전하량의 절댓값, 이온일 때 전하량의 부호] 리턴 
    
    (ex) ['Li',3] => ['Li',1,'+']
    
    '''

    if eleInfo == 'no':
        return eleInfo
    
    name = eleInfo[0]
    num = eleInfo[1]

    # 전자가 원자수 = outshell_num, 전하량 절댓값 = junha, 이온 전하 부호 = sign
    junha = 0
    sign = ''
    outshell_num = 0

    # 수소와 헬륨의 전자가 원자와 전하량, 그리고 전하량 부호를 구하는 공식은 다른 원소와 다르므로 따로 구해준다
    if num == 1:
        outshell_num = 1
        junha = 1
        sign = '-'

    elif num == 2:
        outshell_num = 2
        junha = 0
        sign = 'nohands'
            
    else:
        # 수소와 헬륨을 제외한 원소들: 원자가 전자를 구하는 공식 : (원자번호 - 2)를 8로 나누어주었을 때의 나머지
        outshell_num = (num-2) % 8 

        # 전자가 원자를 통해 전하량을 구한다  (전하량의 부호 => sign    전하량의 절댓값 => junha)  
        if outshell_num > 4: 
            junha = 8 - outshell_num
            sign = '-'
            
        elif outshell_num == 4:
            # 전자가 원자 4개 => sign = fourhanded
            junha = 4
            sign = 'fourhands'
        elif 0 < outshell_num < 4:
            junha = outshell_num
            sign = '+'
        
        elif outshell_num == 0:
            # 전자가 원자 0개 => sign = 'nohands'     
            junha = 0
            sign = 'nohands'

    return [name, junha, sign]        

def ionNumFormat(n):
    '''
    이온결합을 할 때 한 개의 원소가 이온결합에 참여하면 빈 스트링을 리턴함. 
    이온결합에 참여하는 원소가 2개 이상이면 원소의 개수인 숫자 n을 아래첨자로 바꾸어줌. 
    '''
    if n == 1:
        return ''
    else:
        return get_sub(str(n))

def Ion_collab(elOne,elTwo):
    '''
    두 이온에 대한 정보를 리스트 형태로 입력 => 두 이온의 이온결합 유무, 또는 이온결합식을 알려줌
    '''
         
    if (elOne or elTwo) == 'no':
        return '주기율표에 있는 원소를 입력해주시길 바랍니다. '
    if elOne[0] == elTwo[0]:
        return '이온결합은 서로 다른 두 원소 사이에서만 일어날 수 있습니다.\n다시 시도해 주십시오.'
    
    nameOne = elOne[0]
    junhaOne = elOne[1]
    signOne = elOne[2]

    nameTwo = elTwo[0]
    junhaTwo = elTwo[1]
    signTwo = elTwo[2]

    # 사용자가 입력한 원소 중 18족 원소가 있으면 이온결합을 할 수 없다고 알려주기
    if signOne == 'nohands':
        return nameOne+'은 18족 원소이기 때문에 이온결합을 할 수 없습니다'
    elif signTwo=='nohands':
        return nameTwo+'은 18족 원소이기 때문에 이온결합을 할 수 없습니다'
    elif signOne == signTwo =='nohands':
        return nameOne+'과',nameTwo+'은 18족 원소이기 때문에 이온결합을 할 수 없습니다'
    
    elif signOne == 'fourhands' or signTwo == 'fourhands':
        return '14족 원소는 공유결합을 하는 것이 이온결합을 하는 것 보다 효율적이기 때문에 14족 원소는 이온결합을 하지 않습니다'

    if signOne != signTwo:
        lComMun = leastCommonMultipul(junhaOne,junhaTwo)
        num1 = ionNumFormat(int(lComMun / junhaOne))
        num2 = ionNumFormat(int(lComMun / junhaTwo))

        if elOne[2] == '+':
            return '이온결합물: '+ nameOne+num1+nameTwo+num2
        else:
            return '이온결합물: '+ nameTwo+num2+nameTwo+num1

    
    elif signOne == signTwo == '+':
        return '양이온끼리는 이온결합을 할 수 없습니다'
    
    elif signOne == signTwo == '-':
        return '음이온끼리는 이온결합을 할 수 없습니다.'

def tryPro():
    print('\n두 원소를 차례대로 입력하세요.\n')
    ask1 = input('원소 1: ')
    ask2 = input('원소 2: ')
    
    aa = getElementInfo(ask1)
    bb = getElementInfo(ask2)

    a = getIon(aa) 
    b = getIon(bb)
    myResult = Ion_collab(a,b)
    
    print('\n계산중...\n')
    time.sleep(1)
    print(myResult+'\n')

    ask = input('다시 하시겠습니까? (y/n): ')
    if ask == 'y':
        a = tryPro()
    else:
        print('\n감사합니다.\n')
    
if __name__=='__main__': 
    print('\n이온결합 실험실에 오신 것을 환영합니다!\n')
    a = tryPro()