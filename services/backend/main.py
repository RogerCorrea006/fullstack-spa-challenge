
import uvicorn

if __name__ == "__main__":
    config = uvicorn.Config("src.api:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()