# Goal of this app

This app has the goal to show how containerization works, how to make a containerized app secure and finally to show clean Python structured code. Aimed to showcase Python and Docker skills.

## Which security measures has this app implemented?

- Docker:

By default, Docker containers run as the root user, which has unrestricted access to the system. That’s risky—especially if the app is exposed to the internet. Running as a non-root user:

Reduces the risk of hacking due to privileges not being restricted

Limits the damage if the app is compromised

Aligns with security best practices for containerized applications

- Passwords:

We are using Werkzeug as to protect the passwords from being hacked.
More information about it can be found at: https://techmonger.github.io/4/secure-passwords-werkzeug/
