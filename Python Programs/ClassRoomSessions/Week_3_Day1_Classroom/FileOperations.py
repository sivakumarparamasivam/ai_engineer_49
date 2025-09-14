def generate_test_report():
    with open("report.txt", "w") as f:
        f.write("TestCase1 - Passed\n")
        f.write("TestCase2 - Failed\n")
        f.write("TestCase3 - Passed\n")
       

    with open("report.txt", "a") as f:
        f.write("TestCase4 - Passed\n")
        f.write("TestCase5 - Failed\n")
        

    with open("report.txt", "r") as f:
        lines = f.readlines()

    total_tests = 0
    passed_count = 0
    failed_count = 0

    for line in lines:
        line = line.strip()
        print(line)
        total_tests += 1
        if "Passed" in line:
            passed_count += 1
        elif "Failed" in line:
            failed_count += 1

    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f.isClosed())
   

generate_test_report()
