from github import Github

github = Github('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')

repository = github.get_repo('Parveer-B/Pressure-Graphs-Grafana')

with open('uploads/extorrdata.csv', 'r') as file:
    data = file.read()

repository.create_file('uploads/dataset.csv', 'upload csv', data, branch='main')