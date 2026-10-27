# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000


def evaluate_student(student):
    marks = student["marks"]
    total = sum(marks)
    aggregate = total / len(marks)

    student["total"] = total
    student["aggregate"] = aggregate
    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate marks below 75%")

    if any(mark < MIN_SUBJECT_MARKS for mark in marks):
        reasons.append("Subject-wise minimum marks not met")

    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if student["income"] > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 2,50,000")

    student["reasons"] = reasons
    student["eligible"] = len(reasons) == 0


def main():
    students = []
    n = int(input("Enter number of applicants: "))

    if n <= 0:
        print("Number of applicants must be positive.")
        return

    for i in range(n):
        print(f"\nApplicant {i + 1}")

        app_id = int(input("Application ID: "))
        name = input("Student name: ")

        subject_count = int(input("Number of subjects: "))
        if subject_count <= 0:
            print("Number of subjects must be positive.")
            return

        marks = []
        for j in range(subject_count):
            mark = float(input(
                f"Marks for subject {j + 1} (out of 100): "
            ))
            marks.append(mark)

        attendance = float(input("Attendance percentage: "))
        income = float(input("Annual family income (Rs.): "))

        student = {
            "id": app_id,
            "name": name,
            "marks": marks,
            "attendance": attendance,
            "income": income
        }

        evaluate_student(student)
        students.append(student)

    eligible = [s for s in students if s["eligible"]]
    rejected = [s for s in students if not s["eligible"]]

    # Tie-breaking priority:
    # 1. Higher aggregate
    # 2. Higher attendance
    # 3. Higher total marks
    # 4. Lower application ID
    eligible.sort(key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        -s["total"],
        s["id"]
    ))

    print("\n===== SCHOLARSHIP MERIT LIST =====")

    if eligible:
        for rank, s in enumerate(eligible, start=1):
            print(
                f"Rank {rank}: ID={s['id']}, "
                f"Name={s['name']}, "
                f"Aggregate={s['aggregate']:.2f}%, "
                f"Attendance={s['attendance']:.2f}%"
            )
    else:
        print("No eligible applicants.")

    print("\n===== INELIGIBLE APPLICANTS =====")

    if rejected:
        for s in rejected:
            print(f"ID={s['id']}, Name={s['name']}")
            print("Reasons: " + ", ".join(s["reasons"]))
    else:
        print("No ineligible applicants.")


if __name__ == "__main__":
    main()
