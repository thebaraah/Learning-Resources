import express from "express";
import {
  deleteUser,
  deleteUserByAdmin,
  getMe,
  getUsers,
  loginUser,
  registerUser,
} from "../controllers/userController.js";
import { authenticate } from "../middleware/auth.js";

const router = express.Router();

router.get("/", authenticate, getUsers);
router.post("/register", registerUser);
router.post("/login", loginUser);
router.get("/me", authenticate, getMe);
router.delete("/me", authenticate, deleteUser);
router.delete("/:name", authenticate, deleteUserByAdmin);

export default router;
