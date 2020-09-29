from flask import Flask

module= Flask(__name__)

 

@module.route("/")
def hello():
 return "Hello from FastCGI via IIS!"

 

if __name__ == '__main__':
    module.run()
