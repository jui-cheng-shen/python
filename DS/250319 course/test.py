data = input()

data.split() #if input: "add 11", then output: ['add', '11']

data.split()[0] #if input: "add 11", then output: 'add'
#[0] 不再split()的括號內是因為split()是將字串分割成list，所以要用list的方式取值
print()
input()

#[0]