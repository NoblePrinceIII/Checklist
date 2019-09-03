checklist = list()


# Create
def create(item):
    checklist.append(item)


# Read
def read(index):
    return checklist[index]


# Update
def update(index, item):
    checklist[index] = item


# Destroy
def destroy(index):
    checklist.pop(int(index))
    print(checklist)


# Lists of all items
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


# marks item completed
def mark_completed(index):
    checklist[index] = " √ " + checklist[index]


# user inputs
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def select(function_code):
    try:
        # Creates Item on the List
        if function_code == "C":
            input_item = user_input("Input item: ")
            create(input_item)
            # Reads List
        elif function_code == "R":
            item_index = int(user_input("R to read index: "))
            print(read(item_index))
            # Update Index
        elif function_code == "U":
            try:
                item_index = int(user_input("Update Index: "))
                item_update = user_input("Update Here: ")
                update(item_index, item_update)
                return True
            except ValueError:
                print("Invalid Input")
            # Destroy's an item in Index
        elif function_code == "D":
            item_index = int(user_input("Index Number: "))
            destroy(item_index)
        # Shows whats in Index
        elif function_code == "P":
            list_all_items()

        # Allows user to checklist
        elif function_code == "X":
            item_index = int(user_input("X index to complete: "))
            mark_completed(item_index)

            return True
    except:
        print("Invalid Notation or No Index")

# def test():
#     create("purple sox")
#     create("red cloak")
#     print(read(0))
#     print(read(1))#     destroy(1)
#     print(read(0))
#     list_all_items()
# test()


running = True

while running:
    selection = user_input(
        "Press C create list, R to read Index " +
        "Press U to Update Index P to " +
        "display list Press D to Delete Press X when completed: ")
    select(selection.upper())
