def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for a in asteroids:
        if a > 0:
            stack.append(a)
        else:
            left = True
            while len(stack) > 0:
                l = stack[-1]
                if l < 0:
                    break
                elif a + l == 0:
                    stack.pop()
                    left = False
                    break
                elif a + l < 0:
                    stack.pop()
                elif a + l > 0:
                    left = False
                    break
                else:
                    left = True
                    break
            if left:
                stack.append(a)

    return stack

if __name__ == "__main__":
    asteroids = [-2,-1,1,2]
    print(asteroidCollision(asteroids))