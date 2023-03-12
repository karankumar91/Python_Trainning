import requests
import json

# Set up authentication using a personal access token
base_url="https://api.github.com/"
token="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"
headers = {
    'Authorization': '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'
}

# Define the parameters for the new team
data = {
    'name': 'new-team',
    'description': 'This is a new team',
    'permission': 'push'
}

# Send a request to create the new team
response = requests.post('https://api.github.com/', headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 201:
    print('New team created successfully')
else:
    print('Error creating new team:', response.text)

# Get information about a team
team_id = response.json()['id']
response = requests.get(f'https://api.github.com/teams/{team_id}', headers=headers)

# Check if the request was successful
if response.status_code == 200:
    team_data = response.json()
    print(f'Team name: {team_data["name"]}')
    print(f'Team description: {team_data["description"]}')
    print(f'Team permission: {team_data["permission"]}')
else:
    print('Error getting team information:', response.text)

# Update a team's information
data = {
    'name': 'updated-team-name',
    'description': 'This is an updated team',
    'permission': 'pull'
}
response = requests.patch(f'https://api.github.com/teams/{team_id}', headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    print('Team updated successfully')
else:
    print('Error updating team:', response.text)

# Add a team member
username = 'myusername'
response = requests.put(f'https://api.github.com/teams/{team_id}/memberships/{username}', headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print(f'User {username} added to the team')
else:
    print('Error adding user to team:', response.text)

# Remove a team member
response = requests.delete(f'https://api.github.com/teams/{team_id}/memberships/{username}', headers=headers)

# Check if the request was successful
if response.status_code == 204:
    print(f'User {username} removed from the team')
else:
    print('Error removing user from team:', response.text)

# Delete a team
response = requests.delete(f'https://api.github.com/teams/{team_id}', headers=headers)

# Check if the request was successful
if response.status_code == 204:
    print('Team deleted successfully')
else:
    print('Error deleting team:', response.text)
