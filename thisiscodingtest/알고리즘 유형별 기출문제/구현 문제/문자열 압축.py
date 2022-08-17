# 이 풀이는 사실상 이해가 잘 되지 않았다.
# def solution(s):
#     result=[]
#     if len(s)==1:
#         return 1
#     for i in range(1, (len(s)//2)+1):
#         b = ''
#         cnt = 1
#         tmp=s[:i]

#         for j in range(i, len(s), i):
#             if tmp==s[j:i+j]:
#                 cnt+=1
#             else:
#                 if cnt!=1:
#                     b = b + str(cnt)+tmp
#                 else:
#                     b = b + tmp
#                 tmp=s[j:j+i]
#                 cnt = 1
#         if cnt!=1:
#             b = b + str(cnt) + tmp
#         else:
#             b = b + tmp
                
#         result.append(len(b))
# return min(result)


# 풀긴했는데 시간초과가 나온다...
def solution(s):
    answer = len(s)

    # 문자열을 몇개로 나눌것인가.
    for i in range(1, int(len(s)/2) + 1):
        pos = 0
        length = len(s)

        # unit이 몇번 반복되었는지 드디어 구해졌다!
        while pos + i <= len(s):
            unit = s[pos : pos+i]
            pos += i

            cnt = 0
            while pos + i <= len(s):
                if (unit == s[pos:pos+i]):
                    cnt += 1
                else:
                    break

            if cnt > 0:
                length -= i * cnt

                if cnt < 9:
                    length += 1
                elif cnt < 99:
                    length += 2
                elif cnt < 999:
                    length += 3
                else:
                    length += 4

    answer = min(answer, length)
    return answer

        




