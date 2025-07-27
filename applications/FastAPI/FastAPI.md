# FastAPI

books:
* Lubanovic, Bill. **FastAPI: Modern Python Web Development**. 2023. O’Reilly.
  * 我们将构建一个中型网络服务，用于访问和管理关于神秘生物（虚构的生物creatures）以及寻找它们的虚构探险家explorers的数据。

code structure:
```shell
src/
  web           # web layer
  service       # business logic layer
  data          # storage interface layer
  model         # Pydantic model definitions
  fake          # stub data
  test          # test: e.g. pytest
    unit        # unit tests, not cross layers
      web
      service
      data
    integration # integration tests
    full        # end-to-end/contract tests
  main.py       # start Uvicorn program and FastAPI package
  errors.py     # exceptions
  auth.py       # authentication

# each folder
__init__.py     # package
creature.py     # creature code for this layer - 生物
explorer.py     # explorer code for this layer - 探险家
```

routers:
- `APIRouter`

FastAPI endpoints:
- `/docs`
- `/redocs`

data layer pagination, sorting:
- `offset`, `size`
- `sort`

SLA consideration
- logging 
- metrics: Prometheus, Grafana
- monitoring/observability
- tracing: OpenTelemetry - https://opentelemetry.io/docs/languages/python/

secutiry:
- Authentication: authn
  - username/password
  - API key
  - OAuth2: `python-jose[cryptography]`, `passlib`, `python-multipart`
  - JWT
- Authorization: authz

automated full testing
- property-based testing: openapi.json - `hypothesis`, `schemathesis`

load testing
- `locust`, `locust-grasshopper`

production
- Gunicorn
- HTTPS
- Docker

files:
* https://github.com/Kludex/python-multipart
* https://github.com/Tinche/aiofiles
* `File()`
* `UploadFile`
* `FileResponse`
* `StreamingResponse`
* `StaticFiles`

forms, templates
- `Form`
- `Jinja2Templates`

data discovery and visualization
- CSV, TSV, PSV
- python-tabulate: https://github.com/astanin/python-tabulate
- pandas
- Matplotlib, Plotly, Dash, Seaborn, Bokeh
- Map: PyGIS, PySAL, Cartopy, Folium, Python Client for Google Maps Services, Geemap, Geoplot, GeoPandas, ArcGIS, ArchPy

games
- Adventurelib
- PyGame, primer
- pyglet
- Python Arcade
- HARFANG
- Panda3D