# Git conflict demo in class

This repository is created to demonstrate git conflict resolution in class.
Please follow the steps below to create and resolve a git conflict:

1. create a new git repository with `git init`
2. Create an initial commit `git add . && git commit -m "initial commit"`
3. Create a new branch, modify app.js to add a small validation

```javascript
if (name === "") {
  console.log("I need to know your name!");
} else {
  console.log(`Hello, ${name}! This is a beautiful name`);
}
```

4. Commit the changes in the new branch
5. Switch back to main
6. Add `console.log('Nice to meet you');` after the first `console.log`
7. Commit the changes on main
8. git merge the new branch into main
9. Resolve the conflict while explaining the steps to the class
10. Commit the resolved changes
