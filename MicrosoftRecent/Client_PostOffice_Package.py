def deliver(clients):
    max_count = 0
    shelf_count = 0
    max_client = 0

    for client in clients:
        if client > max_client:
            shelf_count += client - max_client - 1

        else:
            shelf_count -= 1

        max_count = max(max_count, shelf_count)
        max_client = max(max_client, client)

    return max_count


print(deliver([3, 2, 7, 4, 5, 6, 1]))