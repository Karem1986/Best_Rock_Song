# Goal of this app

This app has the goal to show how containerization works, how to make a containerized app secure and finally to show clean Python structured code. Aimed to showcase Python and Docker skills.

## Which security measures has this app implemented?

- Docker:

By default, Docker containers run as the root user, which has unrestricted access to the system. That’s risky—especially if the app is exposed to the internet. Running as a non-root user:

Reduces the risk of hacking due to privileges not being restricted

Limits the damage if the app is compromised

- Passwords:

We are using Werkzeug as to protect the passwords from being hacked.
More information about it can be found at: https://techmonger.github.io/4/secure-passwords-werkzeug/

## Testing flask routes

For this I used Curl and Postman.
If testing with Curl, first start the server with:

```python main_app.py```

Optionally, use postman but delete trailing spaces right after the url with the backspace keyboard. Select POST from the dropdown menu and in select in headers raw/JSON.

Curl command example:

curl -X POST -H "Content-Type: application/json" \
    -d '{"username":"karin","email":"<email@email.com>","password":"5555"}' \
<http://127.0.0.1:8080/signup>

Be aware that testing this command will only work in git bash, powershell requires a different syntax.
More information at:

<https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask>

In "Usin JSON Data".

## Next steps

Explore new tools like apache airflow and https://www.getdbt.com/blog/what-exactly-is-dbt
