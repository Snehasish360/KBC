#kaun banega crorepati
questions=[
    ["Highest score of VIRAT KOHLI in ODI cricket?","one twenty ","one thirty","one fifty","one eighty three",4],
    ["Highest score of ROHIT SHARMA in ODI cricket?","one twenty ","two hundred sixty four","one fifty","one eighty three",2],
    ["Highest score of MS DHONI in ODI cricket?","one twenty ","one thirty","one fifty","one eighty three",4],
    ["Highest score of CRISH GAYLE in ODI cricket?","one twenty ","one thirty","two hundred fifteen","one eighty three",3],
    ["Highest score of SOURAV GANGULY in ODI cricket?","one twenty ","one thirty","one fifty","one eighty three",4],
    ["Highest score of AB DE VILLIERS in ODI cricket?","one twenty ","one thirty","one seventy six","one eighty three",3],
    ["Highest score of SACHIN TENDULKAR in ODI cricket?","two hundred","one thirty","one fifty","one eighty three",1],
    ["Highest score of KANE WILLIAMSON in ODI cricket?","one twenty ","one forty six","one fifty","one eighty three",2],
    ["Highest score of GAUTAM GAMBHIR in ODI cricket?","one twenty ","one thirty","one forty nine","one eighty three",3],
    ["Highest score of KANE WILLIAMSON in ODI cricket?","one forty eight ","one thirty","one fifty","one eighty three",1],
    ["Highest score of VIRENDER SEHWAG in ODI cricket?","one twenty ","one thirty","one fifty","two hundred nineteen",4],
    ["Highest score of KUMAR SANGAKKARA in ODI cricket?","one twenty ","one thirty","one sixty nine","one eighty three",3],
    ["Highest score of SIKHAR DHAWAN in ODI cricket?","one twenty ","one forty three","one fifty","one eighty three",2],
    ["Highest score of KEVIN PETERSEN in ODI cricket?","one twenty ","one thirty","one fifty","one eighty three",2],
    ["Highest score of YUVRAJ SINGH in ODI cricket?","one twenty ","one thirty","one fifty","one eighty three",3],
]
    
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"a. {question[1]}     b.{question[2]}")
    print(f"c. {question[3]}     d.{question[4]}")
    reply = int(input("Enter your answer(1-4) or 0 to quit:"))
    if(reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct Answer, you have won Rs.{levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 10000000
    else:
        print("Wrong Answer!")
        break
print(f"Your take home money is Rs.{money}")
if(money==10000000):
    print("YOU BECOME A CROREPATI!!")
