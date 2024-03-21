from fastapi import FastAPI
from fast_zero.schemas import Message
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/ex', response_class=HTMLResponse)
def read_roots():
    return """
    <html>
    <head>
        <title>Olá Mundo</title>
    </head>
    <body>
        <h1>Olá Mundo!</h1>
    </body>
</html>
"""
        
        


