Height=int(input("Enter the height:"))
Width=int(input("Enter the width:"))
for row in range (Height):
    for col in range (Width):
        value = (row * Width + col) % 10
        print(f"{value:2d}", end=" ")
    print()