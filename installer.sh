if [ -f "gitautoenv" ]; then
    ./gitautoenv
else
    curl https://raw.githubusercontent.com/0xAungkon/pygit-commit-versioning/main/gitautov > gitautov;
    ./gitautoenv
fi

