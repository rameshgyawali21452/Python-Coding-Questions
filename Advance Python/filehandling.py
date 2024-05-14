f = open('love.csv','w')
f.write("s = 'Hey babe how are you , what are you doing'")
f.close()
with open ('love.csv','a') as f:
    f.write("I am back!")
