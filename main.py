import git
def get_status(repo, path):
    changed = [ item.a_path for item in repo.index.diff(None) ]
    if path in repo.untracked_files:
        return 'untracked'
    elif path in changed:
        return 'modified'
    else:
        return 'don''t care'
repo = git.Repo('')
t = repo.head.commit.tree
print(repo.git.diff(t, "--name-only"))