import requests
import json
from collections import defaultdict

# Function to fetch users and deals from HubSpot API
def fetch_users_and_deals():
    url = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=b0d0a4995dc14960dfff6b4ff130'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        return data.get('users', []), data.get('deals', [])
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return [], []


# Function to process permissions and generate results
def process_permissions(users, deals):
    results = []

    # Create a mapping of dealId to ownerUserId
    deal_owner_map = {deal['dealId']: deal['ownerUserId'] for deal in deals}

    # Create a mapping of teamId to list of userIds
    user_team_map = defaultdict(list)
    for user in users:
        for team_id in user.get('teamIds', []):
            user_team_map[team_id].append(user['userId'])

    all_deal_ids_list = list(deal_owner_map.keys())

    for user in users:
        user_id = user['userId']
        view_permission_level = user.get('viewPermissionLevel', 'NONE')
        edit_permission_level = user.get('editPermissionLevel', 'NONE')

        user_result = {
            'userId': user_id,
            'viewableDealIds': [],
            'editableDealIds': []
        }

        # Determine viewableDealIds
        if view_permission_level == 'NONE':
            user_result['viewableDealIds'] = []
        elif view_permission_level == 'OWNED_ONLY':
            user_result['viewableDealIds'] = [deal_id for deal_id, owner_id in deal_owner_map.items() if owner_id == user_id]
        elif view_permission_level == 'OWNED_OR_TEAM':
            user_and_team_deals = set()
            user_and_team_deals.update(deal_id for deal_id, owner_id in deal_owner_map.items() if owner_id == user_id)
            for team_id in user.get('teamIds', []):
                for team_user_id in user_team_map.get(team_id, []):
                    user_and_team_deals.update(deal_id for deal_id, owner_id in deal_owner_map.items() if owner_id == team_user_id)
            user_result['viewableDealIds'] = list(user_and_team_deals)
        elif view_permission_level == 'ALL':
            user_result['viewableDealIds'] = all_deal_ids_list

        # Determine editableDealIds
        if edit_permission_level == 'NONE':
            user_result['editableDealIds'] = []
        elif edit_permission_level == 'OWNED_ONLY':
            user_result['editableDealIds'] = [deal_id for deal_id, owner_id in deal_owner_map.items() if owner_id == user_id]
        elif edit_permission_level == 'OWNED_OR_TEAM':
            user_and_team_deals = set()
            user_and_team_deals.update(deal_id for deal_id, owner_id in deal_owner_map.items() if owner_id == user_id)
            for team_id in user.get('teamIds', []):
                for team_user_id in user_team_map.get(team_id, []):
                    user_and_team_deals.update(deal_id for deal_id, owner_id in deal_owner_map.items() if owner_id == team_user_id)
            user_result['editableDealIds'] = list(user_and_team_deals)
        elif edit_permission_level == 'ALL':
            user_result['editableDealIds'] = all_deal_ids_list

        user_result['viewableDealIds'].sort()
        user_result['editableDealIds'].sort()

        results.append(user_result)

    return results

# Function to post results to an API endpoint
def post_results(results):
    url = 'https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=b0d0a4995dc14960dfff6b4ff130'
    headers = {'Content-Type': 'application/json'}
    json_payload = json.dumps({'results': results})

    try:
        response = requests.post(url, data=json_payload, headers=headers)
        response.raise_for_status()
        print("Results successfully posted.")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Failed to post results: {e}")

# Fetch users and deals
users, deals = fetch_users_and_deals()

if users and deals:
    # Process permissions
    results = process_permissions(users, deals)
    print(json.dumps({'results': results}))
    post_results(results)
else:
    print("No data fetched from API.")