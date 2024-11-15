export enum WebSocketMessageAction {
	SCAN = 'SCAN'
}

export interface IWebSocketMessage {
	action: WebSocketMessageAction;
	content: string;
}
