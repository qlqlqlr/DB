# 18429
def count_valid_plans(day, weight, used_kits):
    global result

    if day == N:
        # 모든 날을 계획한 경우
        result += 1
        return

    for i in range(N):
        if i not in used_kits:
            new_weight = weight + kits[i] - K  # 운동 키트를 사용하여 중량 증가, K만큼 중량 감소
            if new_weight >= 500:
                # 중량이 500 이상이면 다음 날짜로 진행
                new_used_kits = used_kits.copy()
                new_used_kits.add(i)
                count_valid_plans(day + 1, new_weight, new_used_kits)

N, K = map(int, input().split())
kits = list(map(int, input().split()))
result = 0

count_valid_plans(0, 500, set())

print(result)
