let websocketServer;

export const initializeWebSocket = (wss) => {
  websocketServer = wss;
};

export const broadcast = (type, data) => {
  if (!websocketServer) {
    console.error('WebSocket server not initialized');
    return;
  }

  const message = JSON.stringify({ type, data });
  for (const client of websocketServer.clients) {
    if (client.readyState === 1) {
      client.send(message);
    }
  }
};
