#recursive reversing a word
def reverse(word,n):
    if n==0:
        return
    else:
        k=len(word)-n
        reverse(word,n-1)
        print(word[k],end='')
word=input('enter a word::')
reverse(word,len(word))
