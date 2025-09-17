# export FLASK_APP=wsgi.py
# flask run

# Email: admin@cirec.net
# Password: cirec_admin_123


from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
