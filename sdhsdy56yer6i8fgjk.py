def revere(n):
    arr, i , j = list(range(1, n+1)), 0, n-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1; j -= 1
    return arr

n = int(input("Enter list size: "))
guess = input(f"What is the reverse of {n}?: ")
print(f"Reversed {n} = {revere(n)}, your guess: {guess}")

