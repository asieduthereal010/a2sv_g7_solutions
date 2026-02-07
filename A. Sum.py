for _ in range(int(input())):
    input_list = [int(i) for i in input().split(" ")]
    # sorting only 3 numbers is a constant operation. 
    first, last, answer = sorted(input_list)
    if (first + last == answer):
        print("YES")
    else: 
        print("NO")
