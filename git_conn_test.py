from git import Repo

# $ git clone <url> <local_dir>

local_dir = "C:\\AC_MSc_CS"
repo_url = "https://github.com/acor-uk/AC_MSc_CS.git"

#repo = Repo.clone_from(repo_url, local_dir)
repo = Repo.init(local_dir)

def print_files_from_git(root, level=0):
    for entry in root:
        print(f"{'-' * 4 * level}| {entry.path}, {entry.type}")
        if entry.type == "tree":
            print_files_from_git(entry, level + 1)

print_files_from_git(repo.tree())