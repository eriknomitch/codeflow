import os

from llama_index import download_loader
download_loader("GithubRepositoryReader")

from llama_hub.github_repo import GithubRepositoryReader, GithubClient

github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
loader = GithubRepositoryReader(
    github_client,
    owner =                  "jerryjliu",
    repo =                   "llama_index",
    filter_directories =     (["gpt_index", "docs"], GithubRepositoryReader.FilterType.INCLUDE),
    filter_file_extensions = ([".py"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose =                True,
    concurrent_requests =    10,
)

docs = loader.load_data(branch="main")
# alternatively, load from a specific commit:
# docs = loader.load_data(commit_sha="a6c89159bf8e7086bea2f4305cff3f0a4102e370")

for doc in docs:
    print(doc.extra_info)
