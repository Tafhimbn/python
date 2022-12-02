first_name = input("Enter First Name: ")
last_name = input("Enter Second Name: ")
full_name = first_name +" "+last_name
id, semester=input("Enter Student ID & Semester: ").split()
cgpa = float(input("Enter Current CGPA: "))

#circuit_marks, machine_marks, programming_marks, managment_marks = input("Enter Circuit, Machine, Programming & Managment Marks(Keep \",\" between marks): ").split(",")
circuit_marks, machine_marks, programming_marks, managment_marks = input("Enter Circuit, Machine, Programming & Managment Marks(Keep space between marks): ").split(" ")

total_marks = int(circuit_marks) + int(machine_marks) + int(programming_marks) + int(managment_marks)
average_marks = total_marks / 4

print("Name: " + full_name)
print("ID: " + str(id))
print("ID: " + str(semester))
print("CGPA: "+ str(cgpa))
print("Total Marks: " + str(total_marks))
print("Average marks: " + str(average_marks))
print("")
print("Name: "+ str(type(full_name)))
print("ID: "+ str(type(id)))
print("CGPA: "+ str(type(cgpa)))
print("Total Marks: "+ str(type(total_marks)))
print("Average marks: "+ str(type(average_marks)))