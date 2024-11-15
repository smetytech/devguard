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
	import { CornerDownLeft } from 'lucide-svelte';

	let messages: Array<IMessage> = $state([]);
	let value: string = $state('');
	let scrollContainer: HTMLDivElement | null = $state(null);

	function scrollToBottom() {
		if (!scrollContainer) {
			return;
		}

		scrollContainer.scrollTo({ top: scrollContainer.scrollHeight, behavior: 'smooth' });
	}

	async function handleSubmit(event: Event) {
		event.preventDefault();

		if (!value.trim()) {
			return;
		}

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

	function handleWebSocketMessage(message: IMessage) {
		messages = [...messages, { ...message, timestamp: formatTimestamp(message.timestamp) }];
	}

	function handleWebSocketError() {
		displayGeneralErrorToast();
	}

	onMount(() => {
		openWebSocket(handleWebSocketMessage, handleWebSocketError);

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
				<span class="flex">
					<span
						class="{message.type === MessageType.User
							? 'text-green-500'
							: 'text-muted-foreground'} text-sm leading-6"
					>
						~{message.name} %&nbsp;
					</span>
					<span class="font-medium">{message.content}</span>
					<span class="text-muted-foreground ml-auto text-sm leading-6">{message.timestamp}</span>
				</span>
			{/each}
		</div>

		<form class="bg-muted/75 flex items-center gap-2 rounded-xl pl-4" onsubmit={handleSubmit}>
			<span class="text-green-500">~user % </span>

			<input
				class="placeholder:text-muted-foreground grow border-none bg-transparent py-4 outline-none"
				type="text"
				bind:value
			/>

			<div class="pr-4">
				<CornerDownLeft />
			</div>
		</form>
	</div>
</div>
