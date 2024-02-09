def solution(E):
    max_attendees = 0
    num_employees = len(E)

    # Iterate through all pairs of days
    for day1 in range(9):
        for day2 in range(day1 + 1, 10):
            attendees = 0
            # Count employees who can attend on at least one of the two days
            for availability in E:
                if availability[day1] == '1' or availability[day2] == '1':
                    attendees += 1
            # Update max_attendees if the current count is greater
            max_attendees = max(max_attendees, attendees)

    return max_attendees


# Example usage:
# E = ["1100000000", "0011111100", "0000000011"]
# print(solution(E))  # Output: 3


# Example usage:
E = [
    "039",
    "4",
    "14", "32" , "34" , "7"
]

print(solution(E))  # Output: 3