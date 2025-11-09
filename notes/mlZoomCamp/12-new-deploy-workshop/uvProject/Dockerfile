FROM python:3.12.1


# we always want to start with the python version then install the package manager.
RUN pip install uv

# then we set the working environment that is inside the container
WORKDIR /app


# then we copy python version, pyproject, and uvlock into our ./(working directory)
COPY .python-version pyproject.toml uv.lock ./

# install dependencies
RUN uv sync --locked


# copy our web service and our model into our working directory
COPY main.py model.bin ./

# let docker know that we will run something on this port
EXPOSE 9696


# sets the command to run the web service
ENTRYPOINT [ "uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0","--port", "9696"]