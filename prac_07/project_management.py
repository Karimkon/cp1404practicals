import csv
from datetime import datetime
from project import Project


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip header
        for row in reader:
            name, start_date, priority, cost_estimate, completion_percentage = row
            projects.append(Project(
                name,
                datetime.strptime(start_date, "%d/%m/%Y"),
                int(priority),
                float(cost_estimate),
                int(completion_percentage)
            ))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow(
                [project.name, project.start_date.strftime("%d/%m/%Y"), project.priority, project.cost_estimate,
                 project.completion_percentage])


def display_projects(projects):
    incomplete_projects = [p for p in projects if not p.is_complete()]
    completed_projects = [p for p in projects if p.is_complete()]
    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    filtered = [p for p in projects if p.start_date > date]
    filtered.sort()
    return filtered


def add_project(projects):
    name = input("Name: ")
    start_date = datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]

    print(project)
    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


def main():
    projects = load_projects('projects.txt')
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif choice == 's':
            filename = input("Filename to save: ")
            save_projects(filename, projects)
            print(f"Saved projects to {filename}")

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.strptime(date_str, "%d/%m/%Y")
            filtered_projects = filter_projects_by_date(projects, date)
            for project in filtered_projects:
                print(project)

        elif choice == 'a':
            add_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            if input("Do you want to save before quitting? (y/n) ").lower() == 'y':
                save_projects('projects.txt', projects)
            break


if __name__ == '__main__':
    main()
