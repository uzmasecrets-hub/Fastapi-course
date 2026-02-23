from fastapi import FastAPI

# Create the FastAPI application instance
# This `app` object is our entire web server
app = FastAPI(
    title="My First FastAPI App",
    description="A beginner-friendly FastAPI example built in the Udemy course",
    version="1.0.0",
)


# --- Route 1: Root endpoint ---
# @app.get("/") means: handle GET requests to the "/" path
@app.get("/")
async def root():
    """
    The homepage of our API.
    Returns a simple greeting message.
    """
    return {"message": "Hello World"}


# --- Route 2: A slightly more interesting endpoint ---
# Real-world example: an API status/health check endpoint
# Almost every production API has one of these
@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Used by load balancers, monitoring tools, and DevOps pipelines
    to verify the API is running correctly.
    """
    return {
        "status": "healthy",
        "service": "fastapi-course",
        "version": "1.0.0",
    }


# --- Route 3: About endpoint ---
# Another common real-world pattern
@app.get("/about")
async def about():
    """
    Returns information about this API.
    """
    return {
        "name": "FastAPI Course Example",
        "description": "Your first FastAPI application",
        "author": "Your Name",
        "docs": "Visit /docs for interactive API documentation",
    }
