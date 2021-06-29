def solution(clothes):
    answer = 1
    hash_map = {}
    
    for dress in clothes:
        key = dress[1]
        value = dress[0]
        if key in hash_map:
            hash_map[key].append(value)
        else:
            hash_map[key] = [value]
        # ex) output: {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
        # 위와 같이 딕셔너리가 만들어진다.
        
    for key in hash_map.keys():
        answer = answer * (len(hash_map[key])+ 1)

    return answer - 1

# 카테고리 별로 아이템을 한 개씩 조합해야 하는 문제
# 각 카테고리 별로 아이템 갯수를 구해서 다 곱하면 된다.
# (모자의 갯수 + 1) * (바지의 갯수 + 1) * (안경의 갯수 + 1)
# 모자는 쓰지않고, 바지만 입는다거나 하는 경우는 고려되지 않는다.
# 모자랑 안경만 쓰고 바지는 입지 않는 경우도 고려되지 않는다.
# 각 카테고리별로 "해당 카테고리의 아이템을 장착하지 않는경우"는 한 개를 더 추가해서 계산한다 (+1) 20줄의 이유
# 특정 카테고리가 제외되는 경우까지 모두 고려됐다. 하지만 스파이는 반드시 한 개의 아이템을 장착해야 하므로 
# 어떤 아이템도 장착하지 않는 한 개의 경우는 결과에서 빼줘야 한다.
# (모자의 갯수 + 1) * (바지의 갯수 + 1) * (안경의 갯수 + 1) - 1

# answer이 1인 이유는 스파이가 가진 의상의 수는 1개 이상 30개 이하라서 그렇게 정했고, 해시를 사용하려고 했습니다.
# clothes라는 배열에서 dress로 따로 꺼내와서 key엔 dress[1] 인덱스, 즉, [의상의 종류]를 할당시켰고, value값에는 [의상의 이름]을 할당시켰습니다.
# 만약 hash_map 딕셔너리 안에 key 값이 있다면 hash_map[key][value] 이 구조안에 value값을 추가시키겠다. 라는 뜻이고, 그게 아니라면 
# hash_map[key] 안에 2차원배열로 [value] 값을 추가시키겠다 라는 뜻입니다. 
# 그리고 hash_map.keys()안에 key값이 있다면 hash_map[key]값의 길이에서 + 1 한 값을 answer과 곱해 할당시키겠다 = 해당 카테고리의 아이템을 장착하지 않는 경우 한 개를 더 추가해서 계산한다. 이 이유는 그 카테고리, 즉, (모자)*(바지)*(안경) 이렇게 3가지가 있는데 한 가지라도 안 입는 경우도 있기 때문에 +1을 한 것이다.
# 그리고 answer - 1 어떤 아이템도 장착하지 않는 한 개의 경우 수를 뺴줘야했으므로 마무리했습니다.
