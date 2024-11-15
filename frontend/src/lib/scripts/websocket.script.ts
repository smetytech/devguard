import { PUBLIC_WEBSOCKET_URL } from '$env/static/public';
import type { IWebSocketMessage } from '$lib/interfaces/websocket.interface';

let socket: WebSocket | null = null;

export function openWebSocket(
	onMessage: (message: IWebSocketMessage) => void,
	onError: (error: Event) => void
) {
	if (socket) {
		return socket;
	}

	socket = new WebSocket(PUBLIC_WEBSOCKET_URL);

	socket.onmessage = (event) => {
		console.log(event.data);
		onMessage(JSON.parse(event.data));
	};

	socket.onerror = (error) => {
		onError(error);
	};

	socket.onclose = () => {
		socket = null;
	};

	return socket;
}

export function closeWebSocket() {
	if (!socket) {
		return;
	}

	socket.close();
}

export function sendWebSocketMessage(message: IWebSocketMessage) {
	if (!socket || socket.readyState !== WebSocket.OPEN) {
		return;
	}

	socket.send(JSON.stringify(message));
}
