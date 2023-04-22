from fastapi import FastAPI


app = FastAPI()

cursos = {
    1: {
        "titulo": "programação para leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "algoritmos e lógica de programação",
        "aulas": 87,
        "horas": 22
    }
}


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    curso = cursos[curso_id]
    curso.update({"id": curso_id})

    return curso


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, debug=True, reload=True)
