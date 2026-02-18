let services;
try {
  services = await import('./services.solution.js');
} catch {
  services = await import('./services.js');
}

export const {
  getHello,
  login,
  register,
  getProfile,
  getMyPosts,
  createPost,
  editPost,
  deletePost,
} = services;
