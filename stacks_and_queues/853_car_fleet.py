class Solution:
    def carFleet(self, target, position, speed):
        # Using monotonic increasing stack
        stack = []
        cars = []

        # Create array cars combining position and speed
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        # Sort the array with position
        # We need to compute from the end of the array to the start
        # So we are reversing the array instead
        cars.sort()
        cars = cars[::-1]

        # For every car, we are calculating time time required to reach finish line
        # If current time is greater than last greatest time in stack, append to stack
        # This is because since it is slow it will never form a fleet
        # If not, it means the current car will form a fleet since it is faster
        for p, s in cars:
            time = (target - p) / s
            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)

        # The stack now contains all the different times required in increasing order
        # which means they will never cross each other to form a fleet
        return len(stack)

if __name__=="__main__":
    solution = Solution()
    target = 100
    position = [0, 2, 4]
    speed = [4, 2, 1]

    compute = solution.carFleet(target, position, speed)
    print(compute)
