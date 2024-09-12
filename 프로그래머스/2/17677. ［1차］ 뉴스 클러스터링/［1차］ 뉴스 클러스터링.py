# 다중집합: 여러개의 원소를 허용하는 집합.
# 예) {1, 1, 2, 2, 3} 등
# 다중집합의 자카드 연산: 
# 중복되는 원소 k에 대해 교집합 연산 -> min(k_a, k_b)
# 중복되는 원소 k에 대해 합집합 연산 -> max(k_a, k_b)
# {1, 1, 2, 2, 3} 교 {1, 2, 2, 4, 5} = {1, 2, 2}
# {1, 1, 2, 2, 3} 합 {1, 2, 2, 4, 5} = {1, 1, 2, 2, 3, 4, 5} 

# 문자열에 대한 자카드 연산을 위해 문자열을 2개씩 끊어 다중집합으로 만든다. "ABC" -> {"AB", "BC"}
# 공백이나 숫자, 특수 문자가 포함된 문자열은 집합에 포함하지 않는다. 대소문자는 구분하지 않는다.

def able_word(word):
    return ('A' <= word[0] <= 'Z') and ('A' <= word[1] <= 'Z')

# 다중집합 생성 함수
def parse(string):
    dup_set = dict()
    for i in range(len(string) - 1):
        chunk = string[i:i+2]
        # 불가능한 문자
        if not able_word(chunk):
            continue
        if chunk in dup_set:
            dup_set[chunk] += 1
        else:
            dup_set[chunk] = 1
    return dup_set

def intersect(d1, d2):
    result = dict()
    # 교집합이기 때문에 한쪽에서만 진행
    for key, val in d1.items():
        if key in d2:
            result[key] = min(val, d2[key])
    return result

def union(d1, d2):
    result = dict()
    # 한쪽에서 진행 후 다른 쪽에서도 진행
    for key, val in d1.items():
        # 다른쪽에도 존재하는 원소
        if key in d2:
            result[key] = max(val, d2[key])
        # 다른쪽엔 없는 경우
        else:
            result[key] = val
    
    for key, val in d2.items():
        # 다른쪽에도 존재하는 경우
        if key not in d1:
            result[key] = val
    
    return result
            

def jacad(s1, s2):
    # 다중집합 생성
    d1 = parse(s1)
    d2 = parse(s2)
    
    # 교집합 연산
    inter_dup_set = intersect(d1, d2)
    
    # 합집합 연산
    union_dup_set = union(d1, d2)
    
    # 교집합 합집합 크기 구하기
    inter_len = 0
    for val in inter_dup_set.values():
        inter_len += val
        
    union_len = 0
    for val in union_dup_set.values():
        union_len += val
        
    if union_len == 0:
        return 1
    
    return inter_len / union_len

def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    jacad_val = jacad(str1, str2)
    return int(jacad_val * 65536)