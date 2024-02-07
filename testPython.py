def get_overall_status(filename):
    overall_status_line = None
    overall_status_text = None
    with open(filename, 'r') as file:
        for line in file:
            if 'Overall Status:' in line:
                overall_status_line = line.strip()
                overall_status_text = line.split('Overall Status:')[1].strip()
                break
    return overall_status_line, overall_status_text

if __name__ == "__main__":
    filename = "text.txt" 
    overall_status_line, overall_status_text = get_overall_status(filename)

    if overall_status_line:
        
        print("'Overall Status:' ", overall_status_text)
    else:
        print("No log line containing 'Overall Status:' found in the file.")
