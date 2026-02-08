const posts = [];

const generatePostId = () =>
  posts.length > 0 ? posts[posts.length - 1].id + 1 : 1;

export const getAllPosts = () => posts;

export const findPostById = (id) => posts.find((p) => p.id === parseInt(id));

export const createPost = (username, text) => {
  const post = { id: generatePostId(), user: username, text };
  posts.push(post);
  return post;
};

export const updatePost = (id, text) => {
  const post = findPostById(id);
  if (!post) {
    return null;
  }
  post.text = text;
  return post;
};

export const deletePost = (id) => {
  const postIndex = posts.findIndex((p) => p.id === parseInt(id));
  if (postIndex === -1) {
    return null;
  }
  const post = posts[postIndex];
  posts.splice(postIndex, 1);
  return post;
};
