export async function createChat(): Promise<{ id: string }> {
	const url = '/api/chat';
	const method = 'POST';
	const headers = { 'Content-Type': 'application/json' };

	const response = await fetch(url, { method, headers });
	const data = await response.json();

	if (!response.ok) {
		throw data;
	}

	return data;
}
