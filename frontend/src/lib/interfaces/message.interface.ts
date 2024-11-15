export enum MessageType {
	User = 'USER',
	Agent = 'AGENT',
	Tool = 'TOOL'
}

export interface IMessage {
	type: MessageType;
	name: string;
	content: string;
	timestamp: string;
}
