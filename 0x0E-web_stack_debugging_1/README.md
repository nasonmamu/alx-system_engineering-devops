# Nginx Configuration Script

## Description
This Bash script automates the configuration of Nginx to listen on port 80.

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script is doing
- Not allowed to use `wget`
- The Bash script must be 5 lines long or less
- Service (init) must indicate that Nginx is not running

## Usage
1. Clone this repository.
2. Make sure the Bash script `1-debugging_made_short` is executable: `chmod +x 1-debugging_made_short`.
3. Run the script: `./1-debugging_made_short`.

## Script
```bash
#!/usr/bin/env bash
# This script configures Nginx to listen on port 80

apt update
apt install -y nginx
service nginx start
sed -i 's/^\(\s*listen\s*\)80/\180/' /etc/nginx/sites-available/default
service nginx restart
Author
Nasonmamu
