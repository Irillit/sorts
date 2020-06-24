def counting_sort(inp, out, k):
    count = [0] * k
    for j in range(0, len(inp)):
        count[inp[j]] += 1
    for i in range(0, k):
        count[i] += count[i - 1]
    for j in range(len(inp)):
        out[count[inp[j]] - 2] = inp[j]
        count[inp[j]] -= 1


if __name__ == "__main__":
    A = [0, 6, 7, 1, 5, 4, 7, 8]
    B = [0] * len(A)

    counting_sort(A, B, max(A) + 1)
    print(B)
