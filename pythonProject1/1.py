def get_grouped_user_bills(users):
    result = {}
    all_bills = get_all_bills()
    for user in users:
        result[user.id] = [
            bill for bill in all_bills
            if bill.user.id == user.id
        ]
    return result