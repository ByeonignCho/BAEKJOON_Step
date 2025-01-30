a, b = input().split()
print( "{}\n{}\n{}\n{}\n{}".\
      #역슬래시 줄 바꿈 가독성 상승(역슬래시 이후 space금지지)
      format(int(a) + int(b),int(a) - int(b), int(a) * int(b),int(a) // int(b),int(a) % int(b)))
      #\n은 string일때 가능해서 format으로 만들기