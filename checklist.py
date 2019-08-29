checklist = list()

# Define Functions
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item): #check index
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(int(index))
    print(checklist)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))

def mark_completed(index):
    checklist[index] = " √ " + checklist[index]
    # Add code here that marks an item as completed

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)
    # Read item
    elif function_code == "I":
        item_index = int(user_input("Index Number? "))
    # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))
    # Print all items
    elif function_code == "P":
        list_all_items()
    elif function_code == "D":
        input_item = user_input("Destroy Index: ")
        destroy(input_item)
    elif function_code == "R":
        item_index = int(user_input("Return Index: "))
        read(item_index)
        print(read(item_index))
    elif function_code == "U":
         item_index = int(user_input("Update Index: "))
         item_update = user_input("Update Here")
         update(item_index, item_update)
    else:
        return True

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list Press D to Del Press R to Retrun Index Press U to Update Index: ")
    select(selection.upper())
