# FLASK

## Overview

This Flask app serves network-device data and an in-memory collection of server records. The primary application is `app.py`; it loads device data from `API.json` and initializes server records `101` through `105` in `servidores_db`.

The server dictionary is in memory only. Changes made through the API are lost when the process restarts.

## Setup and run

From the project directory, install dependencies and start the development server:

```bash
python -m pip install -r req.txt
python app.py
```

The app listens on `http://127.0.0.1:5000/` and runs with Flask debug mode enabled. Do not expose the debug server publicly.

## API routes

All routes in `app.py` currently accept `GET` requests.

| URL | Function | Behavior |
|---|---|---|
| `/` | `inicio` | Prints `Cambio` and `Hola`; returns the device value for MAC `3D:RF:09:7F`, or `No encontrado` if the key is absent. |
| `/json/<mac>` | `json_data` | Looks up a MAC in `datos_json`, prints its protocols, VLANs, and status, and returns its name. Returns a JSON error with HTTP 404 if the MAC is absent. |
| `/api/saludo` | `saludo` | Returns the complete `servidores_db` dictionary as JSON. |
| `/api/servidor/101` | `obtener_servidor_101` | Returns server `101` as JSON. |
| `/api/servidor/102` | `obtener_servidor_102` | Returns server `102` as JSON. |
| `/api/servidor/103` | `obtener_servidor_103` | Returns server `103` as JSON. |
| `/api/servidor/104` | `obtener_servidor_104` | Returns server `104` as JSON. |
| `/api/servidor/105` | `obtener_servidor_105` | Returns server `105` as JSON. |
| `/api/servidores/filtrar/estado/<estado>` | `filtrar_por_estado` | Returns servers whose status matches `<estado>` without regard to letter case. |
| `/api/servidores/filtrar/politica/<politica>` | `filtrar_por_politica` | Returns servers whose policy matches `<politica>` without regard to letter case. |
| `/api/servidores/agregar/<id_servidor>/<ip>/<name>/<policy>/<status>` | `agregar_servidor` | Adds a server record, or replaces the record if that ID already exists; returns the saved data as JSON. |
| `/api/servidores/actualizar_estado/<id_servidor>/<nuevo_estado>` | `actualizar_estado` | Updates the status of an existing server. Returns HTTP 404 if the ID is absent. |
| `/api/servidores/eliminar/<id_servidor>` | `eliminar_servidor` | Deletes an existing server and returns the removed data. Returns HTTP 404 if the ID is absent. |

### Visual route map

```text
Flask app (app.py)
├── GET /
│   └── inicio: return the default MAC's data
├── GET /json/<mac>
│   └── json_data: return a device name or 404
└── Server records (servidores_db)
    ├── GET /api/saludo
    │   └── saludo: return all records
    ├── GET /api/servidor/101
    ├── GET /api/servidor/102
    ├── GET /api/servidor/103
    ├── GET /api/servidor/104
    ├── GET /api/servidor/105
    │   └── Each returns its individual record
    ├── GET /api/servidores/filtrar/estado/<estado>
    ├── GET /api/servidores/filtrar/politica/<politica>
    │   └── Filter records by status or policy
    ├── GET /api/servidores/agregar/<id_servidor>/<ip>/<name>/<policy>/<status>
    ├── GET /api/servidores/actualizar_estado/<id_servidor>/<nuevo_estado>
    └── GET /api/servidores/eliminar/<id_servidor>
        └── Add, update, or delete an in-memory record
```

## Implementation notes

- The add, update, and delete operations mutate server data through `GET` routes. For a future API, use `POST`, `PATCH`, and `DELETE` respectively, with request data in a JSON body.
- The source opens `API.json`, while the tracked data file is named `api.json`. This may work on a case-insensitive macOS filesystem but fail on case-sensitive systems; make the filename and source reference match before deployment.
- If `API.json` is missing, `app.py` uses a string fallback for the default MAC. `/` can return that value, but `/json/<mac>` expects device records to be dictionaries.
- `copiaapp.py` is a separate, older draft. It contains repeated `/` routes using the same endpoint name, so Flask can raise an assertion error when that module is imported. Run `app.py`, not `copiaapp.py`.
