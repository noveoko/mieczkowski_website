import secrets

# Generate a secure random string
random_string = secrets.token_hex(16)  # 16 bytes = 32 characters

# Replace the SECRET_KEY value in config.py
with open('config.py', 'r') as f:
    config_lines = f.readlines()

with open('config.py', 'w') as f:
    for line in config_lines:
        if line.startswith('SECRET_KEY'):
            f.write(f"SECRET_KEY = '{random_string}'\n")
        else:
            f.write(line)