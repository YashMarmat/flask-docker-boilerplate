### Commands to run (without Docker)

`python3 -m venv myenv`

`source myenv/bin/activate`

`python3 myscript.py`

* visit => http://127.0.0.1:5000

`ctrl + c` (to quit the server)

`deactivate` (to quit virtual env)

### Commands to run (with Docker)

`docker compose up --build`

* visit => http://127.0.0.1:8000 (on local machine)
* http://127.0.0.1:5000 (flask will be running at this port in docker container)

`ctrl + c` (to stop/exit the docker container)

`docker compose down` (to remove the docker container)
