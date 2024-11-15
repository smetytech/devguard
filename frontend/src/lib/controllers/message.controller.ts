import type { IMessage } from '$lib/interfaces/message.interface';

export async function createMessage(message: IMessage, chatId: string) {
	const url = `/api/chat/${chatId}/message`;
	const method = 'POST';
	const headers = { 'Content-Type': 'application/json' };
	const body = JSON.stringify({ message });

	const response = await fetch(url, { method, headers, body });
	const data = await response.json();

	if (!response.ok) {
		throw data;
	}

	return data;
}
