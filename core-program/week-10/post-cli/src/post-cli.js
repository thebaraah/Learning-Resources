import chalk from 'chalk';
import { existsSync } from 'node:fs';
import path from 'node:path';
import promptSync from 'prompt-sync';
const prompt = promptSync();

const __dirname = new URL('.', import.meta.url).pathname; // Get current directory path
const studentServicePath = path.join(__dirname, '../src/services.js');
const solutionServicePath = path.join(__dirname, '../src/services-solution.js');

// Import fetcher functions
const solutionExists = existsSync(solutionServicePath); // Set to false to test starter code
const {
  createPost,
  createUser,
  deletePost,
  deleteUser,
  getPosts,
  loginUser,
  setToken,
  updatePost,
} = solutionExists
  ? await import(solutionServicePath)
  : await import(studentServicePath);

// ============================================================================
// MAIN APPLICATION - Complete solution version
// ============================================================================

/**
 * Prompt for a password with masked input
 * @param {string} message - The prompt message
 * @returns {string} The entered password
 */
const promptPassword = (message) => {
  return prompt(message, { echo: '*' }).trim();
};

/**
 * Register a new user through interactive prompts
 * @returns {Promise<string>} The registered username
 */
const registerNewUser = async () => {
  while (true) {
    let name = prompt('Enter your name or /exit to quit: ').trim();
    if (name.toLowerCase() === '/exit') {
      console.log(chalk.yellow('Exiting the post-cli note app. Goodbye!'));
      process.exit(0);
    }
    if (!name) {
      console.log(chalk.red('Name cannot be empty.'));
      continue;
    }
    if (name.startsWith('/')) {
      console.log(
        chalk.red('Name cannot start with a command prefix (e.g. /view)')
      );
      continue;
    }

    const password = promptPassword('Enter a password: ');
    if (!password) {
      console.log(chalk.red('Password cannot be empty.'));
      continue;
    }

    try {
      const data = await createUser(name, password);
      setToken(data.token);
      console.log(chalk.green(`  User ${name} registered successfully!`));
      return name;
    } catch (error) {
      console.log(chalk.red(error.message));
    }
  }
};

/**
 * Log in an existing user through interactive prompts
 * @returns {Promise<string>} The logged-in username
 */
const loginExistingUser = async () => {
  while (true) {
    let name = prompt('Enter your name or /exit to quit: ').trim();
    if (name.toLowerCase() === '/exit') {
      console.log(chalk.yellow('Exiting the post-cli note app. Goodbye!'));
      process.exit(0);
    }
    if (!name) {
      console.log(chalk.red('Name cannot be empty.'));
      continue;
    }

    const password = promptPassword('Enter your password: ');
    if (!password) {
      console.log(chalk.red('Password cannot be empty.'));
      continue;
    }

    try {
      const data = await loginUser(name, password);
      setToken(data.token);
      console.log(chalk.green(`  Welcome back, ${name}!`));
      return name;
    } catch (error) {
      console.log(chalk.red(error.message));
    }
  }
};

/**
 * Present the authentication menu (register, login, or exit)
 * @returns {Promise<string>} The authenticated username
 */
const chooseAuthAction = async () => {
  console.log(chalk.cyan('\nWelcome to Post Central!'));
  console.log(chalk.blue('  1. Register (new user)'));
  console.log(chalk.blue('  2. Login (existing user)'));
  console.log(chalk.blue('  3. Exit'));

  while (true) {
    const choice = prompt('Choose an option (1/2/3): ').trim();
    switch (choice) {
      case '1':
        return await registerNewUser();
      case '2':
        return await loginExistingUser();
      case '3':
        console.log(chalk.yellow('Goodbye!'));
        process.exit(0);
      default:
        console.log(chalk.red('Please enter 1, 2, or 3.'));
    }
  }
};

/**
 * Display the command menu
 */
const displayMenu = () => {
  console.log(
    chalk.blue(
      '\nCommands: /view (see posts), /update <id> (edit post), /delete <id> (remove post), /exit (quit), /leave (delete account)'
    )
  );
  console.log(chalk.blue('Or type a message to create a post:'));
};

/**
 * Handle the /exit command
 */
const handleExitCommand = () => {
  console.log(chalk.yellow('Exiting the post-cli note app. Goodbye!'));
  process.exit(0);
};

/**
 * Handle the /leave command (delete account)
 */
const handleLeaveCommand = async () => {
  await deleteUser();
  console.log(chalk.yellow('Your account has been deleted. Goodbye!'));
  process.exit(0);
};

/**
 * Handle the /view command (display all posts)
 */
const handleViewCommand = async () => {
  const posts = await getPosts();
  console.log(chalk.cyan('\nAll Posts:'));
  if (posts.length === 0) {
    console.log(chalk.gray('  No posts yet. Be the first to post!'));
  } else {
    posts.forEach((post) => {
      console.log(chalk.gray(`  [${post.id}] ${post.user}: ${post.text}`));
    });
  }
};

/**
 * Handle the /update command (edit a post)
 * @param {string[]} parts - Command parts (e.g., ['/update', '1'])
 */
const handleUpdateCommand = async (parts) => {
  const id = parseInt(parts[1]);
  if (isNaN(id)) {
    console.log(chalk.red('Invalid post ID. Usage: /update <id>'));
    return;
  }
  const newText = prompt('Enter new text: ').trim();
  if (!newText) {
    console.log(chalk.red('Text cannot be empty.'));
    return;
  }
  try {
    await updatePost(id, newText);
    console.log(chalk.green(`  Post ${id} updated successfully`));
  } catch (error) {
    console.log(chalk.red(error.message));
  }
};

/**
 * Handle the /delete command (remove a post)
 * @param {string[]} parts - Command parts (e.g., ['/delete', '1'])
 */
const handleDeletePostCommand = async (parts) => {
  const id = parseInt(parts[1]);
  if (isNaN(id)) {
    console.log(chalk.red('Invalid post ID. Usage: /delete <id>'));
    return;
  }
  try {
    await deletePost(id);
    console.log(chalk.green(`  Post ${id} deleted successfully`));
  } catch (error) {
    console.log(chalk.red(error.message));
  }
};

/**
 * Handle empty input
 */
const handleEmptyInput = () => {
  console.log(chalk.red('Message cannot be empty.'));
};

/**
 * Handle creating a new post
 * @param {string} input - The post text
 */
const handleCreatePost = async (input) => {
  const data = await createPost(input);
  console.log(chalk.green(`  Post created with ID: ${data.id}`));
};

/**
 * Run the main application loop
 */
const runMainLoop = async () => {
  while (true) {
    displayMenu();
    const input = prompt('> ').trim();

    // Parse command and arguments
    const parts = input.split(/\s+/);
    const command = parts[0].toLowerCase();

    switch (command) {
      case '/exit':
        handleExitCommand();
        break;

      case '/leave':
        await handleLeaveCommand();
        break;

      case '/view':
        await handleViewCommand();
        break;

      case '/update':
        await handleUpdateCommand(parts);
        break;

      case '/delete':
        await handleDeletePostCommand(parts);
        break;

      case '':
        handleEmptyInput();
        break;

      default:
        await handleCreatePost(input);
        break;
    }
  }
};

/**
 * Main application entry point
 */
const main = async () => {
  try {
    await chooseAuthAction();
    await runMainLoop();
  } catch (error) {
    console.log(chalk.red(error.message));
    process.exit(1);
  }
};

main();
