def file_read_write():
    try:
        filename = input("Enter the name of the file to read: ")

       
        with open(filename, "r") as infile:
            content = infile.read()

        # convert content  to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Success! Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file you entered does not exist. Please check the name and try again.")
    except IOError:
        print("Error: Could not read or write the file. Please check permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


file_read_write()
