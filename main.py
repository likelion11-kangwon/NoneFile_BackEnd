import uvicorn

host = "127.0.0.1"
port = 8000
app_name = "Router.router:app"

if __name__ == "__main__":
    config = uvicorn.Config(app=app_name, host=host, port=port)
    server = uvicorn.Server(config=config)
    server.run()
