import requests

def fetch_and_process_users(sort_key='name', descending=False):
    """
    Fetches, processes, and sorts user data from JSONPlaceholder API.
    Default sorting is by name in ascending order.

    Args:
        sort_key (str): The key to sort by ('id', 'name', or 'company_name').
        descending (bool): Whether to sort in descending order.

    Returns:
        list: A list of dictionaries containing user info.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        # Fetch user data
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        user_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return []

    # Process user data
    processed_users = [
        {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'company_name': user['company']['name']
        }
        for user in user_data
    ]

    # Validate sort key
    valid_keys = {'id', 'name', 'company_name'}
    if sort_key not in valid_keys:
        raise ValueError(f"Invalid sort key. Choose from {valid_keys}")

    # Sort users
    return sorted(processed_users, key=lambda x: x[sort_key], reverse=descending)

# Example usage
if __name__ == "__main__":
    users_sorted_by_name = fetch_and_process_users(sort_key='name')
    users_sorted_by_company = fetch_and_process_users(sort_key='company_name')
    users_sorted_by_id_desc = fetch_and_process_users(sort_key='id', descending=True)

    print("Sorted by Name:", users_sorted_by_name[:3])  # Print first 3 results
    print("Sorted by Company:", users_sorted_by_company[:3])
    print("Sorted by ID (Descending):", users_sorted_by_id_desc[:3])
