def print_all_product(array):
    """Print in row all products from table"""
    for row in array:
        print(f"{row['id']}: {row['name']}:=> б - {row['proteins']} || ж - {row['fat']} || у - {row['carbs']} ")