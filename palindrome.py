def is_palindrome (w):
    ws = w.split(" ")
    word = []
    ws.reverse()
    for i in ws:
        word.append(i[::-1])
    ws_j = "".join(w.split(" "))
    word_j = "".join(word)
    if word_j == ws_j:
        print("Es palíndromo (★ ω ★)")
    else:
        print("No es palíndromo ¯\_(ツ)_/¯")
pali = input("Dime un palíndromo:")
is_palindrome(pali)