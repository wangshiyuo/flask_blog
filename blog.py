from app import creat_app


app = creat_app()

if __name__ == '__main__':
    app.run(host=app.config.get('HOST'), port=app.config.get('PORT'))
