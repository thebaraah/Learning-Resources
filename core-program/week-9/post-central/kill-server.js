import { execSync } from "node:child_process";
import { PORT } from "./config/constants.js";

try {
  if (process.platform === "win32") {
    const output = execSync(`netstat -ano`, { encoding: "utf8" });
    const lines = output
      .split("\n")
      .filter((l) => l.includes(`:${PORT}`) && l.includes("LISTENING"));
    for (const line of lines) {
      const pid = line.trim().split(/\s+/).pop();
      execSync(`taskkill /PID ${pid} /F`, { stdio: "inherit" });
    }
  } else {
    execSync(`kill -9 $(lsof -t -i:${PORT})`, { stdio: "inherit" });
  }
} catch {
  console.log(`No process found on port ${PORT}`);
}
