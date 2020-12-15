# 오답노트

## dfs,bfs_1.py

다음 중 어디가 틀린 것일까?

```python
    # 상하좌우 체크
    for i in range(4):
        x = n + dn[i]
        y = n + dm[i]
        print(f'check {x},{y}')
        if x >= 0 and x < N and y >= 0 and y < M: # in map
            if map[x][y] == '0': # valid. 1 is invalid
                if not visited[x][y]:
                    print(direction[i])
                    dfs(map, x, y)
```

정말 단순한 실수이다. **y = n + dm[i] >> y = m + dm[i]**  
이거 때문에 계속 안되서 고민하고, 오히려 낙담하고 1시간은 버린듯 하다.  

이러한 실수를 줄이는 방법은?  

그냥 너무 마음이 조급해서 그런 것은 아닐까?  
예상치 못하게 잘 안되는 경우에는,  
오타가 없나 먼저 점검할 것.  

그리고, **if 조건문도 중첩해도 되니까 오히려 이해하기 쉽게 사용할 것**  
나는 특히 if 조건문 잘못 작성해서 오작동하는 경우가 많은 듯.  