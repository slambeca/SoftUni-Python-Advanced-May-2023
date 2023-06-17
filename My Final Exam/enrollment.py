def gather_credits(credits_needed, *courses):
    credits_taken = 0
    already_enrolled_courses = []

    for course in courses:
        course_name = course[0]
        course_credits = course[1]

        if course_name in already_enrolled_courses:
            continue

        if credits_taken >= credits_needed:
            break

        credits_taken += course_credits
        already_enrolled_courses.append(course_name)

    if credits_taken >= credits_needed:
        already_enrolled_courses.sort()
        result = f"Enrollment finished! Maximum credits: {credits_taken}.\n"
        result += f"Courses: {', '.join(already_enrolled_courses)}"
    else:
        result = f"You need to enroll in more courses! You have to gather {credits_needed - credits_taken} " \
                     f"credits more."

    return result.strip()


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
