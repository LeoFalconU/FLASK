# FLASK

## Overview

This Flask application reads device data from `API.json` and defines routes for returning device information and sample JSON data.

`API.json` is loaded when `app.py` is imported, using a path relative to the current working directory. Run the app from the project directory and ensure that file is present.

## Routes declared in `app.py`

The routes use Flask’s default method, `GET`.

| URL | View function | Behavior |
|---|---|---|
| `/` | `inicio` | Prints `Cambio` and `Hola`, then returns `datos_json["3D:RF:09:7F"]`. |
| `/json/<mac>` | `json_data` | Looks up the device using `<mac>`, prints its `Protocolos`, `VLANs`, and `Status`, then returns its `Name`. |
| `/api/saludo` | `saludo` | Returns JSON records `101`–`105`, each containing `ip`, `name`, `policy`, and `status`. |
| `/api/saludo` | `funcion1` | An unfinished handler with no return value. |

### Visual route map

```text
Flask app
├── GET /
│   └── inicio
│       ├── Prints "Cambio" and "Hola"
│       └── Returns datos_json["3D:RF:09:7F"]
├── GET /json/<mac>
│   └── json_data(mac)
│       ├── Looks up datos_json[mac]
│       ├── Prints Protocolos, VLANs, and Status
│       └── Returns the device Name
└── GET /api/saludo
    ├── saludo
    │   └── Returns JSON records 101–105
    └── funcion1
        └── Incomplete; returns no response
```

## Issues to address

- `/` is declared six times with the same endpoint name, `inicio`. Flask will raise an `AssertionError` while importing `app.py` because the endpoint is registered with different function objects.
- `/api/saludo` is declared twice. `funcion1` has no response implementation; remove it or give it a distinct URL and a valid response.
- `json_data` assumes the requested MAC address exists and its record contains all referenced keys. Unknown or incomplete records will cause an error.
- The code enables Flask debug mode. Use debug mode only during local development.

As written, the duplicate `/` declarations prevent the application from starting, so the routes above document the declarations in the source, not a currently working app.

## Run locally

From the project directory:

```bash
python app.py
```
