from extra.linked_list import add_tail, imprimir, reverse

if __name__ == "__main__":
    data = [1,2,3,4,5]
    head = None

    for d in data:
        head = add_tail(head, d)
    imprimir(head)
    print("\nreversed")
    r = reverse(head)
    imprimir(r)