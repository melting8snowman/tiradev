from invoke import task
# run by : poetry run invoke #taskname

@task
def start(ctx):
    ctx.run("python src/connectfour.py")

@task
def start3(ctx):
    ctx.run("python3 src/connectfour.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage report -m")
    ctx.run("coverage html")
