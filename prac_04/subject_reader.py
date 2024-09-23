def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # Convert student number to integer value
            data.append(parts)  # Add the list to data
    return data

def display_subject_details(subject_data):
    for subject in subject_data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students in total")

def main():
    subject_data = load_data('subject_data.txt')
    display_subject_details(subject_data)

if __name__ == "__main__":
    main()
