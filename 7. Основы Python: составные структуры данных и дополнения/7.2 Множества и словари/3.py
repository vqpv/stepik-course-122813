required = set(input().split())
optional = set(input().split())
user_data = set(input().split())

print(required.issubset(user_data) and not user_data - (required | optional))
