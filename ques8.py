#Lab exercise 1: ques8

people = [{"name":"John Doe","age":30,"blood_group":"A+"},
          {"name":"Jane Smith","age":25,"blood_group":"B-"},
          {"name":"Emily Davis","age":40,"blood_group":"O+"},
          {"name":"Michael Brown","age":35,"blood_group":"AB-"},
          {"name":"William Johnson","age":28,"blood_group":"A-"},
          {"name":"Oliver Martinez","age":33,"blood_group":"O-"},
          {"name":"Sophia Anderson","age":27,"blood_group":"AB+"},
          {"name":"James Thomas","age":45,"blood_group":"A+"},
          {"name":"Isabella Lee","age":38,"blood_group":"b-"}
          ]

for i in range(len(people)):
    d = people[i]
    print("Name:",d['name'])
    print("Age:",d['age'])
    print("Blood Group:",d['blood_group'])
    print("-----------------")
    
