from flask import Flask
from app import create_App
import sys 

print(sys.path)



app = create_app()



if __name__ == "__main__":
    app.run(debug=True, port=8000)
