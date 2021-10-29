from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def index():
    return {"msg": "Hello! :wave:"}


def foo(bar: str) -> str:
    string = f"foo{bar}"
    print(string)
    return string
