from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
from routes.index import user

app.include_router(user)


# Define your allowed hosts
ALLOWED_HOSTS = {"example.com", "www.example.com", "127.0.0.1:8000", "localhost:8000","localhost:3000","127.0.0.1:3000"}

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow all origins (use specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.middleware("http")
async def allowed_hosts_middleware(request: Request, call_next):
    # Get the host from the request headers
    print(request.headers)
    host = request.headers.get("host", "").lower()
    print(host,'----------------')

    if host not in ALLOWED_HOSTS:
        # Return 403 Forbidden if the host is not allowed
        return JSONResponse(
            content={"detail": "Host not allowed"},
            status_code=403,
        )

    # Continue processing the request
    response = await call_next(request)
    return response