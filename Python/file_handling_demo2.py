input_file_name = "Rust_logo.png"
output_file_name = "copy.png"
with open(input_file_name,"rb") as input:
    with open(output_file_name,"wb") as output:
        output.write(input.read())