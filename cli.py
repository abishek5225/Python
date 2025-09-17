
def do_something(name): 
    print(name)
    process_file(name)

def process_file(name):
    print('Processed file')


name = input("Enter prompt: ")
do_something(name)