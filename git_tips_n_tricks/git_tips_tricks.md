# Guide website: [Git-tricks](https://www.honeybadger.io/blog/git-tricks/)

## *See PDF: [git_tips_tricks_may_2021.pdf](./assets/guides/git_tips_tricks_2021_may.pdf) (website above exported as PDF on the 20th July 2021)*

1. Beautiful log:  
```git log --oneline --graph --decorate```

2. Clean up local branches removed when fetch or pull  
```git config --global fetch.prune true```

3. Delete local branches merged into master  
```git branch --merged master | grep -v "master" | xargs -n 1 git branch -d```

4. Force delete local branch, not merged in master  
```git branch -D branch_name```

5. Go to old commit and come back again to HEAD when wrong rebase.

```bash
git reflog
git checkout sha1_of_commit
git checkout HEAD
```

6. Selectively organize commits (specially useful when one or few files with several changes)  
```git add -p```

7. [Git emojis](https://gist.github.com/rxaviers/7360908)

8. Nice git tutorial, directly provided by git
```git help tutorial```
