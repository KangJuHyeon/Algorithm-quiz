# 어피치가 제이지에게 닦달을 했어? DB 캐시 크기를 얼마로 해야 효율적인지는 우리도 몰라;
# 제이지가 날 도와줘야지😭
# DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

# 문제접근
# 입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.
# hit, miss의 정의를 알고 차근차근 조건을 맞춰간다.

# 수도코드(1)
def solution(cacheSize, cities):
    time, cache = 0, [] # 실행시간 카운트, 캐시안에 도시 이름 넣을 박스 선언

    # 대소문자 구분하지 않는다.
    cities = [ i.lower() for i in cities ]
    print(cities)

    # 캐시크기가 0일 때, 0이라 실행시간? 없음 time = 5
    if cacheSize == 0:
        return len(cities) * 5
    
    for data in cities:
        # print(data)

        # hit (존재하는 데이터가 들어온 경우)
        if data in cache:
            cache.pop(0) # 맨 앞에 있는 값 pop
            print(cache)
            cache.append(data)  
            print(cache)
            time += 1
        # miss (새로운 데이터가 들어온 경우)
        else:
            # 만약 cache의 길이가 cacheSize와 같다면
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(data)
            print(cache)
            time += 5
    return time
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 문제풀이(1)
def solution(cacheSize, cities):
    index = 0 # 캐시 인덱스 지정
    time, cache = 0, [] # 실행시간 카운트, 캐시를 담을 빈 배열 선언

    # 캐시크기가 0일 때, 모든 cities가 miss이기 때문에 (도시이름 길이) * 5
    if cacheSize == 0: 
        return len(cities) * 5

    for i in cities:
        # 대소문자 구분하지 않는다.
        city_name = i.lower()
        print(city_name)
        if city_name in cache:
            cache.append(i)
            print(cache)
        else:
            time += 5
            print(time)
            # cacheSize = 5일때, time 7이라면 새로운 데이터 hit
            if index < cacheSize:
                cache.append(city_name)
                print(cache)
                index += 1
                print(index)
            # cacheSize = 5일때, time 5보다 작을 때
            else:
                cache.pop(0)
                print(cache)
                cache.append(city_name)
                print(cache)
    
    return time
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 문제풀이(2)
def solution(cacheSize, cities):
    cities = [i.lower() for i in cities]
    time, cache = 0, []
    
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for data in cities:
            if not data in cache:
                if len(cache) < cacheSize:
                    cache.append(data)
                    time += 5
                else:
                    cache.pop(0)
                    cache.append(data)
                    time += 5
            else:
                cache.pop(cache.index(data))
                cache.append(data)
                time += 1
    
    return time
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))