from app import create_app

app,db,ma,api = create_app(config="config.py")

if __name__ == "__main__":
    app.run()