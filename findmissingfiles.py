import sys

n = len(sys.argv)
print("Total arguments passed:", n)

if len(sys.argv) == 3:
    my_file = open(sys.argv[1], "r")
    my_file_2 = open(sys.argv[2], "r")

    source1 = my_file.read()
    source1_list = source1.split("\n")

    source2 = my_file_2.read()
    source2_list = source2.split("\n")

    print("Size of list: ", len(source1_list))
    print("Size of 2nd list: ", len(source2_list))

    set_of_files_in_source = set(source2_list)

    missing_files_between_source_and_dest = [x for x in source1_list if x not in set_of_files_in_source]

    #print(missing_files_between_source_and_dest)

    print("# of missing files : ", len(missing_files_between_source_and_dest))
    missing_files = open("missing_files.txt", "w")

    for missing_file in missing_files_between_source_and_dest:
        missing_files.write(missing_file + "\n")

    #missing_files.writelines(missing_files_between_source_and_dest)
    missing_files.close()
    
else:
    print("Not the right number of args!")
