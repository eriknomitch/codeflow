from dotenv import load_dotenv

load_dotenv()

import os
from pathlib import Path


from llama_index import download_loader, VectorStoreIndex, ServiceContext
download_loader("GithubRepositoryReader")

from llama_hub.github_repo import GithubRepositoryReader, GithubClient

github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
loader = GithubRepositoryReader(
    github_client,
    owner =                  "StoryMagic",
    repo =                   "story-magic-web",
    filter_directories =     (["pages"], GithubRepositoryReader.FilterType.INCLUDE),
    filter_file_extensions = ([".ts", ".tsx"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose =                True,
    concurrent_requests =    10,
)

docs = loader.load_data(branch="main")
# alternatively, load from a specific commit:
# docs = loader.load_data(commit_sha="a6c89159bf8e7086bea2f4305cff3f0a4102e370")

for doc in docs:
    print(doc.extra_info)
