from git import Repo, GitCommandError

# Configuración del repositorio
repo_url = "https://github.com/tu-organizacion/tu-repo-documentos.git"
local_path = "tu-repo-documentos"

# Clonar el repositorio si no existe localmente
try:
    repo = Repo.clone_from(repo_url, local_path)
    print("Repositorio clonado correctamente.")
except GitCommandError as e:
    print(f"Error al clonar el repositorio: {e}")

# Crear y cambiar a una nueva rama
branch_name = "update-procedures"
try:
    new_branch = repo.create_head(branch_name)
    new_branch.checkout()
    print(f"Cambiado a la nueva rama: {branch_name}")
except GitCommandError as e:
    print(f"Error al crear o cambiar de rama: {e}")

# Realizar cambios en un archivo
file_path = f"{local_path}/docs/procedures/procedure1.txt"
try:
    with open(file_path, 'a') as file:
        file.write("\nNueva actualización de procedimientos al final del documento.")
    repo.git.add(file_path)
    repo.git.commit('-m', 'Actualización de procedimientos')
    print("Cambios guardados y commit realizado.")
except IOError as e:
    print(f"Error al abrir o modificar el archivo: {e}")

# Empujar los cambios al repositorio remoto
try:
    repo.git.push('--set-upstream', 'origin', branch_name)
    print("Cambios subidos al repositorio remoto.")
except GitCommandError as e:
    print(f"Error al subir cambios: {e}")

