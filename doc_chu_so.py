'''Vào một ngày đẹp trời, Bình được giám đốc giao cho viết 1 con AI có khả năng đọc số thành văn bản.
 Nghĩ mãi nhưng vẫn bế tắc, bạn hãy giúp Bình thử xem nhé. Yêu cầu như sau:
     Hãy viết một hàm với tên là convert_text nhận đối số đầu vào là một số nguyên dương. 
     Hàm này sau đó sẽ biến đổi và trả về các chữ số của số đầu vào thành một xâu ký tự tương 
     ứng với các chữ số có mặt trong nó dưới dạng văn bản đọc 
     tương ứng với nó: 0 thành zero. 1 thành one, 2 thành two, 3 thành three, 4 thành four,.... Chẳng hạn
'''
def convert_text(n):
    i=0
    lis = []
    lis1 = []
    b=n
    while n!=0:
        a = n % 10
        lis.append(int(a))
        n -= a
        n /=10
    lis=lis[::-1]
    while i<len(str(b)):
        lis1.append(text_number[lis[i]])
        i+=1
    l=" ".join(lis1)
    return l
text_number = ['zero','one','two','three','four','five','six','seven','eight','nine']
n=int(input())
print(convert_text(n))




