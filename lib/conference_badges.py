def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    name_lists = [f"Hello, my name is {name}." for name in names]
    return name_lists


def assign_rooms(names):
    i = 1
    room_assignment = [f"Hello, {name}! You'll be assigned to room {ind+1}!" for ind, name in enumerate(names) ] 
    return(room_assignment)


def printer(names):
    badge_creator = (batch_badge_creator(names))
    room_assigner = (assign_rooms(names))
    i=0
    for i in range(len(badge_creator)):
        print(badge_creator[i])
    for i in range(len(room_assigner)):
        print(room_assigner[i])

   


printer(["Arel", "Carol"])
