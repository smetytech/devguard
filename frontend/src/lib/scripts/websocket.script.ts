import { PUBLIC_WEBSOCKET_URL } from '$env/static/public';
import type { IMessage } from '$lib/interfaces/message.interface';

let socket: WebSocket | null = null;

export function openWebSocket(
	chatId: string,
	onMessage: (message: IMessage) => void,
	onError: (error: Event) => void
) {
	if (socket) {
		return socket;
	}

	socket = new WebSocket(`${PUBLIC_WEBSOCKET_URL}/${chatId}`);

	socket.onmessage = (event) => {
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

export function sendWebSocketMessage(message: string) {
	if (!socket || socket.readyState !== WebSocket.OPEN) {
		return;
	}

	socket.send(message);
}
