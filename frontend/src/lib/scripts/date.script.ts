export function formatTimestamp(timestamp: Date | string) {
	const date = new Date(timestamp);
	const minutes = date.getMinutes().toString().padStart(2, '0');
	const seconds = date.getSeconds().toString().padStart(2, '0');

	return `${minutes}:${seconds}`;
}
