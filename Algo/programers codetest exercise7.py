#스택/큐 3번 다리를 지나는 트럭

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]



def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)




    return answer


print(solution(bridge_length, weight, truck_weights))


#뭔가... 계속 하나씩 부족... 그냥 다른 사람 풀이를 보고 이해하기로 하였다.