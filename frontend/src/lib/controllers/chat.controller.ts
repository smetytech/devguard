export async function createChat() {
	const url = '/api/chat';
	const method = 'POST';
	const headers = { 'Content-Type': 'application/json' };

	const response = await fetch(url, { method, headers });
	const data = await response.json();

	if (!response.ok) {
		throw data;
	}
	return data
}

export async function createMessage(chatId: string,type:string, content: string) {
	const url = `/api/chat/${chatId}/message`;
	const method = 'POST';
	const headers = { 'Content-Type': 'application/json' };
	const body = JSON.stringify({type,content});

	const response = await fetch(url, { method, headers, body });
	const data = await response.json();

	if (!response.ok) {
		throw data;
	}
	return data;
}
