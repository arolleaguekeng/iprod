
from cx_Freeze import setup, Executable

executables = [
    Executable(script="main.py", icon="noai.ico", base="Win32GUI"),
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.

buildOptions = dict(
    includes=["subprocess", "re", "os", "socket", "shutil", "tkinter"],
    include_files=["wifi.txt", "noai.ico", "stop.png", "partage.png", "noa-i.png"],
)

setup(
    name="i_prod",
    version="0.1",
    description="Application pour un artiste",
    author="AGUEKENG AROLLE DUBOIS",
    options=dict(build_exe=buildOptions),
    executables=executables
)