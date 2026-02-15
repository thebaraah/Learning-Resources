export default class WebSocketClient {
  #ws = null;
  #url;
  #callbacks;
  #reconnectAttempts = 0;
  #maxReconnectAttempts = 5;
  #reconnectDelay = 3000;

  constructor(url, callbacks) {
    this.#url = url;
    this.#callbacks = callbacks;
  }

  connect() {
    try {
      this.#ws = new WebSocket(this.#url);

      this.#ws.onopen = () => {
        console.log('WebSocket connected');
        this.#reconnectAttempts = 0;
        this.#callbacks.onStatusChange('connected');
      };

      this.#ws.onmessage = (event) => {
        try {
          const message = JSON.parse(event.data);
          console.log('WebSocket message received:', message);
          this.#callbacks.onMessage(message);
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      this.#ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        this.#callbacks.onStatusChange('disconnected');
      };

      this.#ws.onclose = () => {
        console.log('WebSocket disconnected');
        this.#callbacks.onStatusChange('disconnected');
        this.#attemptReconnect();
      };
    } catch (error) {
      console.error('Error creating WebSocket:', error);
      this.#callbacks.onStatusChange('disconnected');
    }
  }

  #attemptReconnect() {
    if (this.#reconnectAttempts < this.#maxReconnectAttempts) {
      this.#reconnectAttempts++;
      console.log(
        `Attempting to reconnect (${this.#reconnectAttempts}/${this.#maxReconnectAttempts})...`
      );
      setTimeout(() => this.connect(), this.#reconnectDelay);
    } else {
      console.error('Max reconnection attempts reached');
    }
  }

  disconnect() {
    if (this.#ws) {
      this.#ws.close();
      this.#ws = null;
    }
  }
}
