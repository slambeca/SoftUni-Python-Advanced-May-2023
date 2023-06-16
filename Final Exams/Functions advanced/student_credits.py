GOAL = 240


def students_credits(*courses):
    result_from_dict = ""
    points_result_dict = {}
    total_credits = 0

    strings = list(courses)

    for element in strings:
        element_args = element.split("-")
        course_name = element_args[0]
        course_total_credits = int(element_args[1])
        max_test_points = int(element_args[2])
        student_points = int(element_args[3])

        student_score = student_points / max_test_points * course_total_credits
        total_credits += student_score

        points_result_dict[course_name] = student_score

    sorted_dict = dict(sorted(points_result_dict.items(), key=lambda x: -x[1]))

    if total_credits >= GOAL:
        result = f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result = f"Diyan needs {GOAL - total_credits:.1f} credits more for a diploma.\n"

    for key, value in sorted_dict.items():
        result_from_dict += f"{key} - {value:.1f}\n"

    return (result + result_from_dict).strip()


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)