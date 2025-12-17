def generate_certificate(level, score):
    file_name = f"certificates/{level.lower()}_certificate.txt"

    with open(file_name, "w") as f:
        f.write("PYTHON COURSE CERTIFICATE\n")
        f.write("-------------------------\n")
        f.write(f"Level Completed: {level}\n")
        f.write(f"Score: {score}\n")
        f.write("Status: PASSED\n")

    print("Certificate Generated:", file_name)
