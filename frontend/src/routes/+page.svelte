<script lang="ts">
	import { onMount, tick } from 'svelte';
	import { MessageType, type IMessage } from '$lib/interfaces/message.interface';
	import { displayGeneralErrorToast } from '$lib/scripts/toast.script';
	import {
		closeWebSocket,
		openWebSocket,
		sendWebSocketMessage
	} from '$lib/scripts/websocket.script';
	import { formatTimestamp } from '$lib/scripts/date.script';
	import { Message } from '$lib/components/other/message';
	import { TerminalInput } from '$lib/components/other/terminal-input';
	import { createChat } from 'src/lib/controllers/chat.controller';
	import { createMessage } from 'src/lib/controllers/message.controller';

	let chatId: string;
	let messages: Array<IMessage> = $state([]);
	let scrollContainer: HTMLDivElement | null;

	function scrollToBottom() {
		if (!scrollContainer) {
			return;
		}

		scrollContainer.scrollTo({ top: scrollContainer.scrollHeight, behavior: 'smooth' });
	}

	async function handleSubmit(value: string) {
		sendWebSocketMessage(value);

		messages = [
			...messages,
			{
				type: MessageType.User,
				name: 'user',
				content: value,
				timestamp: formatTimestamp(new Date())
			}
		];
		value = '';

		await tick();
		scrollToBottom();
	}

	async function handleWebSocketMessage(message: IMessage) {
		try {
			await createMessage(message, chatId);

			messages = [...messages, { ...message, timestamp: formatTimestamp(message.timestamp) }];

			await tick();
			scrollToBottom();
		} catch {
			displayGeneralErrorToast();
		}
	}

	function handleWebSocketError() {
		displayGeneralErrorToast();
	}

	onMount(async () => {
		try {
			const { id } = await createChat();
			chatId = id;
			openWebSocket(id, handleWebSocketMessage, handleWebSocketError);
		} catch {
			displayGeneralErrorToast();
		}
	});

	onMount(() => {
		return () => {
			closeWebSocket();
		};
	});
</script>

<div class="h-[calc(100dvh-4.5rem)] p-4 lg:p-6">
	<div
		class="flex h-full w-full flex-col gap-6 rounded-xl bg-gradient-to-br from-[#F4F4F4] to-[#C7C7C9] p-4 font-mono dark:from-[#4E4E54] dark:to-[#1F1F29]"
	>
		<div class="flex items-center justify-center">
			<div class="flex items-center gap-1.5">
				<span class="h-3.5 w-3.5 rounded-full bg-[#ED6A5E]"></span>
				<span class="h-3.5 w-3.5 rounded-full bg-[#F4BF4F]"></span>
				<span class="h-3.5 w-3.5 rounded-full bg-[#61C554]"></span>
			</div>

			<span class="mx-auto block w-fit text-center text-sm">Terminal</span>

			<div class="flex items-center gap-1.5 opacity-0">
				<span class="h-3.5 w-3.5 rounded-full bg-[#ED6A5E]"></span>
				<span class="h-3.5 w-3.5 rounded-full bg-[#F4BF4F]"></span>
				<span class="h-3.5 w-3.5 rounded-full bg-[#61C554]"></span>
			</div>
		</div>

		<div class="grow space-y-2 overflow-y-auto" bind:this={scrollContainer}>
			{#each messages as message}
				<Message {message} />
			{/each}
		</div>

		<TerminalInput submit={handleSubmit} />
	</div>
</div>
