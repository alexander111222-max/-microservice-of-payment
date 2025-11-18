import uvicorn
from fastapi import FastAPI



app = FastAPI()






def main():
    uvicorn.run(app)


if __name__ == "__main__":
    main()

